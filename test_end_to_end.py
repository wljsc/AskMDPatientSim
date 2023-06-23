################################################################
# PURPOSE

# Now that we are testing the test questio drive and the guidance
# options, it is time to try true end to end testing.

# Part 1: auto-mode response script --> test consultation service    --> finding list
# Part 2: finding list		    --> test guidance option service --> guidance options

################################################################
# IMPORTS

import test_question_driver as tqd


tdq.question_and_answer_loop(
			start_conversation_with = 26,
			log_basedir = TODO 
			patient_sim_script_fpath = 'dob_height_weight_then_random_unless_error.json',
			record_user_replies_for_reply_filename = TODO ,
			timestamp_in_log_dir = True,
			if_reply_script_UnlessError_means_LogAndContinue = True)