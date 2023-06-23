# test_question_driver_experiments.py
################################################################
# PURPOSE

# The purpose of this file is to be a story like rendering of what has been tried and what are the results.

################################################################
# ACTUAL EXPERIMENTS (put newest on top)


#run_patient_sim_script_over_consults(DIR_OF_CPD_FILES, patient_sim_script_fpath = "../PatientSimulatorScripts/test_record_14.01.json")

# run_patient_sim_script_over_consults(DIR_OF_CPD_FILES, log_basedir = "../TstCoupProgLogs/CONSYS-299", patient_sim_script_fpath = "../PatientSimulatorScripts/consys-299.json")

# Try 19 bc it is one of several that does not have gender as first question.

#question_and_answer_loop(19, log_basedir = "../TstCoupProgLogs/", record_user_replies_for_reply_filename = "../PatientSimulatorScripts/try-dob-is-first-question.json")


# Consults_whose_1st_Qstn_Is_DateOfBirth = {'ConsultDescriptorType' : 'PlainList', 'ListOfCpdNumbers' : [19, 26, 70, 72, 76, 82, 85, 89, 131, 146, 188, 189]}

# run_patient_sim_script_over_consults(\
# 	consults_descriptor = Consults_whose_1st_Qstn_Is_DateOfBirth, 
# 	patient_sim_script_fpath = "../PatientSimulatorScripts/try-dob-is-first-question.json", 
# 	log_basedir = "../TstCoupProgLogs/ConsultsWhose1stQstnIsDateOfBirth/")

#question_and_answer_loop(155, log_basedir = "../TstCoupProgLogs/")

#question_and_answer_loop(14, log_basedir = "../TstCoupProgLogs/", record_user_replies_for_reply_filename = "../PatientSimulatorScripts/will-it-mistakenly-skip-pregnancy-on-14.json")

#question_and_answer_loop(14, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "../PatientSimulatorScripts/will-it-mistakenly-skip-pregnancy-on-14-if-female.json")
# ...2022-06-14T15:39:43EDT transformed the above to this..
#question_and_answer_loop(14, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "../PatientSimulatorScripts/CONSYS-309-does-it-skip-pregnancy-question-if-female.json")



#question_and_answer_loop(19, log_basedir = "../TstCoupProgLogs/", record_user_replies_for_reply_filename = "../PatientSimulatorScripts/auto_mode_for_consults_that_have_dob_as_first_question.json")

#question_and_answer_loop(14, log_basedir = "../TstCoupProgLogs/")
#question_and_answer_loop(62, log_basedir = "../TstCoupProgLogs/")

# The last time we ran this, as of 2022-06-22T12:27:38PDT whence MAJOR
# dev on @func handle_mixed_response_content_list happened might be
# just about code complete, the above run of #62 was the one we were
# doing.  I..e we were doing that before all this major refactoring
# work.

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
# I just showed I can do 70 and 72,
# we know from 2022-06-24T13:55:55PDT that 76 has issues.
# what about the rest, i.e. these -82, 85, 89, 131, 146, 188, 189]:
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

for cpd in [85, 89, 131, 146, 188, 189]:
	question_and_answer_loop(cpd, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "../PatientSimulatorScripts/dob_height_weight_then_all_zero_unless_error.json")

#question_and_answer_loop(19, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "../PatientSimulatorScripts/dob_height_weight_then_all_zero_unless_error.json")
# 2022-06-24T13:51:24PDT this worked after atetpgn to fixing the UnboundLocalError: local variable 'user_reply_txt' referenced before assignment


#question_and_answer_loop(14, log_basedir = "../TstCoupProgLogs/")

#question_and_answer_loop(101, log_basedir = "../TstCoupProgLogs/")

#question_and_answer_loop(14, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "../PatientSimulatorScripts/first_try_auto_mode_policy_always_zero.json")


