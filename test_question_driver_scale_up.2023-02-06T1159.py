# test_question_driver_scale_up.py

import os
import json
import pdb
import sys

from test_question_driver import question_and_answer_loop
from test_question_driver import sub_dir_name_for_consult_test_run
from utils import now_yyyy_mm_ddThhmmss
		  
################################################################
# CONSTANTS

# move to config.py?

DEFAULT_PATIENT_ANSWER_SCRIPT_BASE_DIR = "../PatientSimulatorScripts/"
DEFAULT_LOG_FOR_FULLSCALE_RUNS = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/GenDataForTestGuidOpt-FullScale"

def run_test_question_driver_over_list_of_consult_lists	(
	consult_list_objects,
	base_dir_for_massive_run_of_runs,
	patient_ans_script_base_dir = DEFAULT_PATIENT_ANSWER_SCRIPT_BASE_DIR,
	run_name = None):

	"""

	Output:
	
	Results are saved in a newly created unique directory that is
	placed in @param base_dir_for_massive_run_of_runs, which must
	be a directory path.

	The name of the name of the newly created Unique directories
	is a timestamp. That is how uniqueness of the name is
	guaranteed. If you want to give a more descriptive name than
	just a timestamp you can specify the optional parameter
	@param run_name

	"""

	for counter, obj in enumerate(consult_list_objects):
		if counter == 0:
				if not(os.path.isdir(base_dir_for_massive_run_of_runs)):
					print("Error, non existant directory: {base_dir_for_massive_run_of_runs}")
					pdb.set_trace()
				else:
					timestamp_for_this_run_of_runs = now_yyyy_mm_ddThhmmss()
					if run_name:
						dir_name = timestamp_for_this_run_of_runs + "." + run_name
					else:
						dir_name = timestamp_for_this_run_of_runs
						
					dirpath_for_this_list_of_consults = os.path.join(base_dir_for_massive_run_of_runs, dir_name)
					os.mkdir(dirpath_for_this_list_of_consults)

		my_run_name			= obj['my_run_name']
		my_list_of_consults		= obj['list_of_consults']
		my_patient_ans_script_filename	= obj['patient_ans_script_filename']
		
		run_test_question_driver_over_consult_list(
			list_of_consults = my_list_of_consults,
			base_dir = dirpath_for_this_list_of_consults,
			run_name = my_run_name,
			patient_ans_script_filename = my_patient_ans_script_filename,
			patient_ans_script_base_dir = patient_ans_script_base_dir)

# TODO probaly clearer if we rename this to:
# run_test_question_driver_over_test_group
# or
# run_test_question_driver_over_consult_test_group

def run_test_question_driver_over_consult_list(list_of_consults, base_dir, run_name,
	patient_ans_script_filename, patient_ans_script_base_dir = DEFAULT_PATIENT_ANSWER_SCRIPT_BASE_DIR):

	"""
	Trying to piece together what this does:

	It runs a list of CPDs over the same script of answers.

	There is a concept of a test_group.  I *think* the test group
	is the @param list_of_consults.
	
	givn @base_dir



	it will run @func question_and_answer_loop over each consult.

	if there is an exception thrown, then there should a a file
	created that has the exception message and other data.

	the name of that file will be something like this:

	Error.Consult.2022-11-30T071149-Cpd-29.txt

	"""

	print("################################################################")
	print("################################################################")
	print(f"##### Hear Yee, Hear Yee, at {now_yyyy_mm_ddThhmmss()} we are commencing .... ###############")
	print("##### run_test_question_driver_over_consult_list ###############")
	print("#### called on these args: #####################################")
	args_as_dict = locals().copy()
	args_as_pretty_str = json.dumps(args_as_dict, indent = 4)
	print(args_as_pretty_str)
	print("################################################################")
	print("################################################################")

	my_patient_sim_script_fpath = os.path.join(patient_ans_script_base_dir, patient_ans_script_filename)
	# my_patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error_for_children.json",
	
	if not(os.path.isfile(my_patient_sim_script_fpath)):
		print(f"""ERROR: patient_ans_script filepath does not exist.
		patient_ans_script_base_dir: {patient_ans_script_base_dir}
		patient_ans_script_filename: {patient_ans_script_filename}""")
		pdb.set_trace()

	dir_name_for_this_test_group = f"{now_yyyy_mm_ddThhmmss()}.{run_name}"
	dir_path_for_this_test_group = os.path.join(base_dir, dir_name_for_this_test_group)
	os.mkdir(dir_path_for_this_test_group)

	for consult_number in list_of_consults:
		timestamp_for_run_of_this_consult = now_yyyy_mm_ddThhmmss()
		# 2022-11-15T22:15:03PST late night debugging
		# print("inspect for weirdness")
		# pdb.set_trace()

		# print("cpd 29, it should fail inside of this try right?")
		# pdb.set_trace()
		
		try:
			question_and_answer_loop(consult_number,
				log_basedir = dir_path_for_this_test_group,
				patient_sim_script_fpath = my_patient_sim_script_fpath,
				timestamp_in_log_dir = timestamp_for_run_of_this_consult,
				if_reply_script_UnlessError_means_LogAndContinue = True)
				
		except Exception as error_msg:
			print("################################################################")
			print("#### Exception Thrown !!!!! ####################################")
			print(f"#### Consult {consult_number} #################################")
			print(f"#### error_msg is: {error_msg} #################################")
			print("################################################################")
			
			exc_type, exc_obj, exc_tb = sys.exc_info()
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]			

			filename_of_error_file = "Error." + sub_dir_name_for_consult_test_run(timestamp_for_run_of_this_consult, consult_number) + ".txt"
			filepath_of_error_file = os.path.join(dir_path_for_this_test_group, filename_of_error_file)
			with open(filepath_of_error_file, 'w') as out_obj:
				print(f"This was the error message that occured during this run of Consult Number {consult_number}", file=out_obj)
				print("", file=out_obj)

				print("################")
				print("Here is the error message:", file=out_obj)
				print("", file=out_obj)				
				print(error_msg, file=out_obj)
				print("\n\n", file=out_obj)

				print("################")
				print("""Here is info from calling: 
					exc_type, exc_obj, exc_tb = sys.exc_info()
					fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]""",
					file=out_obj)

				print(f"exc_type: {exc_type}", file=out_obj)
				print(f"exc_obj: {exc_obj}", file=out_obj)
				print(f"exc_tb: {exc_tb}", file=out_obj)
				print(f"fname: {fname}", file=out_obj)
				print(f"exc_tb.tb_lineno: {exc_tb.tb_lineno}", file=out_obj)

# ChildrensConsults_not_suffering_Consys_322 = \
# [311, 315, 318, 320, 321, 323, 324, 325, 326, 327, 329, 330, 331]
# # SCRIPT: sex_dob_height_weight_then_all_zero_unless_error_for_children.json

# # NeedWork: 2
# ChildrensConsults_yes_suffering_Consys_322 = \
# [322, 328]
# # SCRIPT: sex_dob_height_weight_then_all_zero_unless_error_for_children.json

# BirthSexFirst_Height_Weight_AllZeroUnlessError_Okay = \
# [3, 6, 7, 8, 9, 11, 14, 15, 16, 17, 20, 24, 27, 29, 32,
# 40, 47, 49, 55, 57, 59, 66]
# # SCRIPT: sex_dob_height_weight_then_all_zero_unless_error.json

# 2022-12-04T22:43:34PST Maybe it would be clearer if
# TEST_LIST_OF_CONSULT_LIST_OBJECTS was renamed to 
# LIST_OF_TEST_GROUPS_FOR_TRIAL_RUN_01
# 2022-12-04T23:03:32PST okay i did the rename

LIST_OF_TEST_GROUPS_FOR_TRIAL_RUN_01 = [
	{
	#'list_of_consults' : [3, 6, 7, 8, 9, 11, 14, 15, 16, 17, 20, 24, 27, 29, 32,
	'list_of_consults' : [29, 32],
	'my_run_name' : "BirthSexFirst_Height_Weight_AllZeroUnlessError_Okay",
	'patient_ans_script_filename' : 'sex_dob_height_weight_then_all_zero_unless_error.json'
	},
	{
	'my_run_name' : "ChildrensConsults_not_suffering_Consys_322",
	'list_of_consults' : [311, 315],
	'patient_ans_script_filename' : 'sex_dob_height_weight_then_all_zero_unless_error_for_children.json'
	},
	{
	'my_run_name' : "ChildrensConsults_yes_suffering_Consys_322",
	'list_of_consults' : [322, 328],
	'patient_ans_script_filename' : 'sex_dob_height_weight_then_all_zero_unless_error_for_children.json'
	}
	]

# run_test_question_driver_over_list_of_consult_lists(
# 	consult_list_objects = LIST_OF_TEST_GROUPS_FOR_TRIAL_RUN_01,
# 	base_dir_for_massive_run_of_runs = DEFAULT_LOG_FOR_FULLSCALE_RUNS
# 	)

LIST_OF_TEST_GROUPS_FOR_TRIAL_RUN_02 = [
	{
	'list_of_consults' : [3, 6, 7, 8, 9, 11, 14, 15, 16, 17, 20, 24, 27, 29, 32],
	'my_run_name' : "BirthSexFirst_Height_Weight_AllZeroUnlessError_Okay",
	'patient_ans_script_filename' : 'sex_dob_height_weight_then_all_zero_unless_error.json'
	},
	{
	'my_run_name' : "ChildrensConsults_not_suffering_Consys_322",
	'list_of_consults' : [311, 315, 318, 320, 321, 323, 324, 325, 326, 327, 329, 330, 331],
	'patient_ans_script_filename' : 'sex_dob_height_weight_then_all_zero_unless_error_for_children.json'
	},
	{
	'my_run_name' : "ChildrensConsults_yes_suffering_Consys_322",
	'list_of_consults' : [322, 328],
	'patient_ans_script_filename' : 'sex_dob_height_weight_then_all_zero_unless_error_for_children.json'
	}
	]

FULL_LIST_OF_TEST_GROUPS_01 =\
	[
	{
	'my_run_name' : "DOB_First_Height_Weight_Then_All_Zero_Unless_Error_Yes_Working",	
	'list_of_consults' : 	[70, 72, 85, 89, 131, 146, 188],
	'patient_ans_script_filename' : 'dob_height_weight_then_all_zero_unless_error.json'
	},
	{
	'my_run_name' :			"DOB_First_Height_Weight_Then_All_Zero_Unless_Error_Not_Working",
	'list_of_consults' :		[76, 82],
	'patient_ans_script_filename' : 'dob_height_weight_then_all_zero_unless_error.json'
	},
	{
	'my_run_name' : "RemainingConsultsAssumed_SexDOBHeightWeight_yes_okay",
	'list_of_consults' : [
		73, 77, 98, 101, 102, 108, 110, 115, 116, 119, 127, 134,
		142, 144, 145, 147, 148, 152, 155, 156, 157, 158, 159, 160,
		161, 163, 165, 166, 168, 176, 178, 179, 181, 182, 183, 184,
		187, 610
	],
	'patient_ans_script_filename' : 'sex_dob_height_weight_then_all_zero_unless_error.json'
	},
	{
	'my_run_name' : "RemainingConsultsAssumed_SexDOBHeightWeight_not_okay",
	'list_of_consults' : [
		87, 89, 117, 140, 308
		],

	'patient_ans_script_filename' : 'sex_dob_height_weight_then_all_zero_unless_error.json'
	# see Triage Notes (in test_question_driver_experiments.py) for RemainingConsultsAssumed_SexDOBHeightWeight_not_okay	
	},
	{
	'my_run_name' : "BirthSexFirst_Height_Weight_AllZeroUnlessError_Okay",
	'list_of_consults' : [3, 6, 7, 8, 9, 11, 14, 15, 16, 17, 20, 24, 27, 29, 32, 40, 47, 49, 55, 57, 59, 66],
	'patient_ans_script_filename' : 'sex_dob_height_weight_then_all_zero_unless_error.json'
	},
	{
	'my_run_name' : "BirthSexFirst_Height_Weight_AllZeroUnlessError_NeedingAttention",
	'list_of_consults' : [6, 7, 28, 43, 62],
	'patient_ans_script_filename' : 'sex_dob_height_weight_then_all_zero_unless_error.json'
	},
	{
	'my_run_name' : "ChildrensConsults_not_suffering_Consys_322",
	'list_of_consults' : [311, 315, 318, 320, 321, 323, 324, 325, 326, 327, 329, 330, 331],
	'patient_ans_script_filename' : 'sex_dob_height_weight_then_all_zero_unless_error_for_children.json'
	},
	{
	'my_run_name' : "ChildrensConsults_yes_suffering_Consys_322",
	'list_of_consults' : [322, 328],
	'patient_ans_script_filename' : 'sex_dob_height_weight_then_all_zero_unless_error_for_children.json'
	},
	{
	'my_run_name' : "Consults_suffering_Consys_299",
	'list_of_consults' : [14, 62],
	'patient_ans_script_filename' : 'sex_dob_height_weight_then_all_zero_unless_error.json'
	# see Triage Notes (in test_question_driver_experiments.py) for Consults_suffering_Consys_299	
	}
	]

# run_test_question_driver_over_list_of_consult_lists(
# 	consult_list_objects = FULL_LIST_OF_TEST_GROUPS_01,
# 	base_dir_for_massive_run_of_runs = DEFAULT_LOG_FOR_FULLSCALE_RUNS
# 	)


TEST_THE_STRAGGLERS = [
	{
	'my_run_name' : "TestStraggler-CPD-4",
	'list_of_consults' : [4],
	'patient_ans_script_filename' : 'sex_dob_height_weight_then_all_zero_unless_error.json'
	},
	{
	'my_run_name' : "TestStraggler-CPD-19",
	'list_of_consults' : [19],
	'patient_ans_script_filename' : 'dob_height_weight_then_all_zero_unless_error.json'
	}
	]


# run_test_question_driver_over_list_of_consult_lists(
# 	consult_list_objects = TEST_THE_STRAGGLERS, 
# 	base_dir_for_massive_run_of_runs = DEFAULT_LOG_FOR_FULLSCALE_RUNS
# 	)

FULL_LIST_OF_TEST_GROUPS_02 =\
	[
	
	# this should the same as FULL_LIST_OF_TEST_GROUPS_01
	# except the two stragglers, i.e. 4 and 19 are added.

	# and the following, i.e. 6, 7, 14, 62, 89 which were
	# duplicates in FULL_LIST_OF_TEST_GROUPS_01 are not duplicates
	# any more here in FULL_LIST_OF_TEST_GROUPS_02

	# 2022-12-14T09:15:04PST changing order of run names because
	# this massive run: 2022-12-13T225238/ seemed to ok for the
	# first two, i.e.
	# "DOB_First_Height_Weight_Then_All_Zero_Unless_Error_Yes_Working",
	# and
	# "DOB_First_Height_Weight_Then_All_Zero_Unless_Error_Not_Working",
	# 
	# but then starting here...
	# "RemainingConsultsAssumed_SexDOBHeightWeight_yes_okay"
	# ...had flakiness and then every dir after that was even
	# worse, probably everything errored always with this error:
	#
	# HTTPSConnectionPool(host='api.qa.sharecare.com', port=443):
	# Max retries exceeded with url: /consultation/next (Caused by
	# SSLError(SSLEOFError(8, 'EOF occurred in violation of
	# protocol (_ssl.c:1108)')))
	#
	# so, at 2022-12-14T09:18:27PST, I'm moving those three to the
	# end to expose the ones to testing who completely failed
	# during the 2022-12-13 mass run (i.e. 2022-12-13T225238/)

	# 2022-12-20T23:21:52PST moved this run group from the back to the front of the list
	# after MASSIVE changes which look like they merely prevented
	# had with hanging on 7 and that's it, no onther consutls!?!?!
	# Well at least I can see if it worked early in the test run.
	{
	'my_run_name' : "JIRA-CI-3784_sex_dob_h_w",
	'list_of_consults' : [7, 62, 308],
	'patient_ans_script_filename' : 'sex_dob_height_weight_then_all_zero_unless_error.json',

	'comment' : """2022-12-19T10:43:18PST 62 was in
	Consults_suffering_Consys_299 but Consys_299 resolved.  But
	now CPD 62 still suffers from
	https://arnoldmedia.jira.com/browse/CI-3784 so it was moved to JIRA-CI-3784_sex_dob_h_w.  

	308 was in
	RemainingConsultsAssumed_SexDOBHeightWeight_not_okay and has
	been moved to here, JIRA-CI-3784_sex_dob_h_w, bc it too
	suffers from CI-3784

	2022-12-19T11:42:46PST 7 was moved from
	BirthSexFirst_Height_Weight_AllZeroUnlessError_NeedingAttention
	to JIRA-CI-3784_sex_dob_h_w

	"""
	
	},
	{
	'my_run_name' : "RemainingConsultsAssumed_SexDOBHeightWeight_not_okay",
	'list_of_consults' : [
		87, 117, 140
		],

	'patient_ans_script_filename' : 'sex_dob_height_weight_then_all_zero_unless_error.json'
	# see Triage Notes (in test_question_driver_experiments.py) for RemainingConsultsAssumed_SexDOBHeightWeight_not_okay	
	},
	{
	'my_run_name' : "BirthSexFirst_Height_Weight_AllZeroUnlessError_Okay",
	'list_of_consults' : [3, 8, 9, 11, 15, 16, 17, 20, 24, 27, 32, 40, 47, 49, 55, 57, 59, 66],
	'patient_ans_script_filename' : 'sex_dob_height_weight_then_all_zero_unless_error.json'
	},
	{
	'my_run_name' : "BirthSexFirst_Height_Weight_AllZeroUnlessError_JIRAs",
	'list_of_consults' : [29],
	'patient_ans_script_filename' : 'sex_dob_height_weight_then_all_zero_unless_error.json',
	'comment' : "29 is https://arnoldmedia.jira.com/browse/CI-3760"
	},
	{
	'my_run_name' : "BirthSexFirst_Height_Weight_AllZeroUnlessError_NeedingAttention",
	'list_of_consults' : [28, 43],
	'patient_ans_script_filename' : 'sex_dob_height_weight_then_all_zero_unless_error.json',
	'comment' : """2022-12-19T11:42:46PST 7 was moved from
	BirthSexFirst_Height_Weight_AllZeroUnlessError_NeedingAttention
	to JIRA-CI-3784_sex_dob_h_w"""
	},
	{
	'my_run_name' : "ChildrensConsults_not_suffering_Consys_322",
	'list_of_consults' : [311, 315, 318, 320, 321, 323, 324, 325, 326, 327, 329, 330, 331],
	'patient_ans_script_filename' : 'sex_dob_height_weight_then_all_zero_unless_error_for_children.json'
	},
	{
	'my_run_name' : "ChildrensConsults_yes_suffering_Consys_322",
	'list_of_consults' : [322, 328],
	'patient_ans_script_filename' : 'sex_dob_height_weight_then_all_zero_unless_error_for_children.json'
	},
	{
	'my_run_name' : "Consults_suffering_Consys_299",
	'list_of_consults' : [14],
	'patient_ans_script_filename' : 'sex_dob_height_weight_then_all_zero_unless_error.json'
	# see Triage Notes (in test_question_driver_experiments.py) for Consults_suffering_Consys_299
	# 2022-12-19T10:39:34PST I see that Consults_suffering_Consys_299 is resolved.  But
	# 62 is still failing, now due to https://arnoldmedia.jira.com/browse/CI-3784.  
	},
	{
	'my_run_name' : "DOB_First_Height_Weight_Then_All_Zero_Unless_Error_Yes_Working",	
	'list_of_consults' : 	[26, 19, 70, 72, 85, 89, 131, 146, 188, 189],
	# 2022-12-19T10:30:30PST moved 26 from BirthSexFirst_Height_Weight_AllZeroUnlessError_NeedingAttention to DOB_First_Height_Weight_Then_All_Zero_Unless_Error_Yes_Working
	# 2022-12-19T10:56:25PST not sex first, dob first, moved 189 from RemainingConsultsAssumed_SexDOBHeightWeight_yes_okay to DOB_First_Height_Weight_Then_All_Zero_Unless_Error_Yes_Working
	'patient_ans_script_filename' : 'dob_height_weight_then_all_zero_unless_error.json'
	},
	{
	'my_run_name' :			"DOB_First_Height_Weight_Then_All_Zero_Unless_Error_Not_Working",
	'list_of_consults' :		[76, 82],
	'patient_ans_script_filename' : 'dob_height_weight_then_all_zero_unless_error.json'
	},
	{
	'my_run_name' : "RemainingConsultsAssumed_SexDOBHeightWeight_yes_okay",
	'list_of_consults' : [
		4, 73, 77, 98, 101, 102, 108, 110, 115, 116, 119, 127, 134,
		142, 144, 145, 147, 148, 152, 155, 156, 157, 158, 159, 160,
		161, 163, 165, 166, 168, 176, 178, 179, 181, 182, 183, 184,
		187, 610
	],
	'patient_ans_script_filename' : 'sex_dob_height_weight_then_all_zero_unless_error.json'
	},
	{
	'my_run_name' : "JIRA-CI-3784_sex_dob_h_w",
	'list_of_consults' : [308],
	'patient_ans_script_filename' : 'sex_dob_height_weight_then_all_zero_unless_error.json'
	# see Triage Notes (in test_question_driver_experiments.py) for RemainingConsultsAssumed_SexDOBHeightWeight_not_okay	
	},
	{
	'my_run_name' : "JIRA-CONSYS_334_blood_pressure",
	'list_of_consults' : [6],
	'patient_ans_script_filename' : 'sex_dob_height_weight_blood_pressure_then_all_zero_unless_error.json',
	'comment' : """2022-12-19T11:20:10PST was in
	BirthSexFirst_Height_Weight_AllZeroUnlessError_NeedingAttention
	but moved bc needed a blood pressure value and thus this new
	script
	(i.e. sex_dob_height_weight_blood_pressure_then_all_zero_unless_error.json')
	but still suffers from https://arnoldmedia.jira.com/browse/CONSYS-334"""
	}
	]

# At 2022-12-13T22:50:39PST I have checked
# diary-TestCoupletPrograms.org and other notes and it appears that we
# have not run FULL_LIST_OF_TEST_GROUPS_02 quite yet.  So here goes!!
# That run has started and it is here:
# /Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/GenDataForTestGuidOpt-FullScale/2022-12-13T225238

# 2022-12-19T08:24:59PST saved test_question_driver_scale_up.2022-12-14T0919.py
# and am now making edits to the FULL_LIST_OF_TEST_GROUPS_02

# run_test_question_driver_over_list_of_consult_lists(
# 	consult_list_objects = FULL_LIST_OF_TEST_GROUPS_02,
# 	base_dir_for_massive_run_of_runs = DEFAULT_LOG_FOR_FULLSCALE_RUNS
# 	)

################################################################

# 2022-12-20T22:52:55PST massive change.  It should fix the halt we
# had with 7.

# 2022-12-27T23:37:27MST the test run just finished, cursory look
# suggests it is ok.  need to do a deeper look.

# run_test_question_driver_over_list_of_consult_lists(
# 	consult_list_objects = FULL_LIST_OF_TEST_GROUPS_02,
# 	base_dir_for_massive_run_of_runs = DEFAULT_LOG_FOR_FULLSCALE_RUNS
# 	)

################################################################

FULL_LIST_OF_TEST_GROUPS_03 =\
	[
	
	# this should the same as FULL_LIST_OF_TEST_GROUPS_02
	# except each auto-mode script "all_zero" is replaced with
	# with 7"random"

	# 2023-01-22T22:35:02PST this was last, but I moved it to be first
	{
	'my_run_name' : "JIRA-CONSYS_334_blood_pressure",
	'list_of_consults' : [6],
	'patient_ans_script_filename' : 'sex_dob_height_weight_blood_pressure_then_random_unless_error.json',
	'comment' : """2022-12-19T11:20:10PST was in
	BirthSexFirst_Height_Weight_AllZeroUnlessError_NeedingAttention
	but moved bc needed a blood pressure value and thus this new
	script
	(i.e. sex_dob_height_weight_blood_pressure_then_random_unless_error.json')
	but still suffers from https://arnoldmedia.jira.com/browse/CONSYS-334 'Support blood pressure format ex: 120/80'"""
	},

	# 2023-01-22T22:38:37PST I moved this (immediately below) to
	# be further up bc it had an error on the last
	# (2023-01-17T101224) run.  The error was 'list index out of
	# range' with 308
	{
	'my_run_name' : "JIRA-CI-3784_sex_dob_h_w",
	'list_of_consults' : [7, 62, 308],
	'patient_ans_script_filename' : 'sex_dob_height_weight_then_random_unless_error.json',

	'comment' : """2022-12-19T10:43:18PST 62 was in
	Consults_suffering_Consys_299 but Consys_299 resolved.  But
	now CPD 62 still suffers from
	https://arnoldmedia.jira.com/browse/CI-3784 so it was moved to JIRA-CI-3784_sex_dob_h_w.  

	308 was in
	RemainingConsultsAssumed_SexDOBHeightWeight_not_okay and has
	been moved to here, JIRA-CI-3784_sex_dob_h_w, bc it too
	suffers from CI-3784

	At 2023-01-16T22:12:20PST Bill notes that both 62 and 308 (and
	7) are mentioned on CI-3784.  These should stop erroring out
	once we get content for build 62.1 in the DB.

	2022-12-19T11:42:46PST 7 was moved from
	BirthSexFirst_Height_Weight_AllZeroUnlessError_NeedingAttention
	to JIRA-CI-3784_sex_dob_h_w

	"""
	
	},

	# 2023-01-22T22:44:08PST for run_005_w_random_answers I moved this up bc
	# 29 got the no next question error last time and we have a new KB now.
	{
	'my_run_name' : "BirthSexFirst_Height_Weight_AllZeroUnlessError_JIRAs",
	'list_of_consults' : [29],
	'patient_ans_script_filename' : 'sex_dob_height_weight_then_random_unless_error.json',
	'comment' : """
	
	https://arnoldmedia.jira.com/browse/CONSYS-418 where we have
	'No value received via onNext for awaitSingle'

	29 is https://arnoldmedia.jira.com/browse/CI-3760 "Consult 29,
	GO record 12 has GEN = 0" but sometime prior to
	2023-01-23T07:18:36PST it was resolved by Lisa.

	  """
	},


	{
	'my_run_name' : "DOB_First_Height_Weight_Then_Random_Unless_Error_Yes_Working",	
	'list_of_consults' : 	[26, 19, 70, 72, 85, 89, 131, 146, 188, 189],
	# 2022-12-19T10:30:30PST moved 26 from BirthSexFirst_Height_Weight_AllZeroUnlessError_NeedingAttention to DOB_First_Height_Weight_Then_Random_Unless_Error_Yes_Working
	# 2022-12-19T10:56:25PST not sex first, dob first, moved 189 from RemainingConsultsAssumed_SexDOBHeightWeight_yes_okay to DOB_First_Height_Weight_Then_Random_Unless_Error_Yes_Working
	'patient_ans_script_filename' : 'dob_height_weight_then_random_unless_error.json'
	},
	{
	'my_run_name' : "ChildrensConsults_not_suffering_Consys_322",
	'list_of_consults' : [311, 315, 318, 320, 321, 323, 324, 325, 326, 327, 329, 330, 331],
	'patient_ans_script_filename' : 'sex_dob_height_weight_then_random_unless_error_for_children.json'
	},
	{
	'my_run_name' : "RemainingConsultsAssumed_SexDOBHeightWeight_not_okay",
	'list_of_consults' : [
		87, 117, 140
		],

	'patient_ans_script_filename' : 'sex_dob_height_weight_then_random_unless_error.json'
	# see Triage Notes (in test_question_driver_experiments.py) for RemainingConsultsAssumed_SexDOBHeightWeight_not_okay	
	},
	{
	'my_run_name' : "BirthSexFirst_Height_Weight_AllZeroUnlessError_Okay",
	'list_of_consults' : [3, 8, 9, 11, 15, 16, 17, 20, 24, 27, 32, 40, 47, 49, 55, 57, 59, 66],
	'patient_ans_script_filename' : 'sex_dob_height_weight_then_random_unless_error.json'
	},
	{
	'my_run_name' : "BirthSexFirst_Height_Weight_AllZeroUnlessError_NeedingAttention",
	'list_of_consults' : [28, 43],
	'patient_ans_script_filename' : 'sex_dob_height_weight_then_random_unless_error.json',
	'comment' : """2022-12-19T11:42:46PST 7 was moved from
	BirthSexFirst_Height_Weight_AllZeroUnlessError_NeedingAttention
	to JIRA-CI-3784_sex_dob_h_w"""
	},
	{
	'my_run_name' : "ChildrensConsults_yes_suffering_Consys_322",
	'list_of_consults' : [322, 328],
	'patient_ans_script_filename' : 'sex_dob_height_weight_then_random_unless_error_for_children.json'
	},
	{
	'my_run_name' : "Consults_suffering_Consys_299",
	'list_of_consults' : [14],
	'patient_ans_script_filename' : 'sex_dob_height_weight_then_random_unless_error.json'
	# see Triage Notes (in test_question_driver_experiments.py) for Consults_suffering_Consys_299
	# 2022-12-19T10:39:34PST I see that Consults_suffering_Consys_299 is resolved.  But
	# 62 is still failing, now due to https://arnoldmedia.jira.com/browse/CI-3784.  
	},
	{
	'my_run_name' :			"DOB_First_Height_Weight_Then_Random_Unless_Error_Not_Working",
	'list_of_consults' :		[76, 82],
	'patient_ans_script_filename' : 'dob_height_weight_then_random_unless_error.json'
	},
	{
	'my_run_name' : "RemainingConsultsAssumed_SexDOBHeightWeight_yes_okay",
	'list_of_consults' : [
		4, 73, 77, 98, 101, 102, 108, 110, 115, 116, 119, 127, 134,
		142, 144, 145, 147, 148, 152, 155, 156, 157, 158, 159, 160,
		161, 163, 165, 166, 168, 176, 178, 179, 181, 182, 183, 184,
		187, 610
	],
	'patient_ans_script_filename' : 'sex_dob_height_weight_then_random_unless_error.json'
	}
	# 2023-01-16T21:43:00PST comment out bc there's already one named 'JIRA-CI-3784_sex_dob_h_w' and it already has 308, amongst others.
	# {
	# 'my_run_name' : "JIRA-CI-3784_sex_dob_h_w",
	# 'list_of_consults' : [308],
	# 'patient_ans_script_filename' : 'sex_dob_height_weight_then_random_unless_error.json'
	# # see Triage Notes (in test_question_driver_experiments.py) for RemainingConsultsAssumed_SexDOBHeightWeight_not_okay	
	# },

	]

# run_test_question_driver_over_list_of_consult_lists(
# 	consult_list_objects = FULL_LIST_OF_TEST_GROUPS_03,
# 	base_dir_for_massive_run_of_runs = DEFAULT_LOG_FOR_FULLSCALE_RUNS,
# 	run_name = "1st_w_random_answers"
# 	)
# the above ended up with these...
#
# 2022-12-28T000447.1st_w_random_answers
# 2023-01-03T221146.1st_w_random_answers
# 2023-01-10T070544.1st_w_random_answers
#
# so 2023-01-03T221146.1st_w_random_answers should be renamed 2023-01-03T221146.2nd_w_random_answers
# so 2023-01-10T070544.1st_w_random_answers should be renamed 2023-01-10T070544.3rd_w_random_answers

# run_test_question_driver_over_list_of_consult_lists(
# 	consult_list_objects = FULL_LIST_OF_TEST_GROUPS_03,
# 	base_dir_for_massive_run_of_runs = DEFAULT_LOG_FOR_FULLSCALE_RUNS,
# 	run_name = "run_004_w_random_answers"
# 	)
# TODO 2023-01-17T10:01:53PST I don't think I've done a Guidance Option on the above, yet

# 2023-01-17T10:02:10PST about to start this.
# run_test_question_driver_over_list_of_consult_lists(
# 	consult_list_objects = FULL_LIST_OF_TEST_GROUPS_03,
# 	base_dir_for_massive_run_of_runs = DEFAULT_LOG_FOR_FULLSCALE_RUNS,
# 	run_name = "run_004_w_random_answers"
# 	)

# 2023-01-22T22:34:14PST about to start
# run_test_question_driver_over_list_of_consult_lists(
# 	consult_list_objects = FULL_LIST_OF_TEST_GROUPS_03,
# 	base_dir_for_massive_run_of_runs = DEFAULT_LOG_FOR_FULLSCALE_RUNS,
# 	run_name = "run_005_w_random_answers"
# 	)
# 	# 2023-01-23T16:09:07PST this did not have the new kb.  But it ran fast!!

# 2023-01-23T16:09:37PST starting
# run_test_question_driver_over_list_of_consult_lists(
# 	consult_list_objects = FULL_LIST_OF_TEST_GROUPS_03,
# 	base_dir_for_massive_run_of_runs = DEFAULT_LOG_FOR_FULLSCALE_RUNS,
# 	run_name = "run_006_w_random_answers_1st_w_new_kb"
# 	)

# run_test_question_driver_over_list_of_consult_lists(
# 	consult_list_objects = FULL_LIST_OF_TEST_GROUPS_03,
# 	base_dir_for_massive_run_of_runs = DEFAULT_LOG_FOR_FULLSCALE_RUNS,
# 	run_name = "run_007_w_random_answers"
# 	)

JUST_THE_BLOOD_PRESSURE_AND_A1C_ONES =\
	[
	{
	'my_run_name' : "JustCpd62-AIC",
	'list_of_consults' : [62],
	'patient_ans_script_filename' : 'special_script_for_cpd_62_v01.json',
	'comment' : """

	2023-02-04T07:24:39PST dealing with this error from a most recent run

	"BotError JSON is: A1C must be between 3.0 and 30.0."

	Dealing with 2023-01-30T093709.JIRA-CI-3784_sex_dob_h_w/Consult.2023-01-30T093751-Cpd-62/conversation_text.org:BotError JSON is: A1C must be between 3.0 and 30.0.

	Full Path is:

	~/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/GenDataForTestGuidOpt-FullScale/2023-01-31T195050.run_007_w_random_answers/2023-01-31T195522.JIRA-CI-3784_sex_dob_h_w/Consult.2023-01-31T195556-Cpd-62/conversation_text.org

	See "* 2023-02-01 Meeting" in diary.
	  """
	},	
	{
	'my_run_name' : "JustCpd7-BloodPressure",
	'list_of_consults' : [7],
	'patient_ans_script_filename' : 'sex_dob_hgt_wgt_waist_bp_then_random_unless_error.json',

	'comment' : """
	2023-02-04T07:21:54PST dealing with this error from a most recent run

	2023-01-31T195522.JIRA-CI-3784_sex_dob_h_w/Consult.2023-01-31T195522-Cpd-7/conversation_text.org:BotError JSON is: Please provide an entry for SYSTOLIC BLOOD PRESSURE between 40 and 300.

	Full path is:

	~/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/GenDataForTestGuidOpt-FullScale/2023-01-31T195050.run_007_w_random_answers/2023-01-31T195522.JIRA-CI-3784_sex_dob_h_w/Consult.2023-01-31T195522-Cpd-7/conversation_text.org

	See "* 2023-02-01 Meeting" in diary.

	"""
	
	}
	]

# run_test_question_driver_over_list_of_consult_lists(
# 	consult_list_objects = JUST_THE_BLOOD_PRESSURE_AND_A1C_ONES,
# 	base_dir_for_massive_run_of_runs = DEFAULT_LOG_FOR_FULLSCALE_RUNS,
# 	run_name = "run_class_08_focused_on_cpd_7_and_62"
# 	)

import test_consult_set_2023_02_06T1150
run_test_question_driver_over_list_of_consult_lists(
	consult_list_objects = test_consult_set_2023_02_06T1150.consult_set,
	base_dir_for_massive_run_of_runs = DEFAULT_LOG_FOR_FULLSCALE_RUNS,
	run_name = "run_class_08_focused_col_contains_no_ele_matching_pred"
	)
