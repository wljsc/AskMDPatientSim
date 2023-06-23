# test_question_driver_scale_up_full_battery_2023_02_15a.py

################################################################
# HISTORY:

# this is a copy-n-edit of test_question_driver_scale_up_full_battery_2023_02_06a.py

################################################################

# test_question_driver_scale_up_full_battery_2023-02-06a.py
full_battery =\
	[
	
	# this should the same as FULL_LIST_OF_TEST_GROUPS_02
	# except each auto-mode script "all_zero" is replaced with
	# with 7"random"

	# 2023-02-15T11:51:15PST I movies this to the very top of the list
	# bc it had an error and I want to make it run early to quickly
	# verify the syntax issue was fixed.
	#
	# 2023-01-22T22:38:37PST I moved this (immediately below) to
	# be further up bc it had an error on the last
	# (2023-01-17T101224) run.  The error was 'list index out of
	# range' with 308
	{
	'my_run_name' : "JIRA-CI-3784_sex_dob_h_w",
	'list_of_consults' : [308],
	# 'patient_ans_script_filename' : 'sex_dob_height_weight_then_random_unless_error.json',
	#
	# 2023-02-15T10:56:13PST because of this error (which has been happening a lot lately but no time to fix)...
	#
	# Logs-Generic/GenDataForTestGuidOpt-FullScale/2023-02-15T004548.run_class_13_first_with_all_consults_and_do_guidance_options/2023-02-15T004606.JIRA-CI-3784_sex_dob_h_w/Consult.2023-02-15T004606-Cpd-308/conversation_text.org:BotError JSON is: You have entered a date of birth outside the allowed range.
	#
	# replacing the above script with the below (which should have an in range birth date)
	'patient_ans_script_filename' : 'sex_dob_height_weight_then_random_unless_error_for_children.json',

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

	# 2023-02-07T10:40:16PST adding JustCpd62-AIC
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
	# 2023-02-07T10:41:54PST adding JustCpd7-BloodPressure
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