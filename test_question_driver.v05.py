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
import pdb

################################################################
# CONSTANTS

MultipleChoice = "all in response_content_list have no type, thus they are all responses that are discrete multiple-choice type answers, i.e. not user typed in values"
TypeIn = "all eles in response_content_list have a type, thus they are all responses that want to have a user typed in value"

STEP_SLOWLY_P = False

def question_and_answer_loop(start_conversation_with, log_basedir = None):

	"""

	@start_conversation_with should be json that sets the state
	for the users reply.  

	If you want to start at the very beginning of consult, then if
	the consult number is CONSULT_NUMBER then
	start_conversation_with should be:

	{"consultationId": CONSULT_NUMBER}

	"""
	
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
		
	log_dir = None

	consultation_id = initiate_conversation_json['consultationId']

	print("################################################################")
	print(f"##### Starting Dialog: Consult {initiate_conversation_json['consultationId']} ######")
	print("################################################################")

	users_reply = json.dumps(initiate_conversation_json)
	
	if log_basedir is not None:

		sub_dir_for_this_run = f"Consult.{now_yyyy_mm_ddThhmm()}-Cpd-{consultation_id}"
		log_dir = os.path.join(log_basedir, sub_dir_for_this_run)
		os.mkdir(log_dir)
	
	while True:

		bot_reply = post_next(users_reply, log_dir, question_index_seq)

		if skip_to_next_question_bc_of_error_p(bot_reply):
			users_reply = skip_to_next_question(bot_reply)
			# TODO( 2022-05-20T10:59:29PDT, ) log that we are skipping to next
			continue
		
		#!users_reply, question_index_seq = process_system_reply(bot_reply, remembered_consult_id, log_dir)
		# Shortly after 2022-05-16T13:16:48PDT you can delete the above commented out line
		
		users_reply, question_index_seq = process_system_reply(bot_reply, log_dir)		

#!! return(user_response_object_str, question_index_seq)

		
def post_next(payload, log_dir, question_index_seq):
	# 2022-05-16T11:26:00PDT prolly delete question_index_seq are all things with this timestamp

	"""

	log_dir, question_index_seq

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
	print("#### Payload is:")
	print(payload)

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
		print()
		print("Ugh, we posted @param payload (i.e. json representation of user response and finding list) and the bot is returning an error!!!")
		print("you might want to look at the value of @param payload to see if something was formatted in an obviously bad way")
		print()
		print("Here is the error msg:")
		print()
		print(error_msg)
		print()
		options = ["skip to next question", "edit the payload and post again", "go into the debugger", "quit"]
		options_listing = ""
		for nth, option_txt in enumerate(options):
			options_listing += f"\n{nth}: option_txt"
		print("Would you like to:", options_listing)
		user_reply_text = input("Type In Your Choice Here: ")
		choice_txt = options_listing[user_reply_text]
		if choice_txt == "skip to next question":
			# TODO(2022-05-20T10:56:00PDT, ) log this.
			result_json['re_write_this_post_as_next_question'] = payload
		else:
			print("Okay, we will enter the debugger so you can decide what to do.")
			# TODO(2022-05-20T10:55:36PDT, ) log this.
			pdb.set_trace()

		
	if log_dir is not None:
		if error_msg:
			print("okay, this is just nagware to log this !!")
			pdb.set_trace()
		else:

			# 2022-05-16T11:26:00PDT prolly delete this all with this timestamp
			# if question_index_seq is None:
			# 	question_number_str = "Unknown"
			# else:
			# 	question_number_str = str(question_index_seq)
			# out_filename = "bot-reply-{question_number_str}-Q.json"
	
			nth_question = result_json['questionIndexSeq']
			question_id = result_json['questionId']
	
			if nth_question > 10:
				nth_question_str = "0" + str(nth_question)
			else:
				nth_question_str = str(nth_question)
				
			out_filename = f"Q{nth_question_str}-bot-quest-Id{question_id}.json"
			
			out_fpath = os.path.join(log_dir, out_filename)
			with open(out_fpath, 'w') as out_obj:
				print(json.dumps(result_json, indent=4, sort_keys=True), file=out_obj)


	return(result_json)

#def pose_question_to_user(json_result):

#print(post_next("food"))


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
def process_system_reply(json_input, log_dir):
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
	#print("Just entered process_system_reply - what is json_input?")
	# pdb.set_trace() commented out bc see 2022-05-12T08:49:02PDT
	#print("Just entered process_system_reply - what is json_input?")

	

	consult_id = json_input.get('consultationId')
	question_id = json_input['questionId']
	nth_question = json_input['questionIndexSeq']

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

	#question_index_seq = json_input['questionIndexSeq']
	question_index_seq = json_input.get('questionIndexSeq', -777)
		
	response_sections = json_input['responseSections']
	num_response_sections = len(response_sections)

	if log_dir is not None:
		conversation_log_filepath = os.path.join(log_dir, "conversation_text.org")
	else: 
		conversation_log_filepath = None

	print("2022-05-20T15:48:48PDT hey, where are we, we are about to set findings_to_add to []")
	print("does findings_to_add have a value?")
	pdb.set_trace()
	findings_to_add = []

	for resp_section_num, response_section in enumerate(response_sections):
	
		print(f"Working on response_section {resp_section_num + 1} of {num_response_sections} such sections")
		# we add 1 bc it is zero initial

		response_header =  response_section['header']
		print()
		sys_quest_num_str = f"SysQues# {question_index_seq}"
		string_to_log_and_print = f"{sys_quest_num_str} ResponseHeader: {response_header}"
		print(string_to_log_and_print)
		log(conversation_log_filepath, string_to_log_and_print)
		print()		
		print("Possible Responses:\n")
		allowed_responses = response_section['responses']
		response_counter = 0
		
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

		print("2022-05-20T15:42:00PDT hey sin't the 1st question one of these neither all type-in all multipl choice things?")
		pdb.set_trace()
		
		if all(elements_that_have_no_type):
			response_content_list_choice_mode = MultipleChoice
		elif any(elements_that_have_no_type):
			print("This is odd we have some possible_user_responses that are like multiple choice and others that are typein.  What's going on here?")
			pdb.set_trace()
		else:
			response_content_list_choice_mode = TypeIn


		if response_content_list_choice_mode == TypeIn:

			################
			# Big Branch 1: Give a type-in value for each response ele
			################
			
			for response_number, response_content in enumerate(response_content_list):

				print("WATI WAIT WAIT WAIT")
				pdb.set_trace()
				# In Multiple Choice, response_txt is
				# a little text blurb that corresponds
				# to the name of one of several
				# multiple choice options (e.g. one
				# such blurb might be "pain" another
				# might be " morning joint stiffness")

				response_txt = response_content['name']

				text_description_of_systems_turn = f"** {sys_quest_num_str} TypeIn Num {response_number}: {response_txt}"
				print(text_description_of_systems_turn)
				log(conversation_log_filepath, text_description_of_systems_turn)

				print("defaultUnit: ", response_content['findingValue']['defaultUnit'])
				print("allowable units are: ", response_content['findingValue']['units'])

				response_type = response_content['findingValue']['type']
				
				print()
				print()				
				user_type_in_response = input(f"\nPlease enter a value of type {response_type}: ")
				print()
				print()				

				text_description_of_users_turn = f"* USER REPLY TO SUB QUESTION #{response_number}: {user_type_in_response}"
				print(text_description_of_users_turn)
				print()
				print()				
				log(conversation_log_filepath, text_description_of_users_turn)
				
				finding_to_add = convert_user_type_in_val_to_finding(user_type_in_response, response_content, consult_id)

			print("2022-05-20T15:48:48PDT hey, we are just about to append to findings_to_add in type-in mode")
			print("so what is the curent valu of findings_to_add ?")
			pdb.set_trace()

			findings_to_add.append(finding_to_add)
			
		################
		# Big Branch 2: Multiple Choice
		################

		elif response_content_list_choice_mode == MultipleChoice:

			################
			# Step 1: List the choices to the user
			################
			
			for nth_choice, response_content in enumerate(response_content_list):
				response_txt = response_content['name']
				# what is 'name' well,
				# response_content is ele in response_content_list
				# response_content_list is from response_section['responses']
				# response_section is from response_sections (a list)

				# response_sections is from original
				# json_input to this func
				# (i.e. process_system_reply)
				# 'responseSections'

				text_description_of_systems_turn = f"** {sys_quest_num_str} MultiChoiceOptions Num {nth_choice}: {response_txt}"
				print(text_description_of_systems_turn)
				log(conversation_log_filepath, text_description_of_systems_turn)


				# (2) the name of a type in value.  E.g.  .
				# 'most recent AI1C %'.  In addition you can
				# also have things like 'units' followed by a
				# list of json objects corresponding to each
				# unit option.

				print(f"{nth_choice}: {response_txt}")
				log(conversation_log_filepath, f"{nth_choice}: {response_txt}")

			################
			# Step 2: Solicit the User's Answer
			################

			print()
			print()			
			users_choice = input("\nWhat do you chose (answer must be an integer from choices listed above) ")
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
			log(conversation_log_filepath, f"* USERS CHOICE {question_index_seq} Answer#: {users_choice} Text: {chosenfindingName}")

			finding_to_add = {}
			
			finding_to_add['id'] = chosenfindingRecNo
			finding_to_add['state'] = "PRESENT"

			id_for_humans = f"Fnd-{chosenfindingName}-GenNo-{chosenfindingEntNo}-Cpd-{consult_id}-RecNum-{chosenfindingRecNo}"
			finding_to_add['idForHumans'] = id_for_humans

			print("Users choice represented as a finding to add to the finding list:")
			finding_to_add_pretty_txt = json.dumps(finding_to_add, indent=4, sort_keys=True)
			print(finding_to_add_pretty_txt)

			print("2022-05-20T15:48:48PDT hey, we are just about to append to findings_to_add in multiple choice mode")
			print("so what is the curent valu of findings_to_add ?")
			pdb.set_trace()
			
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



#	if STEP_SLOWLY_P:
	if True:
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
		# if question_index_seq is None:
		# 	question_number_str = "Unknown"
		# else:
		# 	question_number_str = str(question_index_seq)
		# out_filename = "bot-rpl-2-usr-ans-2-q{question_number_str}.json"

		if nth_question > 10:
			nth_question_str = "0" + str(nth_question)
		else:
			nth_question_str = str(nth_question)
			
		out_filename = f"Q{nth_question_str}-user-reply-Id{question_id}.json"
		out_fpath = os.path.join(log_dir, out_filename)
		with open(out_fpath, 'w') as out_obj:
			print(json.dumps(user_response_object, indent=4, sort_keys=True), file=out_obj)
			
	return(user_response_object_str, question_index_seq)

def convert_user_type_in_val_to_finding(user_type_in_response, response_content, consult_id):

	valued_finding_to_add = {}

	if STEP_SLOWLY_P:

		print()
		print()				
		print("We've just entered @func convert_user_type_in_val_to_finding")
		pdb.set_trace()

	finding_recno = response_content['respNo']
	valued_finding_to_add['id'] = finding_recno

	finding_entity_number = response_content['entNo']
	
	response_type = response_content['findingValue']['type']

	finding_value_object			= response_content['findingValue']
	finding_value_object['value']		= user_type_in_response		
	finding_value_object['valueType']	= response_content['findingValue']['type']
	finding_value_object['valueTypeUnits']	= response_content['findingValue']['defaultUnit']
	#2022-05-20T16:04:35PDT I don't think we need this, it's makes folowing the traces too hard
	finding_value_object['format']		= response_content['findingValue']['format']

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

def skip_to_next_question_bc_of_error_p(bot_reply):
	if (bot_reply.get('re_write_this_post_as_next_question')):
		return(True)
	else:
		return(False)	

def skip_to_next_question(bot_reply):
	post_to_re_write = bot_reply['re_write_this_post_as_next_question']
	user_response_obj = json.loads(post_to_re_write)
	user_response_obj['questionId'] = user_response_obj['myNextQuestionId']
	user_response_obj['myNextQuestionId'] = "There is no next Question Id bc we've already skip / advanced to the next question!!!"
	user_response_str = json.dumps(user_response_obj)
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

# {"id": 181, "valueObject": {"value": "12/29/1988", "valueType": "DATE", "format": "DATE"}, "state": "PRESENT"}
		
#process_system_reply(system_reply_to_quest21_consult_14_ankle_problem_began_last_24_hours)

#question_and_answer_loop("../TstCoupProgLogs/")

#question_and_answer_loop({"consultationId": 14})

#question_and_answer_loop(start_conversation_with = "PickUpFromWhereYouLeftOff/consult-14-conv-01-QID-55-surgury-in-past-few-months.json", log_basedir = "../TstCoupProgLogs/")
#question_and_answer_loop(start_conversation_with = "PickUpFromWhereYouLeftOff/consult-14-conv-01-QID-55-surgury-in-past-few-months-female.json", log_basedir = "../TstCoupProgLogs/")

#question_and_answer_loop({"consultationId": 62}, log_basedir = "../TstCoupProgLogs/")

question_and_answer_loop(62, log_basedir = "../TstCoupProgLogs/")

#question_and_answer_loop(14, log_basedir = "../TstCoupProgLogs/")

#question_and_answer_loop(62, log_basedir = "../TstCoupProgLogs/")

# 2022-05-19T12:56:31PDT trying shortest consult: stress managment
#question_and_answer_loop(155, log_basedir = "../TstCoupProgLogs/")

#question_and_answer_loop(start_conversation_with = "PickUpFromWhereYouLeftOff/consult_62_conv_Q1_QID_1_what_is_your_height.json", log_basedir = "../TstCoupProgLogs/")
# 2022-05-19T13:34:38PDT this dies early on, i forget why/

#question_and_answer_loop(62, log_basedir = "../TstCoupProgLogs/")

#question_and_answer_loop(start_conversation_with = "PickUpFromWhereYouLeftOff/consult_62_conv_Q1_QID_1_what_is_your_height_try2.json", log_basedir = "../TstCoupProgLogs/")





