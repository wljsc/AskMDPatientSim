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

# 2022-06-30T17:08:27PDT test_question_driver_regression_and_triage.v01.py



# 2022-06-30T07:53:04PDT created this by copying section called
# "Moving Towards Regression Tests"

################################################################
# ACTUAL CODE CONTENT IS BELOW HERE
################################################################
# IMPORTS

from test_question_driver import question_and_answer_loop

################################

# NotNeedWork = 8
DOB_First_Height_Weight_Then_All_Zero_Unless_Error_Yes_Working = \
[70, 72, 85, 89, 131, 146, 188, 189]
# dob_height_weight_then_all_zero_unless_error.json

# YesNeedWork: 2
DOB_First_Height_Weight_Then_All_Zero_Unless_Error_Not_Working = \
[76, 82]
# dob_height_weight_then_all_zero_unless_error.json
# TODO need triage notes

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
187, 610
]
# sex_dob_height_weight_then_all_zero_unless_error.json")

# YesNeedWork: 5
RemainingConsultsAssumed_SexDOBHeightWeight_not_okay = \
[
87, 89, 117, 140, 147, 184, 308, 
]
# sex_dob_height_weight_then_all_zero_unless_error.json
# see Triage Notes (below) for RemainingConsultsAssumed_SexDOBHeightWeight_not_okay

################################

# NotNeedWork 20
BirthSexFirst_Height_Weight_AllZeroUnlessError_Okay = \
[3, 8, 9, 11, 14, 15, 16, 17, 20, 24, 27, 29, 32,
40, 47, 49, 55, 57, 59, 66]
# SCRIPT: sex_dob_height_weight_then_all_zero_unless_error.json

# YesNeedWork: 6
BirthSexFirst_Height_Weight_AllZeroUnlessError_NeedingAttention = \
[6, 7, 26, 28, 43, 62]
# SCRIPT: sex_dob_height_weight_then_all_zero_unless_error.json
# TODO keep making Triage Notes see "Triage Notes for BirthSexFirst_Height_Weight_AllZeroUnlessError_NeedingAttention"

################################

# NotNeedWork 13 (2022-06-29)
ChildrensConsults_not_suffering_Consys_322 = \ 
[311, 315, 318, 320, 321, 323, 324, 325, 326, 327, 329, 330, 331]
# SCRIPT: sex_dob_height_weight_then_all_zero_unless_error_for_children.json

# YesNeedWork: 2
ChildrensConsults_yes_suffering_Consys_322 = \
[322, 328]
# SCRIPT: sex_dob_height_weight_then_all_zero_unless_error_for_children.json

################################
# YesNeedWork: 2
Consults_suffering_Consys_299 = [14, 62] 

# SCRIPT: sex_dob_height_weight_then_all_zero_unless_error.json")
# see Triage Notes (below) for Consults_suffering_Consys_299

################################################################
# Triage Notes for RemainingConsultsAssumed_SexDOBHeightWeight_not_okay
################################################################
#87,  PROBLEM
# BotAsks QuesSeq# 5 QuesId# 1 Title: 'Frequency of asthma symptoms' CPD: 87
# 87 Problem ResponseHeader: 'How frequent are your asthma symptoms?'
# TypeError: Cannot read property 'length' of undefined

#89, PROBLEM (easy fix - just dob first, right?)
#BotAsks QuesSeq# 1 QuesId# 18 Title: 'Date of birth' CPD: 89
#Text '0' could not be parsed, unparsed text found at index 0

# 117, PROBLEM
# BotAsks QuesSeq# 3 QuesId# 1 Title: 'Type of MS' CPD: 117
# ResponseHeader: 'Which type of MS do you have?'
# TypeError: Cannot read property 'length' of undefined

# 140, PROBLEM
# BotAsks QuesSeq# 4 QuesId# 28 Title: 'Severity of symptoms' CPD: 140
# ResponseHeader: 'How severe are your allergy symptoms?'
# TypeError: Cannot read property 'length' of undefined

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
# I *am* able to continue beyond this 

# BotAsks QuesSeq# 8 QuesId# 5 Title: 'Medications' CPD: 184

# WARNING: Weird, why is @param response_content_list empty!?!?! (while in BotAsks QuesSeq# 8 QuesId# 5 Title: 'Medications' CPD: 184)

# FLAG: response_content_list_choice_mode just set to MultipleChoice

# FLAG: response_content_type_abbrev_list: []


# RESPONSE_SECTION 1 is a MultiChoice Question but THERE ARE NO CHOICES!!!

# BotSubQuestion# 1 of 3:
# 			AnswerFormat: MultipleChoice
# 			ResponseHeader: 'Are you taking any medications?'
# 			Weirdly, this is a case when we have zero choices!!
			

			
# FLAG: response_content_list_choice_mode just set to MultipleChoice

# FLAG: response_content_type_abbrev_list: ['MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice']


# RESPONSE_SECTION 2 is a MultiChoice Question

# BotSubQuestion# 2 of 3:
# AnswerFormat: MultipleChoice
# ResponseHeader: 'Individual medicines'



# Bot MultiChoiceOption # 0: abiraterone
# Bot MultiChoiceOption # 1: azelastine nasal spray
# Bot MultiChoiceOption # 2: clonidine
# Bot MultiChoiceOption # 3: clozapine
# Bot MultiChoiceOption # 4: conivaptan
# Bot MultiChoiceOption # 5: dabrafenib
# Bot MultiChoiceOption # 6: doxorubicin
# Bot MultiChoiceOption # 7: doxylamine
# Bot MultiChoiceOption # 8: felbamate
# Bot MultiChoiceOption # 9: fluvoxamine
# Bot MultiChoiceOption # 10: fusidic acid
# Bot MultiChoiceOption # 11: idelalisib
# Bot MultiChoiceOption # 12: lamotrigine
# Bot MultiChoiceOption # 13: methadone
# Bot MultiChoiceOption # 14: methyldopa
# Bot MultiChoiceOption # 15: metoprolol
# Bot MultiChoiceOption # 16: mirabegron
# Bot MultiChoiceOption # 17: olanzapine
# Bot MultiChoiceOption # 18: orphenadrine
# Bot MultiChoiceOption # 19: paraldehyde
# Bot MultiChoiceOption # 20: potassium chloride
# Bot MultiChoiceOption # 21: rufinamide
# Bot MultiChoiceOption # 22: sodium oxybate
# Bot MultiChoiceOption # 23: thalidomide
# Bot MultiChoiceOption # 24: thioridazine
# Bot MultiChoiceOption # 25: topiramate


# FLAG: AUTO MODE: user_reply_txt is: 0


# User chose: 0
# Users choice represented as a finding to add to the finding list:
# {
#     "id": "64065",
#     "idForHumans": "Fnd-abiraterone-GenNo-64065-Cpd-184-RecNum-64065",
#     "state": "PRESENT"
# }
# FLAG: response_content_list_choice_mode just set to Mixed_TypeInAndMultipleChoice

# FLAG: response_content_type_abbrev_list: ['MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice', 'MultiChoice', 'TypeIn']

# We expected findings_to_add to be [].  This violates assumption at 2022-06-22T11:35:40PDT.
# Thus we may need to make different place about removing findings_to_add
# See also 2022-06-22T11:38:24PDT.  Also see 2022-06-22T11:39:15PDT where we do a similar redundant test
# Ref Anchor is 2022-06-23T14:02:03PDT
# > /Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Code/test_question_driver.py(1601)process_system_reply()
# -> handle_mixed_response_content_list(\
# (Pdb) 


# 308, PROBLEM
# BotAsks QuesSeq# 1 QuesId# 1 Title: 'Birth sex, date of birth' CPD: 308
# ResponseHeader: 'None
# TypeError: Cannot read property 'getResponses' of null

################################################################
# Triage Notes for BirthSexFirst_Height_Weight_AllZeroUnlessError_NeedingAttention
# [6, 7, 26, 28, 43, 62]

# 6, PROBLEM 
# "FullTopic": "High Blood Pressure Diagnosis"
# BotAsks QuesSeq# 3 QuesId# 10 Title: 'Blood pressure'
# Please provide an entry for SYSTOLIC BLOOD PRESSURE that is greater than the DIASTOLIC BLOOD PRESSURE.

################################################################
# Triage Notes for Consults_suffering_Consys_299

# TODO see 2022-06-29T17:54:59PDT in diary-TestCoupletPrograms.org (need to improve test_question_driver.py)

################################################################
# RUN THE REGRESSION TESTS

for cpd in DOB_First_Height_Weight_Then_All_Zero_Unless_Error_Yes_Working:
 	question_and_answer_loop(cpd,
 		log_basedir = "../RegressionTestLogs2/",
		patient_sim_script_fpath = "../PatientSimulatorScripts/dob_height_weight_then_all_zero_unless_error.json")


for cpd in RemainingConsultsAssumed_SexDOBHeightWeight_yes_okay:
 	question_and_answer_loop(cpd,
 		log_basedir = "../RegressionTestLogs2/",
		patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json")
	   
for cpd in BirthSexFirst_Height_Weight_AllZeroUnlessError_Okay:
 	question_and_answer_loop(cpd,
 		log_basedir = "../RegressionTestLogs2/",
		patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json")

for cpd in ChildrensConsults_not_suffering_Consys_322:
 	question_and_answer_loop(cpd,
 		log_basedir = "../RegressionTestLogs2/",
		patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error_for_children.json")


