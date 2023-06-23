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
[26, 70, 72, 85, 89, 131, 146, 188, 189]
# dob_height_weight_then_all_zero_unless_error.json

# YesNeedWork: 2
DOB_First_Height_Weight_Then_All_Zero_Unless_Error_Not_Working = \
[76, 82]
# dob_height_weight_then_all_zero_unless_error.json
# see Triage Notes for DOB_First_Height_Weight_Then_All_Zero_Unless_Error_Not_Working

################################

# NotNeedWork = 36
RemainingConsultsAssumed_SexDOBHeightWeight_yes_okay = \
[
73, 77, 98, 101, 102, 108, 110, 115, 116, 119, 127, 134,
142, 144, 145, 148, 152, 155, 156, 157, 158, 159, 160,
161, 163, 165, 166, 168, 176, 178, 179, 181, 182, 183, 
187, 610
]
# sex_dob_height_weight_then_all_zero_unless_error.json")

RemainingConsultsAssumed_SexDOBHeightWeight_yes_okay_continuing = \
[
148, 152, 155, 156, 157, 158, 159, 160,
161, 163, 165, 166, 168, 176, 178, 179, 181, 182, 183, 
184, 187, 610
]
# sex_dob_height_weight_then_all_zero_unless_error.json")

# YesNeedWork: 1
RemainingConsultsAssumed_SexDOBHeightWeight_not_okay = \
[
87
]
# sex_dob_height_weight_then_all_zero_unless_error.json
# see Triage Notes (below) for RemainingConsultsAssumed_SexDOBHeightWeight_not_okay

# YesNeedWork: 1
RemainingConsultsAssumed_SexDOBHeightWeight_not_okay_JIRAified = \
[
117, 140, 147
]
# SCRIPT: sex_dob_height_weight_then_all_zero_unless_error.json
# JIRAS:
# 117 https://arnoldmedia.jira.com/browse/CONSYS-329 (created 2022-07-02T20:26:56PDT) 
# 140 https://arnoldmedia.jira.com/browse/CONSYS-330 (created 2022-07-02T20:26:56PDT) CPD # 140 Cannot read property 'length' of undefined
# 147 https://arnoldmedia.jira.com/browse/CONSYS-331 (created 2022-07-02T22:32:05PDT) CPD #147: can't determine that question is a type in


################################

# NotNeedWork 20
BirthSexFirst_Height_Weight_AllZeroUnlessError_Okay = \
[3, 8, 9, 11, 14, 15, 16, 17, 20, 24, 27, 29, 32,
40, 47, 49, 55, 57, 59, 66]
# SCRIPT: sex_dob_height_weight_then_all_zero_unless_error.json

# NotNeedWork 1
BirthSexFirst_Height_Weight_DiabetesMngmntr_Okay = \
[62]
# SCRIPT: cpd-62-diabetes.2022-07-02a.json

# YesNeedWork: 5
BirthSexFirst_Height_Weight_AllZeroUnlessError_NeedingAttention = \
[6, 7, 28, 43]
# SCRIPT: sex_dob_height_weight_then_all_zero_unless_error.json
# TODO keep making Triage Notes see "Triage Notes for BirthSexFirst_Height_Weight_AllZeroUnlessError_NeedingAttention"
# 6, 7 figure out how to add blood pressure (see triage notes)
################################

# NotNeedWork 13 (2022-06-29)
ChildrensConsults_not_suffering_Consys_322 = \
[311, 315, 318, 320, 321, 323, 324, 325, 326, 327, 329, 330, 331]
# SCRIPT: sex_dob_height_weight_then_all_zero_unless_error_for_children.json

# YesNeedWork: 3
ChildrensConsults_yes_suffering_Consys_322 = \
[322, 328, 308]
# SCRIPT: sex_dob_height_weight_then_all_zero_unless_error_for_children.json

################################
# YesNeedWork: 2
Consults_suffering_Consys_299 = [14] 

# SCRIPT: sex_dob_height_weight_then_all_zero_unless_error.json")
# see Triage Notes (below) for Consults_suffering_Consys_299

################################################################
# Triage Notes for DOB_First_Height_Weight_Then_All_Zero_Unless_Error_Not_Working
################################################################
# 76, PROBLEM
# BotAsks QuesSeq# 5 QuesId# 56 Title: 'Menopause Rating Scale 1' CPD: 76
# ResponseHeader: 'Do you have hot flashes, sweating (episodes of sweating)?'
# User chose: 0
# TypeError: Cannot read property 'length' of undefined
# TODO add to other JIRA(s) with TypeError: Cannot read property 'length' of undefined
# SCRIPT: dob_height_weight_then_all_zero_unless_error.json

# 82, PROBLEM
# BotAsks QuesSeq# 3 QuesId# 1 Title: 'Bladder emptiness after urinating' CPD: 82
# ResponseHeader: 'Over the past month, how often have you had a sensation of not emptying your bladder completely after you finished urinating?'
# User chose: 0
# "TypeError: Cannot read property 'length' of undefined"
# SCRIPT: dob_height_weight_then_all_zero_unless_error.json
# TODO add to other JIRA(s) with TypeError: Cannot read property 'length' of undefined

################################################################
# Triage Notes for RemainingConsultsAssumed_SexDOBHeightWeight_not_okay
################################################################
# 87,  PROBLEM
# BotAsks QuesSeq# 5 QuesId# 1 Title: 'Frequency of asthma symptoms' CPD: 87
# 87 Problem ResponseHeader: 'How frequent are your asthma symptoms?'
# TypeError: Cannot read property 'length' of undefined
# TODO add to other JIRA(s) with TypeError: Cannot read property 'length' of undefined 

# 89, RESOLVED
# BotAsks QuesSeq# 1 QuesId# 18 Title: 'Date of birth' CPD: 89
# Text '0' could not be parsed, unparsed text found at index 0
# https://arnoldmedia.jira.com/browse/CONSYS-324 RESOLVED.

# 117, PROBLEM
# BotAsks QuesSeq# 3 QuesId# 1 Title: 'Type of MS' CPD: 117
# ResponseHeader: 'Which type of MS do you have?'
# TypeError: Cannot read property 'length' of undefined
# TODO add to other JIRA(s) with TypeError: Cannot read property 'length' of undefined

# 140, PROBLEM
# BotAsks QuesSeq# 4 QuesId# 28 Title: 'Severity of symptoms' CPD: 140
# ResponseHeader: 'How severe are your allergy symptoms?'
# TypeError: Cannot read property 'length' of undefined
# TODO add to other JIRA(s) with TypeError: Cannot read property 'length' of undefined

# 147, PROBLEM - either a simulator problem or it's answering weight to a height question so script needs to change
# BotAsks QuesSeq# 2 QuesId# 30 Title: 'Height and weight' CPD: 147
# ResponseHeader: 'What is your height?
# FLAG: AUTO MODE: user_reply_txt is: 166

# User chose: 166
# Traceback (most recent call last):
#   File "test_question_driver_regression_and_triage.py", line 131, in <module>
#     question_and_answer_loop(cpd,
#   File "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Code/test_question_driver.py", line 766, in question_and_answer_loop
#     process_system_reply(bot_output_json,
#   File "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Code/test_question_driver.py", line 1552, in process_system_reply
#     response_content = response_content_list[users_choice]
# IndexError: list index out of range

# 184 PROBLEM CPD: 184

# 2022-07-02T22:57:44PDT This was resolved.  There were notes which I
# saved to: "2022-07-02T22:55:27PDT Spew from Triage Section of"
# ~/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/diary-TestCoupletPrograms.org

# 308, PROBLEM
# BotAsks QuesSeq# 1 QuesId# 1 Title: 'Birth sex, date of birth' CPD: 308
# ResponseHeader: 'None
# TypeError: Cannot read property 'getResponses' of null
# see https://arnoldmedia.jira.com/browse/CONSYS-322 

################################################################
# Triage Notes for BirthSexFirst_Height_Weight_AllZeroUnlessError_NeedingAttention
# [6, 7, 26, 43]

# 6, PROBLEM 
# "FullTopic": "High Blood Pressure Diagnosis"
# BotAsks QuesSeq# 3 QuesId# 10 Title: 'Blood pressure'
# Please provide an entry for SYSTOLIC BLOOD PRESSURE that is greater than the DIASTOLIC BLOOD PRESSURE.
# TODO figure out how to enter blood pressure

# 7, PROBLEM  # "High Blood Pressure Management",
# TODO figure out how to enter blood pressure

################################################################
# Triage Notes for Consults_suffering_Consys_299

# TODO see 2022-06-29T17:54:59PDT in diary-TestCoupletPrograms.org
# (need to improve test_question_driver.py)
# 2022-07-02T18:49:39PDT I think progress has been made against this.  I know I 
# was just ablve to take 62 out of Consults_suffering_Consys_299

################################################################
# RUN THE REGRESSION TESTS

def run_regression_tests(regression_test_dir):

	if os.path.exists(regression_test_dir): 

		print("""I don't think you really want to run this.
		You want the output to be stored in a tabula rasa dir
		so that for each CPD output dir, you know the code
		that generated this was the same.""")
		pdb.set_trace()

	else:
		os.mkdir(regression_test_dir)

	for cpd in DOB_First_Height_Weight_Then_All_Zero_Unless_Error_Yes_Working:
		question_and_answer_loop(cpd,
			log_basedir = regression_test_dir,
			patient_sim_script_fpath = "../PatientSimulatorScripts/dob_height_weight_then_all_zero_unless_error.json")

	for cpd in RemainingConsultsAssumed_SexDOBHeightWeight_yes_okay:
	 	question_and_answer_loop(cpd,
	 		log_basedir = regression_test_dir,
			patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json")
	   
	for cpd in BirthSexFirst_Height_Weight_DiabetesMngmntr_Okay:
	 	question_and_answer_loop(cpd,
	 		log_basedir = regression_test_dir,
			patient_sim_script_fpath = "../PatientSimulatorScripts/cpd-62-diabetes.2022-07-02a.json")

	for cpd in BirthSexFirst_Height_Weight_AllZeroUnlessError_Okay:
	 	question_and_answer_loop(cpd,
	 		log_basedir = regression_test_dir,
			patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json")

	for cpd in ChildrensConsults_not_suffering_Consys_322:
	 	question_and_answer_loop(cpd,
	 		log_basedir = regression_test_dir,
			patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error_for_children.json")
	)


run_regression_tests("RegressionTestLogs4")