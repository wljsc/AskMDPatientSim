# test_question_driver_scale_up_small_set_for_smoke_tests_2023_02_12a.py
# based on test_question_driver_scale_up_full_battery_2023-02-06a.py
# and trim down
full_battery =\
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
	'list_of_consults' : [308],
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
	{
	'my_run_name' : "DOB_First_Height_Weight_Then_Random_Unless_Error_Yes_Working",	
	'list_of_consults' : 	[26, 19, 70],
	# 2022-12-19T10:30:30PST moved 26 from BirthSexFirst_Height_Weight_AllZeroUnlessError_NeedingAttention to DOB_First_Height_Weight_Then_Random_Unless_Error_Yes_Working
	# 2022-12-19T10:56:25PST not sex first, dob first, moved 189 from RemainingConsultsAssumed_SexDOBHeightWeight_yes_okay to DOB_First_Height_Weight_Then_Random_Unless_Error_Yes_Working
	'patient_ans_script_filename' : 'dob_height_weight_then_random_unless_error.json'
	},

	]

small_battery =\
	[
	
	{
	'my_run_name' : "JIRA-CONSYS_334_blood_pressure",
	'list_of_consults' : [6],
	'patient_ans_script_filename' : 'sex_dob_height_weight_blood_pressure_then_random_unless_error.json',
	},
	{
	'my_run_name' : "JIRA-CI-3784_sex_dob_h_w",
	'list_of_consults' : [308],
	'patient_ans_script_filename' : 'sex_dob_height_weight_then_random_unless_error.json',
	},
	{
	'my_run_name' : "DOB_First_Height_Weight_Then_Random_Unless_Error_Yes_Working",	
	'list_of_consults' : 	[26],
	'patient_ans_script_filename' : 'dob_height_weight_then_random_unless_error.json'
	},

	]