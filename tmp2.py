import config
import json
import pdb

def post_contributing_findings(payload, log_dir = None)

	# CAUTION: this might wanna be merged or partially merged with @fun post_users_reply
	# the post function in @file test_question_driver.py

	""" 

	We post a payload which is a json formatted string, which
	consists of a set stateemnts about findings are present.

	The end point should respond with a finding list.  The finding
	list should have all of the original findings plus one or more
	additional findings assuming the current finding proxy under
	examination runs correctly.

	@return bot_output_json - what the bot says in response to
	this post.

	@return payload_as_dict

	result = post_contributing_findings(TEST_PAYLOAD_1)

	"""
	
	if STEP_SLOWLY_2:
		print("In @func  post_contributing_findings")
		pdb.set_trace()
		
	print("################################################################")
	print("### Just Entered @fun post_users_reply ################################")
	print("################################################################")
	print()
	
	payload_as_dict = json.loads(payload)
	
	print(f"#### Contributing Findings Payload TODO consider spelling out human readable findings list here? ####")
	print("#### Payload (start of json object) ####")
	print()
	print(json.dumps(payload_as_dict, indent = 4, sort_keys = True))
	print()	
	print("#### Payload (end of json object) ####")

	print()

	# url = 'https://api.dev.sharecare.com/consultation/next'
	# ... 2022-06-22T13:10:33PDT dev is dead, long live qa...
	# url = 'https://api.qa.sharecare.com/consultation/next'
	
	headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

	post_response = requests.post(url = config.FINDING_PROXY_ENDPOINT, data=payload, headers=headers)

	if post_response.status_code == 503:
		print("We are getting a status of 503, i.e. Service Unavailable")
		print("Here is what the response to the post looks like if we call print on it:")
		print(post_response.status)
		pdb.set_trace()

	if post_response.status_code not in [200, 500]:

		# We can skip past error of 500 bc usaully what we
		# want is the error message buried in the json and
		# that gets printed out to the operator elsewhere in
		# the code.
		
		print("post_response.status_code:", post_response.status_code)
		print("TODO this trace is a reminder to put in a test to make sure <to be filled in> is always the status")
		print("so that we can characterize the range and frequencies of the various statuses we'll get")
		pdb.set_trace()

	bot_output_json = json.loads(post_response.text)
	
	#pdb.set_trace()
	#result_str = json.dumps(bot_output_json, indent=4, sort_keys=True)

	error_msg = bot_output_json.get('error')
	if error_msg:

		question_seq_index += 1
		if question_seq_index > 10:
			question_seq_index_str = "0" + str(question_seq_index)
		else:
			question_seq_index_str = str(question_seq_index)

		question_id = "NoID-BcBotError"
		
		error_report_string = \
f"""################################################################
Dag Nabit! We are getting an error.  Here it is:

{error_msg}

################################################################
Here is the payload that was posted to the bot that resulted in the error:

{payload}

################################################################"""

		print(error_report_string)

	################################################################
	# LEGACY_STUFF_1 COPIED FROM @FUNC POST_USERS_REPLY (START OF SECTION)
	#
	# 	if log_dir is not None:

	# 		print("Sorry I have not been programmed to handle a log dir yet!!!")
		
	# 		out_filename = filename_str_for_bot_question(question_seq_index_str, question_id)
			
	# 		out_fpath = os.path.join(log_dir, out_filename)
	# 		with open(out_fpath, 'w') as out_obj:
	# 			print(error_report_string, file=out_obj)

	# 		# What to say in the CONVERSATION_FILENAME file
	# 		if CONVERSATION_INVARIANT_MODE_P:
	# 			sys_quest_num_str = f"QuesSeq# {question_seq_index}"			
	# 		else:
	# 			sys_quest_num_str = f"QuesSeq# {question_seq_index} QuesID# {question_id}"
	# 		string_to_log_and_print = f"{sys_quest_num_str} ResponseHeader: BotError"
	# 		print(string_to_log_and_print)
	# 		log(conversation_log_filepath, string_to_log_and_print)
	# LEGACY_STUFF_1 COPIED FROM @FUNC POST_USERS_REPLY (START OF SECTION)	
	################################################################

	# print("################")

	# if CONVERSATION_INVARIANT_MODE_P:
	# 	sys_quest_num_str = f"QuesSeq# {question_seq_index} (ConsultID {payload_as_dict['consultationId']})"
	# else:
	# 	sys_quest_num_str = f"QuesSeq# {question_seq_index} QuesID# {question_id} (ConsultID {payload_as_dict['consultationId']})"

	print(f"Bot Response is {sys_quest_num_str}")

	print("Bot JSON Response To Contributing Findings Post (start of section)")

	print()
	pretty_bot_output_json_str = json.dumps(bot_output_json, indent=4, sort_keys=True)
	print(pretty_bot_output_json_str)
	print()

	print("Bot JSON Response To Users Post (end of section)")
	print("################")

	################################################################
	# LEGACY_STUFF_2 COPIED FROM @FUNC POST_USERS_REPLY (START OF SECTION)

	# TODO(2022-07-11T17:52:26PDT, ) decide if / how to adapt this
	# for current purposes.

	# if log_dir is not None:
	# 	if error_msg:

	# 		# TODO(2022-06-01T22:13:10PDT, ) does the
	# 		# error get logged like other stuff?  i am
	# 		# pretty sure the nag is no longer needed, it
	# 		# already logs the error - soewhere else,
	# 		# right?
			
	# 		pass

	# 	else:

	# 		question_seq_index = bot_output_json['questionIndexSeq']
			
	# 		question_id = bot_output_json.get('questionId', "NO_QUES_ID_BC_NO_MORE_QUESTIONS")
	
	# 		if question_seq_index > 10:
	# 			question_seq_index_str = "0" + str(question_seq_index)
	# 		else:
	# 			question_seq_index_str = str(question_seq_index)

	# 		out_filename = filename_str_for_bot_question(question_seq_index_str, question_id)
			
	# 		out_fpath = os.path.join(log_dir, out_filename)
	# 		with open(out_fpath, 'w') as out_obj:
	# 			print(pretty_bot_output_json_str, file=out_obj)
	# LEGACY_STUFF_2 COPIED FROM @FUNC POST_USERS_REPLY (END OF SECTION)	
	################################################################


	#### return from post_users_reply
	return(bot_output_json)
	#### return from post_users_reply


# print("################################################################")
# print('################ {"consultationId": 14 } ################')
# print(json.dumps(post_users_reply('{"consultationId": 14 }'), indent=4, sort_keys=True))

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

# print(json.dumps(post_users_reply(answer_to_quest21_consult_14_How_long_ago_did_your_foot_or_ankle_problem_begin), indent=4, sort_keys=True))

# system_reply_to_quest21_consult_14_ankle_problem_began_last_24_hours = post_users_reply(answer_to_quest21_consult_14_How_long_ago_did_your_foot_or_ankle_problem_begin)

CONSTRUCT_FINDING_VALUE_OBJECT_DE_NOVO_P = False

