import requests
import json
#import json-diff
from deepdiff import DeepDiff

#!from testing_targets import Result_from_start_Consult14

import pdb 

#def post_next(json_body):

def question_and_answer_loop():
	current_consultationId = 14
	bot_reply = post_next('{"consultationId": 14 }')
	while True:
		next_question_id = process_system_reply(bot_reply)
		input_json = {"consultationId": current_consultationId, "questionId": next_question_id}

def post_next(payload):
	"""

	>>> result_json = post_next('{"consultationId": 14 }')
	>>> result_json == Result_from_start_Consult14
	True

	# If there is a diff, try this:
	# >>> the_diff = DeepDiff(result, Result_from_start_Consult14)
	# >>> the_diff_pretty = json.dumps(the_diff, indent=4, sort_keys=True)
	# >>> print(the_diff_pretty)

	"""
	
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


print("################################################################")
print('################ {"consultationId": 14 } ################')
print(json.dumps(post_next('{"consultationId": 14 }'), indent=4, sort_keys=True))

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

print('################################################################')
print('################ System Reply To: How long ago did your foot or ankle problem begin ################')

print(json.dumps(post_next(answer_to_quest21_consult_14_How_long_ago_did_your_foot_or_ankle_problem_begin), indent=4, sort_keys=True))

system_reply_to_quest21_consult_14_ankle_problem_began_last_24_hours = post_next(answer_to_quest21_consult_14_How_long_ago_did_your_foot_or_ankle_problem_begin)

def process_system_reply(json_input):
	response_sections = json_input['responseSections']
	
	if len(response_sections) != 1:
		print("I don't yet know how to handle cases in which there is not exacgtly one val in response_sections")
		pdb.set_trace()
		print("I don't yet know how to handle cases in which there is not exacgtly one val in response_sections")		

	else:
		response_section = response_sections[0]
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
		next_question_id = json_input["nextQuestionId"]
		return(next_question_id)
		
#process_system_reply(system_reply_to_quest21_consult_14_ankle_problem_began_last_24_hours)

question_and_answer_loop()