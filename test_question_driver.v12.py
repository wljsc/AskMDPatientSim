# test_question_driver.py
################################################################
# TODOs

# TODO(2022-05-19T12:50:27PDT, ) TODO TODO don't forget to log error in logs!!

# TODO(2022-05-19T11:24:56PDT, ) when writing to conversation_text.org and answer is not
# multiple choice include it in the log
#
# And also if there is only one choice like this, we do not see my responses:

# * USERS CHOICE 12 Answer#: 0 Text: toes turn white or blue
# * SYSTEM QUESTION  13: Have you had surgery or other procedure in the past few months?
# 0: surgery, joint injection, or other procedure to the foot or ankle in the past few weeks
# * SYSTEM QUESTION  14: If you have tried treating your foot or ankle problem, what did you do and did it help?
# 0: null
# * SYSTEM QUESTION  15: Do you have any of these muscle, joint, or bone symptoms?
# 0: episodes of joint pain always occur with fever
# 1: joint pain that migrates from joint to joint
# 2: one or more finger joints swollen
# 3: sausage-shaped finger
# 4: widening or thickening (clubbing) of the fingertips
# 5: wrist swollen
# 6: bone pain
# 7: back pain
# 8: cramping leg pain with use
# 9: calf pain
# * USERS CHOICE 15 Answer#: 0 Text: episodes of joint pain always occur with fever

# TODO(2022-05-19T11:49:07PDT, ) why does the bot list multiple choice but the website lists a type in
# [[<<Link-2022-05-19-Thu-11-52>>][(*)]]
#
# * SYSTEM QUESTION  24: Are you taking any medications?
# 0: estrogen
# 1: calcium channel blocker
# 2: glitazone
# * USERS CHOICE 24 Answer#: 0 Text: estrogen



################################################################
# HISTORY (start of section - put newest on top)


# 2022-06-10T17:15:24PDT test_question_driver.v12.py

# to be written up

# 2022-06-03T11:18:38PDT test_question_driver.v11.py

# decent stopping point before more changes.

# 2022-06-01T16:02:30PDT test_question_driver.v10.py

# crude version of auto mode WORKS!!!

# but in order to do a massive test of all the first two questions
# until error across all consults, I need to change the way
# conversation.org is formated.  So that will happen AFTER this
# version (i.e. 10)

# 2022-06-01T16:02:30PDT test_question_driver.v09.py

# beginning to implement 'auto mode'.  Problem is that I am doing it
# by reading from the file and it's all messed up.  So, abandoning
# that and instead going to read in whole file and do json.loads.
# Store the script as a list and we pop(0) the list to go through it.
# I have not started on the new json.loads approach and am freezing
# this version in case I want to abort the new approach.

# 2022-05-31T17:56:59PDT test_question_driver.v08.py

# did a TON of refactoring of the elements for the questions, very
# confusing bc there are the meaningless JSON elemets in the CPD db,
# and then different names in terms of what the bot presents of those,
# context dependence of meaning (e.g. response_content['name'] means
# 'multiple choice option' in the context of a multiple choice, but 
# nd there is also variability, like
#<START QUOTE FROM BELOW>
# Is this inconsistent or is there a method behind it, for TypeIn: 
#
# - for some, SubQuestionTxt: 'date of birth' and ResponseHeader: None
# - for others, SubQuestionTxt: 'null' and ResponseHeader: What is your height?
#<END QUOTE FROM BELOW>
#

# TODO(2022-05-31T18:00:48PDT, ) next actions - leaving this uncommented
# to that it shows up prominently when try to run: (1) each time there
# is input( (e.g. seeking user input) there will be a wrapper around
# those.  It will ask "are we in automatic mode", if not, ask the user,
# if so look up in the script.  The script is a json file which is a
# array.  the nth ele corresponds to the nth question.  the nth ele has
# things like questionseq number, consult id, questionID etc and so, at
# each turn it reads from the script and it asks itself, does this match
# what i expect? the script json for that turn will aslo say 'okay if it
# DOES match, then how do you response - e.g. for the 13th turn chose a
# random ele, for the 2nd give this answer text.  when recording a human
# users trace, this will be saved so that the script can be
# reconstructeed.  in the begining, it might be the bareset bone thing.
# e.g. just a list of answers.  e.g. like this:

# [response: '0'],
# [response: '12/28/1988'],
# [resposne: '71'],
# [resposne: '161']




# 2022-05-31T12:53:21PDT test_question_driver.v07.py (for real)

# alas this won't run bc the work started at 2022-05-31T12:28:39PDT is in mid-flight.

# 2022-05-31T12:53:07PDT realized I forgot to save test_question_driver.v07.py

# 2022-05-31T12:28:39PDT starting to work on automatic question answering.

# 2022-05-31T12:26:13PDT test_question_driver.v07.py (not really - see 2022-05-31T12:53:07PDT, immed above)

# i've fixed the formatted problem mentioned in v06.  not sure what
# else is different but i intuite it is generally better.

# 2022-05-23T16:10:33PDT test_question_driver.v06.py

# been tryingt to imporve the formatting but i messed something out
# i cut out big branch 2, or the essential meat of big branch 1.

# 2022-05-20T19:18:04PDT test_question_driver.v05.py

# we have the ability to handle an error by skipping to the next
# question. And we are about to improve the variety of responses to an
# error from the bot.

# Specfically, we are not quite, but about to add the ability to not
# only skip to the next question but also to essentially pretend the
# error dide not happen.  I.e. to take the input that caused the bot
# to error and edit that input, take the edited input and re-try.

# 2022-05-19T13:57:07PDT test_question_driver.v04.py

# in this version we've been using it for while.
# it has ability to pick up where left off (search for PickUpFromWhereYouLeftOff/)

# it has abiliyt to save the conversation to conversation_text.org so
# tyou can replay it on the website.

# it's got the beginnings of decent logging

# 2022-05-13T10:53:40PDT freezing test_question_driver.v03.py 

# it kinda works, but in the next version i want to try just taking
# the entire chosen response optioh and using that as the 'selected
# finding' rather than constructing a finding afresh.

# HISTORY (end of section)
################################################################
# IMPORTS

import os
import requests
import json
#import json-diff
from deepdiff import DeepDiff
import datetime as dt
from time import sleep
import pdb

################################################################
# CONSTANTS

MultipleChoice = "all in response_content_list have no type, thus they are all responses that are discrete multiple-choice type answers, i.e. not user typed in values"
TypeIn = "all eles in response_content_list have a type, thus they are all responses that want to have a user typed in value"

STEP_SLOWLY_P = False

CONVERSATION_INVARIANT_MODE_P = True

# For explanation of CONVERSATION_INVARIANT_MODE_P see...
# "2022-06-01T21:57:11PDT Example Justifying Why We need CONVERSATION_INVARIANT_MODE_P"
# ...in diary-TestCoupletPrograms.org.

def question_and_answer_loop(start_conversation_with, log_basedir = None, patient_sim_script_fpath = None, record_user_replies_for_reply_filename = None):

	"""

	@param start_conversation_with should be json that sets the state
	for the users reply.  

	If you want to start at the very beginning of consult, then if
	the consult number is CONSULT_NUMBER then
	start_conversation_with should be:

	{"consultationId": CONSULT_NUMBER}

	@param patient_sim_script_fpath if None, just operates as
	normal, or 'manual' mode.  I.e. the operator of this simulator
	gives answers to each question from the AskMD bot when prompted.

	For AUTO mode then @param patient_sim_script_fpath
	needs to point to a json file.  This file specifies for each
	user turn, what should be the response.

	@param record_user_replies_for_reply_filename is used if you
	want to 'record' the series of answers that the human operator
	of the patient simulator uses so that later that 'recording'
	can be 'played back' in automatic patient simulator mode.  The
	file it saves is a JSON so best to name the file with a .json
	suffix.

	"""

	if patient_sim_script_fpath is None:
		user_reply_script_json = None
		print("SIMULATOR MODE IS MANUAL")
	else:
		with open(patient_sim_script_fpath, 'r') as user_reply_script_fileobj:
		 	user_reply_script_json = json.load(user_reply_script_fileobj)
		print(f"SIMULATOR MODE IS AUTOMATIC - following script described in {patient_sim_script_fpath}")

	if record_user_replies_for_reply_filename:
		with open(record_user_replies_for_reply_filename, 'w') as record_fobj:
			print("[", file = record_fobj)
			# the script is a list of json objects.  Thus at start time we need to start the list with a [
			# TODO(2022-06-01T17:24:37PDT, ) give an ] for the end of the script!!
			
	#print("Just entered question_and_answer_loop()")
	# pdb.set_trace() commented out bc see 2022-05-12T08:49:02PDT
	#print("Just entered question_and_answer_loop()")	

	if type(start_conversation_with) == int:
		initiate_conversation_json = {"consultationId": start_conversation_with}
		question_index_seq = 0
		
	elif type(start_conversation_with) == str:
		initiate_conversation_json = read_json_file(start_conversation_with)
		question_index_seq = initiate_conversation_json.get('questionIndexSeq', -777)
	else:
		print("Unexpected type for @param start_conversation_with ")
		pdb.set_trace()
		
	consultation_id = initiate_conversation_json['consultationId']

	print("################################################################")
	print(f"##### Starting Dialog: Consult {initiate_conversation_json['consultationId']} ######")
	print("################################################################")

	users_reply = json.dumps(initiate_conversation_json)
	
	if log_basedir is not None:
		sub_dir_for_this_run = f"Consult.{now_yyyy_mm_ddThhmm()}-Cpd-{consultation_id}"
		log_dir = os.path.join(log_basedir, sub_dir_for_this_run)
		os.mkdir(log_dir)

	else:
		log_dir = None

	if log_dir is not None:
		conversation_log_filepath = os.path.join(log_dir, "conversation_text.org")
	else: 
		conversation_log_filepath = None

	while True:

		bot_output, user_input_json, question_seq_index = post_next(users_reply, log_dir, question_index_seq, conversation_log_filepath)

		error_msg = bot_output.get('error')
		if error_msg:

			print()
			print("Ugh, we posted @param payload (i.e. json representation of user response and finding list) and the bot is returning an error!!!")
			print("you might want to look at the value of @param payload to see if something was formatted in an obviously bad way")
			print()
			print("Here is the error msg:")

			question_id = user_input_json['questionId']
			if CONVERSATION_INVARIANT_MODE_P:
				sys_quest_num_str = f"QuesSeq# {question_seq_index}"
			else:
				sys_quest_num_str = f"QuesSeq# {question_seq_index} QuesID# {question_id}"			
			string_to_log_and_print = f"BotReplies with Error to {sys_quest_num_str}\nBotError JSON is:\n{error_msg}\n"
			log(conversation_log_filepath, string_to_log_and_print)
			

			print()
			print(error_msg)
			print()
			options = ["skip to next question", "edit the payload and post again", "go into the debugger", "quit"]
			options_listing = ""
			for nth, option_txt in enumerate(options):
				options_listing += f"\n{nth}: {option_txt}"
			print("Would you like to:", options_listing)
			#user_reply_text = user_input_wrapper("Type In Your Choice Here: ")
			user_reply_text = user_input_wrapper("Type In Your Choice Here: ", user_reply_script_json, record_user_replies_for_reply_filename)
			user_reply_int = int(user_reply_text)
			choice_txt = options[user_reply_int]

			string_to_log_and_print = f"UserReply to BotError for {sys_quest_num_str} is: '{choice_txt}'\n"
			print(string_to_log_and_print)
			log(conversation_log_filepath, string_to_log_and_print)
			
			if choice_txt == "skip to next question":
				# TODO(2022-05-20T10:56:00PDT, ) log this.
				users_reply = skip_to_next_question(user_input_json)
				continue
				
			elif choice_txt == "edit the payload and post again":
				print("Okay, you chose to edit the payload and post again.")
				print()
				print("So, how do you go about editing the payload?")
				print()
				print("Well, what you need to do is take the value of @param user_input,")
				print("Next edit that value and bind that new value to @param users_reply (a string, not a dict)")
				print("And then continue from the error that we are about to enter")
				pdb.set_trace()
				continue
			
			elif choice_txt == "go into the debugger":
				print("Okay, we will enter the debugger so you can decide what to do.")
				# TODO(2022-05-20T10:55:36PDT, ) log this.
				pdb.set_trace()
				
			elif choice_txt == "quit":
				#exit()
				return("Program Done!!")
			
			else:
				print("Unexpected option, whats going on!?!?!")
				pdb.set_trace()

		
		users_reply, question_index_seq = process_system_reply(bot_output, log_dir, conversation_log_filepath, user_reply_script_json, record_user_replies_for_reply_filename)
		


#!! return(user_response_object_str, question_index_seq)


# 2022-05-24T11:25:18PDT looking for question_id

def post_next(payload, log_dir, question_seq_index, conversation_log_filepath):
	# 2022-05-16T11:26:00PDT prolly delete question_seq_index are all things with this timestamp

	"""

	log_dir, question_seq_index

	>>> result_json = post_next('{"consultationId": 14 }')
	>>> result_json == Result_from_start_Consult14
	True

	# If there is a diff, try this:
	# >>> the_diff = DeepDiff(result, Result_from_start_Consult14)
	# >>> the_diff_pretty = json.dumps(the_diff, indent=4, sort_keys=True)
	# >>> print(the_diff_pretty)

	"""
	print("################################################################")
	print("### Just Entered @fun post_next ################################")
	print("################################################################")
	print()
	
	payload_as_dict = json.loads(payload)
	question_id = payload_as_dict.get('questionId', "NoQuestionIdSpecified")
	
	print(f"#### Payload for User Answer to Ques QuesSeq# {question_seq_index} QuesID# {question_id}")
	print("#### Payload (start of json object) ####")
	print()
	print(json.dumps(payload_as_dict, indent = 4, sort_keys = True))
	print()	
	print("#### Payload (end of json object) ####")

	print()
	#print("Just entered post_next - is the input (payload) - see if you can get 'unable to move there or whatever'")
	# pdb.set_trace() commented out bc see 2022-05-12T08:49:02PDT
	#print("Just entered post_next - is the input (payload) - see if you can get 'unable to move there or whatever'")	

	url = 'https://api.dev.sharecare.com/consultation/next'
	#payload = '{    "consultationId": 14 }' 
	headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

	r = requests.post(url, data=payload, headers=headers)
	
	result_json = json.loads(r.text)
	#pdb.set_trace()
	#result_str = json.dumps(result_json, indent=4, sort_keys=True)

	error_msg = result_json.get('error')
	if error_msg:

		question_seq_index += 1
		if question_seq_index > 10:
			question_seq_index_str = "0" + str(question_seq_index)
		else:
			question_seq_index_str = str(question_seq_index)

		question_id = "NoID-BcBotError"
		
		error_report_string = f"""
		################################################################
		Dag Nabit! We are getting an error.  Here it is:
		
		{error_msg}
		
		################################################################
		Here is the payload that was posted to the bot that resulted in the error:

		{payload}

		################################################################
		"""

		print(error_report_string)
		
		if log_dir is not None:
			out_filename = f"Q{question_seq_index_str}-bot-quest-Id-{question_id}.json"
			out_fpath = os.path.join(log_dir, out_filename)
			with open(out_fpath, 'w') as out_obj:
				print(error_report_string, file=out_obj)

			# What to say in the conversation_text.org file
			if CONVERSATION_INVARIANT_MODE_P:
				sys_quest_num_str = f"QuesSeq# {question_seq_index}"			
			else:
				sys_quest_num_str = f"QuesSeq# {question_seq_index} QuesID# {question_id}"
			string_to_log_and_print = f"{sys_quest_num_str} ResponseHeader: BotError"
			print(string_to_log_and_print)
			log(conversation_log_filepath, string_to_log_and_print)


		# print("################################################################")
		# print("Dag Nabit! We are getting an error.  Here it is:")
		# print()
		# print(error_msg)
		# print()
		# print("################################################################")

		
	# TODO(2022-05-20T19:36:11PDT, ) if exiting this fnwith error, maybe log that fact?"

	print("################")

	if CONVERSATION_INVARIANT_MODE_P:
		sys_quest_num_str = f"QuesSeq# {question_seq_index} (ConsultID {payload_as_dict['consultationId']})"
	else:
		sys_quest_num_str = f"QuesSeq# {question_seq_index} QuesID# {question_id} (ConsultID {payload_as_dict['consultationId']})"

	print(f"Bot Response is {sys_quest_num_str}")

	print("Bot JSON Response To Users Post (start of section)")

	print()
	pretty_result_json_str = json.dumps(result_json, indent=4, sort_keys=True)
	print(pretty_result_json_str)
	print()

	print("Bot JSON Response To Users Post (end of section)")
	print("################")
		
	if log_dir is not None:
		if error_msg:
			#print("okay, this is just nagware to log this error !!")
			#pdb.set_trace()
			# TODO(2022-06-01T22:13:10PDT, ) i am pretty sure the nag is no longer needed, 
			# it already logs the error - soewhere else, right?
			pass

		else:

			# 2022-05-16T11:26:00PDT prolly delete this all with this timestamp
			# if question_seq_index is None:
			# 	question_number_str = "Unknown"
			# else:
			# 	question_number_str = str(question_seq_index)
			# out_filename = "bot-reply-{question_number_str}-Q.json"

			# There is no error, so let's get the
			# question_seq_index from the json rather than
			# incrementing it.
	
			question_seq_index = result_json['questionIndexSeq']
			question_id = result_json['questionId']
	
			if question_seq_index > 10:
				question_seq_index_str = "0" + str(question_seq_index)
			else:
				question_seq_index_str = str(question_seq_index)
				
			out_filename = f"Q{question_seq_index_str}-bot-quest-Id-{question_id}.json"
			
			out_fpath = os.path.join(log_dir, out_filename)
			with open(out_fpath, 'w') as out_obj:
				print(pretty_result_json_str, file=out_obj)

	#### return from post_next
	return(result_json, payload_as_dict, question_seq_index)
	#### return from post_next


# print("################################################################")
# print('################ {"consultationId": 14 } ################')
# print(json.dumps(post_next('{"consultationId": 14 }'), indent=4, sort_keys=True))

# Comment This Out - some error
# answer_to_quest21_consult_14_How_long_ago_did_your_foot_or_ankle_problem_begin = \
# {
#     "myquestionId": "question-21-consultation-14-How long ago did your foot or ankle problem begin",
#     "questionId": "21",
#     "consultationId": 14,
#     "findings": [
#         {
#             "id": 18,
#             "valueObject": {
#                 "value": "71",
#                 "valueType": "LENGTH",
#                 "valueTypeUnit": 4,
#                 "format": "INT"
#             },
#             "state": "PRESENT"
#         },
#         {
#             "id": 12,
#             "valueObject": {
#                 "value": "205",
#                 "valueType": "WEIGHT",
#                 "valueTypeUnit": 2,
#                 "format": "INT"
#             },
#             "state": "PRESENT"
#         },
#         {
#             "id": 184,
#             "myfindingId": "male-finding-184",
#             "state": "PRESENT"
#         },
#         {
#             "id": 181,
#             "myfindingId": "date-of-birth-finding-181",
#             "valueObject": {
#                 "value": "12/29/1988",
#                 "valueType": "DATE",
#                 "format": "DATE"
#             },
#             "state": "PRESENT"
#         },
#         {
#             "id": "27",
#             "myFindingId": "past 24 hours finding-27-consultation-14",
#             "state": "PRESENT"
#         }
#     ]
# }



answer_to_quest21_consult_14_How_long_ago_did_your_foot_or_ankle_problem_begin = \
'{"questionId": 21, "consultationId": 14}'

# print('################################################################')
# print('################ System Reply To: How long ago did your foot or ankle problem begin ################')

# print(json.dumps(post_next(answer_to_quest21_consult_14_How_long_ago_did_your_foot_or_ankle_problem_begin), indent=4, sort_keys=True))

# system_reply_to_quest21_consult_14_ankle_problem_began_last_24_hours = post_next(answer_to_quest21_consult_14_How_long_ago_did_your_foot_or_ankle_problem_begin)

CONSTRUCT_FINDING_VALUE_OBJECT_DE_NOVO_P = False

#def process_system_reply(json_input, remembered_consult_id, log_dir):
# Shortly after 2022-05-16T13:16:48PDT you can delete the above commented out def
def process_system_reply(json_input, log_dir, conversation_log_filepath, user_reply_script_json, record_user_replies_for_reply_filename):
	"""

	This function receives some input - a dict.  The intput is the
	bot response.

	Usually that response contains what questions to ask the user.

	Thus this function, extract the questions and the multiple
	choice responses, prints them out for the user.

	Collects the users response and assembles it and finding list?
	question number etc into a form that the bot wants.

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

	question_title = json_input['title']

	# yee olde waye...
	#sys_quest_num_str = f"QuesSeq# {question_seq_index} QuesId# {question_id}" # TODO maybe we want to add consult id here, too?

	# ....yee slightly newer waye...
	# sys_quest_num_str = f"QuesSeq# {nth_question} QuesId# {question_id}" 
	# TODO maybe we want to add consult id here, too?...maybe not.
	# Why maybe not?
	# Well, this will make it harder to compare conversation.org files bc even if the sequence of questions and answers
	# is exactly the same, the traces will differ bc the consult id is different.  This issue is why we need to have 
	# CONVERSATION_INVARIANT_MODE_P

	# ...yee newest waye...

	if CONVERSATION_INVARIANT_MODE_P:
		sys_quest_num_str = f"QuesSeq# {nth_question}"
	else:
		sys_quest_num_str = f"QuesSeq# {nth_question} QuesId# {question_id}" 

	my_next_question_id = json_input['nextQuestionId']
	
	# Why gather my_next_question_id?  In order to process the
	# json_input, query the user, and assembe a valid json reply
	# based on user's answer(s) we do not need 'nextQuestionId'.
	# However, we want to get the value so that if we post a reply
	# to the bot and bot throws an error, then we can see in our
	# reply what is the next question id.  Thus, in case the bot
	# replies with an error, we post another reply to the bot that
	# says, 'okay, skip that question and lets go to the next one'
	
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

	top_level_question_description = f"BotAsks {sys_quest_num_str} Title: '{question_title}'"

	print("################################################################")
	print(top_level_question_description)
	log(conversation_log_filepath, top_level_question_description)

	findings_to_add = []

	for resp_section_num, response_section in enumerate(response_sections):

		response_header =  response_section['header']

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
			print("Weird, why is @param response_content_list empty!?!?!")
			pdb.set_trace()
		
		elements_that_have_no_type = []
		for ele in response_content_list:
			#has_no_type_p = ele['findingValue']['type'] == 'NONE'
			has_no_type_p = ele['findingValue']['type'].lower() == 'none'
			elements_that_have_no_type.append(has_no_type_p)

		if all(elements_that_have_no_type):
			response_content_list_choice_mode = MultipleChoice
		elif any(elements_that_have_no_type):
			print("This is odd we have some possible_user_responses that are like multiple choice and others that are typein.  What's going on here?")
			pdb.set_trace()
		else:
			response_content_list_choice_mode = TypeIn

		################
		# Big Branch 1: Give a type-in value for each response ele
		################

		if response_content_list_choice_mode == TypeIn:

			print()
			print(f"RESPONSE_SECTION {resp_section_num + 1} is a Type-In Question")
			print()

			################
			# TypeIn Step 1: TODO not sure what to call this, just mimicing what the 3? Steps we have for multiple choice
			################

# What is response_header?  
# In Cpd-14:
# BotAsks QuesSeq# 1 QuesId# 68 Title: Birth sex, date of birth
# 
# BotAsks QuesSeq# 2 QuesId# 10 Title: Height and weight
# 
# Is this inconsistent or is there a method behind it, for TypeIn: 
#
# - for some, SubQuestionTxt: 'date of birth' and ResponseHeader: None
# - for others, SubQuestionTxt: 'null' and ResponseHeader: What is your height?


			text_description_of_systems_typein_turn = \
\
f"""BotSubQuestion# {resp_section_num + 1} of {num_response_sections}:
AnswerFormat: TypeIn
ResponseHeader: '{response_header}"""

			print(text_description_of_systems_typein_turn)
			log(conversation_log_filepath, text_description_of_systems_typein_turn)

			# For TypeIn
			for response_number, response_content in enumerate(response_content_list):

				if len(response_content_list) != 1:
					print("WHAT!!! At 2022-05-31T14:59:42PDT Bill was moderately certain that any type in question would only have exactly one element in response_content_list but his lenght is:", len(response_content_list))
					print("Yes at 2022-05-31T16:50:36PDT he believes that this is not = 1 only if we have a multiple choice question bc each response_content is a possible multi-choice answer")
					pdb.set_trace()

			# TODO(2022-05-31T16:50:36PDT, ) if the belief
			# desribed at 2022-05-31T16:50:36PDT turns out
			# to be true, maybe in rename
			# response_content_list to
			# multiple_choice_options IN THE MULTI-CHOICE
			# section, but prolly NOT this section.


		# 2022-05-31T14:57:27PDT more printing changes, hopw they are okay (START OF SECTION)
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

				response_txt = response_content['name']

				# 2022-05-31T14:43:10PDT just removed the below, such removal should not cause an error.
				# once sure of removal, then delete
				# 2022-05-31T14:50:11PDT looks like we should be good, after 1 day, blow away!!
				# sys_quest_num_str = f"Bot QuesSeq# {question_seq_index} QuesId# {question_id}"

				#text_description_of_systems_typein_turn = f"Bot TypeIn Resp# {response_number}: {response_txt}"
				# 2022-05-31T12:46:40PDT renaming Resp to BotSubQuestion# {response_number} (TypeIn)
				# text_description_of_systems_typein_turn = f'BotSubQuestion# {response_number}: SubQuestionTxt: "{response_txt}" AnswerFormat: TypeIn'
				# 2022-05-31T15:06:52PDT more changes

# 2022-05-31T17:18:58PDT moving this out of the loop to be analogous to how we do it with multiple choie
# 				text_description_of_systems_typein_turn = \
# \
# f"""BotSubQuestion# {resp_section_num + 1} of {num_response_sections}:
# SubQuestionTxt: '{response_txt}'
# AnswerFormat: TypeIn
# ResponseHeader: '{response_header}"""
				
				# What is response_header?  
				# In Cpd-14:
				# BotAsks QuesSeq# 1 QuesId# 68 Title: Birth sex, date of birth
				# 
				# BotAsks QuesSeq# 2 QuesId# 10 Title: Height and weight
				# 
				# Is this inconsistent or is there a method behind it, for TypeIn: 
				#
				# - for some, SubQuestionTxt: 'date of birth' and ResponseHeader: None
				# - for others, SubQuestionTxt: 'null' and ResponseHeader: What is your height?

				text_description_of_response_txt_for_typein = f"Bot SubQuestionTxt: '{response_txt}'"
				print(text_description_of_response_txt_for_typein)
				log(conversation_log_filepath, text_description_of_response_txt_for_typein)


				print()
				print("defaultUnit: ", response_content['findingValue']['defaultUnit'])
				print("allowable units are: ", response_content['findingValue']['units'])

				response_type = response_content['findingValue']['type']
				
				print()
				print()				
				usr_prompt_txt = f"\nPlease enter a value of type {response_type}: "
				user_type_in_response = user_input_wrapper(usr_prompt_txt, user_reply_script_json, record_user_replies_for_reply_filename)
				print()
				print()				

				# 2022-05-31T14:43:10PDT just removed the below, such removal should not cause an error.
				# once sure of removal, then delete
				# 2022-05-31T14:50:11PDT looks like we should be good, after 1 day, blow away!!
				# sys_quest_num_str = f"QuesSeq# {question_seq_index} QuesId# {question_id}"

				# text_description_of_users_turn = f"UserReply {sys_quest_num_str} (TypeIn) Resp# {response_number}: {user_type_in_response}"
				# ... per 2022-05-31T12:46:40PDT (see above) renaming ...
				# text_description_of_users_turn = f"UserReply (TypeIn) to {sys_quest_num_str} SubQuestion# {response_number}: {user_type_in_response}"
				# .. 2022-05-31T15:11:48PDT using different variables ...
				text_description_of_users_turn = f"UserReply (TypeIn) to {sys_quest_num_str} SubQuestion# {resp_section_num}: {user_type_in_response}"

				print()
				print(text_description_of_users_turn)
				print()				

				log(conversation_log_filepath, "")
				log(conversation_log_filepath, text_description_of_users_turn)
				log(conversation_log_filepath, "")
				
				finding_to_add = convert_user_type_in_val_to_finding(user_type_in_response, response_content, consult_id)

				if STEP_SLOWLY_P:				
					print("################################################################")
					print("2022-05-27T09:57:47PDT hey, hey, hey about to append to findings_to_add in type-in mode")
					print("finding_to_add is", finding_to_add)
					print("findings_to_add is", findings_to_add)

				findings_to_add.append(finding_to_add)

				if STEP_SLOWLY_P:				
					print("Do you want to see what the findings_to_add looks like now, after adding?")
					pdb.set_trace()
					print("################################################################")


			if STEP_SLOWLY_P:				
				print("2022-05-20T15:48:48PDT hey, we are just about to append to findings_to_add in type-in mode")
				print("so what is the curent valu of findings_to_add ?")
				pdb.set_trace()

			
		################
		# Big Branch 2: Multiple Choice
		################

		elif response_content_list_choice_mode == MultipleChoice:

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
			log(conversation_log_filepath, text_description_of_systems_multichoice_turn)

			# For MultiChoie
			for nth_choice, response_content in enumerate(response_content_list):

				# TODO(2022-05-31T16:50:36PDT, ) see
				# 2022-05-31T16:50:36PDT above for
				# maybe renaming response_content_list
				# to multiple_choice_options

				response_txt = response_content['name']

				# what is 'name' well,
				# response_content is ele in response_content_list
				# response_content_list is from response_section['responses']
				# response_section is from response_sections (a list)

				# response_sections is from original
				# json_input to this func
				# (i.e. process_system_reply)
				# 'responseSections'

				################
				# 2022-05-31T16:40:15PDT Yee Olde Waye Has Been Commented Out and replace with see 2022-05-31T16:40:39PDT
				#text_description_of_systems_multichoice_turn = f"{sys_quest_num_str} MultiChoiceOption # {nth_choice}: {response_txt}"
				#text_description_of_systems_multichoice_turn = f"Bot MultiChoiceOption # {nth_choice}: {response_txt}"
				#print(text_description_of_systems_multichoice_turn)
				#log(conversation_log_filepath, text_description_of_systems_multichoice_turn)

				# 2022-05-31T16:54:42PDT but then
				# maybe delete the above
				# (i.e. 2022-05-31T16:40:15PDT) as I
				# realize that this is probly to articualte the multiple choices.
				text_description_of_response_txt_for_multichoice = f"Bot MultiChoiceOption # {nth_choice}: {response_txt}"
				print(text_description_of_response_txt_for_multichoice)
				log(conversation_log_filepath, text_description_of_response_txt_for_multichoice)

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

			print()
			print()
			usr_prompt_txt = "\nWhat do you chose (answer must be an integer from choices listed above) "
			users_choice = user_input_wrapper(usr_prompt_txt, user_reply_script_json, record_user_replies_for_reply_filename)
			print()
			print()			
			
			users_choice = int(users_choice)

			if (users_choice != 0) and (not(int(users_choice))):
				print(f"Need to answer with an integer and you answered with: {users_choice}")
				pdb.set_trace()

			################
			# Step 3: Convert the Answer into a Finding and Add to the Finding List
			################

			response_content = response_content_list[users_choice]
			chosenfindingRecNo = response_content['respNo']
			chosenfindingEntNo = response_content['entNo']
			chosenfindingName = response_content['name']

			print("User chose:", users_choice)

			# 2022-05-31T14:43:10PDT just removed the below, such removal should not cause an error.
			# once sure of removal, then delete
			# 2022-05-31T14:50:11PDT looks like we should be good, after 1 day, blow away!!
			#sys_quest_num_str = f"QuesSeq# {question_seq_index} QuesId# {question_id}"

			log(conversation_log_filepath, "")
			log(conversation_log_filepath, f"UserReply {sys_quest_num_str} MultiChoice#: {users_choice} Text: {chosenfindingName}")
			log(conversation_log_filepath, "")

			finding_to_add = {}
			
			finding_to_add['id'] = chosenfindingRecNo
			finding_to_add['state'] = "PRESENT"

			id_for_humans = f"Fnd-{chosenfindingName}-GenNo-{chosenfindingEntNo}-Cpd-{consult_id}-RecNum-{chosenfindingRecNo}"
			finding_to_add['idForHumans'] = id_for_humans

			print("Users choice represented as a finding to add to the finding list:")
			finding_to_add_pretty_txt = json.dumps(finding_to_add, indent=4, sort_keys=True)
			print(finding_to_add_pretty_txt)

			# print("2022-05-20T15:48:48PDT hey, we are just about to append to findings_to_add in multiple choice mode")
			# print("so what is the curent valu of findings_to_add ?")
			# pdb.set_trace()
			
			findings_to_add.append(finding_to_add)

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



	if STEP_SLOWLY_P:
		print()
		print()				
		print("So look at findings_to_add, do they seem ok?")
		print(json.dumps(findings_to_add, indent = 4, sort_keys = True))
		pdb.set_trace()

	updated_findings_list = json_input["findings"] + findings_to_add

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
			
		out_filename = f"Q{nth_question_str}-user-reply-Id{question_id}.json"
		out_fpath = os.path.join(log_dir, out_filename)
		with open(out_fpath, 'w') as out_obj:
			print(json.dumps(user_response_object, indent=4, sort_keys=True), file=out_obj)

	#### returning from process_system_reply			
	#return(user_response_object_str, question_seq_index)
	return(user_response_object_str, nth_question)
	#### returning from process_system_reply

def convert_user_type_in_val_to_finding(user_type_in_response, response_content, consult_id):

	valued_finding_to_add = {}

	if STEP_SLOWLY_P:

		print()
		print()				
		print("We've just entered @func convert_user_type_in_val_to_finding")
		pdb.set_trace()

	finding_recno = response_content['respNo']

	# 2022-05-20T21:04:30PDT changed finding_recno to int(finding_recno)
	# hoping to fix issue
	valued_finding_to_add['id'] = int(finding_recno)

	finding_entity_number = response_content['entNo']
	
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
	print("Assemble the choice thing")
	pdb.set_trace()
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

	
	finding_name = response_content['name']

	rec_num = response_content['respNo']

	id_for_humans = f"Fnd-{finding_name}-GenNo-{finding_entity_number}-Cpd-{consult_id}-RecNum-{rec_num}"
	valued_finding_to_add['idForHumans'] = id_for_humans

	if STEP_SLOWLY_P:

		print()
		print()				

		print("Check @param valued_finding_to_add to see if you like what we are going to return from convert_user_type_in_val_to_finding")
		pdb.set_trace()
	
	return(valued_finding_to_add)

# Can prolly comment this out
# def skip_to_next_question_bc_of_error_p(bot_reply):
# 	if (bot_reply.get('re_write_this_post_as_next_question')):
# 		return(True)
# 	else:
# 		return(False)	

def skip_to_next_question(user_input_json):

# skip_to_next_quesiton is a misnomer.  It really skips two questions.
# see
# [[file:~/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/diary-TestCoupletPrograms.org::Link-2022-05-25-Wed-22-36][this]]
# for the full explanation.  TODO we can probably do a real skip this question.

	"""This function is intended to be used if the bot has errored
	out and we want to somehow skip over the question that caused
	the bot to error out.  So, takes the original user_input which
	says it as a reply to question number N and makes it tell a
	lie.  It makes it say I am not for question number N, I am for
	question number N+1.  In this way it convinces the bot to skip
	to the next question.  user_input has to have the special
	'myNextQuestionId' added to it before being called so that it
	knows that record number of then nth +1 question."""
	
	#user_response_obj = json.loads(user_input)

	user_input_json['questionId'] = user_input_json['myNextQuestionId']
	user_input_json['myNextQuestionId'] = "There is no next Question Id bc we've already skip / advanced to the next question!!!"
	user_response_str = json.dumps(user_input_json)
	return(user_response_str)

def exit_if_no_more_questions(bot_reply):
	if bot_reply['questionId'] is None:
		if len(bot_reply['responseSections']) == 0:
			print("################################################################")
			print("# Congratulations, you answered the last question, we're done. #")
			print("################################################################")
			exit()
		else:
			print("################################################################")
			print("# Odd, reponseSections is the empty list, but questionId is None #")
			print("################################################################")
			print("Entering debugger so you can diagnose.")
			pdb.set_trace()
	if len(bot_reply['responseSections']) == 0:
		print("################################################################")
		print("# Odd, reponseSections is the empty list yet questionId is not None #")
		print("################################################################")
		print("Entering debugger so you can diagnose.")
		pdb.set_trace()
	else:
		return()

def user_input_wrapper(prompt_text, user_reply_script_json = None, record_user_replies_for_reply_filename = None):
	"""TODO consider merging this with the currently (2022-06-01) unused fn called handle_user_input(prompt_text)"""

	#print("Just called user_input_wrapper")
	#pdb.set_trace()

	if user_reply_script_json is None:
		user_reply_txt = input(prompt_text)
	else:
		current_user_reply_json = user_reply_script_json.pop(0)
		user_reply_txt = current_user_reply_json['user_reply_txt']
		print("AUTO MODE: user_reply_txt is:", user_reply_txt)

	if record_user_replies_for_reply_filename:
		with open(record_user_replies_for_reply_filename, 'a') as record_fobj:
			user_turn_json = json.dumps({"user_reply_txt" : user_reply_txt})
			new_json_obj_to_write = user_turn_json + ","
			print(new_json_obj_to_write, file = record_fobj)

	return(user_reply_txt)

def handle_user_input(prompt_text):
	"""
	if user types n that means none of the above.
	if user types e that means enter debugger.
	if user types s that means list the sequence of questiojs and answers given so far in user friendly English
	if user types j that means see the json input that we are processing
	if the user types in p that means see what the users post was
	"""
	print("""In addition there are these 'meta' options:
	n none of the above options.p
	e that means enter debugger.
	s list sequence of questions and answers given so far in user friendly English (e.g. to faciliate replication on AskMD)
	j see the json input that we are processing	
	if the user types in p that means see what the users post was""")
	

	users_choice = input(prompt_text)
	if users_choice == 'e':
		pass

def log(filepath, text):
	with open(filepath, 'a') as out_fobj:
		print(text, file=out_fobj)
		
def read_json_file(filepath):
	with open(filepath, 'r') as in_obj:
		json_data = json.load(in_obj)
		return(json_data)

def now_yyyy_mm_ddThhmm():
	"""return current time in a filename friendly format"""
	return(dt.datetime.now().strftime("%Y-%m-%dT%H%M"))

def now_yyyy_mm_ddThhmmss():
	"""return current time in a filename friendly format"""
	return(dt.datetime.now().strftime("%Y-%m-%dT%H%M%S"))


#process_system_reply(system_reply_to_quest21_consult_14_ankle_problem_began_last_24_hours)

#question_and_answer_loop({"consultationId": 14})

#question_and_answer_loop(start_conversation_with = "PickUpFromWhereYouLeftOff/consult-14-conv-01-QID-55-surgury-in-past-few-months.json", log_basedir = "../TstCoupProgLogs/")
#question_and_answer_loop(start_conversation_with = "PickUpFromWhereYouLeftOff/consult-14-conv-01-QID-55-surgury-in-past-few-months-female.json", log_basedir = "../TstCoupProgLogs/")

#question_and_answer_loop({"consultationId": 62}, log_basedir = "../TstCoupProgLogs/")


# 2022-05-19T12:56:31PDT trying shortest consult: stress managment
#question_and_answer_loop(155, log_basedir = "../TstCoupProgLogs/")

#question_and_answer_loop(start_conversation_with = "PickUpFromWhereYouLeftOff/consult_62_conv_Q1_QID_1_what_is_your_height.json", log_basedir = "../TstCoupProgLogs/")
# 2022-05-19T13:34:38PDT this dies early on, i forget why/



#question_and_answer_loop(start_conversation_with = "PickUpFromWhereYouLeftOff/consult_62_conv_Q1_QID_1_what_is_your_height_try2.json", log_basedir = "../TstCoupProgLogs/")



#question_and_answer_loop(14, log_basedir = "../TstCoupProgLogs/")

#question_and_answer_loop(62, log_basedir = "../TstCoupProgLogs/")
#question_and_answer_loop(1000, log_basedir = "../TstCoupProgLogs/")

#question_and_answer_loop(3, log_basedir = "../TstCoupProgLogs/")
#question_and_answer_loop(1001, log_basedir = "../TstCoupProgLogs/")
#question_and_answer_loop(1000, log_basedir = "../TstCoupProgLogs/")

#question_and_answer_loop(1003, log_basedir = "../TstCoupProgLogs/")

#question_and_answer_loop(14, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = None, record_user_replies_for_reply_filename = "test_record_14.01.json")

#question_and_answer_loop(14, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "test_record_14.01.json", record_user_replies_for_reply_filename = None)
#question_and_answer_loop(62, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "test_record_14.01.json", record_user_replies_for_reply_filename = None)

#question_and_answer_loop(3, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "test_record_14.01.json", record_user_replies_for_reply_filename = None)
#question_and_answer_loop(4, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "test_record_14.01.json", record_user_replies_for_reply_filename = None)
#question_and_answer_loop(6, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "test_record_14.01.json", record_user_replies_for_reply_filename = None)
#question_and_answer_loop(7, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "test_record_14.01.json", record_user_replies_for_reply_filename = None)

# Cpd-0008.json
# Cpd-0009.json
# Cpd-0011.json
# Cpd-0014.json
# Cpd-0015.json
# Cpd-0016.json

#for db in [8, 9, 11, 14, 15, 15]:
	# oops, repeated 15 caused a problem
#	question_and_answer_loop(db, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "test_record_14.01.json", record_user_replies_for_reply_filename = None)
	#sleep(1.3)
#	sleep(2)

# Cpd-0016.json

def run_patient_sim_script_over_consults(consults_descriptor, patient_sim_script_fpath, log_basedir = "../TstCoupProgLogs/"):


	"""

	@param log_basedir : you can just use the default.  But if you
	have a batch run and you want all the results to live in an
	exclusive dir, then you might say e.g.

	log_basedir = "../TstCoupProgLogs/CONSYS-299"

	"""
	
	list_of_db_numbers = obtain_db_numbers(consults_descriptor)

	if not(os.path.exists(patient_sim_script_fpath)):
		print("Error @param patient_sim_script_fpath points to a file that does not exist.")
		print("Maybe there is a typo in the value you have for @param patient_sim_script_fpath or you forgot to save a file at that location?")
		print("The value of @param patient_sim_script_fpath is:")
		print(patient_sim_script_fpath)
		pdb.set_trace()
	
	if not(os.path.exists(log_basedir)):
		os.mkdir(log_basedir)

	for just_the_db_number in list_of_db_numbers:

		print("################################################################")
		print("################################################################")
		print(f"# Calling question_and_answer_loop on CPD {just_the_db_number} #")
		print("################################################################")
		print("################################################################")

		question_and_answer_loop(just_the_db_number, log_basedir = log_basedir, patient_sim_script_fpath = patient_sim_script_fpath, record_user_replies_for_reply_filename = None)

		#!!! TODO uncomment this, remove the line above (2022-06-03T15:55:49PDT)
		# try:
		# 	question_and_answer_loop(just_the_db_number, log_basedir = log_basedir, patient_sim_script_fpath = patient_sim_script_fpath, record_user_replies_for_reply_filename = None)
		# except Exception as e:
		# 	print("################################################################")
		# 	print("################################################################")
		# 	print(f"# Exception when running CPD {just_the_db_number} #############")
		# 	print("# Exception is")
		# 	print(e)
		# 	print("################################################################")
		# 	print("################################################################")


def obtain_db_numbers(consults_descriptor):
	
	type_of_consult_descriptor = consults_descriptor.get('ConsultDescriptorType') 

	if type_of_consult_descriptor is None:
		print("ERROR: @param consults_descriptor is missing a value for 'ConsultDescriptorType'...")  
		print("...consults_descriptor is the argument to @func run_patient_sim_script_over_consults...")
		print("...it needs to be called with a value for the key 'ConsultDescriptorType'...")
		print("...as of 2022-06-03 its allowed values are 'PlainList', 'GlobExpression'...")
		pdb.set_trace()

	elif type_of_consult_descriptor == 'PlainList':
		list_of_cpd_numbers_to_return = consults_descriptor['ListOfCpdNumbers']

	elif type_of_consult_descriptor == 'EverythingInDir':
		dir_for_consults = consults_descriptor['DirForConsults']
		list_of_cpd_numbers_to_return = obtain_cpd_numbers_from_dir(dir_path)

	elif type_of_consult_descriptor == 'GlobExpression':
		dir_for_consults = consults_descriptor['DirForConsults']
		glob_expr = consults_descriptor['ActualGlobExpr']
		list_of_cpd_numbers_to_return = obtain_cpd_numbers_from_glob_expression(glob_expr, dir_for_consults)
		
	else:
		print("ERROR: @param invalid value for consults_descriptor 'ConsultDescriptorType'...")  
		print("...consults_descriptor is the argument to @func run_patient_sim_script_over_consults...")
		print("...it needs to be called with a value for the key 'ConsultDescriptorType'...")
		print("...as of 2022-06-03 its allowed values are 'PlainList', 'GlobExpression'...")

		pdb.set_trace()

	return(list_of_cpd_numbers_to_return)

def obtain_cpd_numbers_from_dir(dir_path):
	cpd_filename_list = os.listdir(mydir)
	cpd_filename_list.sort()
	return_list_of_cpd_numbers = []
	for cpd_filename in cpd_filename_list:
		with_front_stuff_removed = cpd_filename.lstrip("Cpd-0")
		# e.g. with_front_stuff_removed will be "1.json" if filename is "Cpd-0000000001.json"
		just_the_db_number = with_front_stuff_removed.rstrip(".json")
		just_the_db_number = int(just_the_db_number)
		return_list_of_cpd_numbers.append(just_the_db_number)
	return(return_list_of_cpd_numbers)


def obtain_cpd_numbers_from_glob_expression(glob_expr, dir_for_consults):
	print("Sorry Charlie this has not yet been implemented.")
	pdb.set_trace()



DIR_OF_CPD_FILES = "/Users/william.jarrold/ShCr/AskMD/Code/Packages/Consultation.API7/Consultation.API/app-data/couplet/consults/2022-02-04-Draft13"

#run_patient_sim_script_over_consults(DIR_OF_CPD_FILES, patient_sim_script_fpath = "../PatientSimulatorScripts/test_record_14.01.json")

# run_patient_sim_script_over_consults(DIR_OF_CPD_FILES, log_basedir = "../TstCoupProgLogs/CONSYS-299", patient_sim_script_fpath = "../PatientSimulatorScripts/consys-299.json")

# Try 19 bc it is one of several that does not have gender as first question.

#question_and_answer_loop(19, log_basedir = "../TstCoupProgLogs/", record_user_replies_for_reply_filename = "../PatientSimulatorScripts/try-dob-is-first-question.json")


# Consults_whose_1st_Qstn_Is_DateOfBirth = {'ConsultDescriptorType' : 'PlainList', 'ListOfCpdNumbers' : [19, 26, 70, 72, 76, 82, 85, 89, 131, 146, 188, 189]}

# run_patient_sim_script_over_consults(\
# 	consults_descriptor = Consults_whose_1st_Qstn_Is_DateOfBirth, 
# 	patient_sim_script_fpath = "../PatientSimulatorScripts/try-dob-is-first-question.json", 
# 	log_basedir = "../TstCoupProgLogs/ConsultsWhose1stQstnIsDateOfBirth/")

#question_and_answer_loop(155, log_basedir = "../TstCoupProgLogs/")

#question_and_answer_loop(14, log_basedir = "../TstCoupProgLogs/", record_user_replies_for_reply_filename = "../PatientSimulatorScripts/will-it-mistakenly-skip-pregnancy-on-14.json")
#question_and_answer_loop(14, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "../PatientSimulatorScripts/will-it-mistakenly-skip-pregnancy-on-14-if-female.json")
#question_and_answer_loop(14, log_basedir = "../TstCoupProgLogs/")
#question_and_answer_loop(62, log_basedir = "../TstCoupProgLogs/")
#question_and_answer_loop(14, log_basedir = "../TstCoupProgLogs/")

#question_and_answer_loop(101, log_basedir = "../TstCoupProgLogs/")