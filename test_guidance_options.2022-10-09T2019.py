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
import os
import glob
import pdb

import config
import utils

################################################################
# CONSTANTS

GUIDANCE_OPTION_RESPONSE_FILENAME = "guid_opt_enpoint_response.json"

GuidanceOptionsResults = "GuidanceOptionsResults"
# This is a special sub dir when you have a bunch of consult results in one dir
# and you want to run guidance option gen over all of them, the results get put in this
# special subdir

################################################################

def test_guidance_options_from_many_dirs(dir_of_dirs, verbose_p = True):
	questionaire_result_dirs = os.listdir(dir_of_dirs)

	if GuidanceOptionsResults in questionaire_result_dirs:
		questionaire_result_dirs.remove(GuidanceOptionsResults)
	
	if len(questionaire_result_dirs) == 0:
		print("There are no subdirs in {dir_of_dirs}")
		print("Thus we can not run @func test_guidance_options_from_many_dirs")
		pdb.set_trace()
		
	print("################################################################")
	print(f"{utils.now_yyyy_mm_ddThhmmss()} Started test_guidance_options_from_many_dirs")
	print()
	print("These are the dirs:")

	for d in questionaire_result_dirs: print(d)
	
	sub_dir_for_guidance_options_fullpath = os.path.join(dir_of_dirs, GuidanceOptionsResults)
	
	if not(os.path.exists(sub_dir_for_guidance_options_fullpath)):
		os.mkdir(sub_dir_for_guidance_options_fullpath)
				
	for questionaire_dir in questionaire_result_dirs:
		print("Flag: Pausing Here, about to call: ")
		print("test_guidance_options_from_dir(questionaire_dir, log_basedir = sub_dir_for_guidance_options_fullpath, verbose_p = True)")
		print("...like so...")
		print(f"""test_guidance_options_from_dir(\n{questionaire_dir}, \nlog_basedir = {sub_dir_for_guidance_options_fullpath}, \nverbose_p = {verbose_p})""")
		pdb.set_trace()
		test_guidance_options_from_dir(questionaire_dir, log_basedir = sub_dir_for_guidance_options_fullpath, verbose_p = True)

def test_guidance_options_from_dir(finding_list_input_dir, log_basedir = None, verbose_p = True):
# TODO (2022-10-09T20:14:37PDT, ) rename finding_list_input_dir to questionaire_dir or questionaire_results_dir

#def test_guidance_options_from_dir(sub_dir_name, log_basedir = None, verbose_p = True):

	"""Purpose: to a kind of end-to-end posting thing.

	It reads a json finding list (a json string) from
	@param input_finding_list_filepath

	"""
	print(f"{utils.now_yyyy_mm_ddThhmmss()} Started test_guidance_options_from_dir", locals())
	
	finding_list_input_dir = finding_list_input_dir.rstrip("/")
	sub_dir_name= os.path.basename(finding_list_input_dir)

	finding_list_input_dir = os.path.join(log_basedir, sub_dir_name)

	if not(os.path.isdir(finding_list_input_dir)):
		print("finding_list_input_dir has to be a directory but is not")
		pdb.set_trace()


	matching_files_list = glob.glob(os.path.join(finding_list_input_dir, "*NO_QUES_ID_BC_NO_MORE_QUESTIONS*"))

	if len(matching_files_list) > 1:
	   print("There were more than one file that matched '*NO_QUES_ID_BC_NO_MORE_QUESTIONS*' in the current intput subdir")
	   print(f"The dubdir is {sub_dir_name}")
	   print(f"The full dirpath of the subdir is: {finding_list_input_dir}")
	   pdb.set_trace()
	   
	elif len(matching_files_list) < 1:
	   print("No files matched   '*NO_QUES_ID_BC_NO_MORE_QUESTIONS*' in the current intput subdir")
	   print(f"The dubdir is {sub_dir_name}")
	   print(f"The full dirpath of the subdir is: {finding_list_input_dir}")
	   pdb.set_trace()
	 
	else:
	   finding_list_input_filepath = matching_files_list[0]

	with open(finding_list_input_filepath, 'r') as f_obj:
		finding_list_json_dict = json.load(f_obj)
		
	test_guidance_options_from_dict(finding_list_json_dict, log_basedir = log_basedir, log_sub_dir_prefix = sub_dir_name, verbose_p = verbose_p)
	

def test_guidance_options_from_dict(payload_as_json_dict, log_basedir = None, log_sub_dir_prefix = "", verbose_p = True, timestamp_in_log_dir_p = True):

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
	on 3 different consults (70, 72 and 85) finding lists and they
	are:

	Consult.2022-10-09T1407-Cpd-70
	Consult.2022-10-09T1408-Cpd-72
	Consult.2022-10-09T1408-Cpd-85

	Suppose it is about 2022-10-09T1700 hrs and you are about to
	run the guidance optoin tester on the results (i.e. the
	finding lists) of the above three consults?  Well, that means
	you need to call this funciton i.e. @func
	test_guidance_options_from_dict on the results corresponding
	to each of the above three dirs.  You might specify each of
	the above dirs as the prefix for each of the above dir.  As a
	result, after you run it on those three you will have a dir
	listing that looks like this...

	Consult.2022-10-09T1407-Cpd-70.GuidOpt2022-10-09T1700
	Consult.2022-10-09T1408-Cpd-72.GuidOpt2022-10-09T1701
	Consult.2022-10-09T1408-Cpd-85.GuidOpt2022-10-09T1702

	@return bot_output_json - what the bot says in response to
	this post.

	>>> from UnitTestStuff.test_guidance_options_01 import INPUT_FOR_TEST_O1_OF_TEST_GUIDANCE_OPTIONS_FROM_DICT
	>>> from UnitTestStuff.test_guidance_options_01 import TARGET_OUTPUT_FOR_TEST_O1_OF_TEST_GUIDANCE_OPTIONS_FROM_DICT

	>>> TEST_INPUT_01_JSON = INPUT_FOR_TEST_O1_OF_TEST_GUIDANCE_OPTIONS_FROM_DICT

	#>>> TEST_INPUT_01_STR = json.load(TEST_INPUT_01_JSON)

	>>> TEST_TARGET_O1_JSON = TARGET_OUTPUT_FOR_TEST_O1_OF_TEST_GUIDANCE_OPTIONS_FROM_DICT

	#>>> bot_out_json, error_str = test_guidance_options_from_dict(TEST_INPUT_01_STR, log_basedir = None, verbose_p = False)

	>>> bot_out_json, error_str = test_guidance_options_from_dict(TEST_INPUT_01_JSON, log_basedir = None, verbose_p = False)
	>>> error_str == ""
	True

	>>> bot_out_json == TEST_TARGET_O1_JSON
	True

	"""

	#payload_as_json_dict = json.loads(payload_as_json_str)
	payload_as_json_str = json.dumps(payload_as_json_dict)
	
	if log_basedir is not None:
		consultation_id =  payload_as_json_dict["consultationId"]
		if log_sub_dir_prefix != "":
			log_sub_dir_prefix += "."
		if timestamp_in_log_dir_p:
			sub_dir_for_this_run = f"{log_sub_dir_prefix}GuidOpt.{utils.now_yyyy_mm_ddThhmmss()}.Cpd-{consultation_id}"
		else:
			sub_dir_for_this_run = f"{log_sub_dir_prefix}GuidOpt.Cpd-{consultation_id}"

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
		print("### Just Entered @fun test_guidance_options_from_dict ###############")
		print("################################################################")

	if verbose_p:
		print("#### Payload (start of json object) ####")
		print()
		print(json.dumps(payload_as_json_dict, indent = 4, sort_keys = True))
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
		exception_string = f"Error because post_response.status_code != 200.  Response code was {post_response.status_code}"
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
		print("### About To Exit @fun test_guidance_options_from_dict #######")
		print("################################################################")

	#### return from post_users_reply
	return(bot_output_json, error_report_string)
	#### return from post_users_reply



#test_input_file = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/GenDataForTestGuidOpt/2022-10-09T1403.FirstHeightWeight-ThenAllZero/Consult.2022-10-09T1407-Cpd-70/Q019-bot-quest-IdNO_QUES_ID_BC_NO_MORE_QUESTIONS.json"
test_input_dir = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/GenDataForTestGuidOpt/2022-10-09T1403.FirstHeightWeight-ThenAllZero/Consult.2022-10-09T1407-Cpd-70/"
test_log_basedir = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/GenDataForTestGuidOpt/2022-10-09T1403.FirstHeightWeight-ThenAllZero/"

#read_finding_list_post_go_save_results((test_input_file, log_basedir = test_log_basedir, verbose_p = True)
#test_guidance_options_from_dir(test_input_dir, log_basedir = test_log_basedir, verbose_p = True)

test_guidance_options_from_many_dirs(dir_of_dirs = test_log_basedir, verbose_p = True)