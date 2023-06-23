# test_guidance_options.py
################################################################
# PURPOSE (start of section)

# To test the guidance option endpoint.

################################################################
# HOW IT WORKS  (start of section)

# Note: For Examples and a history of prior runs see
# test_guidance_options_experiments.py 

# Step 1: Get a Finding List using other scripts

# You need to generate a finding list by going through a questionaire.
# You can use the code in test_question_driver.py to drive a human
# operator through the questionnaire.

# There are also automatic modes,

# - you can have it read from a script of answers)
# e.g. (if my faint memory as of 2022-10-21T07:04:41PDT is correct)

# - you can turn on a a semi-automatic response mode (e.g. always
# answer 0 except for the first two questions in which you first
# provide a fixed weight and a fixed height.

# Step 2: Run the scripts in here on the finding list produced from
# step 1.

# NOTE: see test_question_driver_experiments.py for a history of
# developmental prior runs of the test_question_driver.  But for a big
# scale up of test_question_driver see
# test_question_driver_scale_up.py

################################################################
# WHAT IS WHAT IS GUIDANCE_OPTIONS_RESULTS_FULL_DIRPATH?

#
		# It is a sub-dir named GuidanceOptionsResults (yes, aka "GuidanceOptionsResults")
		#	
		# Its parent dir houses not only GuidanceOptionsResults but a bunch of other dirs
		# which are siblings to GuidanceOptionsResults.
		#
		# Each of those sibling dirs corresponds to a run of the test_question_driver over
		# a specific consult at a specific time.  For example, we might have
		#
		# Consult.2022-11-08T1042-Cpd-8/
		# Consult.2022-11-08T1042-Cpd-9/
		#
		# and many more.
		#
		# Now, GuidanceOptionsResults should contain one (or possible more than one) analogs of each such sibling
		# dir such that that analog dir has guidance options results.
		#
		# For example, the GuidanceOptionsResults that is a sibling of those 2 actually has these
		# subdirs...
		#
		# Consult.2022-11-08T1042-Cpd-8.GuidOpt.2022-11-09T201050.Cpd-8
		# Consult.2022-11-08T1042-Cpd-9.GuidOpt.2022-11-09T201223.Cpd-9
		#
		# Hopefully its clear from the names what is the mapping
		# between each such GuidOpt dir (i.e. a 'guidance
		# options' result dir) and the consult dir from which
                # that guidance option run derived its finding list.
		#
		# Now, as it happens, the guidance options generator was run over
		# All the sibling dirs (i.e. Consult.<datetime>-Cpd-<integer>)
		# more than once.  The first time it was run was on 2022-11-09
		#
		# But you can also see these additional sub dirs in GuidanceOptionsResults
		# that it was run again on 2022-12-12 becuase of these...
		#
		# Consult.2022-11-08T1042-Cpd-8.GuidOpt.2022-12-12T201639.Cpd-8
		# Consult.2022-11-08T1042-Cpd-9.GuidOpt.2022-12-12T201842.Cpd-9
		#
		# Thus, hopefuly from the above dirnames we can deduce that

		# (1) the test question driver (TQD) was run over a
                # bunch of consults starting 2022-11-08T1042.
		#
		# (2) Cpd-8 and Cpd-9 were run as part of that batch
		# run that started at 2022-11-08T1042
		#
		# (3) guidance option tester was run over the Cpd-8 results twice,
		# at 2022-11-09T201050 and 2022-12-12T201639.
		#
		# (4) guidance option tester was run over the Cpd-9 results twice,
		# at 2022-11-09T201223 and 2022-12-12T201842


################################################################
# HISTORY (start of section)
# (newest on top)

# test_guidance_options.2022-12-12T1943.py

# 2022-12-12T1943 coming back to this after long hiatus,
# about to start making comments to clarify or guess clarify my undertansing.

# test_guidance_options.2022-10-09T2250.py

# Weeks later, i.e. at 2022-10-21T07:00:19PDT, I am saving that
# version bc it is the last write and I am coming back after a long
# hiatus.  Very likely it was a solid run.

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

	questionaire_result_dirs_b4_removal = questionaire_result_dirs
	questionaire_result_dirs = [sub_dir for sub_dir in questionaire_result_dirs if os.path.isdir(os.path.join(dir_of_dirs, sub_dir))]

	print("\nOkay, here's list of the things that aren't directories (if any):")
	print(set(questionaire_result_dirs_b4_removal).difference(set(questionaire_result_dirs)))

	if GuidanceOptionsResults in questionaire_result_dirs:
		questionaire_result_dirs.remove(GuidanceOptionsResults)
	
	if len(questionaire_result_dirs) == 0:
		print(f"There are no subdirs in {dir_of_dirs}")
		print("Thus we can not run @func test_guidance_options_from_many_dirs")
		pdb.set_trace()
		
	print("################################################################")
	print(f"{utils.now_yyyy_mm_ddThhmmss()} Started test_guidance_options_from_many_dirs")
	print()
	print("These are the dirs:")

	for d in questionaire_result_dirs: print(d)
	
	for questionaire_dir in questionaire_result_dirs:
		#print("Flag: Pausing Here, about to call: ")
		#print("test_guidance_options_from_dir(questionaire_dir, log_basedir = guidance_options_results_full_dirpath, verbose_p = True)")
		#print("...like so...")
		#print(f"""test_guidance_options_from_dir(\n{questionaire_dir}, \nlog_basedir = {dir_of_dirs}, \nverbose_p = {verbose_p})""")
		#pdb.set_trace()
		test_guidance_options_from_dir(questionaire_dir, dir_of_dirs = dir_of_dirs, verbose_p = True)

def test_guidance_options_from_dir(consult_subdir_name, dir_of_dirs = None, verbose_p = True):
#def test_guidance_options_from_dir(finding_list_input_dir, log_basedir = None, verbose_p = True):

# TODO (2022-10-09T20:14:37PDT, ) rename finding_list_input_dir to
# questionaire_dir or questionaire_results_dir or
# consult_results_subdir_name or FINALLY consult_subdir_name.  Update
# much later (i.e. at 2022-12-12T20:37:23PST) I think this TODO has
# been completed, but I see the param called consult_subdir_name.

#def test_guidance_options_from_dir(sub_dir_name, log_basedir = None, verbose_p = True):

	"""Purpose: to a kind of end-to-end posting thing.

	SUMMARY:

	It reads a finding list from a file and posts that to the
	guidance option endpoint.  The guidance options endpoint is
	expected to reply with a list of guidance options.  

	In the near term (e.g. circa 2022-12-12) we pass a test of the
	guidance options endpoint, if, given a valid finding list,
	that the endpoint returns without throwing some kind of error.

	In the longer term, we might imagine doing various kinds of
	validation on the guidance ouptions output.

	MORE DETAILS:

	It reads a json finding list (a json string) from a directory
	that has recorded the results of a consult.  A dir which
	contains the results of a consult is created by the
	test_question_driver (more precisely, I *believe* that is
	@func question_and_answer_loop in test_question_driver.py.

	An example value of @param sub_dir_name is:
	'Consult.2022-11-08T1042-Cpd-7'

	An example value of @param log_basedir is:
	'/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/GenDataForTestGuidOpt/2022-11-08T1034.BirthSexFirst_Height_Weight_AllZeroUnlessError_Okay

	And the key part of that is:
	Logs-Generic/GenDataForTestGuidOpt/2022-11-08T1034.BirthSexFirst_Height_Weight_AllZeroUnlessError_Okay

	So, where does it actually get the finding list from?

	It looks in the directory which contains the output of running
	the test question driver on a given consult, i.e. by
	log_basedir and joining sub_dir_name.

	It will find a *bunch* of files there.  Many of which contain
	finding lists.  So, how does it know which file to look in?

	The answer is that it looks for a file that contains
	NO_QUES_ID_BC_NO_MORE_QUESTIONS.  The test question driver
	saves a finding list for each turn (it actually saves a pair
	of files for each turn, i.e. the usr_reply and the bot_quest).

	When the test question driver finds there are no more
	questions, then the last finding list it saves contains
	NO_QUES_ID_BC_NO_MORE_QUESTIONS.

	It means "no question id because there are no more questions."

	Look, here (*) is a list of the successive json files, one for
	each bot / user turn:

	Q021-bot-quest-Id016.json
	Q021-usr-reply-Id016.json
	Q022-bot-quest-Id061.json
	Q022-usr-reply-Id061.json
	Q023-bot-quest-IdNO_QUES_ID_BC_NO_MORE_QUESTIONS.json

	So, the penultimate one had question id 61.

	And the very last one, i.e. the one that we want to read the
	final final finding list from is called..

	Q023-bot-quest-IdNO_QUES_ID_BC_NO_MORE_QUESTIONS.json

	When I said "look here(*)" I meant here:

	~/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/GenDataForTestGuidOpt/2022-11-08T1034.BirthSexFirst_Height_Weight_AllZeroUnlessError_Okay/Consult.2022-11-08T1042-Cpd-8

	"""

	#pdb.set_trace()
	#print("Flag: Pausing test_guidance_options_from_dir so you can step by step")
	
	print(f"{utils.now_yyyy_mm_ddThhmmss()} Started test_guidance_options_from_dir", locals())
	
	consult_results_full_dirpath = os.path.join(dir_of_dirs, consult_subdir_name)

	if not(os.path.isdir(consult_results_full_dirpath)):
		print("consult_results_full_dirpath has to be a directory but is not")
		pdb.set_trace()

		# TODO (2022-12-13T22:18:27PST, )
		# 'NO_QUES_ID_BC_NO_MORE_QUESTIONS' should be replaced
		# with replaced with a constant by the name
		# NO_QUES_ID_BC_NO_MORE_QUESTIONS and that constant
		# should be defined in config.  See also
		# 2022-12-13T22:17:11PST in test_question_driver.py


	matching_files_list = glob.glob(os.path.join(consult_results_full_dirpath, "*NO_QUES_ID_BC_NO_MORE_QUESTIONS*"))

	# There should be exactly one file in matching_files_list,
        # i.e. a file whose name looks like this
        # Q027-bot-quest-IdNO_QUES_ID_BC_NO_MORE_QUESTIONS.json A file
        # like that is the one that contains the final finding list
        # once the user has reached the last question.

	################
	# RE matching_files_list Three cases below
	#
	# CASE 1: If there is more than one matching file
	# That is a very strange pathology.

	# CASE 2: there are no matching files

	# that is most likely because the test_question_driver died
	# before it reached the last question for the given consult.
	# If that has happened, the guidance options can't be
	# generated.  Thus, all we want to do is make clear 'Hey, we
	# tried to run the guidance options but we didn't bc there was
	# no file indicating it was the final .json containing the
	# final answers from the user.

	# CASE 3: there is exactly one matching file

	# Hoorray a successful test_question_driver run, we can now
	# hit the guidance option end point

	# CASE 1 (see above):
	
	if len(matching_files_list) > 1:
	   print("There were more than one file that matched '*NO_QUES_ID_BC_NO_MORE_QUESTIONS*' in the current consult results dir")
	   print(f"The consult results directory name is {consult_subdir_name}")
	   print(f"Its full dirpath is: {consult_results_full_dirpath}")
	   pdb.set_trace()

	else:
		guidance_options_results_full_dirpath = os.path.join(dir_of_dirs, GuidanceOptionsResults)

		# What is guidance_options_results_full_dirpath?
		#
		# see important detailed explanation at the top of this file.
		#

		if not(os.path.exists(guidance_options_results_full_dirpath)):
			os.mkdir(guidance_options_results_full_dirpath)

		# CASE 2 (see above)
		if len(matching_files_list) < 1:

			print("No files matched '*NO_QUES_ID_BC_NO_MORE_QUESTIONS*' in the current consults results dir")
			print(f"The consult results directory name is {consult_subdir_name}")
			print(f"Its full dirpath is: {consult_results_full_dirpath}")

			filename_for_why_no_guidance_options = f"{consult_subdir_name}GuidOpt.{utils.now_yyyy_mm_ddThhmmss()}.NoGO-NoFindingFinalFindingList-Error.txt"
			filepath_for_why_no_guidance_options = os.path.join(guidance_options_results_full_dirpath, filename_for_why_no_guidance_options)

			with open(filepath_for_why_no_guidance_options, 'x') as out_obj:
				print(\
"""There were no guidance options generated for this consult.  

This is not because of a failure of the guidance options endpoint.

Rather, there were no guidance options because it appears that the
test question driver did not succeed in generating a final finding
list.

This is very likely because the 'dialog' with test_question_driver and
question consultation service failed at some point.  

LONG VERSION EXPLAINING IN MORE DETAIL (AND PROBABLY CONFUSING/REDUNDANT!)

In test_guidance_options.py there is @func
test_guidance_options_from_dir

It looked for the results log of running the test question driver for
the present consult...

(i.e. those in ../{consult_subdir_name})

...However, could not find a final finding list.  

It could not find a final finding list because there was no file that
matched *NO_QUES_ID_BC_NO_MORE_QUESTIONS*.

(We assume that if a consult finishes than there would be a file
matching that name and it would contain the full finding list.

In other words, we assume that if the test question driver ran a
succssful consult, then all of the quesitons would have been answered
and thus no errors would have been thrown.  A successful consult would
have reached the last question and the test_question_driver would save
a file that contains.""", file = out_obj)

		# CASE 3 (see above)
		else:
			finding_list_input_filepath = matching_files_list[0]
			with open(finding_list_input_filepath, 'r') as f_obj:
			
				finding_list_json_dict = json.load(f_obj)
				
				test_guidance_options_from_dict(finding_list_json_dict, 
					log_basedir = guidance_options_results_full_dirpath, 
					log_sub_dir_prefix = consult_subdir_name,
					verbose_p = verbose_p)

def test_guidance_options_from_dict(
	payload_as_json_dict,
	log_basedir = None,
	log_sub_dir_prefix = "",
	verbose_p = True,
	timestamp_in_log_dir_p = True):

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

	consult_id =  payload_as_json_dict["consultationId"]
	
	if log_basedir is not None:

		if log_sub_dir_prefix != "":
			log_sub_dir_prefix += "."
		if timestamp_in_log_dir_p:
			sub_dir_for_this_run = f"{log_sub_dir_prefix}GuidOpt.{utils.now_yyyy_mm_ddThhmmss()}.Cpd-{consult_id}"
			# Example values:
			# Consult.2022-11-08T1042-Cpd-9.GuidOpt.2022-12-12T201842.Cpd-9
			# Consult.2022-11-08T1047-Cpd-24.GuidOpt.2022-11-09T201109.Cpd-24
		else:
			sub_dir_for_this_run = f"{log_sub_dir_prefix}GuidOpt.Cpd-{consult_id}"

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

	error_msg_exception_during_post = None
	
	headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

	all_has_gone_well_so_far_p = True
	error_report_string = ""	


	try:

		post_response = requests.post(url = config.GUIDANCE_OPTIONS_ENDPOINT, data=payload_as_json_str, headers=headers)
		
	except Exception as e:
	
		print("Exception Thrown while posting:")
		print(e)
		error_report_string = e

	if error_msg_exception_during_post:

		# TODO(2022-12-13T22:47:38PST, ) This piece of code is unreachable!!
		all_has_gone_well_so_far_p = False
		
		print("This error occured while running:")
		print(f"Consult: {consult_id}")
		print(f"log_basedir is: {log_basedir}")
		print(f"log_sub_dir_prefix is: {log_sub_dir_prefix}")

		print("Pausing here to allow you to take note of exception thrown while posting")
		pdb.set_trace()
	       		
		# TODO(2022-10-09T15:59:36PDT, ) prolly wanna save
		# this to a file, but lets see what kinds of
		# exceptions if any we get before we go to automate a
		# response.

	elif post_response.status_code != 200:

		all_has_gone_well_so_far_p = False
		
		error_report_string = f"Error because post_response.status_code != 200.  Response code was {post_response.status_code}"
		#raise Exception(exception_string)
		
		print("Tracing Because of post_response.status_code != 200")
		print(error_report_string)

		print("This error occured while running:")
		print(f"Consult: {consult_id}")
		print(f"log_basedir is: {log_basedir}")
		print(f"log_sub_dir_prefix is: {log_sub_dir_prefix}")
		
		print("Pausing here to allow you to take note of exception thrown while posting")
		pdb.set_trace()

		# TODO(2022-10-09T16:00:46PDT, ) prolly wanna save
		# this to a file, but lets see what kinds of
		# exceptions if any we get before we go to automate a
		# response.

	else:

		bot_output_json = json.loads(post_response.text)
	
		error_returned_from_endpoint = bot_output_json.get('error')

	if not(all_has_gone_well_so_far_p):
	
		bot_output_json = None

	elif error_returned_from_endpoint:
		
		error_report_string = \
		f"""################################################################
		Dag Nabit! Guidance Option Endpoint Returns JSON with an error.  
		
		The context in which the error was obtained:  TODO populate @param potential_error_msg_txt

		@param potential_error_msg_txt (which as of
		2022-09-28T07:23:32PDT we are not sure we need and
		which has yet to be defined, see
		
		The text of the error is:
		
		{error_returned_from_endpoint}
		
		################################################################
		Here is the payload that was posted to the service that resulted in the error:
		<START OF PAYLOAD>
		
		{payload}

		<END OF PAYLOAD>
		################################################################
		"""
		
		print(textwrap.dedent(error_report_string))

		print("This error occured while running:")
		print(f"Consult: {consult_id}")
		print(f"log_basedir is: {log_basedir}")
		print(f"log_sub_dir_prefix is: {log_sub_dir_prefix}")

		#print_4_grep(consult_id, ErrType_ReplyIsError, error_msg, program_rec_num, program_title, consult_name, combo_of_fnd_ids)

		# print_4_grep is legacy stuff from this file's
                # progenitor (i.e. test_finding_proxies.py).  unclear
                # if we want to adopt it here at this point (i.e. at
                # 2022-10-09T16:02:13PDT in the early days of writing
                # this wcript)

		print("Okay, sign, you need to figure out what kinda logging if any you want to do here")
		pdb.set_trace()

	################ Finally, We have a Case of 'Success' so error_report_string should be the empty string
	else:

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

# The below must have been used in test_guidance_options.2022-10-09T2250.py...
#
# test_log_basedir = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/GenDataForTestGuidOpt/2022-10-09T1403.FirstHeightWeight-ThenAllZero/"
#
# but, now as of 2022-10-21T07:36:29PDT ,  we are coming back after a hiatus and so we will do it in a new dir, i.e. this
#
# test_log_basedir = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/GenDataForTestGuidOpt/2022-10-21T0736/"
#
# ...but a little later, i.e. at 2022-10-21T07:40:46PDT i realize no, we can actually test in the old dir log i.e.
#
# test_log_basedir = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/GenDataForTestGuidOpt/2022-10-09T1403.FirstHeightWeight-ThenAllZero/"
#
# ...bc it needs to read from the questionairre output dirs and then it will write new dirs in the GuidanceOptionsResults/ subdir.
#
# so here we go using the old dir

#test_log_basedir = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/GenDataForTestGuidOpt/2022-10-09T1403.FirstHeightWeight-ThenAllZero/"


#read_finding_list_post_go_save_results((test_input_file, log_basedir = test_log_basedir, verbose_p = True)
#test_guidance_options_from_dir(test_input_dir, log_basedir = test_log_basedir, verbose_p = True)

#test_log_basedir = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/GenDataForTestGuidOpt/2022-10-27T1632.DebuggingTest/"
#test_log_basedir = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/GenDataForTestGuidOpt/2022-10-27T1632.DebuggingTest/"
#test_log_basedir = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/GenDataForTestGuidOpt/2022-10-28T1103.DOBFirstHeightWeightThenAllZeroUnlessError/"
# file last write date was 2022-10-28T12:17 thus I assume that is when the immeditaely above run was done (assumption made at 2022-10-31T12:23:42PDT)

# 2022-10-31T12:23:48PDT about to try this which has the biggest batch of consults yet:
# test_log_basedir = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/GenDataForTestGuidOpt/2022-10-28T1230.SexDOBHeightWeight/"
# test_guidance_options_from_many_dirs(dir_of_dirs = test_log_basedir, verbose_p = True)
