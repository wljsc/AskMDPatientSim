################################################################
# PURPOSE:

# This was for doing one off testing.  Typically one CPD at a time.
# Newer runs go at the bottom.

# Being able to see test history can be useful in copy-n-paste or just
# for knowledge what has recdntly been done.

# This can also be useful for learning various recipes, patterns in
# calling the patient simulator.

################################################################

from test_question_driver import question_and_answer_loop

#question_and_answer_loop(320, log_basedir = "../TstCoupProgLogs/")

# 2022-06-30T07:19:02PDT these all worked and are now in the regression suite ChildrensConsults_not_suffering_Consys_322
# for cpd in [311, 315, 318]:
#  	question_and_answer_loop(cpd,
#  		log_basedir = "../TstCoupProgLogs/",
#  		patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error_for_children.json")

#question_and_answer_loop(87,
#question_and_answer_loop(72,
#question_and_answer_loop(3,
#	log_basedir = "../TstCoupProgLogs/")

# question_and_answer_loop(62,
# 	log_basedir = "../TstCoupProgLogs/",
# 	patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json")

# question_and_answer_loop(62,
#  	log_basedir = "../TstCoupProgLogs/")

# question_and_answer_loop(62,
#   	log_basedir = "../TstCoupProgLogs/",
#   	patient_sim_script_fpath = "../PatientSimulatorScripts/cpd-62-diabetes.2022-07-02a.json")

# 2022-07-02T15:28:29PDT trying to debug the difference between
# diff -r RegressionTestLogs2/Consult.2022-06-30T1026-Cpd-73/Q031-usr-reply-Id005.json RegressionTestLogs3/Consult.2022-07-02T1445-Cpd-73/Q031-usr-reply-Id005.json
# question_and_answer_loop(73,
#   	log_basedir = "../TstCoupProgLogs/",
#   	patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json")

# 2022-07-02T17:52:48PDT 72 checks out
# question_and_answer_loop(72,
#   	log_basedir = "../TstCoupProgLogs/",
#    	patient_sim_script_fpath = "../PatientSimulatorScripts/dob_height_weight_then_all_zero_unless_error.json")
# cd /Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/TstCoupProgLogs
#diff -r ../RegressionTestLogs2/Consult.2022-06-30T1022-Cpd-72  Consult.2022-07-02T1744-Cpd-72/


# question_and_answer_loop(117,
#    	log_basedir = "../TstCoupProgLogs/",
#    	patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json")
# 2022-07-06T13:38:34PDT resllving CONSYS-329

# question_and_answer_loop(140,
#   	log_basedir = "../TstCoupProgLogs/",
#   	patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json")

#question_and_answer_loop(140,
# question_and_answer_loop(147,
#  	log_basedir = "../TstCoupProgLogs/",
#  	patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json")


# Hooray, 184 works!!
# question_and_answer_loop(184,
#  	log_basedir = "../TstCoupProgLogs/",
#  	patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json")

# question_and_answer_loop(308,
#   	log_basedir = "../TstCoupProgLogs/",
# 	patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json")
# JIRA Consys_322 

# BirthSexFirst_Height_Weight_AllZeroUnlessError_NeedingAttention
# TODO 7 sex_dob_height_weight_then_all_zero_unless_error.json

# Blood Pressure
# question_and_answer_loop(7,
#   	log_basedir = "../TstCoupProgLogs/")
#  	patient_sim_script_fpath = "../PatientSimulatorScripts/cpd-7-sex-dob-hgt-wgt-blood-pressure.json")

# question_and_answer_loop(76,
#   	log_basedir = "../TstCoupProgLogs/",
#  	patient_sim_script_fpath = "../PatientSimulatorScripts/dob_height_weight_then_all_zero_unless_error.json")

# question_and_answer_loop(82,
#   	log_basedir = "../TstCoupProgLogs/",
#  	patient_sim_script_fpath = "../PatientSimulatorScripts/dob_height_weight_then_all_zero_unless_error.json")

# 2022-07-03T08:17:04PDT working on 87

# question_and_answer_loop(87,
#   	log_basedir = "../TstCoupProgLogs/",
#  	patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json")

# 2022-07-03T08:25:43PDT workingon 26 in BirthSexFirst_Height_Weight_AllZeroUnlessError_NeedingAttention

# question_and_answer_loop(26,
#   	log_basedir = "../TstCoupProgLogs/",
#  	patient_sim_script_fpath = "../PatientSimulatorScripts/dob_height_weight_then_all_zero_unless_error.json")
# yay, it works!!

# 2022-07-03T08:34:55PDT working on 28 in BirthSexFirst_Height_Weight_AllZeroUnlessError_NeedingAttention

# question_and_answer_loop(28,
#   	log_basedir = "../TstCoupProgLogs/",
#  	patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json")

# question_and_answer_loop(43,
#   	log_basedir = "../TstCoupProgLogs/",
#  	patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json")


# question_and_answer_loop(322,
#   	log_basedir = "../TstCoupProgLogs/",
#  	patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error_for_children.json")

# question_and_answer_loop(28,
#   	log_basedir = "../TstCoupProgLogs/")

# question_and_answer_loop(4,
#   	log_basedir = "../TstCoupProgLogs/")
# This worked fine, and response patterns seem to be of this type:
# sex_dob_height_weight_then_all_zero_unless_error.json


#question_and_answer_loop(19,
#  	log_basedir = "../TstCoupProgLogs/")
#This also worked fine, and response patterns seem to be of this type:
#dob_height_weight_then_all_zero_unless_error.json

# question_and_answer_loop(6,
#   	log_basedir = "../TstCoupProgLogs/",
#   	patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json"
# 	)

################################################################

# 2022-07-06T13:43:52PDT Testing the bunch of consults related to
# Cannot read property 'length' of undefined
# and then Please select one XXX response.

# e.g.
# Testing the bunch of consulgs related to Cannot read property 'length' of undefined
# and then Please select one MENOPAUSE RATING SCALE

# question_and_answer_loop(43,
#   	log_basedir = "../TstCoupProgLogs/",
#  	patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json")
# 2022-07-06T13:49:06PDT worked!!
# DONE RESOLVE CONSYS-332 ADD TO WORKINST LIST IN REGRESSION FILE

# CONSYS-319 CPD #76 errors out during hot flashes question: Cannot read property 'length' of undefined
# TO DO A NEW PROBLEM Please select one MENOPAUSE RATING SCALE response.
# 
# question_and_answer_loop(76,
#    	log_basedir = "../TstCoupProgLogs/",
#   	patient_sim_script_fpath = "../PatientSimulatorScripts/dob_height_weight_then_all_zero_unless_error.json")
# 2022-07-06T13:49:06PDT worked!!
# DONE RESOLVE CONSYS-332 ADD TO WORKINST LIST IN REGRESSION FILE

# question_and_answer_loop(82,
#   	log_basedir = "../TstCoupProgLogs/",
#   	patient_sim_script_fpath = "../PatientSimulatorScripts/dob_height_weight_then_all_zero_unless_error.json")
# Please select one BLADDER EMPTINESS AFTER URINATING response.
# 2022-07-06T13:49:06PDT worked!!
# DONE RESOLVE CONSYS-332 ADD TO WORKINST LIST IN REGRESSION FILE

# question_and_answer_loop(87,
#   	log_basedir = "../TstCoupProgLogs/",
#  	patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json")
# DONE RESOLVE CONSYS-332 ADD TO WORKINST LIST IN REGRESSION FILE

# question_and_answer_loop(148,
#   	log_basedir = "../TstCoupProgLogs/",
#  	patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json")
# DONER ESOLVE CONSYS-332 ADD TO WORKINST LIST IN REGRESSION FILE



# CONSYS-330 CPD # 140 Cannot read property 'length' of undefined (created 2022-07-02T20:26:56PDT)
# question_and_answer_loop(140,
#  	log_basedir = "../TstCoupProgLogs/",
#   	patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json")
# Please select one SEVERITY OF SYMPTOMS response.
# 2022-07-06T13:49:06PDT worked!!
# TODO RESOLVE CONSYS-330 ADD TO WORKINST LIST IN REGRESSION FILE



# question_and_answer_loop(77,
#   	log_basedir = "../TstCoupProgLogs/",
#    	patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json")

# question_and_answer_loop(77,
#   	log_basedir = "../TstCoupProgLogs/",
#    	patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json")
# Error:  Please provide a height between 1 foot and 8 feet.

# question_and_answer_loop(47,
#   	log_basedir = "../TstCoupProgLogs/",
#    	patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json")

# question_and_answer_loop(47,
#   	log_basedir = "../TstCoupProgLogs/",
#    	patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json")

# question_and_answer_loop(47,
#   	log_basedir = "../TstCoupProgLogs/",
#    	patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_random_unless_error.json")

#question_and_answer_loop(155, log_basedir = "../TstCoupProgLogs/")

