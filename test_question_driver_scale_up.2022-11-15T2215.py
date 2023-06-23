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
	patient_ans_script_base_dir = DEFAULT_PATIENT_ANSWER_SCRIPT_BASE_DIR):

	for counter, obj in enumerate(consult_list_objects):
		if counter == 0:
				if not(os.path.isdir(base_dir_for_massive_run_of_runs)):
					print("Error, non existant directory: {base_dir_for_massive_run_of_runs}")
					pdb.set_trace()
				else:
					timestamp_for_this_run_of_runs = now_yyyy_mm_ddThhmmss()
					dirpath_for_this_list_of_consults = os.path.join(base_dir_for_massive_run_of_runs, timestamp_for_this_run_of_runs)
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

	print("################################################################")
	print("################################################################")
	print("##### Here Yee, Here Yee, we are commencing .... ###############")
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
		try:
	
			question_and_answer_loop(consult_number,
				log_basedir = dir_path_for_this_test_group,
				patient_sim_script_fpath = my_patient_sim_script_fpath,
				timestamp_in_log_dir = timestamp_for_run_of_this_consult)
				
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
				print(error_msg, file=out_obj)
				print(file=out_obj)
				
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



TEST_LIST_OF_CONSULT_LIST_OBJECTS = [
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

run_test_question_driver_over_list_of_consult_lists(
	consult_list_objects = TEST_LIST_OF_CONSULT_LIST_OBJECTS,
	base_dir_for_massive_run_of_runs = DEFAULT_LOG_FOR_FULLSCALE_RUNS
	)

