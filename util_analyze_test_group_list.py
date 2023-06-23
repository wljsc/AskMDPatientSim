################################################################
# PURPOSE:

# given a test group list, output
# the list of unique scripts it calls.
# the list of consults mentioned
# the list of consults skipped
# maybe, for each consult, it's script.

def ret_list_of_scripts(test_group_list):
	uniq_set_of_scripts = set()
	for item in test_group_list:
		script = item['patient_ans_script_filename']
		uniq_set_of_scripts.add(script)
	return(list(uniq_set_of_scripts))

# from test_question_driver_scale_up import FULL_LIST_OF_TEST_GROUPS_02
# ret_list_of_scripts(FULL_LIST_OF_TEST_GROUPS_02)
# result = ret_list_of_scripts(FULL_LIST_OF_TEST_GROUPS_02)
# for r in result: print(r)

# from test_question_driver_scale_up import FULL_LIST_OF_TEST_GROUPS_03
# ret_list_of_scripts(FULL_LIST_OF_TEST_GROUPS_03)
# result = ret_list_of_scripts(FULL_LIST_OF_TEST_GROUPS_03)
# for r in result: print(r)
