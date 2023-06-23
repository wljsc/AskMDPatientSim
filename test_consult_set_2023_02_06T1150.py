# test_consult_set_2023_02_06T1150.py
# This is meant to be called by test_question_driver_scale_up.py

consult_set =\
	[
	
	# 2023-02-06T11:53:36PST this was copied-n-edit from FULL_LIST_OF_TEST_GROUPS_03 in test_question_driver_scale_up.py
	# Then I cut down to omly have 14, 321, 323, 331, 325 which get the {"error":"Collection contains no element matching the predicate."}

	{
	'my_run_name' : "Consults_suffering_Consys_299",
	'list_of_consults' : [14],
	'patient_ans_script_filename' : 'sex_dob_height_weight_then_random_unless_error.json'
	# see Triage Notes (in test_question_driver_experiments.py) for Consults_suffering_Consys_299
	# 2022-12-19T10:39:34PST I see that Consults_suffering_Consys_299 is resolved.  But
	# 62 is still failing, now due to https://arnoldmedia.jira.com/browse/CI-3784.  
	},
	{
	'my_run_name' : "ChildrensConsults_not_suffering_Consys_322",
	#'list_of_consults' : [311, 315, 318, 320, 321, 323, 324, 325, 326, 327, 329, 330, 331],
	'list_of_consults' : [321, 323, 325, 331],	
	'patient_ans_script_filename' : 'sex_dob_height_weight_then_random_unless_error_for_children.json'
	}
	
	]
