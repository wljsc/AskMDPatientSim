################################################################
# IMPORTS

import datetime as dt
import json
from tzlocal import get_localzone

################################################################
# CONSTANTS

# PARANOID_P = True
# 2022-06-14T16:26:56EDT only needs to be true if you are worried
# about filenames in logs having the correct padding for integers.
# Probably ignorable, so just set to False for safety
PARANOID_P = False

################################################################

def now_yyyy_mm_ddThhmmss(utc_offset_p = False):
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
		choices = None):

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
					print(ASK_OPERATOR_HOW_TO_HANDLE_BOT_ERROR_STR)
					user_reply_txt = input(prompt_text)
				else:
					user_reply_txt = "0"

					# 2022-06-24T13:31:07PDT not
					# sure why I had the next
					# line.  I put it here, bc I
					# was mimicing
					# 2022-06-24T13:30:35PDT, see
					# above.  If days pass and
					# still not clear, then
					# delete.
					#
					#current_user_reply_json = None

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

def log(filepath, text):
	with open(filepath, 'a') as out_fobj:
		print(text, file=out_fobj)

################################################################
		
