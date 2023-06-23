################################################################
# HISTORY (start of section)
# (newest on top)

# 2022-09-28T07:11:02PDT started writing
# as copy-n-edit of post_contributing_findings from test_finding_proxies.py

# 2022-09-28T07:10:47PDT created this file (test_guidance_options.py)

# HISTORY (end of section)
################################################################
# IMPORTS

import json
import requests

import config

################################################################

#def post_findings_to_guidance_options(payload_as_json_str, error_report_obj, log_dir = None):
def post_findings_to_guidance_options(payload_as_json_str, log_dir = None):

	""" 

	We post a payload which is a json formatted string, which
	consists of a set stateemnts about findings are present.

	The end point should respond with a set of guidance options.

	@return bot_output_json - what the bot says in response to
	this post.

	"""
	
	# if STEP_SLOWLY_2:
	# 	print("In @func  post_guidance_options")
	# 	pdb.set_trace()
		
	print("################################################################")
	print("### Just Entered @fun post_findings_to_guidance_options ###############")
	print("################################################################")
	print()
	
	payload_as_dict = json.loads(payload_as_json_str)
	
	print("#### Payload (start of json object) ####")
	print()
	print(json.dumps(payload_as_dict, indent = 4, sort_keys = True))
	print()	
	print("#### Payload (end of json object) ####")

	print()

	# 2022-09-28T07:16:24PDT I dunno if I need headers here is
	#what I had for the progenitor
	#i.e. test_finding_proxies.post_contributing_findings
	#
	headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

	post_response = requests.post(url = config.GUIDANCE_OPTIONS_ENDPOINT, data=payload_as_json_str, headers=headers)

	if post_response.status_code != 200:
		exception_string = f"Error because post_response.status_code != 200.  Response code was {post_reponse.status_code}"
		raise Exception(exception_string)

	bot_output_json = json.loads(post_response.text)
	
	#pdb.set_trace()
	#result_str = json.dumps(bot_output_json, indent=4, sort_keys=True)

	error_msg = bot_output_json.get('error')
	error_report_string = None

	#potential_error_msg_txt = error_report_obj[0]
	
	if error_msg:
		
		error_report_string = \
		f"""################################################################
		Dag Nabit! Finding Service Returns JSON with an error.  
		
		The context in which the error was obtained:  TODO populate @param potential_error_msg_txt

		@param potential_error_msg_txt (which as of
		2022-09-28T07:23:32PDT we are not sure we need and
		which has yet to be defined, see
		
		The text of the error is:
		
		{error_msg}
		
		################################################################
		Here is the payload that was posted to the service that resulted in the error:
		<START OF PAYLOAD>
		
		{payload}

		<END OF PAYLOAD>
		################################################################"""
		
		print(textwrap.dedent(error_report_string))

		#print_4_grep(consult_id, ErrType_ReplyIsError, error_msg, program_rec_num, program_title, consult_name, combo_of_fnd_ids)


	print("Bot JSON Response To Contributing Findings Post (start of section)")

	print()
	pretty_bot_output_json_str = json.dumps(bot_output_json, indent=4, sort_keys=True)
	print(pretty_bot_output_json_str)
	print()

	print("Bot JSON Response To Users Post (end of section)")
	print("################")

	print("################################################################")
	print("### About To Exit @fun post_findings_to_guidance_options #######")
	print("################################################################")

	#### return from post_users_reply
	return(bot_output_json, error_report_string)
	#### return from post_users_reply

from UnitTestStuff.test_guidance_options_01 import INPUT_FOR_TEST_O1_OF_POST_FINDINGS_TO_GUIDANCE_OPTIONS

TEST_INPUT_01_JSON = INPUT_FOR_TEST_O1_OF_POST_FINDINGS_TO_GUIDANCE_OPTIONS

TEST_INPUT_01_STR = json.dumps(TEST_INPUT_01_JSON)

post_findings_to_guidance_options(TEST_INPUT_01_STR, log_dir = None)