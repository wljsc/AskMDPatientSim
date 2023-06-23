# test_question_driver_experimentsq.py
################################################################
# PURPOSE (start of section)

# The purpose of this file (test_question_driver_experiments.py) is to
# be a story like rendering of what has been tried and what are the
# results.

# It is NOT for development of functions.  It is for different calls
# probably only to just one function, i.e. question_and_answer_loop.

# For the dev of fns see test_question_driver.py

# test_question_driver_history_or_dev_test_runs.py is probably not of
# interest to anyone.  Only if you want to see some of the fn's called
# while the system was being developed.  This might be helfpul to
# discover various 'recipes'

# PURPOSE (end of section)
################################################################
# HISTORY (start of section)
# (newest stuff on top)

# 2022-10-09T13:50:01PDT saving some more historical versions as I return to working on this

# (env) william.jarrold@bactespc6217 Code % mv test_question_driver_experiments.py~ test_question_driver_experiments.2022-09-16T0934.py
# mv test_question_driver_experiments.py~ test_question_driver_experiments.2022-09-16T0934.py
# test_question_driver_experiments.py~ -> test_question_driver_experiments.2022-09-16T0934.py
# (env) william.jarrold@bactespc6217 Code % mv test_question_driver_experiments.py test_question_driver_experiments.2022-09-23T0914.py
# mv test_question_driver_experiments.py test_question_driver_experiments.2022-09-23T0914.py
# test_question_driver_experiments.py -> test_question_driver_experiments.2022-09-23T0914.py
# (env) william.jarrold@bactespc6217 Code % 

# 2022-09-16T09:36:15PDT creaetd this (History) section.

################
# 2022-07-02T1827 test_question_driver_experiments.2022-07-02T1827.py

# 2022-09-16T09:43:47PDT like the entry below I saved this version long after it existed, see the unix
# commands for what I mean...

# (env) william.jarrold@bactespc6217 Code % ll test*que*exp*
# ll test*que*exp*
# -rw-r--r--  1 william.jarrold  staff   8342 Jun 24 15:25 test_question_driver_experiments.py~
# -rw-r--r--  1 william.jarrold  staff  19826 Jul  2 18:27 test_question_driver_experiments.py
# 
# mv test_question_driver_experiments.py test_question_driver_experiments.2022-07-02T1827.py

# 2022-07-02T1827 test_question_driver_experiments.2022-07-02T1827b.py
# 2022-07-02T1827 test_question_driver_experiments.2022-07-02T1827.py

################
# 2022-06-24T1525 test_question_driver_experiments.2022-06-24T1525.py

# As of 2022-09-16T09:37:13PDT I dunno what is the state of this
# version.  I just saved it with a timestamp version (rather than s ~
# version) so that I can track history.

# here are the releavnt unix commands that I used...

# (env) william.jarrold@bactespc6217 Code % ll test*que*exp*
# ll test*que*exp*
# -rw-r--r--  1 william.jarrold  staff   8342 Jun 24 15:25 test_question_driver_experiments.py~
# -rw-r--r--  1 william.jarrold  staff  19826 Jul  2 18:27 test_question_driver_experiments.py
#
# mv test_question_driver_experiments.py~ test_question_driver_experiments.v01.py
# mv test_question_driver_experiments.py test_question_driver_experiments.2022-07-02T1827.py
# oops wrong month!!!
# mv test_question_driver_experiments.2022-07-24T1525.py test_question_driver_experiments.2022-06-24T1525.py

# HISTORY (end of section)
################################################################
# IMPORTS (start of section)

from test_question_driver import question_and_answer_loop

# IMPORTS (end of section)
################################################################
# ACTUAL EXPERIMENTS (put newest on bottom)

#question_and_answer_loop(19, log_basedir = "../TstCoupProgLogs/")

#question_and_answer_loop(19, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "../TstCoupProgLogs/Consult.2022-06-22T1727-Cpd-19/recording_of_user_replies_for_sim_script.json")
# The below only takes us in automode to the QuesSeq# 23 Title: 'Other medication information'
# But the below should take us "all the way"
#question_and_answer_loop(19, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "../TstCoupProgLogs/Consult.2022-06-23T1406-Cpd-19/recording_of_user_replies_for_sim_script.json")
# 2022-06-23T23:41:18PDT starting try first_try_auto_mode_policy_always_zero.json again.
# question_and_answer_loop(14, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "../PatientSimulatorScripts/first_try_auto_mode_policy_always_zero.json")
# question_and_answer_loop(26, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "../TstCoupProgLogs/Consult.2022-06-23T1406-Cpd-19/recording_of_user_replies_for_sim_script.json")
#question_and_answer_loop(19, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "../PatientSimulatorScripts/dob_height_weight_then_all_zero.json")
# GOOD NEWS - the above auto-mode conversation matches 
# what i had from the script based one, as shown by this diff:
# diff Consult.2022-06-23T2357-Cpd-19/conversation_text.org Consult.2022-06-23T2332-Cpd-19/conversation_text.org 
 # which returned zero.

# Try all the remaining ones that are dob first:

#for cpd in [70, 72, 76, 82, 85, 89, 131, 146, 188, 189]:
#	question_and_answer_loop(cpd, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "../PatientSimulatorScripts/dob_height_weight_then_all_zero.json")

# question_and_answer_loop(76, log_basedir = "../TstCoupProgLogs/")
# question_and_answer_loop(76, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "../PatientSimulatorScripts/dob_height_weight_then_all_zero_unless_error.json")
# TODO(2022-06-24T13:55:55PDT, ) i hit 0 to go to the next but then i get this:
#     "error": "400 BAD_REQUEST \"Failed to read HTTP message\"; nested exception is org.springframework.core.codec.DecodingException: JSON decoding error: Cannot deserialize value of type `int` from String \"There is no next Question Id bc we've already skip / advanced to the next question!!!\": not a valid `int` value; nested exception is com.fasterxml.jackson.databind.exc.InvalidFormatException: Cannot deserialize value of type `int` from String \"There is no next Question Id bc we've already skip / advanced to the next question!!!\": not a valid `int` value\n at [Source: (io.netty.buffer.ByteBufInputStream); line: 1, column: 2114] (through reference chain: com.sharecare.consultation.route.request.SessionRequest[\"questionId\"])"


# 2022-06-24T07:56:34PDT MILESTONE: reported https://arnoldmedia.jira.com/browse/CONSYS-319 about 76, Menopause
# also we implemented "AnswerZero-UnlessBotError" so let's go back to 70 and 72 and see if there are other error outs

#for cpd in [70, 72]:
#	question_and_answer_loop(cpd, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "../PatientSimulatorScripts/dob_height_weight_then_all_zero_unless_error.json")# 2022-06-24T13:16:17PDT
# getting UnboundLocalError: local variable 'user_reply_txt' referenced before assignment
# when calling the above.
# But now 2022-06-24T13:57:56PDT since, Fixed 2022-06-24T13:51:24PDT, we are now finding that this works.
#
# So, i was trying...
#for cpd in [70, 72, 76, 82, 85, 89, 131, 146, 188, 189]:
#	question_and_answer_loop(cpd, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "../PatientSimulatorScripts/dob_height_weight_then_all_zero.json")
#
# I just showed I can do 70 and 72, thus...

# CPD 70 is ok
#
# we know from 2022-06-24T13:55:55PDT that 76 has issues.
# what about the rest, i.e. these [82, 85, 89, 131, 146, 188, 189]:
#
# 2022-06-24T13:59:38PDT lets try it!!


#for cpd in [82, 85, 89, 131, 146, 188, 189]:
#	question_and_answer_loop(cpd, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "../PatientSimulatorScripts/dob_height_weight_then_all_zero.json")
# 2022-06-24T14:05:31PDT inifite loop.  Ooops!!!

#for cpd in [82, 85, 89, 131, 146, 188, 189]:
#	question_and_answer_loop(cpd, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "../PatientSimulatorScripts/dob_height_weight_then_all_zero_unless_error.json")

# 2022-06-24T14:07:23PDT getting
# TypeError: Cannot read property 'length' of undefined (this is the same error as in https://arnoldmedia.jira.com/browse/CONSYS-319)
#
# In 82 in response to :
#
# BotAsks QuesSeq# 3 QuesId# 1 Title: 'Bladder emptiness after urinating'
# ResponseHeader: 'Over the past month, how often have you had a sensation of not emptying your bladder completely after you finished urinating?'
#
# Bot MultiChoiceOption # 0: not at all

# thus
# CPD 82 needs attention from Bill

# for cpd in [85, 89, 131, 146, 188, 189]:
# 	question_and_answer_loop(cpd, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "../PatientSimulatorScripts/dob_height_weight_then_all_zero_unless_error.json")

#question_and_answer_loop(19, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "../PatientSimulatorScripts/dob_height_weight_then_all_zero_unless_error.json")
# 2022-06-24T13:51:24PDT this worked after atetpgn to fixing the UnboundLocalError: local variable 'user_reply_txt' referenced before assignment

################################################################
# SO, SUMMING UP THE ABOVE,

# All These Should Work
#for cpd in [70, 72, 76, 82, 85, 89, 131, 146, 188, 189]:
# EXCEPT
# 76 and 82

# Indeed they all worked!! See 2022-06-24T16:32:36PDT in diary-TestCoupletPrograms.org
# for cpd in [70, 72, 85, 89, 131, 146, 188, 189]:
# 	question_and_answer_loop(\
# 		cpd,
# 		log_basedir = "../TstCoupProgLogs/",
# 		patient_sim_script_fpath = "../PatientSimulatorScripts/dob_height_weight_then_all_zero_unless_error.json")

# thus

# CPD 85 is okay

# CPD 89 is okay

# CPD 13 is okay

# CPD 146 is okay

# CPD 188 is okay

# CPD 189 is okay


# 2022-06-24T16:35:58PDT calling enought done for Consults Such that first question is date of birth 
################################################################
# let's try the firt q male vs female

#question_and_answer_loop(4, log_basedir = "../TstCoupProgLogs/")
#question_and_answer_loop(4, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json")
# the above worked!!!
#question_and_answer_loop(70, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json")

#for cpd in [3, 6, 7, 8, 9, 11, 14, 15, 16, 17, 20, 24, 26, 27, 28, 29, 32, 40, 43, 47, 49, 55, 57, 59, 62, 66]:
#	question_and_answer_loop(cpd, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json")

# CPD 3 is okay

# CPD 6 needs better script
# QuesSeq# 4 QuesID# NoID-BcBotError ResponseHeader: BotError
#    "error": "Please provide an entry for SYSTOLIC BLOOD PRESSURE that is greater than the DIASTOLIC BLOOD PRESSURE.",

# CPD 7 needs better script
#Bot Response is QuesSeq# 5 QuesID# NoID-BcBotError (ConsultID 7)
#    "error": "Please provide an entry for SYSTOLIC BLOOD PRESSURE that is greater than the DIASTOLIC BLOOD PRESSURE.",

# CPD 8 is ok Consult.2022-06-24T1700-Cpd-8/

# CPD 9 is ok Consult.2022-06-24T1700-Cpd-9/

# CPD 11 is ok Consult.2022-06-24T1701-Cpd-11/

# for cpd in [8, 9, 11, 14, 15, 16, 17, 20, 24, 26, 27, 28, 29, 32, 40, 43, 47, 49, 55, 57, 59, 62, 66]:
# 	question_and_answer_loop(cpd, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json")

# CPD 14 is okay

# CDP 15 is okay

# CPD 16 is okay

# CPD 17 is okay

# CPD 20 is okay

# CPD 24 is okay

# So #26 is a DOB first question
# BotAsks QuesSeq# 1 QuesId# 25 Title: 'Date of birth'
# RESPONSE_SECTION 1 is a Type-In Question

# FLAG: AUTO MODE: user_reply_txt is: 0

# ################################################################
# Dag Nabit! We are getting an error.  Here it is:

# Text '0' could not be parsed, unparsed text found at index 0

# QuesSeq# 2 QuesID# NoID-BcBotError ResponseHeader: BotError
# ################
# Bot Response is QuesSeq# 2 QuesID# NoID-BcBotError (ConsultID 26)
# Bot JSON Response To Users Post (start of section)


# 2022-06-24T18:05:10PDT lets pick up where we left off:

# for cpd in [27, 28, 29, 32, 40, 43, 47, 49, 55, 57, 59, 62, 66]:
#  	question_and_answer_loop(cpd, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json")

# CPD 27 is okay

# CPD 28 needs attention from Bill

# ################
# Bot Response is QuesSeq# 3 QuesID# 15 (ConsultID 28)
# Bot JSON Response To Users Post (start of section)

# ################################################################
# BotAsks QuesSeq# 4 QuesId# 20 Title: 'Cholesterol and triglyceride levels'
# FLAG: response_content_list_choice_mode just set to TypeIn

# FLAG: response_content_type_abbrev_list: ['TypeIn', 'TypeIn', 'TypeIn', 'TypeIn']


# RESPONSE_SECTION 1 is a Type-In Question

# BotSubQuestion# 1 of 1:
# AnswerFormat: TypeIn
# ResponseHeader: 'Enter your most recent cholesterol and triglyceride levels. Leave blank if you are unsure.
# WHAT!!! At 2022-05-31T14:59:42PDT Bill was moderately certain that any type in question would only have exactly one element in response_content_list but his lenght is: 4
# Yes at 2022-05-31T16:50:36PDT he believes that this is not = 1 only if we have a multiple choice question bc each response_content is a possible multi-choice answer
# > /Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Code/test_question_driver.py(1316)process_system_reply()
# -> response_name = response_content['name']
# (Pdb)

# for cpd in [29, 32, 40, 43, 47, 49, 55, 57, 59, 62, 66]:
#   	question_and_answer_loop(cpd, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json")

# CPD 29 is okay

# CPD 32 is okay

# CPD 40 is okay

# CPD 43 needs attention from Bill (looks like another '"TypeError: Cannot read property 'length' of undefined")

# Bot Response is QuesSeq# 2 QuesID# 3 (ConsultID 43)
# BotAsks QuesSeq# 3 QuesId# 12 Title: 'COPD symptom severity'
# FLAG: response_content_list_choice_mode just set to MultipleChoice

# FLAG: response_content_type_abbrev_list: ['MultiChoice', 'MultiChoice']

# RESPONSE_SECTION 1 is a MultiChoice Question

# BotSubQuestion# 1 of 1:
# AnswerFormat: MultipleChoice
# ResponseHeader: 'Which of these describes your COPD symptoms?'





# Bot MultiChoiceOption # 0: few, mild day-to-day symptoms
# Bot MultiChoiceOption # 1: many or severe day-to-day symptoms


# FLAG: AUTO MODE: user_reply_txt is: 0


# User chose: 0


# ################################################################
# QuesSeq# 4 QuesID# NoID-BcBotError ResponseHeader: BotError
# ################
# Bot Response is QuesSeq# 4 QuesID# NoID-BcBotError (ConsultID 43)
# Bot JSON Response To Users Post (start of section)

# {
#     "error": "TypeError: Cannot read property 'length' of undefined"
# }


# okay lets continue on from 43

# interesting
# Type In Your Choice Here: 3
# 3
# FLAG: AUTO MODE: user_reply_txt is: 3
# UserReply to BotError for QuesSeq# 4 QuesID# 12 is: 'quit'


#for cpd in [47, 49, 55, 57, 59, 62, 66]:
#   	question_and_answer_loop(cpd, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json")

# CPD 47 is okay

# CPD 49 is okay

# CPD 55 is okay

# CPD 59 is okay

# CPD 62 needs attention from Bill

# BotAsks QuesSeq# 3 QuesId# 1 Title: 'Type of diabetes'
# Bot Response is QuesSeq# 3 QuesID# 1 (ConsultID 62)
# ################################################################
# BotAsks QuesSeq# 4 QuesId# 66 Title: 'Blood glucose'
# FLAG: response_content_list_choice_mode just set to TypeIn

# FLAG: response_content_type_abbrev_list: ['TypeIn', 'TypeIn']


# RESPONSE_SECTION 1 is a Type-In Question

# BotSubQuestion# 1 of 1:
# AnswerFormat: TypeIn
# ResponseHeader: 'What are your blood glucose measurements?
# WHAT!!! At 2022-05-31T14:59:42PDT Bill was moderately certain that any type in question would only have exactly one element in response_content_list but this length is: 2
# Yes at 2022-05-31T16:50:36PDT he believes that this is not = 1 only if we have a multiple choice question bc each response_content is a possible multi-choice answer
# > /Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Code/test_question_driver.py(1316)process_system_reply()
# -> response_name = response_content['name']
# (Pdb)

# for cpd in [66]:
#    	question_and_answer_loop(cpd, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json")

# CPD 66 is okay

RemainingConsultsAssumed_SexDOBHeightWeight = \
[
#73, 
#77, 
#87, 
#89,
#98,
# 101,
# 102,
# 108,
# 110,
# 115,
# 116,
# 117,
# 119,
# 127,
# 134,
# 140,
# 142,
# 144,
# 145,
# 147,
# 148,
# 152,
# 155,
# 156,
# 157,
# 158,
# 159,
# 160,
# 161,
# 163,
# 165,
# 166,
# 168,
# 176,
# 178,
# 179,
# 181,
# 182,
# 183,
# 184
# 187,
# 308,
# 311,
# 315,
# 318,
# 320,
# 321,
# 322, nYou have entered a date of birth outside the allowed range.
# 323, ditto 
# 324, ditto
# 325, ditto 
# 326, ditto 
# 327, ditto
# 328, ditto 
# 329, ditto 
# 330, ditto 
# 331, ditto 
# 610
]

#for cpd in RemainingConsultsAssumed_SexDOBHeightWeight:
#    	question_and_answer_loop(cpd, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json")

#question_and_answer_loop(320, log_basedir = "../TstCoupProgLogs/")

################
# 2022-06-29T17:40:12PDT ChildrensConsults can be eliminagted.
# It is now covered by
#	ChildrensConsults_yes_suffering_Consys_322
#	ChildrensConsults_not_suffering_Consys_322
#
#ChildrensConsults = [
#320,
# 321, ok
# 322, problem 
#323, ok
#324, ok
#325, ok
#326,ok
#327, ok
#328,problem 
# 329, #ok
# 330, # ok
#331] #ok

#question_and_answer_loop(320, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error_for_children.json")
# the above worked

# for cpd in ChildrensConsults:
# 	question_and_answer_loop(cpd,
# 		log_basedir = "../TstCoupProgLogs/",
# 		patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error_for_children.json")
# the above was done as of 2022-06-28.  IIR correctly (at 2022-06-29T09:33:38PDT) there are mostly ok's and then two problems and these have
# been JIRAd'

################################################################
# 2022-06-29

# 2022-06-29T09:34:06PDT what status on https://arnoldmedia.jira.com/browse/CONSYS-310
# getting weirndess with json in the inpput to postman so just run the simulator

#question_and_answer_loop(14, log_basedir = "../TstCoupProgLogs/")

################################################################
# Moving Towards Regression Tests

################################

DOB_First_Height_Weight_Then_All_Zero_Unless_Error_Yes_Working = \
[70, 72, 85, 89, 131, 146, 188, 189]
# dob_height_weight_then_all_zero_unless_error.json

# Anchor=2022-10-09T13:54:36PDT using the above, at down below

# NeedWork: 2
DOB_First_Height_Weight_Then_All_Zero_Unless_Error_Not_Working = \
[76, 82]
# dob_height_weight_then_all_zero_unless_error.json
# TODO need triage notes

################################

RemainingConsultsAssumed_SexDOBHeightWeight_yes_okay = \
[
73, 77, 98, 101, 102, 108, 110, 115, 116, 119, 127, 134,
142, 144, 145, 147, 148, 152, 155, 156, 157, 158, 159, 160,
161, 163, 165, 166, 168, 176, 178, 179, 181, 182, 183, 184,
187, 610
]
# sex_dob_height_weight_then_all_zero_unless_error.json")

# NeedWork: 5
RemainingConsultsAssumed_SexDOBHeightWeight_not_okay = \
[
87, 89, 117, 140, 308
]
# sex_dob_height_weight_then_all_zero_unless_error.json
# see Triage Notes (below) for RemainingConsultsAssumed_SexDOBHeightWeight_not_okay

################################

BirthSexFirst_Height_Weight_AllZeroUnlessError_Okay = \
[3, 6, 7, 8, 9, 11, 14, 15, 16, 17, 20, 24, 27, 29, 32,
40, 47, 49, 55, 57, 59, 66]
# SCRIPT: sex_dob_height_weight_then_all_zero_unless_error.json

# NeedWork: 6
BirthSexFirst_Height_Weight_AllZeroUnlessError_NeedingAttention = \
[6, 7, 26, 28, 43, 62]
# SCRIPT: sex_dob_height_weight_then_all_zero_unless_error.json
# TODO need triage notes

################################

# len is 13 (2022-06-29)
ChildrensConsults_not_suffering_Consys_322 = \
[311, 315, 318, 320, 321, 323, 324, 325, 326, 327, 329, 330, 331]
# SCRIPT: sex_dob_height_weight_then_all_zero_unless_error_for_children.json

# NeedWork: 2
ChildrensConsults_yes_suffering_Consys_322 = \
[322, 328]
# SCRIPT: sex_dob_height_weight_then_all_zero_unless_error_for_children.json

################################
# NeedWork: 2

Consults_suffering_Consys_299 = [14, 62]
# SCRIPT: sex_dob_height_weight_then_all_zero_unless_error.json")
# see Triage Notes (below) for Consults_suffering_Consys_299

################################################################
# Triage Notes for RemainingConsultsAssumed_SexDOBHeightWeight_not_okay
################################################################
# 87,  PROBLEM
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

# 308, PROBLEM
# BotAsks QuesSeq# 1 QuesId# 1 Title: 'Birth sex, date of birth' CPD: 308
# ResponseHeader: 'None
# TypeError: Cannot read property 'getResponses' of null

################################################################
# Triage Notes for Consults_suffering_Consys_299

# TODO see 2022-06-29T17:54:59PDT in diary-TestCoupletPrograms.org (need to improve test_question_driver.py)

# Update weeks laste, at 2022-10-09T13:50:56PDT, it looks like some
# assumption my code makes about some data strcutre is being violated.
# Thus, the TODO is to adapt my code to this new assumption.  I think
# it has to do with blood pressure questions.


################################################################
# 2022-09-16T09:58:43PDT firing up after long hiatus

# question_and_answer_loop(19, log_basedir = "../TstCoupProgLogs/")

################################################################
# 2022-09-23T10:14:40MDT trying to dust off auto quesiton driver

#question_and_answer_loop(320, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error_for_children.json")

################################################################
# 2022-10-09T13:56:22PDT Trying to run an inchoate 'regression test'
 
# see Anchor=2022-10-09T13:54:36PDT above

for consult_number in DOB_First_Height_Weight_Then_All_Zero_Unless_Error_Yes_Working:
    question_and_answer_loop(consult_number,
	log_basedir = "../Logs-Generic/GenDataForTestGuidOpt/2022-10-09T1403.FirstHeightWeight-ThenAllZero/",
	patient_sim_script_fpath = "../PatientSimulatorScripts/dob_height_weight_then_all_zero_unless_error.json")

