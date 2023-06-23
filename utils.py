################################################################
# HISTORY OF THIS FILE (newest on top)

# 2023-01-10T06:59:15PST trying to resolve problem with ...
# if_reply_script_UnlessError_means_LogAndContinue
#
# as you can see in e.g.
# diary-TestCoupletPrograms.org 2023-01-10T06:39:56PST Any Errors During the Guidance Options Run?
# I am getting errors like this
#
# user_input_wrapper() got an unexpected keyword argument 'if_reply_script_UnlessError_means_LogAndContinue'
#
# I don't fully understand this but I THINK the only fix needed is
# to merely add
# if_reply_script_UnlessError_means_LogAndContinue
# as a keyword to @func user_input_wrapper.



# 2022-12-20T22:33:24PST abouto to intro a new policy.  A sibling of
# AnswerZero-UnlessBotError.  Call it
# AnswerZero-ButIfErrorLogAndContinue

# 2022-12-20T22:33:16PST created this HISTORY section



################################################################
# IMPORTS

import datetime as dt
import json
from tzlocal import get_localzone
import os
import random
import pdb

################################################################
# CONSTANTS

from constants import ASK_OPERATOR_HOW_TO_HANDLE_BOT_ERROR_STR
from constants import MultiChoiceResponseObject
from constants import TypeInResponseObject

# PARANOID_P = True
# 2022-06-14T16:26:56EDT only needs to be true if you are worried
# about filenames in logs having the correct padding for integers.
# Probably ignorable, so just set to False for safety
PARANOID_P = False

################################################################

#def now_yyyy_mm_ddThhmmss(utc_offset_p = False):
# 2023-02-05T08:41:12PST golly, dunno why this was default False!?!?
def now_yyyy_mm_ddThhmmss(utc_offset_p = True):
	"""return current time in a filename friendly format"""
	if utc_offset_p:
		local = get_localzone()
		return(dt.datetime.now().strftime("%Y-%m-%dT%H%M%S%Z"))
		# e.g. '2022-11-15T1950PST'
	else:
		return(dt.datetime.now().strftime("%Y-%m-%dT%H%M%S"))
		# e.g. '2022-11-15T195317'

####
# def pretty_fnd_id(finding_name, finding_entity_number, consult_id, rec_num):
# 	return(f"Fnd-{finding_name}-GenNo-{finding_entity_number}-Cpd-{consult_id}-RecNum-{rec_num}")
#
# 2022-09-17T13:46:42PDT replace the above with the below as part of Update2022-09-17
#

def pretty_fnd_id(finding_name, finding_entity_number, consult_id):
	return(f"Fnd-{finding_name}-GenNo-{finding_entity_number}-Cpd-{consult_id}")

#
####

def ppj(myjson, sort_keys = True, indent = 2):
	"""pretty print json object"""
	print(json.dumps(myjson, sort_keys = sort_keys, indent = indent))

def add_padding_to_int_str(integer_string, expected_max_digits, pad_char = "0"):

	integer_string = str(integer_string)
	str_len = len(integer_string)
	if str_len > expected_max_digits:
		if PARANOID_P:

			# This is merely here to help you know if you
			# need to incresae the padding for numbers
			# filenames that contain the json that encodes
			# the user's reply to the consultation service
			# or the bots question to the user.
			
			# Such padding merely makes file listings
			# prettier in the Log dir for a given
			# questionnaire run.

			# If this is annoying, just set PARANOID_P to
			# False.

			print("Warning from @func add_padding_to_int_str:")
			print("filenames won't be pretty because len integer_string > expected_max_digits!!")
			print("In this case, we are padding the following @param integer_string:")
			print("@param integer_string:", integer_string)
			print("@param expected_max_digits:", expected_max_digits)
			print("thus, you may want to increase expected_max_digits")
			pdb.set_trace()
	if str_len < expected_max_digits:
		pad_this_many_chars = expected_max_digits - str_len
		padding = pad_char*pad_this_many_chars
		res_str_padded_if_nec = padding + integer_string
	else:
		res_str_padded_if_nec = integer_string

	return(res_str_padded_if_nec)

################################################################

def auto_mode_reply_txt_for_rnd_ans_case_01(choices, asking_how_to_handle_bot_error_p):

	"""This is where we implement the following AutoMode response
	policy: RandomAnswerForMultiChoice-UnlessBotError"""

	if not(isinstance(choices, list)):
		print("ERROR: Weird, we are not expecting @param choices to not be a list.  Is there a lurking bug???")
	else:

	#
	# num_choices = len(response_content_list)
	#
	# ..used to be in 'Step 2: Solicit the User's Answer to the Multiple-Choice Question'
	# process_system_reply.
	#
	# Likewise, this...
	#
	# 	num_choices = len(multi_choice_options)
	#
	# ...used to be in solicit_user_ans_to_the_multiple_choice_question
	#
	# Both those forms of the same functionality like this...
	#
		num_choices = len(choices)

		if num_choices == 0:
			print("Weird, num_choices is 0.  What did we do in always chose 0 response mode?")
			pbd.set_trace()
			
		elif num_choices == 1:
			resp_mode = ret_likely_response_mode_for_response_content(choices[0]) # we are in auto_mode_reply_txt_for_rnd_ans_case_01
			if resp_mode == TypeInResponseObject:
				#user_reply_txt = "This is type-in text for the current AutoMode response policy: RandomAnswerForMultiChoice-UnlessBotError"
				user_reply_txt = "0"

				# 2022-07-07T12:44:00PDT Setting this
				# to 0 for now.  Else it will barf on
				# CPD 4:
				# BotAsks QuesSeq# 11 QuesId# 75 Title: 'Headache problem details' CPD: 4
				# ResponseHeader: 'Rate your headache pain on a scale from 1 to 10, where 10 is the worst pain you can imagine.

			elif resp_mode == MultiChoiceResponseObject:
				user_reply_txt = "0"
				
		else:
			response_mode_for_each_choice = [ret_likely_response_mode_for_response_content(c) for c in choices] # we are in auto_mode_reply_txt_for_rnd_ans_case_01
			multi_choice_p_for_each_choice = [m == MultiChoiceResponseObject for m in response_mode_for_each_choice]
			if all(multi_choice_p_for_each_choice):
				user_reply_txt = random.randint(0,num_choices - 1)
			else:
				print("ERROR: Not all of the choices are MultiChoiceResponseObject.  This is unexpected case while executing policy RandomAnswerForMultiChoice-UnlessBotError.  How did you get here?")
				pdb.set_trace()

	return(user_reply_txt)

################################################################

def user_input_wrapper(prompt_text, 
		user_reply_script_json = None, 
		record_user_replies_for_replay_filepath = None,
		asking_how_to_handle_bot_error_p = False,
		choices = None,
		error_msg = None,
		if_reply_script_UnlessError_means_LogAndContinue = False):

	"""

	@func user_input_wrapper is a wrapper around any time we want
	to ask the human operator AskMD Simulator a question.

	It can override any calls for human input if we have a valid
	value for @param user_reply_script_json.  That is how
	AUTO-MODE is implemented

	If we want to record replies for playback later, use @param
	record_user_replies_for_replay_filepath.

	As far as I know, the user can chose to respond "skip" to
	almost any quesiton.  Such a "skip" is done by the human
	operator hitting return to the prompt.  Or if @param
	user_reply_script_json then the value should be
	{'user_reply_txt' : ""}.

	@choices should contain the possible choices before the user.
	These are needed to handle some of the slightly more
	sophisticated AutoMode response policies.  E.g. 


		IF the 'policyInAutoMode' is
		RandomAnswerForMultiChoice-UnlessBotError (this is at
		least a rough approximation of the policy.  best to
		see @func auto_mode_reply_txt_for_rnd_ans_case_01
		which implements this policy.

		AND

		IF the user is being rompted with a multiple choice
                  question (i.e. not a type-in)

		THEN, this function will randomly chose an integer
		that is >= 0 and < num_choices

	TODO consider merging this (i.e. @fun user_input_wrapper) with
	the currently (2022-06-01) unused fn called
	handle_user_input(prompt_text)"""

	#print("Just called user_input_wrapper")
	#pdb.set_trace()

	if user_reply_script_json is None:
		user_reply_txt = input(prompt_text)
	elif user_reply_script_json == []:

		print("STATUS: Okay we've exhuased the list of steps in @param user_reply_script_json.")
		print("Thus, even though we in AUTO-MODE we need to start prompting the user")
		user_reply_txt = input(prompt_text)
	else:
	
		response_policy = user_reply_script_json[0].get('policyInAutoMode')
		if response_policy:

			# if response_policy == "AnswerZero-UnlessBotError":
			#	response_policy = "RandomAnswerForMultiChoice-UnlessBotError"
			# THE ABOVE WAS A TEMPORARY HACK DONE 2022-07-07 in RegressionTestLogs6-Random/

			if response_policy == "AlwaysAnswerZero":
				user_reply_txt = "0"

				# 2022-06-24T13:30:35PDT not sure why
				# I had the next line.  If days pass
				# and still not clear, then delete.
				#
				#current_user_reply_json = None
				
			elif response_policy == "AnswerZero-UnlessBotError":
				if asking_how_to_handle_bot_error_p:
					if if_reply_script_UnlessError_means_LogAndContinue:
						if error_msg is None:
							print("Now this is very strange.")
							print("When we coded this at 2022-12-20T22:42:57PST we did not consider")
							print("how you could ever have asking_how_to_handle_bot_error_p be True yet no error_msg")
							print("For this reason we will now enter the debugger so you can investigate")
							pdb.set_trace()
						print()
						print("The bot's response had an error in it.")
						print("The error_message was this:")
						print()
						print(error_message)
						print()					
						print("We are in auto mode and the response policy is  'AnswerZero-ButIfErrorLogAndContinue'")
						print("Thus, we are going to raise an exception and the message for that exception will be that error message.")
						print("The exception will be caught by machinery in @func run_test_question_driver_over_consult_list in test_question_driver_scale_up.py")
						print()
						raise Exception(error_msg)

					else:
						print(ASK_OPERATOR_HOW_TO_HANDLE_BOT_ERROR_STR)
						user_reply_txt = input(prompt_text)
				else:
					user_reply_txt = "0"

			# NEVER MIND I THINK I AM ABANDONONG THIS
			# CONDITION AND INSTEAD ADDING THIS NEW VRY
			# AD_HOC PARAMETER, i.e.
			# if_reply_script_UnlessError_means_LogAndContinue
			# and setting it to True

			elif response_policy == "AnswerZero-ButIfErrorLogAndContinue":
				if asking_how_to_handle_bot_error_p:
					if error_msg is None:
						print("Now this is very strange.  ")
						print("When we coded this at 2022-12-20T22:42:57PST we did not consider")
						print("how you could ever have asking_how_to_handle_bot_error_p be True yet no error_msg")
						print("For this reason we will now enter the debugger so you can investigate")
						pdb.set_trace()
					print()
					print("The bot's response had an error in it.")
					print("The error_message was this:")
					print()
					print(error_message)
					print()					
					print("We are in auto mode and the response policy is  'AnswerZero-ButIfErrorLogAndContinue'")
					print("Thus, we are going to raise an exception and the message for that exception will be that error message.")
					print()
					raise Exception(error_msg)

				else:
					user_reply_txt = "0"

			

			elif response_policy == "RandomAnswerForMultiChoice-UnlessBotError":
			
				user_reply_txt = auto_mode_reply_txt_for_rnd_ans_case_01(choices, asking_how_to_handle_bot_error_p)
			
			else:
				print(f"We do not yet know how to handle the response policy given, i.e. {response_policy}")
				pdb.set_trace()
		else:
			current_user_reply_json = user_reply_script_json.pop(0)
			user_reply_txt = current_user_reply_json['user_reply_txt']

		#2022-06-16T00:06:47EDT We don't need to trace here for now, but keeping this in case we want to turn it back on
		#print(f"2022-06-14T15:37:47EDT response_policy: {response_policy} current_user_reply_json: {current_user_reply_json} user_reply_txt: {user_reply_txt}")
		#print("Shall we Continue??? If so hit c as you enter the debugger.")
		#pdb.set_trace()

		print("FLAG: AUTO MODE: user_reply_txt is:", user_reply_txt)

		# This was used to help diagnose CONSYS-331 (CPD-147)
		# which was difficult to diagnose so as of
		# 2022-07-04T22:09:02PDT I'm leaving this here in case
		# we need to go down that rabbit hole again.  See
		# other occurrences of 147 or CONSYS-331 for at least
		# some of these debugging tricks.
		#
		# if user_reply_txt in [166, "166"]:
		# 	print("2022-07-02T21:06:13PDT Trying to debug 147")
		# 	pdb.set_trace()

	if record_user_replies_for_replay_filepath:
		with open(record_user_replies_for_replay_filepath, 'a') as record_fobj:
			user_turn_json = json.dumps({"user_reply_txt" : user_reply_txt})
			new_json_obj_to_write = user_turn_json + ","
			print(new_json_obj_to_write, file = record_fobj)

	return(user_reply_txt)


################################################################
# Make output filenames pretty and standardized

def filename_str_for_bot_question(question_seq_index_str, question_id, expected_max_digits = 3):

	question_seq_index_str = add_padding_to_int_str(question_seq_index_str, expected_max_digits)
	question_id		= add_padding_to_int_str(question_id, expected_max_digits)

	return(f"Q{question_seq_index_str}-bot-quest-Id{question_id}.json")

def filename_str_for_user_reply(question_seq_index_str, question_id, expected_max_digits = 3):

	question_seq_index_str  = add_padding_to_int_str(question_seq_index_str, expected_max_digits)
	question_id		= add_padding_to_int_str(question_id, expected_max_digits)

	return(f"Q{question_seq_index_str}-usr-reply-Id{question_id}.json")


################################################################

def log(filepath, text, print_to_stdout_too_p = False):
	with open(filepath, 'a') as out_fobj:
		if print_to_stdout_too_p:
			print(text)
		print(text, file=out_fobj)

################################################################

def subdir_names_in_directory(directory_path, dirnames_to_remove = None):

	"""Gives only sub directory names in directory_path, does not give full path of each subdirectory.
	The filenames of any mere files in directory_path are not returned.
	"""
	
	sub_dir_names = [d for d in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, d))]
	if dirnames_to_remove is not None:
		sub_dir_names = [d for d in sub_dir_names if d not in dirnames_to_remove]

	return(sub_dir_names)

def base_dir_name(path_string):
	"""
	>>> base_dir_name("UnitTestStuff/README")
	'UnitTestStuff'
	>>> base_dir_name("UnitTestStuff/")
	'UnitTestStuff'
	>>> base_dir_name("UnitTestStuff")
	'UnitTestStuff'
	"""
	if os.path.isfile(path_string):
		result = os.path.basename(os.path.dirname(path_string))
	elif os.path.isdir(path_string):
		splitted = path_string.split("/")
		if splitted[-1] == "":
			result = splitted[-2]
		else:
			result = splitted[-1]
	else:
		print("Hrm, need to figure out what @fun utils.base_dir_name should do if path_string is neither a real dir nor a file")
		pdb.set_trace()
	return(result)

################################################################

def ret_likely_response_mode_for_response_content(response_content):

	""" This is called in
	test_question_driver_process_system_reply.process_system_reply
	and here in utils.auto_mode_reply_txt_for_rnd_ans_case_01

	We want to know whether a given response_content item (what
	might be renamed to response_object) is either a:
	
		(1) multiple choice option
		(2) type in response

	Why does this have "likely" in its fun name?  Well, as of
	2022-06-21T21:08:06EDT , I am not absolutely positive that the trick
	below will absolutely determine this.

	See also @fun finding_in_cpd_is_valued_p in @file
	test_finding_proxies.py

	"""

	has_no_type_p = response_content['findingValue']['type'].lower() == 'none'
	if has_no_type_p:
		result = MultiChoiceResponseObject
	else:
		result = TypeInResponseObject
	return(result)

################################################################

def first_2nd_3rd_4th_nth(n: int):
	"""
	>>> first_2nd_3rd_4th_nth(0)
	'0th'
	>>> first_2nd_3rd_4th_nth(1)
	'1st'
	>>> first_2nd_3rd_4th_nth(2)
	'2nd'
	>>> first_2nd_3rd_4th_nth(3)
	'3rd'
	>>> first_2nd_3rd_4th_nth(4)
	'4th'
	>>> first_2nd_3rd_4th_nth(11)
	'11th'

	Yea, this will fail for 101, i.e. it won't spit out 101st
	And for 43, it will wrongly say 43th rather than 43rd.
	"""

	if n >= 4 or n == 0:
		suffix = "th"
	elif n == 1:
		suffix = "st"
	elif n == 2:
		suffix = "nd"
	elif n == 3:
		suffix = "rd"	
	else:
		print("How did you get here, there is a logic problem in this function.")
		pdb.set_trace()
	return(str(n) + suffix)
	
	