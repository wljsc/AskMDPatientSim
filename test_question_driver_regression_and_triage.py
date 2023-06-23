# test_question_driver_regression_and_triage.py
################################################################
# PURPOSE:

# this is the successor to test_question_driver_experiments.py

# whereas that was experiments, now in this
# (test_question_driver_regression_and_triage.py) we are getting well
# defined enough where we have:

# (1) known good cases (aka regression tests)

# (2) things we are triaging, managing, debugging

################################################################
# HISTORY:
# (newest on top)

# test_question_driver_regression_and_triage.2022-07-06T1527.py
# last version before we resolved the hot flashes issues (e.g.
#
# CONSYS-319 CPD #76 errors out during hot flashes question: Cannot read property 'length' of undefined.
# CONSYS-329: CPD # 117 Cannot read property 'length' of undefinedIN QA
# CONSYS-330: CPD # 140 Cannot read property 'length' of undefinedIN QA,
# CONSYS-332: Cpd 43,76,82,87,148  TypeError: Cannot read property 'length' of undefined

# test_question_driver_regression_and_triage.py<Code>

# 2022-07-04T22:28:13PDT added two more that were missing 4 and 19.
# That should be everything.

# 2022-07-04T09:44:29PDT Tallying Status - 14 to 15 consults need work
# 7 suffer from "CONSYS-330 CPD # 140 Cannot read property 'length' of undefined"

# 2022-06-30T17:08:27PDT
# test_question_driver_regression_and_triage.v01.py
# good place to cut bc all the NotNeedWork should actually work


# 2022-06-30T07:53:04PDT created this by copying section called
# "Moving Towards Regression Tests"

################################################################
# ACTUAL CODE CONTENT IS BELOW HERE
################################################################
# IMPORTS

from pathlib import Path
import pdb

from test_question_driver import question_and_answer_loop

################################

# NotNeedWork = 9
DOB_First_Height_Weight_Then_All_Zero_Unless_Error_Yes_Working = \
[19, 26, 70, 72, 76, 82, 85, 89, 131, 146, 188, 189]
# dob_height_weight_then_all_zero_unless_error.json


# DOB_First_Height_Weight_Then_All_Zero_Unless_Error_Not_Working = [] (-: All done


################################

# NotNeedWork = 37
RemainingConsultsAssumed_SexDOBHeightWeight_yes_okay = \
[
4, 73, 87, 101, 108, 110, 140, 115, 119, 127, 134,
142, 144, 145, 148, 152, 155, 156, 157, 158, 159, 
165, 166, 168, 176, 178, 179, 181, 182, 183, 
184, 187, 610
]
# sex_dob_height_weight_then_all_zero_unless_error.json")


# YesNeedWork: 4
RemainingConsultsAssumed_SexDOBHeightWeight_not_okay = \
[
77, 98, 116, 117, 147, 161 , 160, 163,
]
# SCRIPT: sex_dob_height_weight_then_all_zero_unless_error.json
# see Triage Notes for RemainingConsultsAssumed_SexDOBHeightWeight_not_okay

################################

# NotNeedWork 20
BirthSexFirst_Height_Weight_AllZeroUnlessError_Okay = \
[3, 8, 9, 11, 14, 15, 16, 17, 20, 24, 27, 29, 32,
40, 43, 47, 49, 55, 57, 59, 66]
# SCRIPT: sex_dob_height_weight_then_all_zero_unless_error.json

# NotNeedWork 1
BirthSexFirst_Height_Weight_DiabetesMngmntr_Okay = \
[62]
# SCRIPT: cpd-62-diabetes.2022-07-02a.json

# YesNeedWork: 4
BirthSexFirst_Height_Weight_AllZeroUnlessError_NeedingAttention = \
[6, 7, 28]
# SCRIPT: sex_dob_height_weight_then_all_zero_unless_error.json
# see Triage Notes see "Triage Notes for BirthSexFirst_Height_Weight_AllZeroUnlessError_NeedingAttention"
################################

# NotNeedWork 13 (2022-06-29)
ChildrensConsults_not_suffering_Consys_322 = \
[311, 315, 318, 320, 321, 323, 324, 325, 326, 327, 329, 330, 331]
# SCRIPT: sex_dob_height_weight_then_all_zero_unless_error_for_children.json

# YesNeedWork: 3
ChildrensConsults_yes_suffering_Consys_322 = \
[308, 322, 328]
# SCRIPT: sex_dob_height_weight_then_all_zero_unless_error_for_children.json
# See Triage Notes For ChildrensConsults_yes_suffering_Consys_322

################################
# YesNeedWork: 1
Consults_suffering_Consys_299 = [14] 

# SCRIPT: sex_dob_height_weight_then_all_zero_unless_error.json")
# see Triage Notes (below) for Consults_suffering_Consys_299

################################################################
# Triage Notes for DOB_First_Height_Weight_Then_All_Zero_Unless_Error_Not_Working
################################################################


################################################################
# Triage Notes for RemainingConsultsAssumed_SexDOBHeightWeight_not_okay
################################################################

# 117, PROBLEM
# BotAsks QuesSeq# 3 QuesId# 1 Title: 'Type of MS' CPD: 117
# ResponseHeader: 'Which type of MS do you have?'
# TypeError: Cannot read property 'length' of undefined
# SCRIPT: sex_dob_height_weight_then_all_zero_unless_error.json
# WAITING: https://arnoldmedia.jira.com/browse/CONSYS-329 CPD # 117 Cannot read property 'length' of undefined

# 140, PROBLEM
# BotAsks QuesSeq# 4 QuesId# 28 Title: 'Severity of symptoms' CPD: 140
# ResponseHeader: 'How severe are your allergy symptoms?'
# TypeError: Cannot read property 'length' of undefined
# SCRIPT: sex_dob_height_weight_then_all_zero_unless_error.json
# WAITING: https://arnoldmedia.jira.com/browse/CONSYS-330 CPD # 140 Cannot read property 'length' of undefined (created 2022-07-02T20:26:56PDT) 

# 147, PROBLEM
# BotAsks QuesSeq# 2 QuesId# 30 Title: 'Height and weight' CPD: 147
# ResponseHeader: 'What is your height?
# FLAG: AUTO MODE: user_reply_txt is: 166
# SCRIPT: sex_dob_height_weight_then_all_zero_unless_error.json
# WAITING: https://arnoldmedia.jira.com/browse/CONSYS-331 "CPD # 147: can't determine that question is a type in" (created 2022-07-02T22:32:05PDT) 

# User chose: 166
# Traceback (most recent call last):
#   File "test_question_driver_regression_and_triage.py", line 131, in <module>
#     question_and_answer_loop(cpd,
#   File "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Code/test_question_driver.py", line 766, in question_and_answer_loop
#     process_system_reply(bot_output_json,
#   File "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Code/test_question_driver.py", line 1552, in process_system_reply
#     response_content = response_content_list[users_choice]
# IndexError: list index out of range

################################################################
# Triage Notes for BirthSexFirst_Height_Weight_AllZeroUnlessError_NeedingAttention
# [6, 7, 28, 43]

# 6, PROBLEM 
# "FullTopic": "High Blood Pressure Diagnosis"
# BotAsks QuesSeq# 3 QuesId# 10 Title: 'Blood pressure'
# Please provide an entry for SYSTOLIC BLOOD PRESSURE that is greater than the DIASTOLIC BLOOD PRESSURE.
# SCRIPT: sex_dob_height_weight_then_all_zero_unless_error.json
# WAITING: https://arnoldmedia.jira.com/browse/CONSYS-334 334 CPD # 6 & 7 Need to know how to encode blood pressure

# 7, PROBLEM  # "High Blood Pressure Management",
# SCRIPT: sex_dob_height_weight_then_all_zero_unless_error.json
# WAITING: https://arnoldmedia.jira.com/browse/CONSYS-334 334 CPD # 6 & 7 Need to know how to encode blood pressure

# 28, PROBLEM "Diarrhea Diagnosis"
# BotAsks QuesSeq# 4 QuesId# 20 Title: 'Cholesterol and triglyceride levels' CPD: 28
# ResponseHeader: 'Enter your most recent cholesterol and triglyceride levels. Leave blank if you are unsure.
# "TypeError: Cannot read property 'getEntityId' of null"
# WAITING https://arnoldmedia.jira.com/browse/CONSYS-333 CPD # 28: TypeError: Cannot read property 'getEntityId' of null

################################################################
# Triage Notes For ChildrensConsults_yes_suffering_Consys_322
################################################################

# 308, PROBLEM
# BotAsks QuesSeq# 1 QuesId# 1 Title: 'Birth sex, date of birth' CPD: 308
# ResponseHeader: 'None
# TypeError: Cannot read property 'getResponses' of null
# WAITING https://arnoldmedia.jira.com/browse/CONSYS-322 Cpd #322 (& 328,308) "TypeError: Cannot read property 'getResponses' of null"

# 322, PROBLEM
# WAITING (i.e. see https://arnoldmedia.jira.com/browse/CONSYS-322 )

# 328, PROBLEM
# WAITING (i.e. see https://arnoldmedia.jira.com/browse/CONSYS-322 )

################################################################
# Triage Notes for Consults_suffering_Consys_299

################################################################
# IMPORTS
################################################################

import os

################################################################
# CODE
################################################################

def run_regression_tests(regression_test_dir):

	if os.path.exists(regression_test_dir): 

		regression_test_dir_basename = os.path.basename(regression_test_dir)
		
		print(
		f"""
		################
		ERROR: the regression_test_dir {regression_test_dir_basename} already exists!!!
		################

		This function (@fun run_regression_tests) wants to
		prevent you from overwriting/contanimating prior logs
		of regression tests.

		Thus, I think you either:

		(a) want to call @func run_regression_tests with a
		different value for @param regression_test_dir.

		or 

		(b) your prior run using {regression_test_dir} was
		aborted and you should blow it away and start the test
		afresh.

		This is because you want the output for each test of a
		CPD to be stored in a tabula rasa dir so that for each
		CPD output dir, you know the code that generated this
		was the same.""")
		pdb.set_trace()

	else:
		os.mkdir(regression_test_dir)

	for cpd in DOB_First_Height_Weight_Then_All_Zero_Unless_Error_Yes_Working:
		question_and_answer_loop_for_regression_testing(cpd,
			log_basedir = regression_test_dir,
			patient_sim_script_fpath = "../PatientSimulatorScripts/dob_height_weight_then_all_zero_unless_error.json")

	for cpd in RemainingConsultsAssumed_SexDOBHeightWeight_yes_okay:
	 	question_and_answer_loop_for_regression_testing(cpd,
	 		log_basedir = regression_test_dir,
			patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json")
	   
	for cpd in BirthSexFirst_Height_Weight_DiabetesMngmntr_Okay:
	 	question_and_answer_loop_for_regression_testing(cpd,
	 		log_basedir = regression_test_dir,
			patient_sim_script_fpath = "../PatientSimulatorScripts/cpd-62-diabetes.2022-07-02a.json")

	for cpd in BirthSexFirst_Height_Weight_AllZeroUnlessError_Okay:
	 	question_and_answer_loop_for_regression_testing(cpd,
	 		log_basedir = regression_test_dir,
			patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json")

	for cpd in ChildrensConsults_not_suffering_Consys_322:
	 	question_and_answer_loop_for_regression_testing(cpd,
	 		log_basedir = regression_test_dir,
			patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error_for_children.json")


def question_and_answer_loop_for_regression_testing(cpd, log_basedir, patient_sim_script_fpath, timestamp_in_log_dir_p = False):

	"""This is merely a wrapper around @func
	question_and_answer_loop to ensure that, by default, we do NOT
	put timestamps in the dir names for each test.  You want
	regression tests to have log dirs that are 'repeatable'.
	I.e. you can run recursive file diffs on them and if you put a
	timestampe in each dir name then the dir names are different
	bc they were run at different times.  That's why we want
	timestamp_in_log_dir_p to be false (or at least, false by
	default)"""

	question_and_answer_loop(cpd, log_basedir, patient_sim_script_fpath, timestamp_in_log_dir_p = timestamp_in_log_dir_p)

#run_regression_tests("../Logs-Generic/RegressTstLogs/RegressionTestLogs5")
#run_regression_tests("../Logs-Generic/RegressTstLogs/RegressionTestLogs6-Random")
run_regression_tests("../Logs-Generic/RegressTstLogs/RegressionTestLogs7-NonRandom")

# Bot Response is QuesSeq# 2 QuesID# NoID-BcBotError (ConsultID 77)
#  Please provide a height between 1 foot and 8 feet.
# 2022-07-06T08:16:29PDT Edit made but not commited
# 2022-07-06T17:08:57PDT Commit seems not to have taken!! Michael debugging
# TODO



##### Starting Dialog: Consult 102 ######
# TODO   Please provide a height between 1 foot and 8 feet.
# defaultUnit:  {'id': 1, 'display': 'miles'}

##### Starting Dialog: Consult 116 ######
# TODO  Please provide a height between 1 foot and 8 feet.
            # "idForHumans": "Fnd-null-GenNo-16645-Cpd-116-RecNum-16645",
            # "state": "PRESENT",
            # "valueObject": {
            #     "format": "DOUBLE",
            #     "myDisplayForDefaultUnit": "miles",

# Bot Response is QuesSeq# 2 QuesID# NoID-BcBotError (ConsultID 160)
# TODO  Please provide a height between 1 foot and 8 feet.

# Bot Response is QuesSeq# 2 QuesID# NoID-BcBotError (ConsultID 161)
#  Please provide a height between 1 foot and 8 feet.

##### Starting Dialog: Consult 163 ######
# ResponseHeader: 'What is your weight?
# defaultUnit:  {'id': 1, 'display': 'tons'}

# ##### Starting Dialog: Consult 47 ######
# ResponseHeader: 'What is your height?
# defaultUnit:  {'id': 1, 'display': 'miles'}
# FLAG: AUTO MODE: user_reply_txt is: 66
#  Please provide a height between 1 foot and 8 feet.
# TODO

################
# CONSULT 98
# Here is the error msg:
#
#  Please provide a height between 1 foot and 8 feet.
            # "idForHumans": "Fnd-null-GenNo-16645-Cpd-98-RecNum-16645",
            # "state": "PRESENT",
            # "valueObject": {
            #     "format": "DOUBLE",
            #     "myDisplayForDefaultUnit": "miles",

