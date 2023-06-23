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

# test_guidance_options.2023-02-05T1243.py saved this version as I was
# just starting major change of retiring
# test_guidance_options_from_dict and replacing with @func
# test_guidance_options_from_finding_list_file

# 2023-02-04T17:24:06PST implementing reverse_order_p

# test_guidance_options.2023-01-10T2021.py
# saved bc about to make changes at 2023-02-04T14:45:12PST


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
import time

import config
import utils

################################################################
# CONSTANTS

# PRINT_MASSIVE_SPEW_P = False
# 2023-02-05T08:22:57PST trying to diagnose
#PRINT_MASSIVE_SPEW_P = True
# 2023-02-05T08:31:34PST
PRINT_MASSIVE_SPEW_OF_POST_P = False
PRINT_MASSIVE_SPEW_OF_RESPONSE_P = False


POST_HEADERS = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
FINDING_LIST_PAYLOAD_FILENAME   = "finding_list_payload.json"
URL_AND_HEADERS_FILENAME	= "url_and_headers_of_guid_opt_post.json"

# FINDING_LIST_PAYLOAD_FILENAME: typically, this file should be the
# finding list at the end of the consult.  (I suppose in theory you
# *could* decide, 'hey I want to post this finding list to the
# guidance option endpoint' at any random time during the consult but
# AskMD is designed with the expectation that GO endpoint would only
# be called after all the questions had been answered.

YES_DO_SYNC_TO_HEALTH_PROFILE_SUFFIX = "?sync=true"
DONT_SYNC_TO_HEALTH_PROFILE_SUFFIX = "?sync=false"  # TODO ask Jesse if this is ok? See 2023-02-07T22:39:35PST my teams question

GUIDANCE_OPTION_RESPONSE_FILENAME = "guid_opt_enpoint_response.json"

GuidanceOptionsResults = "GuidanceOptionsResults"
# This is a special sub dir when you have a bunch of consult results in one dir
# and you want to run guidance option gen over all of them, the results get put in this
# special subdir

DURATION_LOG_SEP = "\t"
DURATIONS_LOG_FILENAME_SUFFIX	= "tsv"  # assumes DURATION_LOG_SEP = "\t"

DURATIONS_LOG_FILENAME		= "guidance_option_durations"

DURATION_LOG_COLUMN_NAMES = "seconds"

PAUSE_TO_DO_STEP_BY_STEP_P = True



################################################################

def test_guidance_options_full_scale(dir_of_dir_of_dirs, verbose_p = True, reverse_order_p = False, sync_to_health_profile_p = None):

	"""Purpose is to test guidance options using the results of a
	"scale up" or "full scale" run of the question driver.

	More precisely, this runs over the finding lists produced by
	@fun run_test_question_driver_over_list_of_consult_lists from
	@file test_question_driver_scale_up.py

	@param dir_of_dir_of_dirs can be thought of as a directory of
	group directories.  Each such 'group dir' corresponds to a set
	of runs of the test question driver over consults that have
	been grouped together because they share the same auto-mode
	patient script and because they may share an additional set of
	characteristics.

	(For example, circa 2023-01-10 there was a group dir
	called 
	2023-01-10T070544.DOB_First_Height_Weight_Then_Random_Unless_Error_Yes_Working

	and another called 

	2023-01-10T072548.ChildrensConsults_not_suffering_Consys_322

	The first was a Jan 10 run of a set of consults that go by the
	name of
	DOB_First_Height_Weight_Then_Random_Unless_Error_Yes_Working

	And the second was, also run on Jan 10, a run of consutls that
	go by the name of ChildrensConsults_not_suffering_Consys_322

	Maybe I should rename @file test_question_driver_scale_up.py
	to @file test_question_driver_full_scale.py and replace other
	uses of 'scale up'

	@param sync_to_health_profile_p this says whether or not
	health profile is synced when guidance option endpoint is
	caled.  Default is None, meaning do what ever the endpoint
	does by default.  True and False are hopefully obvious? (-:

	"""

	print("################################################################")
	print(f"##### test_guidance_options_full_scale STARTED at {utils.now_yyyy_mm_ddThhmmss()}")
	print("################################################################")


	list_of_run_group_dirs = utils.subdir_names_in_directory(dir_of_dir_of_dirs)

	################
	# 2023-02-04T17:27:12PST added this sorting, presumably runs
	# prior to now had already sorted list_of_run_groups?

	# 2023-02-14T23:42:17PST puzzled as to why I added this.
	# *Faintly* I think what I might have been doing was this: I
	# was doing some test runs and it would fail with certain CPDs
	# or certain run groups.  But alas they came near the end of
	# the test battery bc they were alphabetically toward the end.
	# So, if we set list_of_run_group_dirs to True then we could
	# easily force the bug to be tickled earlier in a test battery
	
	if reverse_order_p:
		list_of_run_group_dirs.sort(reverse=True)
	else:
	     	list_of_run_group_dirs.sort()

	################		

	num_run_of_groups = len(list_of_run_group_dirs)

	print("################################################################")
	print("################################################################")
	print(f"{utils.now_yyyy_mm_ddThhmmss()} Started @fun test_guidance_options_from_scale_up on {num_run_of_groups} run group directories")
	print()
	print("These are the run group dirs:")
	print()
	for n, d in enumerate(list_of_run_group_dirs): print(n, d)

	print()


	# 2023-01-09T22:20:13PST giving up on this.  sigh
	# if PAUSE_TO_DO_STEP_BY_STEP_P == True:
	# 	print("Flag: Pausing test_guidance_options_full_scale so you can step by step")
	# 	no_valid_reply_yet_p = True
	# 	while no_valid_reply_yet_p:
	# 		y_or_n_reply = raw_input("Do you want to continue pausing 'y' or 'n'")
	# 		if y_or_n_reply in ["y", "n"]:
	# 			no_valid_reply_yet_p = False
	# 		else:
	# 			print("Please reply with either 'y' or 'n'")
	# 	if y_or_n_reply == 'y':
	# 		print("Okay, pausing in the debugger.  Hit, n or c etc")
	# 		pdb.set_trace()
	# 	elif y_or_n_reply == 'n':
	# 		print("Okay, continuing.  Will not pause anymore")
	# 		PAUSE_TO_DO_STEP_BY_STEP_P = False
			
	for run_group_dir in list_of_run_group_dirs:
	    test_guidance_options_from_many_dirs(run_group_dir, base_dir = dir_of_dir_of_dirs, reverse_order_p = reverse_order_p, sync_to_health_profile_p = sync_to_health_profile_p)

	print("################################################################")
	print(f"##### test_guidance_options_full_scale COMPLETED at {utils.now_yyyy_mm_ddThhmmss()}")
	print(f"##### {num_run_of_groups} run group directories were run")
	print("################################################################")
	print("################################################################")

def test_guidance_options_from_many_dirs(dir_of_dirs, base_dir = None, verbose_p = True, reverse_order_p = False, sync_to_health_profile_p = None):
	# Maybe rename dir_of_dirs to dir_of_consult_run_dirs
	
	if base_dir:
		dir_of_dirs = os.path.join(base_dir, dir_of_dirs)

	run_group_dir_name = os.path.basename(dir_of_dirs)
	
	questionaire_result_dirnames = utils.subdir_names_in_directory(dir_of_dirs, dirnames_to_remove = [GuidanceOptionsResults])

	################
	# 2023-02-04T17:27:12PST added this sorting, presumably runs
	# prior to now had already sorted list_of_run_groups?
	
	# if reverse_order_p:
	# 	questionaire_result_dirnames.sort(reverse=True)
	# else:
	#      	questionaire_result_dirnames.sort()
	# TODO(2023-02-04T17:42:13PST , ) UNCOMMENT THIS

	################		


	num_questionaire_result_dirs = len(questionaire_result_dirnames)
	
	if num_questionaire_result_dirs == 0:
		print(f"There are no subdirs in {dir_of_dirs}")
		print("Thus we can not run @func test_guidance_options_from_many_dirs")
		print("Maybe you have given the wrong directory or your run of consults did not produce any consult result dirs")
		pdb.set_trace()

	print("################################################################")
	print("################################################################")
	
	#print(f"{utils.now_yyyy_mm_ddThhmmss()} Started @fun test_guidance_options_from_scale_up on {num_run_of_groups} run group directories")
	# 2023-02-04T14:45:12PST replaced the line above with the two lines below
	print(f"{utils.now_yyyy_mm_ddThhmmss()} Started @func test_guidance_options_from_many_dirs on RunGroupDir: {run_group_dir_name}")
	print(f"There are {num_questionaire_result_dirs} questionnaire result dirs")
	
	print()
	print("These are sub-directories that are assumed to contain the results of running the test_question_driver on a given consult")
	print()
	for d in questionaire_result_dirnames: print(d)
	
	for questionaire_dir in questionaire_result_dirnames:
		#print("Flag: Pausing Here, about to call: ")
		#print("test_guidance_options_from_dir(questionaire_dir, log_basedir = guidance_options_results_full_dirpath, verbose_p = True)")
		#print("...like so...")
		#print(f"""test_guidance_options_from_dir(\n{questionaire_dir}, \nlog_basedir = {dir_of_dirs}, \nverbose_p = {verbose_p})""")
		#pdb.set_trace()
		test_guidance_options_from_dir(questionaire_dir, dir_of_dirs = dir_of_dirs, verbose_p = True, sync_to_health_profile_p = sync_to_health_profile_p)

	print(f"{utils.now_yyyy_mm_ddThhmmss()} Completed test_guidance_options_from_many_dirs on {num_questionaire_result_dirs} questionnaire result dirs")
	print("################################################################")
	print("################################################################")



# def test_guidance_options_from_dir(consult_subdir_name, scaled_up_guid_opt_log_filepath, dir_of_dirs = None, verbose_p = True, sync_to_health_profile_p = None):
# want 2023-02-15T12:21:47PST comment bout the below, bc above chanking log_file_p to log_filepath but too risky now

def test_guidance_options_from_dir(consult_subdir_name, dir_of_dirs = None, verbose_p = True, log_file_p = True, sync_to_health_profile_p = None):

#def test_guidance_options_from_dir(consult_subdir_name, dir_of_dirs = None, verbose_p = True, log_file_p = True, sync_to_health_profile_p = None):

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

	if log_file_p:
		log_file = os.path.join(dir_of_dirs, f"test_guidance_log.{utils.now_yyyy_mm_ddThhmmss()}.json")
		
	#pdb.set_trace()
	#print("Flag: Pausing test_guidance_options_from_dir so you can step by step")

	print()
	print(f"{utils.now_yyyy_mm_ddThhmmss()} Started test_guidance_options_from_dir", locals())

	with open(log_file, 'a') as out_file_obj:
		log_event_dict = {"consult_subdir_name" : consult_subdir_name, "now" : utils.now_yyyy_mm_ddThhmmss(), "event" : "start"}
		print(json.dumps(log_event_dict), file=out_file_obj)
	
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

			# 2023-02-05T12:38:40PST as part of "diagnose "Unexpected character (''' (code 39)): was expecting double-quote to start""
			# REPLACE THIS BLOCK ...
			# 
			# with open(finding_list_input_filepath, 'r') as f_obj:
			
			# 	finding_list_json_dict = json.load(f_obj)
				
			# 	bot_output_json, error_report_string = 	test_guidance_options_from_dict(finding_list_json_dict,
			# 		finding_list_input_filepath = finding_list_input_filepath,
			# 		log_basedir = guidance_options_results_full_dirpath, 
			# 		log_sub_dir_prefix = consult_subdir_name,
			# 		verbose_p = verbose_p)
			# 	with open(log_file, 'a') as out_file_obj:
			# 		log_event_dict = {"consult_subdir_name" : consult_subdir_name, "now" : utils.now_yyyy_mm_ddThhmmss(), "event" : "EndCase3", "err_str" : error_report_string}
			# 		print(json.dumps(log_event_dict), file=out_file_obj)

			# WITH THIS BLOCK...
				
			bot_output_json, error_report_string = 	test_guidance_options_from_finding_list_file(
				finding_list_input_filepath = finding_list_input_filepath,			
				log_basedir = guidance_options_results_full_dirpath, 
				log_sub_dir_prefix = consult_subdir_name,
				verbose_p = verbose_p,
				sync_to_health_profile_p = sync_to_health_profile_p)
			with open(log_file, 'a') as out_file_obj:
				log_event_dict = {"consult_subdir_name" : consult_subdir_name, "now" : utils.now_yyyy_mm_ddThhmmss(), "event" : "EndCase3", "err_str" : error_report_string}
				print(json.dumps(log_event_dict), file=out_file_obj)
					
def test_guidance_options_from_finding_list_file(
	finding_list_input_filepath,
	log_basedir,
	log_sub_dir_prefix,
	verbose_p = True,
	timestamp_in_log_dir_p = True,
	log_durations_p = True,
	sync_to_health_profile_p = None):

	"""This is merely a wrapper around @func
	test_guidance_options_from_dict added later then the first dev
	push.  It was needed to make it easy to just run this with a
	simple pathname pointer to the finding list."""

	with open(finding_list_input_filepath, 'r') as f_obj:
		finding_list_json_dict = json.load(f_obj)
		bot_output_json, error_report_string = test_guidance_options_from_dict(
			payload_as_json_dict		= finding_list_json_dict,
			finding_list_input_filepath	= finding_list_input_filepath,
			log_basedir			= log_basedir,
			log_sub_dir_prefix		= log_sub_dir_prefix,
			verbose_p			= verbose_p,
			timestamp_in_log_dir_p		= timestamp_in_log_dir_p,
			log_durations_p			= log_durations_p,
			sync_to_health_profile_p	= sync_to_health_profile_p)

		return(bot_output_json, error_report_string)

# 2023-02-05T12:41:50PST as part of trying to diagnose "Unexpected character (''' (code 39)): was expecting double-quote to start"
# I decied NOT to retire this just put a wrapper around it.

def test_guidance_options_from_dict(
	payload_as_json_dict,
	finding_list_input_filepath,
	log_basedir = None,
	log_sub_dir_prefix = "", verbose_p = True,
	timestamp_in_log_dir_p = True,
	log_durations_p = True,
	sync_to_health_profile_p = None):
	""" 

	We post a payload which is a json formatted string, which
	consists of a set statents about findings that are present.
	In other wrods, a finding list.

	@param payload_as_json_dict is a dict which I believe (at
	2023-01-10T18:03:06PST) is a finding list.  The finding list
	is the result of a running the test_question_driver.py.

	The end point should respond with a set of guidance options.

	@param verbose_p should almost always be true.  If it is false
	there will be no output to the console unless an exception is
	thrown.  Setting to False is good for doc tests and *maybe* if
	you are doing huge numbers of hits to the guidance option end
	point and do not want screen clutter.

	If you want to see the full spew of the finding list posted to
	the guidance option endpoint set XXX to True

	If you want to see the full spew of the guidance options
	result in the response from the guidance option endpoint set XXX to True

	@param finding_list_input_filepath is not really used, it's
	just nice to have the value when running, e.g. for printing
	out status in error messages.

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

	Suppose you have a @param log_dir called
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

	The name
	(e.g. Consult.2022-10-09T1408-Cpd-85.GuidOpt2022-10-09T1702)
	is calculated as described above and saved as
	sub_dir_for_this_run.  

	@param log_durations_p if true then, assuming @param
	log_basedir is not None, it the file "durations.tsv"
	(i.e. DURATIONS_LOG_FILENAME) is saved in sub_dir_for_this_run
	(e.g. Consult.2022-10-09T1408-Cpd-85.GuidOpt2022-10-09T1702)

	@return bot_output_json - what the bot says in response to
	this post.
	@return error_report_string

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
	#payload_as_json_str = json.dumps(payload_as_json_dict)
	# 2023-02-05T08:19:22PST changed the above to the below trying to diagnose "Unexpected character (''' (code 39)): was expecting double-quote to start"
	payload_as_json_str = json.dumps(payload_as_json_dict, indent = 4, sort_keys = True)

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

	   finding_list_payload_filepath     = os.path.join(log_dir, FINDING_LIST_PAYLOAD_FILENAME)
	   guidance_option_response_filepath = os.path.join(log_dir, GUIDANCE_OPTION_RESPONSE_FILENAME)
	   # issues_of_note_filepath = <whatever>
	   
	else: 
	   conversation_log_filepath = None
	   # issues_of_note_filepath = None

	if verbose_p:
		print("################################################################")
		print("### Just Entered @fun test_guidance_options_from_dict ###############")
		print("################################################################")

	if log_dir is not None:
	
	   # we chose 'x' bc each time we call this there should be a
	   # fresh dir created to house @param
	   # finding_list_payload_filepath, so this file should never
	   # be written to more than once, and if this assumption is
	   # violated we wanna know.
	   
		with open(finding_list_payload_filepath, 'x') as out_fobj:
			#print(json.dumps(payload_as_json_dict), file=out_fobj)
			print(payload_as_json_str, file=out_fobj)			
			print(f"Saved payload_as_json_dict to filename: {os.path.basename(finding_list_payload_filepath)}")
			print(f"Directory Name is: {os.path.basename(os.path.dirname(finding_list_payload_filepath))}")
			print(f"(full path is {finding_list_payload_filepath})")

	if verbose_p:
		print("#### Payload (start of json object) ####")
		# 2023-02-06T12:01:31PST started printing this
		print()
		#if PRINT_MASSIVE_SPEW_P:
		if PRINT_MASSIVE_SPEW_OF_POST_P:
			# print(json.dumps(payload_as_json_dict, indent = 4, sort_keys = True))
			# 2023-02-05T08:19:22PST changed the above to the below trying to diagnose "Unexpected character (''' (code 39)): was expecting double-quote to start"
			print(payload_as_json_str)
		else:
			#print("PRINT_MASSIVE_SPEW_P is false so we aren't going to print payload_as_json_str")
			print("PRINT_MASSIVE_SPEW_OF_POST_P is false so we aren't going to print payload_as_json_str")			
		print()	
		print("#### Payload (end of json object) ####")

		print()

	# 2022-09-28T07:16:24PDT I dunno if I need headers here is
	#what I had for the progenitor
	#i.e. test_finding_proxies.post_contributing_findings
	#

	all_has_gone_well_so_far_p = True
	error_report_string = ""
	
	start_time_legible = utils.now_yyyy_mm_ddThhmmss(utc_offset_p = True)
	start_time = time.time()

	if sync_to_health_profile_p is None:
		guid_opt_url = config.GUIDANCE_OPTIONS_ENDPOINT		
	elif sync_to_health_profile_p == True:
		guid_opt_url = config.GUIDANCE_OPTIONS_ENDPOINT	+ YES_DO_SYNC_TO_HEALTH_PROFILE_SUFFIX	
	elif sync_to_health_profile_p == False:
		guid_opt_url = config.GUIDANCE_OPTIONS_ENDPOINT	+ DONT_SYNC_TO_HEALTH_PROFILE_SUFFIX
	else:
		print("""Huh?  How did you get here.  There is an
		inconsitency in the code or you entered an invald
		valid for @parm sync_to_health_profile_p.
		It's value must be one of None, True, False""")
		pdb.set_trace()
 
	if log_dir is not None:
		url_and_headers_of_post = {"url" : guid_opt_url, "headers" : POST_HEADERS}
		url_and_headers_of_post_filepath = os.path.join(log_dir, URL_AND_HEADERS_FILENAME)
		with open(url_and_headers_of_post_filepath, 'x') as url_and_headers_of_post_fileobj:
			print(json.dumps(url_and_headers_of_post, indent=4, sort_keys=True), file = url_and_headers_of_post_fileobj)
	
	try:
		post_response = requests.post(url = guid_opt_url, data=payload_as_json_str, headers=POST_HEADERS)

	except Exception as e:
	
		print("Exception Thrown while posting:")
		print(e)
		error_report_string = e
		all_has_gone_well_so_far_p = False

	end_time = time.time()
	end_time_legible = utils.now_yyyy_mm_ddThhmmss(utc_offset_p = True)
	duration_secs = str(end_time - start_time)
	duration_log_values = [str(consult_id), duration_secs, start_time_legible, end_time_legible,  str(sync_to_health_profile_p)]
	duration_data_row   = DURATION_LOG_SEP.join(duration_log_values)
	#duration_log_column_header = DURATION_LOG_SEP.join(["consult_id", "question_id", "duration_secs", "start_time_legible", "end_time_legible"])
	# 2023-02-07T10:49:22PST changed the abve to the below
	duration_log_column_header = DURATION_LOG_SEP.join(["consult_id", "duration_secs", "start_time_legible", "end_time_legible", "sync_to_health_profile_p"])
	print("Duration Information:")
	print("TODO(2023-02-06T16:20:48PST, ) add in the the thing that jesse wants and add ij the dir name for run infor, e.g. timestamp, and add in error message col")
	print(duration_log_column_header)
	print(duration_data_row)

	if not(all_has_gone_well_so_far_p) and post_response.status_code == 200:
	
		print("""This is very strange.  There must be a bug in this code.  It seems impossible for both:

		post_response.status_code == 200

		and

		all_has_gone_well_so_far_p to be False.

		Let's stop and trace to see what happened.""")
		pdb.set_trace()

	# TODO(2023-02-05T16:40:30PST, ) this next line should be
	# protected.  if there is a serious error post_response won't
	# even be defined.

	if post_response.status_code != 200:

		all_has_gone_well_so_far_p = False
		
		error_report_string = f"Error because post_response.status_code != 200.  Response code was {post_response.status_code}"
		#raise Exception(exception_string)
		
		print("Tracing Because of post_response.status_code != 200")
		print(error_report_string)

		error_returned_from_endpoint = post_response.text
		print("Here is the value of post_response.text:")
		print(error_returned_from_endpoint)

		# TODO 2023-02-06T16:37:44PST See 2023-02-06T16:26:16PST and coordinate
		pretty_bot_output_json_str = error_returned_from_endpoint

		print("The error occured while running @fun test_guidance_options_from_dict on the following:")
		print(f"Consult: {consult_id}")
		print(f"finding_list_input_filepath: {finding_list_input_filepath}")
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

		# TODO 2023-02-06T16:34:11PST See 2023-02-06T16:26:16PST and coordinate
		pretty_bot_output_json_str = error_returned_from_endpoint

	# TODO(2023-02-06T16:26:16PST, ) the code around here is junky and maybe horribly wrong. needs reading refactor etc focus on the return value, i.e. @param error_report_string
	
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

		# 2023-02-06T16:30:08PST See 2023-02-06T16:26:16PST and coordinate
		pretty_bot_output_json_str = error_returned_from_endpoint
		
		print("Okay, sigh, you need to figure out what kinda logging if any you want to do here")
		pdb.set_trace()

	################ Finally, We have a Case of 'Success' so error_report_string should be the empty string
	else:

		pretty_bot_output_json_str = json.dumps(bot_output_json, indent=4, sort_keys=True)

		if verbose_p:
			print("Guidance Options Endpoint JSON Response To Findings List Post (start of section)")
			print()
			if PRINT_MASSIVE_SPEW_OF_RESPONSE_P:
				print(pretty_bot_output_json_str)
			else:
				print("PRINT_MASSIVE_SPEW_OF_RESPONSE_P: is false so we aren't going to print the Finding List Post")
			print()

		if verbose_p:
			print("Guidance Options Endpoint JSON Response To Findings List Post (end of section)")
			print("################")
	
			print("################################################################")
			print("### About To Exit @fun test_guidance_options_from_dict #######")
			print("################################################################")

	if log_dir is not None:
		print("Response from Guidance Option Endpoint is saved to the following filepath:")
		print(guidance_option_response_filepath)
		with open(guidance_option_response_filepath, 'x') as out_fobj:
			print(pretty_bot_output_json_str, file=out_fobj)
	else:
		if verbose_p:
			print("Response is from Guidance Option Endpoint Not Saved to File Because @param log_dir is None")


	if log_durations_p:
		if log_basedir is not None:
			if sync_to_health_profile_p is None:
				sync_to_health_profile_extension = "sync_hlth_prof_default"
			elif sync_to_health_profile_p == True:
				sync_to_health_profile_extension = "sync_hlth_prof_true"
			elif sync_to_health_profile_p == False:
				sync_to_health_profile_extension = "sync_hlth_prof_false"
			else:
				print("How did you get here?  There must be a logic error or other bug related to this part of the code.")
				pdb.set_trace()
				
			durations_full_filename = f"{DURATIONS_LOG_FILENAME}.{sync_to_health_profile_extension}.{DURATIONS_LOG_FILENAME_SUFFIX}"
			log_of_post_durations_filepath = os.path.join(log_dir, durations_full_filename)
			with open(log_of_post_durations_filepath, 'x') as dur_log_fobj:
				print(duration_log_column_header, file=dur_log_fobj)
				print(duration_data_row, file=dur_log_fobj)
			print(f"Durations have been logged in the file called {durations_full_filename}")
			print(f"The parent dir is {os.path.basename(os.path.dirname(log_of_post_durations_filepath))}")
			print(f"The fullpath is: {log_of_post_durations_filepath}")
		else:
			log_of_post_durations_filepath = None
			print("""Warning: you have called
			test_guidance_options.test_guidance_options_from_dict
			with log_durations_p = True however, you also
			called this fn with log_basedir of None.
			Thus, no durations will get logged.""")	


			

	#### return test_guidance_options_from_dict
	return(bot_output_json, error_report_string)
	#### return test_guidance_options_from_dict	


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

# 2023-02-05T11:35:36PST debbugging trying to diagnose "Unexpected character (''' (code 39)): was expecting double-quote to start"

# my_debug_finding_list_input_filepath_01 = '/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/GenDataForTestGuidOpt-FullScale/2023-01-31T195050.run_007_w_random_answers/2023-01-31T231135.Consults_suffering_Consys_299/Consult.2023-01-31T231135-Cpd-14/Q026-bot-quest-IdNO_QUES_ID_BC_NO_MORE_QUESTIONS.json'
# test_guidance_options_from_finding_list_file(
# 	finding_list_input_filepath = my_debug_finding_list_input_filepath_01,
# 	log_basedir		    = config.LOG_DIR_AD_HOC_TEST_GUIDANCE_OPTIONS,
# 	log_sub_dir_prefix	    = utils.now_yyyy_mm_ddThhmmss()+"DebugCpd14-Consult.2023-01-31T231135-Cpd-14",
# 	verbose_p		    = True,
# 	timestamp_in_log_dir_p      = True)
	

# 2023-02-07T22:59:03PST ugh just noticed this.  i probably have all kinds of messed up logs bc this test thing has been here for a heil

# my_debug_finding_list_input_filepath_02 = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/GenDataForTestGuidOpt-FullScale/2023-01-31T195050.run_007_w_random_answers/2023-01-31T231436.DOB_First_Height_Weight_Then_Random_Unless_Error_Not_Working/GuidanceOptionsResults/Consult.2023-01-31T231749-Cpd-82.GuidOpt.2023-02-05T130535.Cpd-82/finding_list_payload.json"

# test_guidance_options_from_finding_list_file(
# 	finding_list_input_filepath = my_debug_finding_list_input_filepath_02,
# 	log_basedir		    = config.LOG_DIR_AD_HOC_TEST_GUIDANCE_OPTIONS,
# 	log_sub_dir_prefix	    = utils.now_yyyy_mm_ddThhmmss()+"DoesThisWork_BasedOn_Consult.2023-01-31T231749-Cpd-82",
# 	verbose_p		    = True,
# 	timestamp_in_log_dir_p      = True)
