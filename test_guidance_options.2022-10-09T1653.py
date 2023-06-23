################################################################
# HISTORY (start of section)
# (newest on top)

# test_guidance_options.2022-10-09T1444.py
# starting to make sig mods after a hiatus

# test_guidance_options.2022-09-28T0744.py
# first version that turns over and appears to produce a decent result

# 2022-09-28T07:11:02PDT started writing
# as copy-n-edit of post_contributing_findings from test_finding_proxies.py

# 2022-09-28T07:10:47PDT created this file (test_guidance_options.py)

# HISTORY (end of section)
################################################################
# IMPORTS

import json
import requests

import config
import utils

################################################################
# CONSTANTS

GUIDANCE_OPTION_RESPONSE_FILENAME = "guid_opt_enpoint_response.json"

################################################################

def read_finding_list_post_go_save_results(input_finding_list_filepath, log_basedir = None, verbose_p = verbose_p):
	"""Purpose: to a kind of end-to-end posting thing.

	It reads a json finding list (a json string) from
	@param input_finding_list_filepath

	"""

	with open(finding_list_input_filepath, 'r') as f_obj:
		finding_list_json_str = json.load(f_obj)

	post_findings_to_guidance_options(finding_list_json_str, log_basedir = log_basedir, verbose_p = verbose_p)

def post_findings_to_guidance_options(payload_as_json_str, log_basedir = None, log_sub_dir_prefix = "", verbose_p = True):

	""" 

	We post a payload which is a json formatted string, which
	consists of a set stateemnts about findings that are present.

	The end point should respond with a set of guidance options.

	@param verbose_p should almost always be true.  If it is false
	there will be no output to the console unless an exception is
	thrown.  Setting to False is good for doc tests and *maybe* if
	you are doing huge numbers of hits to the guidance option end
	point and do not want screen clutter.

	If @param log_basedir is a directory path, it will create a
	sub dir named with the current time (to guarantee a uniq dir
	path and informative bc we know its datetime).  In that dir
	will be the results, e.g. assuming we get a response from the
	guidance option endpoint the response will be saved in
	GUIDANCE_OPTION_RESPONSE_FILENAME (i.e.
	"guid_opt_enpoint_response.json" as of 2022-10-09T16:36:54PDT)

	@log_sub_dir_prefix what does this do?  Well, this only
	applies if @param log_basedir is a directory path.
	log_sub_dir_prefix if log_basedir is None, then this parameter
	is ignored.

	So, assuming @param log_basedir then @param log_sub_dir_prefix
	specifies an optional prefix to put in from of the sub dirs
	name.  Here is an example usage pattern:

	Suppose you have a log_dir called
	2022-10-09T1403.FirstHeightWeight-ThenAllZero

	Suppose in there you have already run the test question driver
	on 3 different consults (70, 72 and 85) finding lists and






	@return bot_output_json - what the bot says in response to
	this post.

	>>> from UnitTestStuff.test_guidance_options_01 import INPUT_FOR_TEST_O1_OF_POST_FINDINGS_TO_GUIDANCE_OPTIONS
	>>> from UnitTestStuff.test_guidance_options_01 import TARGET_OUTPUT_FOR_TEST_O1_OF_POST_FINDINGS_TO_GUIDANCE_OPTIONS

	>>> TEST_INPUT_01_JSON = INPUT_FOR_TEST_O1_OF_POST_FINDINGS_TO_GUIDANCE_OPTIONS
	>>> TEST_INPUT_01_STR = json.dumps(TEST_INPUT_01_JSON)

	>>> TEST_TARGET_O1_JSON = TARGET_OUTPUT_FOR_TEST_O1_OF_POST_FINDINGS_TO_GUIDANCE_OPTIONS

	>>> bot_out_json, error_str = post_findings_to_guidance_options(TEST_INPUT_01_STR, log_basedir = None, verbose_p = False)
	>>> error_str == ""
	True

	>>> bot_out_json == TEST_TARGET_O1_JSON
	True

	"""
	
	# if STEP_SLOWLY_2:
	# 	print("In @func  post_guidance_options")
	# 	pdb.set_trace()

	
	if log_basedir is not None:
		if timestamp_in_log_dir_p:
			sub_dir_for_this_run = f"GuidOpt.{utils.now_yyyy_mm_ddThhmm()}.Cpd-{consultation_id}"
		else:
			sub_dir_for_this_run = f"GuidOpt.Cpd-{consultation_id}"

		log_dir = os.path.join(log_basedir, sub_dir_for_this_run)
		os.mkdir(log_dir)
		if verbose_p:
			print()
			print(f"#### This test_guidance_options.py run is being logged in {sub_dir_for_this_run} ################")
			print(f"#### It is a subdir of {log_basedir} ############################################")
			print(f"#### Log Full path is: {log_dir} ################################################")
			print()
		
	else:
		log_dir = None

	if log_dir is not None:
	   
	   guidance_option_response_filepath = os.path.join(log_dir, GUIDANCE_OPTION_RESPONSE_FILENAME)
	   # issues_of_note_filepath = <whatever>
	   
	else: 
	   conversation_log_filepath = None
	   # issues_of_note_filepath = None

	if verbose_p:
		print("################################################################")
		print("### Just Entered @fun post_findings_to_guidance_options ###############")
		print("################################################################")

	payload_as_dict = json.loads(payload_as_json_str)

	if verbose_p:
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

	try:
		post_response = requests.post(url = config.GUIDANCE_OPTIONS_ENDPOINT, data=payload_as_json_str, headers=headers)
		
	except Exception as e:
	
	       print("Exception Thrown:")
	       print(e)

		# TODO(2022-10-09T15:59:36PDT, ) prolly wanna save
		# this to a file, but lets see what kinds of
		# exceptions if any we get before we go to automate a
		# response.

	if post_response.status_code != 200:
		exception_string = f"Error because post_response.status_code != 200.  Response code was {post_reponse.status_code}"
		raise Exception(exception_string)

		# TODO(2022-10-09T16:00:46PDT, ) prolly wanna save
		# this to a file, but lets see what kinds of
		# exceptions if any we get before we go to automate a
		# response.

	bot_output_json = json.loads(post_response.text)
	
	#pdb.set_trace()
	#result_str = json.dumps(bot_output_json, indent=4, sort_keys=True)

	error_msg = bot_output_json.get('error')
	error_report_string = ""

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

		# print_4_grep is legacy stuff from this file's
                # progenitor (i.e. test_finding_proxies.py).  unclear
                # if we want to adopt it here at this point (i.e. at
                # 2022-10-09T16:02:13PDT in the early days of writing
                # this wcript)

		print("Okay, sign, you need to figure out what kinda logging if any you want to do here")
		pdb.set_trace()

	pretty_bot_output_json_str = json.dumps(bot_output_json, indent=4, sort_keys=True)

	if verbose_p:
		print("Guidance Options Endpoint JSON Response To Findings List Post (start of section)")
		print()
		print(pretty_bot_output_json_str)
		print()

	if log_dir is not None:
		with open(guidance_option_response_filepath, 'x') as out_fobj:
			print(pretty_bot_output_json_str, file=out_fobj)

	if verbose_p:
		print("Guidance Options Endpoint JSON Response To Findings List Post (end of section)")
		print("################")

		print("################################################################")
		print("### About To Exit @fun post_findings_to_guidance_options #######")
		print("################################################################")

	#### return from post_users_reply
	return(bot_output_json, error_report_string)
	#### return from post_users_reply



read_finding_list_post_go_save_results(input_finding_list_filepath