# filename: test_question_driver_process_system_reply.py

################################################################
# HISTORY (put newest entries on top)

# 2023-02-04T09:41:57PST changing the format of UserReply to this
# doing this same change in test_question_driver.py too.

# test_question_driver_process_system_reply.2023-01-29T1951.py
# 2023-02-04T09:41:57PST preserved the above bc about to make the 2023-02-04T09:41:57PST change (see above)

# 2022-09-17 this file (test_question_driver_process_system_reply.py)
# was created To help some debugging, I had (maybe temparaility?)
# moved the definition for process_system_reply from
# test_question_driver.py into a new file called
# test_question_driver_process_system_reply.py.  Then I decided to
# make it permanent.  But this meant I had to move around a bunch of
# functions.

# Update2022-09-17 this is a tag used to name updates that were
# started on 2022-09-17 but not nec copmleted on that date!!  These
# updates were done bc I needed to start re-runnig this code (to test
# the question driver endpoint) becuase I had let it lie for maybe 1
# to 2 months while I worked on the findin gproxy gtester.



################################################################
# Imports

import utils
import config
import json
import os
import pdb

################################################################
# Constants

from constants import TRYING_TO_MIMIC_RegressionTestLogs2_P
from constants import MultipleChoice
from constants import Mixed_TypeInAndMultipleChoice
from constants import TypeIn
from constants import UserChoiceWasNoneOfTheAbove
from constants import MultiChoiceResponseObject
from constants import TypeInResponseObject
from constants import STEP_SLOWLY_P
from constants import STEP_SLOWLY_2
from constants import DIR_OF_CPD_FILES
from constants import CONVERSATION_FILENAME
from constants import ISSUES_OF_NOTE_FILENAME
from constants import TEST_RESPONSE_CONTENT_LIST_OF_MIXED_TYPE_01
from constants import TargetResultForStartConsult14
from constants import ASK_OPERATOR_HOW_TO_HANDLE_BOT_ERROR_STR

################################################################

def process_system_reply(
	json_input, 
	log_dir, 
	conversation_log_filepath, 
	user_reply_script_json, 
	record_user_replies_for_reply_filename, 
	issues_of_note_filepath):

	"""

	This function receives some input - a dict.  The input is the
	bot response.

	Usually that response contains what questions to ask the user.

	Thus, this function, extract the questions and the multiple
	choice responses, prints them out for the user.

	Then it prompts the user for the answers.

	Then it collects the users response and assembles it and
	finding list?  question number etc into a form that the bot
	wants.

	It then returns a result which in a later function can be fed to the bot.

	"""

	consult_id = json_input.get('consultationId')
	question_id = json_input['questionId']

	#question_seq_index = json_input['questionIndexSeq']
	#question_seq_index = json_input.get('questionIndexSeq', -777)
	#nth_question = json_input['questionIndexSeq']
	nth_question = json_input.get('questionIndexSeq', -777)

	# TODO(2022-05-31T15:17:41PDT, ) document under what
	# circumstances will we not have a questionIndexSeq?

	# TODO(2022-05-31T15:19:48PDT, ) on sequence thoughts maybe
	# replace nth_question with the more descriptive and prior
	# name, i.e. question_seq_index

	#question_title = json_input['title']
	# 2022-09-27T22:24:57PDT in one case we see the question title used to be 'null'
	# but now there is no value.  So, we assume that no value is fine.  We will
	# not put 'null' for the question title.  Instead we will put 'No Title'
	#
	# See 2022-09-27T22:26:58PDT in diary-TestCoupletPrograms.org for more details.
	question_title = json_input.get('title', 'NoQuestionTitle')

	# yee olde waye...
	#sys_quest_num_str = f"QuesSeq# {question_seq_index} QuesId# {question_id}" # TODO maybe we want to add consult id here, too?

	# ....yee slightly newer waye...
	# sys_quest_num_str = f"QuesSeq# {nth_question} QuesId# {question_id}" 
	# TODO maybe we want to add consult id here, too?...maybe not.
	# Why maybe not?
	# Well, this will make it harder to compare CONVERSATION_FILENAME files bc even if the sequence of questions and answers
	# is exactly the same, the traces will differ bc the consult id is different.  This issue is why we need to have 
	# CONVERSATION_INVARIANT_MODE_P

	# ...yee newest waye...

	if config.CONVERSATION_INVARIANT_MODE_P:
		sys_quest_num_str = f"QuesSeq# {nth_question}"
	else:
		sys_quest_num_str = f"QuesSeq# {nth_question} QuesId# {question_id}" 

	my_next_question_id = json_input.get('nextQuestionId')

	# If we are processing what the bot said to us (it will be
	# asking us a question) AND if that question it is asking us
	# happens to be the last one, then my_next_question_id will be
	# None.
	
	# Why do we want to gather my_next_question_id?  Well, in
	# order to process the json_input, query the user, and assembe
	# a valid json reply based on user's answer(s) we do not need
	# 'nextQuestionId'.  However, we want to get the value so that
	# if we post a reply to the bot and bot throws an error, then
	# we can see in our reply what is the next question id.  Thus,
	# in case the bot replies with an error, we have the ability
	# to post another reply to the bot that says, 'okay, skip that
	# question and lets go to the next one'
	
	if consult_id is None:
		pdb.set_trace()
		print("Huh!?!? I thought that consultationId was already a part of the bots reply")
		# print("Just letting you know that the json passed into the current fn @process_system_reply does't have consult_id so I am using the input @param remembered_consult_id")
		# pdb.set_trace()
		# consult_id = remembered_consult_id

		
	# 2022-05-31T14:28:41PDT I *think* json_input['responseSections'] corresponds to 
	# 
	response_sections = json_input['responseSections']
	num_response_sections = len(response_sections)

	top_level_question_description = f"BotAsks {sys_quest_num_str} Title: '{question_title}' CPD: {consult_id}"

	print("################################################################")
	print(top_level_question_description)
	utils.log(conversation_log_filepath, top_level_question_description)

	#findings_to_add = []
	#As part of Refactor2022-07-02T08:53:21PDT, changed the above to this
	findings_across_response_sections = []

	################################################################
	# Start Of: Process Each Response Section
	################################################################
	
	for resp_section_num, response_section in enumerate(response_sections):

		findings_from_this_response_section = []

		# TODO(2022-07-02T10:26:20PDT, ) prolly remove this comment block
		# print(f"2022-07-01T21:39:12PDT tracing here in @func process_system_reply")
		# print("This is the first trace we're encountering")
		# print("We are JUST INSIDE OF THIS FOR LOP:")
		# print("	  for resp_section_num, response_section in enumerate(response_sections)")
		# print(f"Note that:\nresp_section_num is {resp_section_num}\n\nresponse_section is {response_section}\n\nresponse_sections is {response_sections}")
		# print()
		# pdb.set_trace()

		#response_header =  response_section['header']
		# 2022-09-16 during DustingOff this was not working, so changed it to this:
		response_header =  response_section.get('header', 'ResponseHeaderMissing:ArtificiallySetByBill-AsPartOfDustingOff')


		# 2022-05-31T14:57:27PDT more printing changes, hopw they are okay (START OF SECTION)
		# If not okay then here you have commenteed out what was here before 2022-05-31T14:57:27PDT
		# If okay after, say, 2022-06-02 then blow away!!
		# print("################")
		# print(f"RESPONSE_SECTION {resp_section_num + 1} of {num_response_sections} such sections")
		# print("################")
		# # we add 1 bc it is zero initial
		#
		#print()
		#
		#string_to_log_and_print = f"BotQuestion: {sys_quest_num_str} ResponseHeader: {response_header}"
		#print()
		#print(string_to_log_and_print)
		#print()
		#
		#log(conversation_log_filepath, "")
		#log(conversation_log_filepath, string_to_log_and_print)
		#log(conversation_log_filepath, "")
		# 2022-05-31T14:57:27PDT more printing changes, hopw they are okay (END OF SECTION)

		allowed_responses = response_section['responses']
		
		response_content_list = []
		for response_content in allowed_responses:
			response_content_list.append(response_content)

		if len(response_content_list) == 0:
			warning_text = f"\nWARNING: Weird, why is @param response_content_list empty!?!?! (while in {top_level_question_description})\n"
			print(warning_text)
			if issues_of_note_filepath:
				with open(issues_of_note_filepath, 'a') as issues_of_note_fobj:
					print(warning_text, file=issues_of_note_fobj)
			if STEP_SLOWLY_2:
				pdb.set_trace()
		
		elements_that_have_no_type = []

		for ele in response_content_list:
			#has_no_type_p = ele['findingValue']['type'] == 'NONE'
			has_no_type_p = ele['findingValue']['type'].lower() == 'none'
			elements_that_have_no_type.append(has_no_type_p)

			# TODO (2022-06-21T21:10:17EDT, ) the above
			# needs to be harmonized with @func
			# utils.ret_likely_response_mode_for_response_content.
			# More than likely this will just go away bc
			# Big Branch 1 and Big Branch 2 will be merged
			# into one fn as @func
			# handle_mixed_response_content_list is trying
			# to do.

		# 2022-06-14T16:33:55EDT for question things in which
		# response_content_list is empty (for example QuesSeq#
		# 21 Title: 'Medications' in Consult #19) maybe we
		# should say if response_content_list == [] then
		# elements_that_have_no_type.append(True) Oh, wait, in
		# such a case elements_that_have_no_type is already []
		# (at least for QuestSeq 21 in Consult #19) I *think*
		# and all([]) returns True.  So, there's not point in
		# doing that.

		if all(elements_that_have_no_type):
			response_content_list_choice_mode = MultipleChoice
			print("FLAG: response_content_list_choice_mode just set to MultipleChoice")

		elif any(elements_that_have_no_type):
			anomaly_detect_result = detect_type_in_vs_multi_choice_anomaly(elements_that_have_no_type)
			if anomaly_detect_result != 'non_anomalous.':
				print(f"Okay now this is QUITE ODD! We have a case of {anomaly_detect_result}")
				pdb.set_trace()
			response_content_list_choice_mode = Mixed_TypeInAndMultipleChoice
			print("FLAG: response_content_list_choice_mode just set to Mixed_TypeInAndMultipleChoice")

			issues_of_note_txt = \
				f"""\nresponse_content_list that have a mix of TypeIn's and Multiple Choice are worth pointing out.
				This particular one can be identified as follows:
				{top_level_question_description}\n"""

			if issues_of_note_filepath:
				with open(issues_of_note_filepath, 'a') as issues_of_note_fobj:
					print(issues_of_note_txt, file=issues_of_note_fobj)

		else:
			response_content_list_choice_mode = TypeIn
			print("FLAG: response_content_list_choice_mode just set to TypeIn")


		# This was used to help diagnose CONSYS-331 (CPD-147)
		# which was difficult to diagnose so as of
		# 2022-07-04T22:09:02PDT I'm leaving this here in case
		# we need to go down that rabbit hole again.  See
		# other occurrences of 147 or CONSYS-331 for at least
		# some of these debugging tricks.
		#
		# if response_header == 'What is your weight?':
		# 	print("################################################################")
		# 	print("################################################################")
		# 	print("################################################################")
		# 	print("Hey" * 10)
		# 	print("################################################################")
		# 	print("################################################################")
		# 	print("################################################################")

		# 	print("response_header is:", response_header)
		# 	print("Debugging 2022-07-02")
		# 	#print("Okay, question header is 'what is your weight'")
		# 	print("and response_content_list_choice_mode is:", response_content_list_choice_mode)
		# 	print("and pretty_print_response_content_type_list(response_content_list) returns:")
		# 	print("and response_content_list is:", utils.ppj(response_content_list))
		# 	print(pretty_print_response_content_type_list(response_content_list))
		# 	pdb.set_trace()


		print()
		pretty_print_response_content_type_list(response_content_list)
		print()

		if STEP_SLOWLY_2:
			print("2022-06-15T11:45:19EDT tracing here, so you can understand mixed type-in multiple choice vs male/faema and bday issue")
			pdb.set_trace()


		################
		# Big Branch 1: Give a type-in value for each response
		# ele (this has been eliminated see
		# test_question_driver.v21.py the the last version
		# that had it - though it did not use it
		###############

		# DONE(2022-07-02T19:01:55PDT, 2022-07-07T07:04:15PDT
		# once we are really sure that 2022-06-22T11:28:04PDT
		# is completed and the needed testing DONE then blow
		# away this if False block.  MAYBE before blowing away
		# it is improtant to closely analyze and make sure
		# that this does not do any important that Big Branch
		# 5 does not also do.

		################
		# Big Branch 2: Multiple Choice - zero choices 
		################
		# zero choices?  yes, this seems like some kind of
		# degenerate case.  But we find it. e.g. QuesSeq# 21
		# Title: 'Medications' in Consult #19)

		# TODO(2022-06-14T17:10:36EDT, ) maybe we should make
		# a new possible value for
		# response_content_list_choice_mode in addition to
		# MultipleChoice that means ZeroChoices or somesuch.


		if response_content_list_choice_mode == MultipleChoice and len(response_content_list) == 0:

			print()
			print(f"RESPONSE_SECTION {resp_section_num + 1} is a MultiChoice Question but THERE ARE NO CHOICES!!!")
			print()

			text_description_of_systems_zero_choice_turn = \
			f"""BotSubQuestion# {resp_section_num + 1} of {num_response_sections}:
			AnswerFormat: MultipleChoice
			ResponseHeader: '{response_header}'
			Weirdly, this is a case when we have zero choices!!
			\n
			"""

			print(text_description_of_systems_zero_choice_turn)
			utils.log(conversation_log_filepath, text_description_of_systems_zero_choice_turn)
			if issues_of_note_filepath:
				with open(issues_of_note_filepath, 'a') as issues_of_note_fobj:
					print(text_description_of_systems_zero_choice_turn, file=issues_of_note_fobj)

			findings_across_response_sections = findings_across_response_sections + findings_from_this_response_section

		################
		# Big Branch 3: Multiple Choice - more than zero choices 
		################

		# anchor reference: 2022-06-22T08:39:01PDT

		elif response_content_list_choice_mode == MultipleChoice and len(response_content_list) > 0:
			
			print()
			print(f"RESPONSE_SECTION {resp_section_num + 1} is a MultiChoice Question")
			print()

			################
			# Multiiple Choice Step 1: List the choices to the user
			################

			# 2022-05-31T16:40:39PDT replacement for 2022-05-31T16:40:15PDT Yee Olde Waye
			text_description_of_systems_multichoice_turn = \
\
f"""BotSubQuestion# {resp_section_num + 1} of {num_response_sections}:
AnswerFormat: MultipleChoice
ResponseHeader: '{response_header}'
\n
"""

			print(text_description_of_systems_multichoice_turn)
			utils.log(conversation_log_filepath, text_description_of_systems_multichoice_turn)

			# For MultiChoice
			for response_number, response_content in enumerate(response_content_list):

			# 2022-06-21T19:09:20EDT renamed nth_choice ->
			# response_number to more closely match what we do for type-in response

				# TODO(2022-05-31T16:50:36PDT, ) see
				# 2022-05-31T16:50:36PDT above for
				# maybe renaming response_content_list
				# to multiple_choice_options.
				# However, see 2022-05-31T16:50:36PDT
				# for probably cancelling this TODO.

				response_name = response_content['name']
				# ref anchor = 2022-06-22T09:30:04PDT

				# what is 'name'? well,
				# response_content is ele in response_content_list
				# response_content_list is from response_section['responses']
				# response_section is from response_sections (a list)

				# response_sections is from original
				# json_input to this func
				# (i.e. process_system_reply)
				# 'responseSections'

				################
				# 2022-05-31T16:40:15PDT Yee Olde Waye Has Been Commented Out and replace with see 2022-05-31T16:40:39PDT
				#text_description_of_systems_multichoice_turn = f"{sys_quest_num_str} MultiChoiceOption # {response_number}: {response_name}"
				#text_description_of_systems_multichoice_turn = f"Bot MultiChoiceOption # {response_number}: {response_name}"
				#print(text_description_of_systems_multichoice_turn)
				#log(conversation_log_filepath, text_description_of_systems_multichoice_turn)

				# 2022-05-31T16:54:42PDT but then
				# maybe delete the above
				# (i.e. 2022-05-31T16:40:15PDT) as I
				# realize that this is probly to articualte the multiple choices.
				text_description_of_response_name_for_multichoice = f"Bot MultiChoiceOption # {response_number}: {response_name}"
				print(text_description_of_response_name_for_multichoice)
				utils.log(conversation_log_filepath, text_description_of_response_name_for_multichoice)

				# 2022-05-31T14:43:10PDT just removed the below, such removal should not cause an error.
				# once sure of removal, then delete
				# 2022-05-31T14:50:11PDT looks like we should be good, after 1 day, blow away!!
				# sys_quest_num_str = f"Bot QuesSeq# {question_seq_index} QuesId# {question_id}"

				# TODO(2022-05-23T12:34:44PDT, ) clean up the following comment

				# (2) the name of a type in value.  E.g.  .
				# 'most recent AI1C %'.  In addition you can
				# also have things like 'units' followed by a
				# list of json objects corresponding to each
				# unit option.

			################
			# Step 2: Solicit the User's Answer to the Multiple-Choice Question
			################

			# anchor ref is 2022-06-22T09:01:45PDT
			# see also @fun
			# solicit_user_ans_to_the_multiple_choice_question
			# which should probably replace this block

			print()
			print()
			usr_prompt_txt = "\nWhat do you chose (answer must be an integer from choices listed above) "
			users_choice = utils.user_input_wrapper(usr_prompt_txt,
				user_reply_script_json,
				record_user_replies_for_reply_filename,
				choices = response_content_list)
			print()
			print()			

			if users_choice ==  "":
				users_choice = UserChoiceWasNoneOfTheAbove
			else:
				users_choice = int(users_choice)

			if users_choice != UserChoiceWasNoneOfTheAbove and (users_choice != 0) and (not(int(users_choice))):
				print(f"Need to answer with an integer and you answered with: {users_choice}")
				print("Please try again:")
				users_choice = int(users_choice)
				if (users_choice != 0) and (not(int(users_choice))):
					print(f"Once again, you need to answer with an integer and you answered with: {users_choice}")
					print("Let's enter the debugger")
					pdb.set_trace()

			################
			# Step 3: Convert the Answer into a Finding and Add to the Finding List
			################

			# reference anchor is: 2022-06-22T09:04:20PDT

			print("User chose:", users_choice)

			if users_choice != UserChoiceWasNoneOfTheAbove:
				response_content = response_content_list[users_choice]
				
				# chosenfindingRecNo = response_content['respNo']
				# Per Update2022-09-17 'respNo' is no more

				chosenfindingEntNo = response_content['entNo']
				chosenfindingName = response_content['name']


			utils.log(conversation_log_filepath, "")
			if users_choice != UserChoiceWasNoneOfTheAbove:
			
				#utils.log(conversation_log_filepath, f"UserReply {sys_quest_num_str} MultiChoice#: {users_choice} Text: {chosenfindingName}")
				# 2023-02-04T09:41:57PST changing the format of UserReply to the following
				utils.log(conversation_log_filepath, f"UserReply: MultiChoice#: {users_choice} Text: {chosenfindingName} {sys_quest_num_str} Cpd-{consult_id}")
				
			else:
			
				#utils.log(conversation_log_filepath, f"UserReply {sys_quest_num_str} MultiChoice#: not-a-number Text: {UserChoiceWasNoneOfTheAbove}")
				# 2023-02-04T09:41:57PST changing the format of UserReply to the following
				utils.log(conversation_log_filepath, f"UserReply: MultiChoice#: not-a-number Text: {UserChoiceWasNoneOfTheAbove} {sys_quest_num_str} Cpd-{consult_id}")
				
			utils.log(conversation_log_filepath, "")

			user_choice_converted_to_finding = {}

			if users_choice != UserChoiceWasNoneOfTheAbove:

				# user_choice_converted_to_finding['id'] = chosenfindingRecNo
				# Comment out the aove per Update2022-09-17 because
				# chosenfindingRecNo has gone away.
				# Now we use 'entNo'. Thus for Update2022-09-17 we add this:
				user_choice_converted_to_finding['entNo'] = chosenfindingEntNo
				
				user_choice_converted_to_finding['state'] = "PRESENT"

				# id_for_humans = f"Fnd-{chosenfindingName}-GenNo-{chosenfindingEntNo}-Cpd-{consult_id}-RecNum-{chosenfindingRecNo}"
				# id_for_humans = utils.pretty_fnd_id(chosenfindingName, chosenfindingEntNo, consult_id, chosenfindingRecNo)
				# 2022-09-17T13:42:27PDT per Update2022-09-17 replacing the above with the below bc chosenfindingRecNo is gone.
				id_for_humans = utils.pretty_fnd_id(chosenfindingName, chosenfindingEntNo, consult_id)
				
				user_choice_converted_to_finding['idForHumans'] = id_for_humans

				print("Users choice represented as a finding to add to the finding list:")
				user_choice_converted_to_finding_pretty_txt = json.dumps(user_choice_converted_to_finding, indent=4, sort_keys=True)
				print(user_choice_converted_to_finding_pretty_txt)

				#findings_to_add.append(finding_to_add)
				# As part of Refactor2022-07-02T08:53:21PDT, changed the above to this
				findings_from_this_response_section.append(user_choice_converted_to_finding)

			findings_across_response_sections = findings_across_response_sections + findings_from_this_response_section
			
		################
		# Big Branch 5: Mixed - Multiple Choice and Give a type-in value for each response ele
		################

		elif response_content_list_choice_mode in [Mixed_TypeInAndMultipleChoice, TypeIn]:
		
			# DONE(2022-06-22T11:28:04PDT, 2022-07-02T18:57:49PDT)
			#
			# @func handle_mixed_response_content_list should
			# probably take over for all the branches.
			# Although this is done, in HISTORY, at
			# 2022-07-02T18:53:54PDT, you can see that "I
			# have not fully tested across all consutls"

			# TODO(2022-06-22T11:28:40PDT, ) we should
			# probably enable the ability to return
			# multiple findings to add....Time passes, I
			# think this TODO can be resolved, see
			# 2022-07-01T11:43:09PDT.

			findings_from_this_response_section = \
				handle_mixed_response_content_list(\
					response_content_list,
					resp_section_num,
					num_response_sections,
					response_header,
					user_reply_script_json,
					record_user_replies_for_reply_filename,
					conversation_log_filepath,
					consult_id,
					sys_quest_num_str,
					response_content_list_choice_mode)

			# TODO(2022-07-02T10:27:26PDT, ) prolly remove this trace block soon
			# print("2022-07-01T17:49:34PDT tracing here (in @fun process_system_reply).")
			# print("We are RIGHT AFTER the call to handle_mixed_response_content_list in which")
			# print("the return value to that fn, gets assigned to @param findings_from_this_response_section,")
			# print()
			# print("Issues around assumption violation of the OUTMODED/ REMOVED findings_to_add must be [] (i.e. 2022-06-22T11:35:40PDT)")
			# print("See also 2022-07-01T17:16:05PDT.  This is part II of the tracing")
			# print("and why findings list is has repeats CPD 62")
			# pdb.set_trace()

			findings_across_response_sections = findings_across_response_sections + findings_from_this_response_section			

		else:
			print("response_content_list_choice_mode was neither MultipleChoice nor TypeIn, how can this be and why wasn't this caught by an earlier check?")
			pbd.set_trace()
			

		if STEP_SLOWLY_P:
			print()
			print()				
			print("DO WE NEED TO STOP AND FIX THE INPUT?  WHAT KIND OF CHECK WILL ALLOW GRACEFUL FAILURE?")
			pdb.set_trace()
			print()

		
		#chosen_response_obj = responses[users_choice]
		#response_json_as_pretty_txt = json.dumps(chosen_response_obj, indent=4, sort_keys=True)
		#print("The object corresponding to user's choice is:", response_json_as_pretty_txt)

	################################################################
	# End Of: Process Each Response Section
	################################################################


	if STEP_SLOWLY_P:
		print()
		print()				
		print("So look at @param findings_across_response_sections, do they seem ok?")
		print(json.dumps(findings_across_response_sections, indent = 4, sort_keys = True))
		pdb.set_trace()


	#updated_findings_list = json_input["findings"] + findings_to_add
	# For Refactor2022-07-02T08:53:21PDT remove the above, add in the below
	updated_findings_list = json_input["findings"] + findings_across_response_sections

	if STEP_SLOWLY_P:
		print()
		print()				
		print("IF you want to look at updated_findings_list...")
		print("THEN Type 'updated_findings_list' or 'json.loads(updated_findings_list, indent=4, sort_keys=True)'")
		print("ELSE hit 'c' to continue execution")
		pdb.set_trace()
	
	user_response_object = {"questionId": question_id, "questionIndexSeq" : nth_question, "consultationId": consult_id, "findings" : updated_findings_list}
	
	print("We are at the end of @func process_system_reply - we have a reply to the bots question and we will soon post it to the bot.")

	if STEP_SLOWLY_P:
		print()
		print()				
		print("Do you want to inspect and possibly modify @param user_response_object, i.e. what to return?")
		pdb.set_trace()

	user_response_object['myNextQuestionId'] = my_next_question_id

	user_response_object_str = json.dumps(user_response_object, indent=4, sort_keys = True)

	if log_dir is not None:

		# 2022-05-16T11:26:00PDT prolly delete this all with this timestamp
		# if question_seq_index is None:
		# 	question_number_str = "Unknown"
		# else:
		# 	question_number_str = str(question_seq_index)
		# out_filename = "bot-rpl-2-usr-ans-2-q{question_number_str}.json"

		if nth_question > 10:
			nth_question_str = "0" + str(nth_question)
		else:
			nth_question_str = str(nth_question)

		#2022-06-10T19:41:11PDT delete this and the above soon.
		#out_filename = f"Q{nth_question_str}-user-reply-Id{question_id}.json"
		out_filename = utils.filename_str_for_user_reply(nth_question_str, question_id)

		out_fpath = os.path.join(log_dir, out_filename)
		with open(out_fpath, 'w') as out_obj:
			#print(json.dumps(user_response_object, indent=4, sort_keys=True), file=out_obj)
			#2022-06-10T18:10:08PDT delete this comment and the prev line a few days from now

			print(user_response_object_str, file=out_obj)


	#### returning from process_system_reply			
	#return(user_response_object_str, question_seq_index)
	return(user_response_object_str, nth_question)
	#### returning from process_system_reply

################################################################

def pretty_print_response_content_type_list(response_content_list):
	"""
	This is just to help debugging / monitoring

	#>>> pretty_print_response_content_type_list([MultiChoiceResponseObject, TypeInResponseObject])
	#["MultiChoice", "TypeIn"]

	#>>> pretty_print_response_content_type_list(["MultiChoiceResponseObject", "TypeInResponseObject"])
	#["MultiChoice", "TypeIn"]

	"""

	response_content_type_list = [utils.ret_likely_response_mode_for_response_content(ele) for ele in response_content_list] # we are in pretty_print_response_content_type_list
	
	#response_content_type_abbrev_list = [ele.rstrip("ResponseObject") for ele in response_content_type_list]
	
	# VERY weird that this does not give us TypeIn,	so, let's just give up on that approach
	# and try the following:

	# First, take note of this:
	# len("ResponseObject") => 14
	#
	# and thus do this...

	response_content_type_abbrev_list = [ele[0:-14] for ele in response_content_type_list]

	#print("response_content_type_list:", response_content_type_list)
	print("FLAG: response_content_type_abbrev_list:", response_content_type_abbrev_list)

################################################################	

def index_where_multi_choice_options_end(response_content_list):
	"""

	This should return the index that is the index of the last
	item that is a multi-choice.  (see the doctest cases in this
	function and @func
	index_where_multi_choice_options_end_internal).

	Why do we have this function?  Well...

	If we have a response_content_list that has some multiple
	choice items, then, as we iterate through that list, we want
	to know when we've reached the last mutliple choice item bc
	after we've printed that one, then we want to prompt the user
	asking 'which one(s) of these options do you choose'

	This function tells us when (i.e. at which index position in
	response_content_list) we want to ask 'which one(s) of these
	options do you choose'


	>>> index_where_multi_choice_options_end(TEST_RESPONSE_CONTENT_LIST_OF_MIXED_TYPE_01)
	0

	# As of 2022-06-22T18:23:01PDT the above is untested.  TODO(2022-06-22T18:23:11PDT, ) TEST IT!

	"""
	response_content_type_list = [utils.ret_likely_response_mode_for_response_content(ele) for ele in response_content_list] # we are in index_where_multi_choice_options_end
	result_index_value = index_where_multi_choice_options_end_internal(response_content_type_list)
	return(result_index_value)

def index_where_multi_choice_options_end_internal(response_content_type_list):
	"""

	Made this _internal verison of @func
	index_where_multi_choice_options_end simply to make writing
	the test cases easy

	>>> M = MultiChoiceResponseObject
	>>> T = TypeInResponseObject

	>>> index_where_multi_choice_options_end_internal([M])
	0

	>>> index_where_multi_choice_options_end_internal([T, M])
	1

	>>> index_where_multi_choice_options_end_internal([T, M, M])
	2

	>>> index_where_multi_choice_options_end_internal([M, T])
	0

	>>> index_where_multi_choice_options_end_internal([M, M, T])
	1

	>>> index_where_multi_choice_options_end_internal([M, M, M, T])
	2
	
	>>> index_where_multi_choice_options_end_internal([T, M, M, M, M])
	4

	Note this function assumes we will never see a case like...

	[T, M, T] or [T, M, T, M] or [T, M, M, T] or [M, T, M] or etc

	see @func detect_type_in_vs_multi_choice_anomaly where we
	verify this assumption.

	"""
	#pdb.set_trace()
	
	def ele_in_expected_response_obj_types_p(x):
		return(x in [TypeInResponseObject, MultiChoiceResponseObject])

	if not(all([ele_in_expected_response_obj_types_p(ele) for ele in response_content_type_list])):
		print("Unexpected response_object_type in response_content_list")
		pdb.set_trace()

	type_of_first_response_content = response_content_type_list[0]

	if type_of_first_response_content == TypeInResponseObject:
		result = len(response_content_type_list) - 1
	elif type_of_first_response_content ==  MultiChoiceResponseObject:
		if TypeInResponseObject in response_content_type_list:
			result = response_content_type_list.index(TypeInResponseObject)
			result = result -1
		else:
			result = len(response_content_type_list) - 1
	else:
		print("How did you get here in @func index_where_multi_choice_options_end!!!?")
		pdb.set_trace()

	return(result)

################################################################

################################################################

TEST_TARGET_FOR_HMRCL_01 = [{'id': '13', 'state': 'PRESENT', 'idForHumans': 'Fnd-systemic corticosteroid-GenNo-64193-Cpd-19-RecNum-13'}, {'id': 104, 'valueObject': {'value': '0', 'valueType': 'ABSOLUTE_STRING', 'format': 'STRING'}, 'state': 'PRESENT', 'idForHumans': 'Fnd-other medication-GenNo-46444-Cpd-19-RecNum-104'}]

def handle_mixed_response_content_list(
	response_content_list, 
	resp_section_num, 
	num_response_sections, 
	response_header, 
	user_reply_script_json, 
	record_user_replies_for_reply_filename, 
	conversation_log_filepath,
	consult_id,
	sys_quest_num_str,
	response_content_list_choice_mode):

	# DONE(2022-06-22T11:35:40PDT, 2022-07-02T09:26:47PDT) try to
	# remove findings_to_add as an arg We probably do not need to
	# pass findings_to_add as an argument but I am being
	# converative.

	"""
	@return findings_from_this_response_section

	What originally motivated this function was handling cases
	in which @param response_content_list was a mix of multiple
	choice and type-in's.

	This assumption violation was first discovered here:

	Consult # 19 QuesSeq# 23 Title: 'Other medication information'.

	#>>> handle_mixed_response_content_list(response_content_list = TEST_RESPONSE_CONTENT_LIST_OF_MIXED_TYPE_01, resp_section_num = 0, num_response_sections = 1, response_header = 'Did you stop taking any medication in the past few weeks?', user_reply_script_json = [], record_user_replies_for_reply_filename = None, conversation_log_filepath = None, consult_id = 19, sys_quest_num_str = "TODO fill value for sys_quest_num_str in later!!")
	#TEST_TARGET_FOR_HMRCL_01
	
	TODO make a test out of the above.  Right now, the fn outputs
	to stdio and so maybe implement a testing mode that silences
	it.
	
	"""

	if STEP_SLOWLY_2:
		print("################################################################")
		print("HEY "* 20)
		print("HEY "* 20)
		print("# Hey just entered brand new (as of 2022-06-22T11:19:46PDT) fn #")
		print("# handle_mixed_response_content_list ###########################")
		print("# tracing just so you know I am being called ###################")
		print("Step Carefully about to enter @func handle_mixed_response_content_list and we are in testing of the that fn")
		print("################################################################")
		pdb.set_trace()

	print()
	print(f"RESPONSE_SECTION {resp_section_num + 1} is a Mix of Type-Ins and Multi Choice")
	print()

	# TODO(2022-07-02T14:31:43PDT, ) we can probably get rid of
	# TRYING_TO_MIMIC_RegressionTestLogs2 once we have a nice
	# alternative Regression Test Log dir other than
	# RegressionTestLogs2
	
	if TRYING_TO_MIMIC_RegressionTestLogs2_P and response_content_list_choice_mode == TypeIn:
			text_description_of_systems_turn = \
\
f"""BotSubQuestion# {resp_section_num + 1} of {num_response_sections}:
AnswerFormat: TypeIn
ResponseHeader: '{response_header}"""

	else:
		text_description_of_systems_turn = \
		f"""BotSubQuestion# {resp_section_num + 1} of {num_response_sections}:
		AnswerFormat: Mixed TypeIn and Multi Choice
		ResponseHeader: '{response_header}"""

	# Btw, at 2022-06-22T08:28:03PDT, if you are wondering about
	# the nature of response_header see "What is response_header?"
	# (~ line 971)

	# 2022-06-22T08:26:05PDT the corresponding old school TypeIn line is circa 910

	print(text_description_of_systems_turn)
	if conversation_log_filepath:
		utils.log(conversation_log_filepath, text_description_of_systems_turn)

	index_to_prompt_user_for_multi_choice = index_where_multi_choice_options_end(response_content_list)

	multi_choice_options = []

	multi_choice_findings_from_this_response_section = []
	type_in_findings_from_this_response_section = []

	# This was used to help diagnose CONSYS-331 (CPD-147)
	# which was difficult to diagnose so as of
	# 2022-07-04T22:09:02PDT I'm leaving this here in case
	# we need to go down that rabbit hole again.  See
	# other occurrences of 147 or 331 for at least some of
	# print("2022-07-02T20:46:25PDT tracing to debug ConsultID 147")
	# print(f"sys_quest_num_str: {sys_quest_num_str}")
	# print("Is sys_quest_num_str == 'QuesSeq# 2'")
	# # or maybe i should see it question_id == 30??
	# pdb.set_trace()

	for response_number, response_content in enumerate(response_content_list):
		response_mode = utils.ret_likely_response_mode_for_response_content(response_content)  # we are in handle_mixed_response_content_list


		if response_mode == TypeInResponseObject:

			################
			# 'old school' analog of this is "Big Branch 1: Give a type-in value for each response ele"
			################

			print()
			print(f"Response_Section {resp_section_num}.  We are on a type-In.  response_number is: {response_number}")
			print()

			# 2022-06-22T08:41:51PDT in the 'old school analog' text_description_of_systems_typein_turn was defined right here

			#response_name = response_content['name']
			# 2022-09-18T22:40:20PDT replace the above with the below per Update2022-09-17
			response_name = response_content.get('name', "NoValueUpdate2022-09-17")

			text_description_of_response_name_for_typein = f"Bot SubQuestionTxt: '{response_name}'"
			# Example Value: "Bot SubQuestionTxt: 'most recent blood glucose'"
			# Re Example Value see also 2022-06-21T18:58:20EDT

			print(text_description_of_response_name_for_typein)
			if conversation_log_filepath:
				utils.log(conversation_log_filepath, text_description_of_response_name_for_typein)

			print()
			#print("defaultUnit: ", response_content['findingValue']['defaultUnit'])
			#2022-09-16 during DustingOff this was not working, so changed it to this per Update2022-09-17
			print("defaultUnit: ", response_content['findingValue'].get('defaultUnit','defaultUnitMissing:ArtificiallySetByBill-AsPartOfDustingOff-and-Update2022-09-17'))
			
			# 2022-09-17T16:00:36PDT I bet we can just let
			# the be 'get' bc maybe we could get away with
			# response_content['findingValue']['defaultUnit']
			# before bc there was never a missing
			# 'defaultUnit' key.  Maybe it was always
			# 'null'.  see At 2022-09-17T16:01:50PDT in
			# diary-TestCoupletPrograms.org.

			


			#print("allowable units are: ", response_content['findingValue']['units'])
			#2022-09-16 during DustingOff this was not working, so changed it to this per Update2022-09-17
			print("allowable units are: ", response_content['findingValue'].get('units','unitsMissing:ArtificiallySetByBill-AsPartOfDustingOff-and-Update2022-09-17'))

			response_type = response_content['findingValue']['type']
			
			print()
			print()				
			usr_prompt_txt = f"\nPlease enter a value of type {response_type}: "
			user_type_in_response = \
				utils.user_input_wrapper(usr_prompt_txt,
					user_reply_script_json,
					record_user_replies_for_reply_filename,
					choices = [response_content])
			print()
			print()				

			#text_description_of_users_turn = f"UserReply (TypeIn) to {sys_quest_num_str} SubQuestion# {response_number}: {user_type_in_response} Note: SubQuestion# can also be called response_number"
			# Example Value: For Cpd-62
			# "UserReply (TypeIn) to QuesSeq# 4 SubQuestion# 0: 20" 
			# RE Example Value: see also 2022-06-21T18:58:20EDT

			# 2023-02-04T09:41:57PST changing the format of UserReply to the following
			text_description_of_users_turn = f"UserReply: {user_type_in_response} (TypeIn) to {sys_quest_num_str} SubQuestion# {response_number} Cpd-{consult_id} Note: SubQuestion# can also be called response_number"

			print()
			print(text_description_of_users_turn)
			print()				

			if conversation_log_filepath:
				utils.log(conversation_log_filepath, "")
				utils.log(conversation_log_filepath, text_description_of_users_turn)
				utils.log(conversation_log_filepath, "")
			
			type_in_finding = convert_user_type_in_val_to_finding(user_type_in_response, response_content, consult_id)

			if STEP_SLOWLY_P:				
				print("################################################################")
				print("BEFORE append to findings_from_this_response_section in type-in mode")
				print("type_in_finding is", type_in_finding)
				print("findings_from_this_response_section is", findings_from_this_response_section)

			type_in_findings_from_this_response_section.append(type_in_finding)

			if STEP_SLOWLY_P:				
				print("AFTER append of the type-in finding, here is @param findings_from_this_response_section")
				print(findings_from_this_response_section)				
				pdb.set_trace()
				print("################################################################")

			# 2022-06-22T08:32:45PDT To find the 'old
			# school' analog of this see approx line 1045
			# and/or search for 2022-05-20T15:48:48PDT


		elif response_mode == MultiChoiceResponseObject:
			if len(response_content_list) == 0:
				print("Something is screwy here - see '\# Big Branch 2: Multiple Choice - zero choices'")
				pdb.set_trace()
			################
			# The old school analog of this is:
			#
			# '# Big Branch 3: Multiple Choice - more than zero choices'
			#
			# i.e. see anchor reference '2022-06-22T08:39:01PDT'
			################

			multi_choice_options.append(response_content)

			response_name = response_content['name']
			# for old school analog see 2022-06-22T09:30:04PDT
			# 2022-09-18T22:41:08PDT eplace the above with the below per Update2022-09-17
			response_name = response_content.get('name', "NoValueUpdate2022-09-17")
			

				# what is 'name' well,
				# response_content is ele in response_content_list
				# response_content_list is from response_section['responses']
				# response_section is from response_sections (a list)

				# response_sections is from original
				# json_input to this func
				# (i.e. process_system_reply)
				# 'responseSections'

			text_description_of_response_name_for_multichoice = f"Bot MultiChoiceOption # {response_number}: {response_name}"
			print(text_description_of_response_name_for_multichoice)
			if conversation_log_filepath:
				utils.log(conversation_log_filepath, text_description_of_response_name_for_multichoice)


			if response_number == index_to_prompt_user_for_multi_choice:
			
			# IF: we are at last multi choice optionsin response_content_list,
			#
			# THEN: we need to ask the user to
			# select which, if any option(s) the chose for
			# their reply to the bot's question.
			
				user_selections_converted_to_findings = \
					solicit_user_ans_to_the_multiple_choice_question(\
						multi_choice_options,
						user_reply_script_json,
						record_user_replies_for_reply_filename,
						conversation_log_filepath,
						consult_id,
						sys_quest_num_str)
				multi_choice_findings_from_this_response_section = \
					multi_choice_findings_from_this_response_section + user_selections_converted_to_findings

		else:
			print("How did you get here?  Unexpected value for @param response_mode in @func handle_mixed_response_content_list.")
			print("Value of @param response_mode is {response_mode}")
			pdb.set_trace()

	findings_from_this_response_section = \
		multi_choice_findings_from_this_response_section + \
		type_in_findings_from_this_response_section

	if STEP_SLOWLY_2:
		print("################################################################")
		print("# Hey just about to exit @fun handle_mixed_response_content_list")
		print("# tracing just so you know ###################")
		print("################################################################")
		pdb.set_trace()

	return(findings_from_this_response_section)

################################################################

# 2022-12-27T23:56:09MST moved ret_likely_response_mode_for_response_content to utils.py


		

################################################################

def convert_user_type_in_val_to_finding(user_type_in_response, response_content, consult_id):

	valued_finding_to_add = {}

	if STEP_SLOWLY_P:

		print()
		print()				
		print("We've just entered @func convert_user_type_in_val_to_finding")
		pdb.set_trace()

	# finding_recno = response_content['respNo']
	# 2022-09-17T15:33:47PDT 'respNo' is removed as part of Update2022-09-17
	# finding_entity_number can be used.

	finding_entity_number = response_content['entNo']

	# 2022-05-20T21:04:30PDT changed finding_recno to int(finding_recno)
	# hoping to fix issue
	# valued_finding_to_add['id'] = int(finding_recno)
	# 2022-09-17T15:34:49PDT commented out the immeidately above line
	# and replaced with the below as part of Update2022-09-17
	valued_finding_to_add['entNo'] = finding_entity_number
	
	response_type = response_content['findingValue']['type']

	#finding_value_object			= response_content['findingValue']

	# 2022-05-20T21:38:06PDT trying somethign radical.  I've been
	# re-using all the detritus but now I stop that.  I created a
	# finding_value_object from the ground up.

	finding_value_object			= {}
	finding_value_object['value']		= user_type_in_response		
	finding_value_object['valueType']	= response_content['findingValue']['type']


	# 2022-05-20T21:40:49PDT wait, the above is a bug I think
	# 2022-06-09T13:55:07PDT add this due to conversationwith Michael relevant to 2022-05-20T21:40:49PDT
	# 2022-06-09T14:00:22PDT TODO make this able to handle non default units
	optional_default_unit = response_content['findingValue'].get('defaultUnit') 
	if optional_default_unit:
		id_for_default_unit = optional_default_unit['id']
		my_display_for_default_unit = optional_default_unit['display']
		finding_value_object['valueTypeUnit'] = id_for_default_unit
		finding_value_object['myDisplayForDefaultUnit'] = my_display_for_default_unit

	finding_value_object['format']		= response_content['findingValue']['format']

	if STEP_SLOWLY_P: 
		print("Check out the finding_value_object to make sure it is being formatted correctly")
		pdb.set_trace()

	# DONE (2022-05-19T20:25:00PDT at least I *think* it is done)
	# these options should be eliminated based on
	# ~2022-05-13T13:55:21PDT call with Michael AFTER he gets the
	# format, defaultUnit, and unit fields putting out things
	# correctly.

	# TODO delete this 2022-05-19T20:24:27PDT region below once we
	# are sure the above is really done

################

# <START OF 2022-05-19T20:24:27PDT COMMENTED REGION TO REMOVE>
# 	#elif response_type == 'DATE':
# 	if response_type == 'DATE':
# 		finding_value_object['format'] = 'DATE'		
# 		finding_value_object['value'] = user_type_in_response
# 		finding_value_object['valueType'] = 'DATE'
		
# 	elif response_type == 'LENGTH':
# 		finding_value_object['format'] = 'INT'
# 		finding_value_object['value'] = user_type_in_response
# 		finding_value_object['valueType'] = 'LENGTH'
# 		finding_value_object['valueTypeUnit'] = 4
# 		# TODO valueTypeUnit = 4 means 'inches', right?  need to support other units of measure.
		
# 	elif response_type == 'WEIGHT':
# 		finding_value_object['format'] = 'INT'
# 		finding_value_object['value'] = user_type_in_response
# 		finding_value_object['valueType'] = 'WEIGHT'
# 		finding_value_object['valueTypeUnit'] = 2
# 		# TODO valueTypeUnit = 2 means 'lbs', right?  need to support other units of measure.


# #	if not(CONSTRUCT_FINDING_VALUE_OBJECT_DE_NOVO_P): 
# 	elif not(CONSTRUCT_FINDING_VALUE_OBJECT_DE_NOVO_P):
	
# 		finding_value_object			= response_content['findingValue']
# 		finding_value_object['value']		= user_type_in_response		
# 		finding_value_object['valueType']	= response_content['findingValue']['type']
# 		finding_value_object['valueTypeUnits']	= response_content['findingValue']['defaultUnit']
# 		finding_value_object['format']		= response_content['findingValue']['format']
		
# 		# TODO this should really be a conversion to the enum referrent
# 		# and eventually we want the ability to chose non default units

# 	else:
# 		pdb.set_trace()
# 		print("Sorry, I dunno how to build valued finding of this type")
# 		print("why don't you try to specify it in the debugger immediately below.")
# 		pdb.set_trace()
#
# <END OF 2022-05-19T20:24:27PDT COMMENTED REGION TO REMOVE>
 

	valued_finding_to_add['valueObject'] = finding_value_object
	valued_finding_to_add['state'] = "PRESENT"
	
	# finding_name = response_content['name'] # 2022-09-18T23:03:45PDT the 'old code'
	# Per Update2022-09-17 assuming that finding_name is now always from
	# but we are testing that assumption (call it the 2022-09-18T23:05:17PDT assumption)
	# see 2022-09-18T23:13:10PDT in diary-TestCoupletPrograms.org
	# 'extensionData': [{'name': 'AdultHeight'}, <etc>]  
	if response_content.get('name'):
		finding_name = response_content.get('name')
	else:
		finding_name = "No Name Found"

	# rec_num = response_content['respNo']
	# 2022-09-17T15:37:07PDT the above was commented out as part of Update2022-09-17

	# id_for_humans = f"Fnd-{finding_name}-GenNo-{finding_entity_number}-Cpd-{consult_id}-RecNum-{rec_num}"
	# id_for_humans = utils.pretty_fnd_id(finding_name, finding_entity_number, consult_id, rec_num)
	# 2022-09-17T15:28:42PDT the above was replaced with the below as part of Update2022-09-17
	id_for_humans = utils.pretty_fnd_id(finding_name, finding_entity_number, consult_id)

	valued_finding_to_add['idForHumans'] = id_for_humans

	if STEP_SLOWLY_P:

		print()
		print()				

		print("Check @param valued_finding_to_add to see if you like what we are going to return from convert_user_type_in_val_to_finding")
		pdb.set_trace()
	
	return(valued_finding_to_add)

################################################################

def detect_type_in_vs_multi_choice_anomaly(elements_that_have_no_type):

	"""
	@RETURN:

		'non_anomalous.'

		xor

		'anomalous.<followed by explanatory text>'
		

	The PURPOSE is to detect any time we have a sequence of
	response_items we *expect* it to be either:

	(1) a sequence of all TypeIn response objects followed by all
	MultiChoice Response Objects

	or

	(2) a sequence of all MultiChoice response objects followed by
	all TypeIn Response Objects

	Why?  Because it would seem funny if we have to render a
	type-in that is 'surrounded' by multi-choices.  I want to know
	if one of these happens bc I want to see how legacy AskMD
	website renders these to the end human user.

	Concretely, this function is looking for either:
	
		(1) a pattern where we have True initially changing to False and then Back to True.
		(1) a pattern where we have False initially changing to True and then Back to True.

	>>> detect_type_in_vs_multi_choice_anomaly([True])
	'non_anomalous.'

	>>> detect_type_in_vs_multi_choice_anomaly([False])
	'non_anomalous.'

	>>> detect_type_in_vs_multi_choice_anomaly([False, True, True])
	'non_anomalous.'

	>>> res1 = detect_type_in_vs_multi_choice_anomaly([False, True, False])
	>>> res1.startswith("anomalous.")
	True

	>>> res2 = detect_type_in_vs_multi_choice_anomaly([False, False, True, False])
	>>> res2.startswith("anomalous.")
	True

	>>> res3 = detect_type_in_vs_multi_choice_anomaly([False, False, False, True, False, False, False])
	>>> res3.startswith("anomalous.")
	True

	"""

	result = "presumed_non_anomalous."
	if elements_that_have_no_type[0] == True:
		for index, ele in enumerate(elements_that_have_no_type[1:]):
			if ele == False:
				if any(elements_that_have_no_type[index+1:]):
					result = f"anomalous. started at True at index={index} changed to False, and then there was a True after that in {elements_that_have_no_type}"

	elif elements_that_have_no_type[0] == False:
		for index, ele in enumerate(elements_that_have_no_type[1:]):
			if ele == True:
				#print("debug here")
				#pdb.set_trace()
				if not(all(elements_that_have_no_type[index+1:])):
					result = f"anomalous. started at False at index={index} changed to True, and then there was a False after that in {elements_that_have_no_type}"
	else:
		print("how did you get here?!?! (in @func detect_type_in_vs_multi_choice_anomaly)")
		pdb_set_trace()

	if result == "presumed_non_anomalous.":
		result = "non_anomalous."
	if result.split(".")[0] not in ["anomalous", "non_anomalous"]:
		print("hrm there is a bug in @func detect_type_in_vs_multi_choice_anomaly")
		pdb.set_trace()
	return(result)

################################################################

# As part of Refactor2022-07-02T08:53:21PDT I have removed
# findings_to_add from the arg sig here

def solicit_user_ans_to_the_multiple_choice_question(
	multi_choice_options, 
	user_reply_script_json, 
	record_user_replies_for_reply_filename, 
	conversation_log_filepath,
	consult_id, 
	sys_quest_num_str):

	user_selections_converted_to_findings = []

	# The 'old school' analog of this is:
	# 
	# 'Step 2: Solicit the User's Answer to the Multiple-Choice Question'
	#

	print()
	print()
	usr_prompt_txt = "\nWhat do you chose (answer must be an integer from choices listed above) "
	users_choice = utils.user_input_wrapper(usr_prompt_txt,
		user_reply_script_json,
		record_user_replies_for_reply_filename,
		choices = multi_choice_options)

	print()
	print()			

	if users_choice ==  "":
		users_choice = UserChoiceWasNoneOfTheAbove
	else:
		users_choice = int(users_choice)

	if users_choice != UserChoiceWasNoneOfTheAbove and (users_choice != 0) and (not(int(users_choice))):
		print(f"Need to answer with an integer and you answered with: {users_choice}")
		print("Please try again:")
		users_choice = int(users_choice)
		if (users_choice != 0) and (not(int(users_choice))):
			print(f"Once again, you need to answer with an integer and you answered with: {users_choice}")
			print("Let's enter the debugger")
			pdb.set_trace()

	################
	# The 'old school' analog of this is:
	# 'Step 3: Convert the Answer into a Finding and Add to the Finding List'
	# see ref ancho 2022-06-22T09:04:20PDT
	################

	print("User chose:", users_choice)

	if users_choice != UserChoiceWasNoneOfTheAbove:
		response_content_for_chosen_option = multi_choice_options[users_choice]

		# chosenfindingRecNo = response_content_for_chosen_option['respNo']
		# 2022-09-17T14:03:23PDT as part of Update2022-09-17
                # 'respNo' is going away and I currently believe that
                # 'entNo' can serve the purpose

		chosenfindingEntNo = response_content_for_chosen_option['entNo']
		chosenfindingName = response_content_for_chosen_option['name']

	if conversation_log_filepath: 
		utils.log(conversation_log_filepath, "")
		if users_choice != UserChoiceWasNoneOfTheAbove:
		
			#utils.log(conversation_log_filepath, f"UserReply {sys_quest_num_str} MultiChoice#: {users_choice} Text: {chosenfindingName}")
			# 2023-02-04T09:41:57PST changing the format of UserReply to the following			
			utils.log(conversation_log_filepath, f"UserReply: {users_choice} (MultiChoice#) Text: {chosenfindingName} {sys_quest_num_str} Cpd-{consult_id}")
			
		else:
		
			#utils.log(conversation_log_filepath, f"UserReply {sys_quest_num_str} MultiChoice#: not-a-number Text: {UserChoiceWasNoneOfTheAbove}")
			# 2023-02-04T09:41:57PST changing the format of UserReply to the following
			utils.log(conversation_log_filepath, f"UserReply: not-a-number (MultiChoice#) Text: {UserChoiceWasNoneOfTheAbove} {sys_quest_num_str} Cpd-{consult_id}")			
		utils.log(conversation_log_filepath, "")

	finding_to_add = {}

	if users_choice != UserChoiceWasNoneOfTheAbove:

		#finding_to_add['id'] = chosenfindingRecNo
		# 2022-09-17T14:12:33PDT the above was replaced with the below as part of Update2022-09-17
		finding_to_add['entNo'] = chosenfindingEntNo

		# DONE(2022-07-18T16:30:31PDT, 2022-09-17T14:12:33PDT) 
		# The old to do text was...
		#
		# <START QUOTE>
		#
		# might need to change the above to 'entNo' See
		# CONSYS-369.  If Michael gets rid of 'recNo' per the
		# JIRA, then, note this 2022-07-18 comment copied from
		# said JIRA:
		#
		# My tester adds an ‘id’ to the finding list based on
		# a user’s answer to a question.  The value of ‘id’ is
		# obtained from the value of ‘recNo’ when the bot
		# “poses the question” to the user/tester.  So, it
		# looks like Bill needs to merely change from using
		# ‘recNo’ to using 'fndNo’.
		#
		# <END QUOTE>

		finding_to_add['state'] = "PRESENT"

	

		#id_for_humans = f"Fnd-{chosenfindingName}-GenNo-{chosenfindingEntNo}-Cpd-{consult_id}-RecNum-{chosenfindingRecNo}"	
		#id_for_humans = utils.pretty_fnd_id(chosenfindingName, chosenfindingEntNo, consult_id, chosenfindingRecNo)
		#2022-09-17T14:15:10PDT the above was replaced with the below as part of Update2022-09-17
		id_for_humans = utils.pretty_fnd_id(chosenfindingName, chosenfindingEntNo, consult_id)

		finding_to_add['idForHumans'] = id_for_humans

		print("Users choice represented as a finding to add to the finding list:")
		finding_to_add_pretty_txt = json.dumps(finding_to_add, indent=4, sort_keys=True)
		print(finding_to_add_pretty_txt)

		user_selections_converted_to_findings.append(finding_to_add)
		# Soon (2022-07-02T09:19:27PDT) we will want to
		# support allowing the user to select more than one
		# option in a multiple choice thus let's keep this as
		# an append while we are doing
		# Refactor2022-07-02T08:53:21PDT

	return(user_selections_converted_to_findings)


################################################################