import os
import requests
import json
#import json-diff
from deepdiff import DeepDiff
import datetime as dt


# 2022-05-13T10:53:40PDT freezing test_question_driver.v03.py 

# it kinda works, but in the next version i want to try just taking
# the entire chosen response optioh and using that as the 'selected
# finding' rather than constructing a finding afresh.

#!from testing_targets import Result_from_start_Consult14

import pdb

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
	
	print("Just entered question_and_answer_loop()")
	# pdb.set_trace() commented out bc see 2022-05-12T08:49:02PDT
	print("Just entered question_and_answer_loop()")	
	remembered_consult_id = 14

	if start_conversation_with is None:
		initiate_conversation_json = {"consultationId": remembered_consult_id }
		question_index_seq = 0
	else:
		initiate_conversation_json = read_json_file(start_conversation_with)
		question_index_seq = initiate_conversation_json['questionId']
	users_reply = json.dumps(initiate_conversation_json)
	log_dir = None
	if log_basedir is not None:

		sub_dir_for_this_run = "Consult." + now_yyyy_mm_ddThhmm()
		log_dir = os.path.join(log_basedir, sub_dir_for_this_run)
		os.mkdir(log_dir)
	
	while True:

		bot_reply = post_next(users_reply, log_dir, question_index_seq)
		exit_if_no_more_questions(bot_reply)
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
		pdb.set_trace()

	if log_dir is not None:

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

	consult_id = json_input.get("consultationId")
	if consult_id is None:
		pdb.set_trace()
		print("Huh!?!? I thought that consultationId was already a part of the bots reply")
		# print("Just letting you know that the json passed into the current fn @process_system_reply does't have consult_id so I am using the input @param remembered_consult_id")
		# pdb.set_trace()
		# consult_id = remembered_consult_id

	question_index_seq = json_input['questionIndexSeq']
		
	response_sections = json_input['responseSections']
	num_response_sections = len(response_sections)
	findings_to_add = []
	for resp_section_num, response_section in enumerate(response_sections):
	
		print(f"Working on response_section {resp_section_num} of {num_response_sections} such sections")

		response_header =  response_section['header']
		print("SYSTEM QUESTION:", response_header)
		print("Possible Responses:\n")
		allowed_responses = response_section['responses']
		response_counter = 0
		response_content_list = []

		for possible_user_response in enumerate(allowed_responses):
			response_number = possible_user_response[0]
			response_content = possible_user_response[1]
			response_content_list.append(response_content)
			response_txt = response_content['name']
			print(f"{response_number}: {response_txt}")
			response_type = response_content['findingValue']['type']

			# verify assumption that type is not "None"
			if (response_number > 0) and (response_type != "NONE"):
			   print("Hey, we have a case in which we have more than one response options that have a ['findingValue']['type'] that is not 'NONE'")
			   pdb.set_trace()

		if len(response_content_list) == 0:
			print("Weird, why is @param response_content_list empty!?!?!")
			pdb.set_trace()
		elif len(response_content_list) == 1:
			response_type = response_content['findingValue']['type']
			user_type_in_response = input(f"\nPlease enter a value of type {response_type}")
			print("User type-in:", user_type_in_response)
			
			# TODO: we are assuming there is only one item in response_content_list, is this a valid assumption?
			finding_to_add = convert_user_type_in_val_to_finding(user_type_in_response, response_content_list, consult_id)
		else:
			users_choice = input("\nWhat do you chose\n (answer must be an integer from choices listed above)")
			print("DO WE NEED TO STOP AND FIX THE INPUT?  WHAT KIND OF CHECK WILL ALLOW GRACEFUL FAILURE?")
			pdb.set_trace()
			users_choice = int(users_choice)

			# TODO: we are assuming there is only one item
			# in response_content_list, need to handle
			# case where user can type in multiple options


			print("User chose:", users_choice)

			response_content = response_content_list[users_choice]
			chosenfindingRecNo = response_content['respNo']
			chosenfindingEntNo = response_content['entNo']
			chosenfindingName = response_content['name']
			finding_to_add = {}
			
			finding_to_add['id'] = chosenfindingRecNo
			finding_to_add['state'] = "PRESENT"

			id_for_humans = f"Fnd-{chosenfindingName}-GenNo-{chosenfindingEntNo}-Cpd-{consult_id}-RecNum-{chosenfindingRecNo}"
			finding_to_add['idForHumans'] = id_for_humans

		
		#chosen_response_obj = responses[users_choice]
		#response_json_as_pretty_txt = json.dumps(chosen_response_obj, indent=4, sort_keys=True)
		#print("The object corresponding to user's choice is:", response_json_as_pretty_txt)

		print("Users choice represented as a finding to add to the finding list:")
		finding_to_add_pretty_txt = json.dumps(finding_to_add, indent=4, sort_keys=True)
		print(finding_to_add_pretty_txt)

		findings_to_add.append(finding_to_add)

	if STEP_SLOWLY_P:
		print("So look at findings_to_add, seem ok?")
		pdb.set_trace()

	updated_findings_list = json_input["findings"] + findings_to_add

	if STEP_SLOWLY_P:
		print("IF you want to look at updated_findings_list...")
		print("THEN Type 'updated_findings_list' or 'json.loads(updated_findings_list, indent=4, sort_keys=True)'")
		print("ELSE hit 'c' to continue execution")
		pdb.set_trace()

	question_id = json_input['questionId']
	nth_question = json_input['questionIndexSeq']
	
	user_response_object = {"questionId": question_id, "questionIndexSeq" : nth_question, "consultationId": consult_id, "findings" : updated_findings_list}
	print("We are at the end of @func process_system_reply - we have a reply to the bots question and we will soon post it to the bot.")

	if STEP_SLOWLY_P:
		print("Do you want to inspect and possibly modify @param user_response_object, i.e. what to return?")
		pdb.set_trace()

	user_response_object_str = json.dumps(user_response_object)

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

def convert_user_type_in_val_to_finding(user_type_in_response, response_content_list, consult_id):

	if len(response_content_list) != 1:
		print("We have been assuming there is only one response when the response is a type-in.  Do we need to change this code?")
		pdb.set_trace()

	response_content = response_content_list[0]
	valued_finding_to_add = {}

	if STEP_SLOWLY_P:
		print("convert the input args to a return value")
		pdb.set_trace()

	finding_recno = response_content['respNo']
	valued_finding_to_add['id'] = finding_recno

	finding_entity_number = response_content['entNo']
	
	finding_value_object = {}

	response_type = response_content['findingValue']['type']
	
	# TODO these options should be eliminated based on
	# ~2022-05-13T13:55:21PDT call with Michael AFTER he gets
	# the format, defaultUnit, and unit fields putting out things correctly.
	
	#elif response_type == 'DATE':
	if response_type == 'DATE':
		finding_value_object['format'] = 'DATE'		
		finding_value_object['value'] = user_type_in_response
		finding_value_object['valueType'] = 'DATE'
		
	elif response_type == 'LENGTH':
		finding_value_object['format'] = 'INT'
		finding_value_object['value'] = user_type_in_response
		finding_value_object['valueType'] = 'LENGTH'
		finding_value_object['valueTypeUnit'] = 4
		# TODO valueTypeUnit = 4 means 'inches', right?  need to support other units of measure.
		
	elif response_type == 'WEIGHT':
		finding_value_object['format'] = 'INT'
		finding_value_object['value'] = user_type_in_response
		finding_value_object['valueType'] = 'WEIGHT'
		finding_value_object['valueTypeUnit'] = 2
		# TODO valueTypeUnit = 2 means 'lbs', right?  need to support other units of measure.


#	if not(CONSTRUCT_FINDING_VALUE_OBJECT_DE_NOVO_P): 
	elif not(CONSTRUCT_FINDING_VALUE_OBJECT_DE_NOVO_P):
	
		finding_value_object			= response_content['findingValue']
		finding_value_object['value']		= user_type_in_response		
		finding_value_object['valueType']	= response_content['findingValue']['type']
		finding_value_object['valueTypeUnits']	= response_content['findingValue']['defaultUnit']
		finding_value_object['format']		= response_content['findingValue']['format']
		
		# TODO this should really be a conversion to the enum referrent
		# and eventually we want the ability to chose non default units

	else:
		pdb.set_trace()
		print("Sorry, I dunno how to build valued finding of this type")
		print("why don't you try to specify it in the debugger immediately below.")
		pdb.set_trace()

	valued_finding_to_add['valueObject'] = finding_value_object
	valued_finding_to_add['state'] = "PRESENT"

	finding_name = response_content['name']

	rec_num = response_content['respNo']

	id_for_humans = f"Fnd-{finding_name}-GenNo-{finding_entity_number}-Cpd-{consult_id}-RecNum-{rec_num}"
	valued_finding_to_add['idForHumans'] = id_for_humans

	if STEP_SLOWLY_P:
		print("Check @param valued_finding_to_add to see if you like what we are going to return from convert_user_type_in_val_to_finding")
		pdb.set_trace()
	
	return(valued_finding_to_add)

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

question_and_answer_loop({"consultationId": 62})





