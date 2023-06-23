import requests
import json
#import json-diff
from deepdiff import DeepDiff

#!from testing_targets import Result_from_start_Consult14

import pdb 

#def post_next(json_body):

def question_and_answer_loop():
	print("Just entered question_and_answer_loop()")
	pdb.set_trace()
	print("Just entered question_and_answer_loop()")	
	remembered_consult_id = 14
	raw_json = {"consultationId": remembered_consult_id }
	stringified_json_for_transport = json.dumps(raw_json)
	#bot_reply = post_next({"consultationId": remembered_consult_id })
	bot_reply = post_next(stringified_json_for_transport)
	while True:
		#pdb.set_trace()
		#next_question_id = int(process_system_reply(bot_reply))
		#input_json = {"consultationId": current_consultationId, "questionId": next_question_id}
		#bot_reply = post_next(input_json)
		system_reply_json_str = process_system_reply(bot_reply, remembered_consult_id)
		bot_reply = post_next(system_reply_json_str)


		
def post_next(payload):

	#OKAY THE NEXT STEP at 2022-05-11T17:35:11PDT IS TO MAKE IT ACCEPT THE WHOLE JSON OBJECT AND THEN FIGURE OUT WHAT TO PROCESS

	"""

	>>> result_json = post_next('{"consultationId": 14 }')
	>>> result_json == Result_from_start_Consult14
	True

	# If there is a diff, try this:
	# >>> the_diff = DeepDiff(result, Result_from_start_Consult14)
	# >>> the_diff_pretty = json.dumps(the_diff, indent=4, sort_keys=True)
	# >>> print(the_diff_pretty)

	"""
	
	print("Just entered post_next - is the input (payload) - see if you can get 'unable to move there or whatever'")
	pdb.set_trace()
	print("Just entered post_next - is the input (payload) - see if you can get 'unable to move there or whatever'")	

	url = 'https://api.dev.sharecare.com/consultation/next'
	#payload = '{    "consultationId": 14 }' 
	headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
	r = requests.post(url, data=payload, headers=headers)
	result_json = json.loads(r.text)
	#pdb.set_trace()
	#result_str = json.dumps(result_json, indent=4, sort_keys=True)
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

def process_system_reply(json_input, remembered_consult_id):
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
	print("Just entered process_system_reply - what is json_input?")
	pdb.set_trace()
	print("Just entered process_system_reply - what is json_input?")	
	error_msg = json_input.get('error')
	if error_msg:
		print()
		print("Ugh, there is an error!!!")
		print()
		print("Here is the error msg:")
		print()
		print(error_msg)
		print()
		pdb.set_trace()
		
	response_sections = json_input['responseSections']
	num_response_sections = len(response_sections)
	for resp_section_num, response_section in enumerate(response_sections):
	
		print(f"Working on response_section {resp_section_num} of {num_response_sections} such sections")

		response_header =  response_section['header']
		print("SYSTEM QUESTION:", response_header)
		print("Possible Responses:\n")
		responses = response_section['responses']
		response_counter = 0
		for possible_user_response in enumerate(responses):
			response_number = possible_user_response[0]
			response_content = possible_user_response[1]
			response_txt = response_content['name']
			print(f"{response_number}: {response_txt}")
		users_choice = input("\nWhat do you chose\n (answer must be an integer)")
		users_choice = int(users_choice)
		print("User chose:", users_choice)
		chosen_response_obj = responses[users_choice]
		response_json_as_pretty_txt = json.dumps(chosen_response_obj, indent=4, sort_keys=True)
		print("The object corresponding to user's choice is:", response_json_as_pretty_txt)

	consult_id = json_input.get("consultationId")

	if consult_id is None:
		print("Just letting you know that the json passed into the current fn @process_system_reply does't have consult_id so I am using the input @param remembered_consult_id")
		pdb.set_trace()
		consult_id = remembered_consult_id
		
	next_question_id = json_input["nextQuestionId"]
	user_response_object = {"questionId": next_question_id, "consultationId": consult_id}
	print("We are at the end of process system reply.")
	print("Do you want to inspect and possibly modify @param user_response_object, i.e. what to return?")
	pdb.set_trace()
	#user_response_object_str = json.loads(user_response_object)
	return(user_response_object)
		
#process_system_reply(system_reply_to_quest21_consult_14_ankle_problem_began_last_24_hours)

question_and_answer_loop()