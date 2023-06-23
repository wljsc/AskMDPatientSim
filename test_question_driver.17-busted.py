# test_question_driver.py
################################################################
# TODOs (put newest on top)

# TODO(2022-06-24T00:24:59PDT, )
#
# if CONVERSATION_INVARIANT_MODE_P:
# 		sys_quest_num_str = f"QuesSeq# {question_seq_index}"
# else:
# 		sys_quest_num_str = f"QuesSeq# {question_seq_index} QuesID# {question_id}"			


# TODO(2022-06-23T23:38:30PDT, ) for the noteworthy events thing, best to
# make it a function, just like @fun log.
# It will have required args like <description text><question id number rec numb thing> etc
# It will print a buncha ###'s demarcating each noteworthing thing.

# TODO(2022-06-23T22:43:04PDT, ) figure out what is going on in things like this..
# "Weird, why is @param response_content_list empty!?!?!"
# that happens e.g. in BotAsks QuesSeq# 21 Title: 'Medications'

# DONE(2022-06-01T17:24:37PDT, 2022-06-23T14:32:52PDT ) give an ] for the end of the script!!

# TODO(2022-06-23T12:03:13PDT, ) if Big Branch 3 survives, then do
# note that at some maybe all of its steps 1, 2, 3 should be replaced
# with @param solicit_user_ans_to_the_multiple_choice_question.  Maybe
# Big Branch 2, also.  But more than likely Big Branch 1 2 3 will be superceeded by
# @func handle_mixed_response_content_list

# TODO(2022-06-23T11:56:05PDT, ) prolly rename user_reply_script_json
# to s.t. like replies_for_auto_mode_json

# TODO( 2022-06-22T19:59:55PDT, ) NEXT ACTIONS make the test cases work that are
# failing.  we REALLY gotta fix @func
# index_where_multi_choice_options_end.  Once we do that, then fire up question_and_answer_loop(19, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "../TstCoupProgLogs/Consult.2022-06-22T1727-Cpd-19/recording_of_user_replies_for_sim_script.json")
#  or even better make a test case for @func handle_mixed_response_content_list


# TODO(2022-06-22T11:28:04PDT, ) handle_mixed_response_content_list
# should probably take over for all the branches.  This to do is
# repeated in lined of the code.

# TODO(2022-06-22T11:28:40PDT, ) we should probably enable the ability
# to return multiple findings to add.This to do is repeated in lined
# of the code.

# TODO(2022-06-21T21:08:36EDT, ) find out for sure whether @func
# ret_likely_response_mode_for_response_content really is the right
# way to determine if its multiple choice or not -- see
# 2022-06-21T21:08:06EDT below.

# TODO(2022-06-21T20:49:13EDT, ) consider renaming response_content_list to response_object_list
# and response_content to response_object

# TODO(2022-06-21T19:16:20EDT, ) consider merging the param names and
# printouts of "SubQuestionTxt", "response_name" and
# "chosenfindingName" into one name to minize confusion.  why?  see
# 2022-06-21T19:14:06EDT

# TODO(2022-05-19T12:50:27PDT, ) TODO TODO don't forget to log error in logs!!

# TODO(2022-05-19T11:24:56PDT, ) when writing to CONVERSATION_FILENAME and answer is not
# multiple choice include it in the log
#
# And also if there is only one choice like this, we do not see my responses:

# * USERS CHOICE 12 Answer#: 0 Text: toes turn white or blue
# * SYSTEM QUESTION  13: Have you had surgery or other procedure in the past few months?
# 0: surgery, joint injection, or other procedure to the foot or ankle in the past few weeks
# * SYSTEM QUESTION  14: If you have tried treating your foot or ankle problem, what did you do and did it help?
# 0: null
# * SYSTEM QUESTION  15: Do you have any of these muscle, joint, or bone symptoms?
# 0: episodes of joint pain always occur with fever
# 1: joint pain that migrates from joint to joint
# 2: one or more finger joints swollen
# 3: sausage-shaped finger
# 4: widening or thickening (clubbing) of the fingertips
# 5: wrist swollen
# 6: bone pain
# 7: back pain
# 8: cramping leg pain with use
# 9: calf pain
# * USERS CHOICE 15 Answer#: 0 Text: episodes of joint pain always occur with fever

# TODO(2022-05-19T11:49:07PDT, ) why does the bot list multiple choice but the website lists a type in
# [[<<Link-2022-05-19-Thu-11-52>>][(*)]]
#
# * SYSTEM QUESTION  24: Are you taking any medications?
# 0: estrogen
# 1: calcium channel blocker
# 2: glitazone
# * USERS CHOICE 24 Answer#: 0 Text: estrogen


# TODOs (end of section)
################################################################
# HISTORY (start of section - put newest on top)

# 2022-06-24T07:31:43PDT MILESTONE auto mode has discovered its first
# real problem and prompted the need for a new resposne policy,
# i.e. "AnswerZero-UnlessBotError"

# 2022-06-23T22:49:14PDT test_question_driver.v16.py

# 2022-06-23T14:20:48PDT MILESTONE: first successful runthrough of
# consult 19 - has mixed resposne_content_list (i.e. debugging of it
# largely? complete)

# 2022-06-22T12:27:38PDT First draft (code complete?) in which we have
# implemented @func handle_mixed_response_content_list.

# 2022-06-21T19:31:47EDT renamed all response_txt -> response_name
# (even if response_txt is a substring)

# 2022-06-21T19:09:20EDT renamed nth_choice ->
# response_number to more closely match what we do for type-in response
# in other words, we are moving toward removing redundancy between hanlding
# of type_in response and multichoice_reponse.

# 2022-06-21T21:20:56EDT just noticing that 2022-06-15T11:45:19EDT
# suggests there might have been a unresolved 'mixed type-in multiple
# choice vs male/faema and bday issue'??

# 2022-06-16T0013 test_question_driver.v15.py
#
# At the time of the save of that (or more precisely
# 2022-06-16T00:12:57EDT) we had this as the  N_E_X_T__A_C_T_I_O_N:
# "okay we think we are done with 'none of the above' kind of answer,
# now let's move on to tackle the real assumption violation"

# 2022-06-15T15:12:48EDT test_question_driver.v14.py Wed

# 2022-06-15T15:08:59EDT recently discovered the problem with the
# assumption that that any time we have a response_content_list all of
# its values are either None type (as in a multiple choice) or all are
# type ins.  I am about to (after test_question_driver.v14.py) make
# major changes to handle that.  I may also make changes to handle no
# choice. 

# 2022-06-14T18:22:45EDT Tue - adding stuff to handle a policy
# (e.g. always chose zero)

# 2022-06-10T20:12:35PDT Fri test_question_driver.v13.py

# made filenames pretty - digts lined up etc.
# making it detect we are done - i.e. no more questions

# 2022-06-10T17:15:24PDT Fri test_question_driver.v12.py

# some variable name improvements.
# added in valueTypeUnit

# 2022-06-03T11:18:38PDT test_question_driver.v11.py

# decent stopping point before more changes.

# 2022-06-01T16:02:30PDT test_question_driver.v10.py

# crude version of auto mode WORKS!!!

# but in order to do a massive test of all the first two questions
# until error across all consults, I need to change the way
# CONVERSATION_FILENAME is formated.  So that will happen AFTER this
# version (i.e. 10)

# 2022-06-01T16:02:30PDT test_question_driver.v09.py

# beginning to implement 'auto mode'.  Problem is that I am doing it
# by reading from the file and it's all messed up.  So, abandoning
# that and instead going to read in whole file and do json.loads.
# Store the script as a list and we pop(0) the list to go through it.
# I have not started on the new json.loads approach and am freezing
# this version in case I want to abort the new approach.

# 2022-05-31T17:56:59PDT test_question_driver.v08.py

# did a TON of refactoring of the elements for the questions, very
# confusing bc there are the meaningless JSON elemets in the CPD db,
# and then different names in terms of what the bot presents of those,
# context dependence of meaning (e.g. response_content['name'] means
# 'multiple choice option' in the context of a multiple choice, but 
# nd there is also variability, like
#<START QUOTE FROM BELOW>
# Is this inconsistent or is there a method behind it, for TypeIn: 
#
# - for some, SubQuestionTxt: 'date of birth' and ResponseHeader: None
# - for others, SubQuestionTxt: 'null' and ResponseHeader: What is your height?
#<END QUOTE FROM BELOW>
#

# 2022-06-21T19:14:06EDT update RE the immediate above (i.e. the
# history entry dated 2022-05-31T17:56:59PDT).  I think there is
# potential confusion bc SubQuestionTxt is the same thing as
# response_name.  And also chosenfindingName elsewhere.  Hence This is
# motivation for the to do dated 2022-06-21T19:16:20EDT see also.




# TODO(2022-05-31T18:00:48PDT, ) next actions - leaving this uncommented
# to that it shows up prominently when try to run: (1) each time there
# is input( (e.g. seeking user input) there will be a wrapper around
# those.  It will ask "are we in automatic mode", if not, ask the user,
# if so look up in the script.  The script is a json file which is a
# array.  the nth ele corresponds to the nth question.  the nth ele has
# things like questionseq number, consult id, questionID etc and so, at
# each turn it reads from the script and it asks itself, does this match
# what i expect? the script json for that turn will aslo say 'okay if it
# DOES match, then how do you response - e.g. for the 13th turn chose a
# random ele, for the 2nd give this answer text.  when recording a human
# users trace, this will be saved so that the script can be
# reconstructeed.  in the begining, it might be the bareset bone thing.
# e.g. just a list of answers.  e.g. like this:

# [response: '0'],
# [response: '12/28/1988'],
# [resposne: '71'],
# [resposne: '161']




# 2022-05-31T12:53:21PDT test_question_driver.v07.py (for real)

# alas this won't run bc the work started at 2022-05-31T12:28:39PDT is in mid-flight.

# 2022-05-31T12:53:07PDT realized I forgot to save test_question_driver.v07.py

# 2022-05-31T12:28:39PDT starting to work on automatic question answering.

# 2022-05-31T12:26:13PDT test_question_driver.v07.py (not really - see 2022-05-31T12:53:07PDT, immed above)

# i've fixed the formatted problem mentioned in v06.  not sure what
# else is different but i intuite it is generally better.

# 2022-05-23T16:10:33PDT test_question_driver.v06.py

# been tryingt to imporve the formatting but i messed something out
# i cut out big branch 2, or the essential meat of big branch 1.
# (LATER, 2022-06-14T16:46:00EDT  It looks like what used to be
# big branch 2 is not big branch 3 and there is a new branch.  the new
# branch is big branch 2.

# 2022-05-20T19:18:04PDT test_question_driver.v05.py

# we have the ability to handle an error by skipping to the next
# question. And we are about to improve the variety of responses to an
# error from the bot.

# Specfically, we are not quite, but about to add the ability to not
# only skip to the next question but also to essentially pretend the
# error dide not happen.  I.e. to take the input that caused the bot
# to error and edit that input, take the edited input and re-try.

# 2022-05-19T13:57:07PDT test_question_driver.v04.py

# in this version we've been using it for while.
# it has ability to pick up where left off (search for PickUpFromWhereYouLeftOff/)

# it has abiliyt to save the conversation to CONVERSATION_FILENAME so
# tyou can replay it on the website.

# it's got the beginnings of decent logging

# 2022-05-13T10:53:40PDT freezing test_question_driver.v03.py 

# it kinda works, but in the next version i want to try just taking
# the entire chosen response optioh and using that as the 'selected
# finding' rather than constructing a finding afresh.

# HISTORY (end of section)
################################################################
# IMPORTS

import os
import requests
import json
#import json-diff
from deepdiff import DeepDiff
import datetime as dt
from time import sleep
import pdb

################################################################
# CONSTANTS (start of section)

MultipleChoice = "all in response_content_list have no type, thus they are all responses that are discrete multiple-choice type answers, i.e. not user typed in values" 
Mixed_TypeInAndMultipleChoice = "Mixed_TypeInAndMultipleChoice"
TypeIn = "all eles in response_content_list have a type, thus they are all responses that want to have a user typed in value"

UserChoiceWasNoneOfTheAbove = "This is hack trying to be an Enum the meaning of which is that the user chose 'None of the above'"

# Yet more enum hacks!!
MultiChoiceResponseObject	=  "MultiChoiceResponseObject"
TypeInResponseObject		= "TypeInResponseObject"


STEP_SLOWLY_P = False

STEP_SLOWLY_2 = False

# STEP_SLOWLY_2 was for traces circa 2022-06-23 when we were in the
# mode of implementing / testing @func
# handle_mixed_response_content_list - i.e. to handle
# response_content_list which was a mix of TypeIn and MultiChoice
# replies.

CONVERSATION_INVARIANT_MODE_P = False

# Typically you want to keep CONVERSATION_INVARIANT_MODE_P False.  The
# only time to change it to True would be when you are needing to
# compare conversation traces files from different runs of the AskMD
# Patient Simulator.

# For the example that motivated creating
# CONVERSATION_INVARIANT_MODE_P see...  "2022-06-01T21:57:11PDT
# Example Justifying Why We need CONVERSATION_INVARIANT_MODE_P" ...in
# diary-TestCoupletPrograms.org.
#
# But here is an attempt to summarize the purpose of it. Sometimes we
# want to compare two conversation files (i.e. CONVERSATION_FILENAME)
# because you are trying to debug why one the conversation for one CPD
# worked ok but for another one it did not.  You can do a diff between
# the two files.  HOWEVER, the question record id's between different
# CPD files can be radically different even though the sequence of
# question sentences actually asked is identical. As a result there
# are tons of spurious diffs when you compare them.  To fix this
# problem we set CONVERSATION_INVARIANT_MODE_P to True. Why?  Bc in
# that mode it will not output the quesiton record number in said
# conversation trace files.


#PARANOID_P = True
# 2022-06-14T16:26:56EDT only needs to be true if you are worried
# about filenames in logs having the correct padding for integers.
# Probably ignorable, so just set to False for safety
PARANOID_P = False

#DIR_OF_CPD_FILES = "/Users/william.jarrold/ShCr/AskMD/Code/Packages/Consultation.API7/Consultation.API/app-data/couplet/consults/2022-02-04-Draft13"
# 2022-06-14T11:57:23EDT changing the above to this (i.e. adding .fixed)
DIR_OF_CPD_FILES = "/Users/william.jarrold/ShCr/AskMD/Code/Packages/Consultation.API7/Consultation.API/app-data/couplet/consults/2022-02-04-Draft13.fixed"

CONVERSATION_FILENAME = "conversation_text.org"

# CONVERSATION_FILENAME: The purpose of this file is to store a human
# readable version of the conversation between the bot and the human
# (or even auto_mode?)  operator of the AskMD Patient Simulator.  You
# might call such a file a conversation trace file.

# 2022-06-23T16:55:15PDT replaced all "conversation_text.org" with CONVERSATION_FILENAME

ISSUES_OF_NOTE_FILENAME = "issues_of_note.org"

# ISSUES_OF_NOTE_FILENAME the purpose of this file is to save
# noteworthy, possibly anomalous events, that happen during a run of
# the AskMD Patient Simulator.

TEST_RESPONSE_CONTENT_LIST_OF_MIXED_TYPE_01 = \
[{'name': 'systemic corticosteroid', 'respNo': '13', 'entNo': '64193', 'mmp': None, 'findingValue': {'type': 'NONE', 'defaultUnit': None, 'units': [], 'format': 'DOUBLE'}, 'extensionData': []}, {'name': 'other medication', 'respNo': '104', 'entNo': '46444', 'mmp': None, 'findingValue': {'type': 'ABSOLUTE_STRING', 'defaultUnit': None, 'units': [], 'format': 'STRING'}, 'extensionData': []}]

TargetResultForStartConsult14 = \
"""{
    "consultationId": 14,
    "questionId": 68,
    "title": "Birth sex, date of birth",
    "nextQuestionId": 10,
    "questionCountSeq": 27,
    "questionIndexSeq": 1,
    "extensionData": [
        {
            "name": "GenderDOB",
            "parameters": null
        }
    ],
    "responseSections": [
        {
            "header": null,
            "responses": [
                {
                    "name": "female",
                    "respNo": "180",
                    "entNo": "12100",
                    "mmp": null,
                    "findingValue": {
                        "type": "NONE",
                        "defaultUnit": null,
                        "units": [],
                        "format": "DOUBLE"
                    },
                    "extensionData": []
                },
                {
                    "name": "male",
                    "respNo": "184",
                    "entNo": "3066",
                    "mmp": null,
                    "findingValue": {
                        "type": "NONE",
                        "defaultUnit": null,
                        "units": [],
                        "format": "DOUBLE"
                    },
                    "extensionData": []
                }
            ]
        },
        {
            "header": null,
            "responses": [
                {
                    "name": "date of birth",
                    "respNo": "181",
                    "entNo": "31314",
                    "mmp": null,
                    "findingValue": {
                        "type": "DATE",
                        "defaultUnit": null,
                        "units": [],
                        "format": "DATE"
                    },
                    "extensionData": []
                }
            ]
        }
    ],
    "findings": []
}"""

# TODO(2022-06-22T18:22:05PDT, ) there are probably LOTS of functions that can use the above for test case!!


# CONSTANTS (end of section)
################################################################


def question_and_answer_loop(
	start_conversation_with,
	log_basedir = None,
	patient_sim_script_fpath = None,
	record_user_replies_for_reply_filename = None):

	"""

	@param start_conversation_with should be json that sets the state
	for the users reply.  

	If you want to start at the very beginning of consult, then if
	the consult number is CONSULT_NUMBER then
	start_conversation_with should be:

	{"consultationId": CONSULT_NUMBER}

	@param patient_sim_script_fpath if None, just operates as
	normal, or 'manual' mode.  I.e. the operator of this simulator
	gives answers to each question from the AskMD bot when prompted.

	For AUTO-MODE AUTO mode AutoMode, Automatic Mode (a.k.a REPLAY mode)
	then @param patient_sim_script_fpath needs to point to a json
	file.  This file specifies for each user turn, what should be
	the response.


	DO YOU WANT TO LOG THE RUN?

	@param log_basedir if this is None, there should be no logs.
	If not None, then it must be a dir path.  A directory
	dedicated to the logging of *this* run will be created.  The
	name of that directory will be
	Consult.{now_yyyy_mm_ddThhmm()}-Cpd-{consultation_id}

	@param record_user_replies_for_reply_filename is used if you
	want to 'record' the series of answers that the human operator
	of the patient simulator uses so that later that 'recording'
	can be 'played back' in automatic patient simulator mode.  The
	file it saves is a JSON so best to name the file with a .json
	suffix.  TODO rename this something like
	write_to_patient_sim_script_fpath or
	record_auto_mode_script_fpath

	Note, if record_user_replies_for_reply_filename is None AND if
	log_basedir is *not* None, then this will automatically save
	in a file called patient_sim_script.json in the directory.

	Thus, there is a sense in which you don't need to worry about
	saving for replay later, it happens by default in the log dir
	created for this run (assuming you have specified a value for
	@param log_basedir.)

	"""

	if patient_sim_script_fpath is None:
		user_reply_script_json = None
		print("SIMULATOR MODE IS ManualMode")
	else:
		with open(patient_sim_script_fpath, 'r') as user_reply_script_fileobj:
			try:
			 	user_reply_script_json = json.load(user_reply_script_fileobj)
			except Exception as error_msg:
				print("################################################################")
				print("ERROR "* 10)
				print("json.load(user_reply_script_fileobj) did not work.")
				print()
				print("The error message is:")
				print(error_msg)
				print()
				print("Most likely what is happening is that the file that is trying to be loaded has malformed json in it")
				print()
				print(f"The filepath for that file is: {patient_sim_script_fpath}")
				print("(That filepath is the value of @param patient_sim_script_fpath)")
				print()
				print("Often times in errors like these, there is a missing ] at the end")
				print("Other times, there is the requisite ] at the end but the last element has a comma which apparently is forbidden")
				print()
				print("If this is the correct diagnosis, then the fix is simply to edit the file pointed to by patient_sim_script_fpath.")
				print("In other words, go into that file and add the missing ] at the end, or delete the forbidden , in the last element")
				print()
				print("To repeat: the file to edit is: {patient_sim_script_fpath}")
				pdb.set_trace()
		print(f"SIMULATOR MODE IS AutoMode - following script described in {patient_sim_script_fpath}")

	#print("Just entered question_and_answer_loop()")
	# pdb.set_trace() commented out bc see 2022-05-12T08:49:02PDT
	#print("Just entered question_and_answer_loop()")	

	if type(start_conversation_with) == int:
		initiate_conversation_json = {"consultationId": start_conversation_with}
		question_index_seq = 0
		
	elif type(start_conversation_with) == str:
		initiate_conversation_json = read_json_file(start_conversation_with)
		question_index_seq = initiate_conversation_json.get('questionIndexSeq', -777)
	else:
		print("Unexpected type for @param start_conversation_with ")
		pdb.set_trace()
		
	consultation_id = initiate_conversation_json['consultationId']

	print("################################################################")
	print(f"##### Starting Dialog: Consult {initiate_conversation_json['consultationId']} ######")
	print("################################################################")
	print(f"#### Current Time at Dialog Start Is: {now_yyyy_mm_ddThhmm()}")

	users_reply = json.dumps(initiate_conversation_json)
	
	if log_basedir is not None:
		sub_dir_for_this_run = f"Consult.{now_yyyy_mm_ddThhmm()}-Cpd-{consultation_id}"
		log_dir = os.path.join(log_basedir, sub_dir_for_this_run)
		os.mkdir(log_dir)
		print()
		print(f"#### This conversation is being logged in {sub_dir_for_this_run} ################")
		print(f"#### It is a subdir of {log_basedir} ############################################")
		print(f"#### Log Full path is: {log_dir} ################################################")
		print()
		
	else:
		log_dir = None

	if log_dir is not None:
		conversation_log_filepath = os.path.join(log_dir, CONVERSATION_FILENAME)
		issues_of_note_filepath   = os.path.join(log_dir, ISSUES_OF_NOTE_FILENAME)

		
		if record_user_replies_for_reply_filename is None:
			record_user_replies_for_reply_filename = os.path.join(log_dir, "recording_of_user_replies_for_sim_script.json")
	else: 
		conversation_log_filepath = None
		issues_of_note_filepath = None

	if record_user_replies_for_reply_filename:

		# 2022-06-23T14:35:46PDT the auto_mode script is a
		# list of json objects.  Thus as we start writing to
		# this script as we are saving the human operator's
		# answers to each question (as a json_list), need to
		# start the list with a '['
		#
		#
		# For the close bracket at the end see
		# 2022-06-23T14:30:32PDT

		with open(record_user_replies_for_reply_filename, 'a') as record_fobj:
			print("[", file = record_fobj)

			# TODO(2022-06-23T14:28:31PDT, ) rename record_user_replies_for_reply_filename to something
			# that mentions auto_mode

	while True:

		# bot_output, user_input_json, question_seq_index = post_users_reply(users_reply, log_dir, question_index_seq, conversation_log_filepath)
		# 2022-06-10T17:48:23PDT getting rid of unecceary and attradtive nuisance return varianble user_input_json
		# 2022-06-10T17:48:23PDT getting rid of it bc users_reply should be just the same
		# 2022-06-10T17:48:23PDT keeping the 2022-06-10T17:48:23PDT comments in case I am wrong
		# 2022-06-10T17:48:23PDT about its deleteabilty.
		# TODO(2022-06-10T17:48:23PDT, ) after several days blow this all away
		
		bot_output_json, question_seq_index = post_users_reply(users_reply, log_dir, question_index_seq, conversation_log_filepath)

		users_reply_json = json.loads(users_reply)
		
		error_msg = bot_output_json.get('error')
		
		if error_msg:

			print()
			print("Ugh, we posted @param payload (i.e. json representation of user response and finding list) and the bot is returning an error!!!")
			print("you might want to look at the value of @param payload to see if something was formatted in an obviously bad way")
			print()
			print("Here is the error msg:")

			question_id = users_reply_json['questionId']
			if CONVERSATION_INVARIANT_MODE_P:
				sys_quest_num_str = f"QuesSeq# {question_seq_index}"
			else:
				sys_quest_num_str = f"QuesSeq# {question_seq_index} QuesID# {question_id}"			
			string_to_log_and_print = f"BotReplies with Error to {sys_quest_num_str}\nBotError JSON is:\n{error_msg}\n"
			log(conversation_log_filepath, string_to_log_and_print)

			if issues_of_note_filepath:
				with open(issues_of_note_filepath, 'a') as issues_of_note_fobj:
					print("################################################################")
					print()
					print(sys_quest_num_str, file=issues_of_note_fobj)
					print(string_to_log_and_print, file=issues_of_note_fobj)
					print()
					print("################################################################")


			print()
			print(error_msg)
			print()

			options = ["edit the payload and post again", "go into the debugger", "quit"]

			my_next_question_id = users_reply_json.get('myNextQuestionId')
			
			if my_next_question_id is None:
				print("")
				print("HEY!!! When we have an error, usually one of your options")
				print("is to skip to the next question. HOWEVER, this time there")
				print("is no such option because there is no next question!!")
				print("")
			else:				
				options = ["skip to next question"] + options

			options_listing = ""
			for nth, option_txt in enumerate(options):
				options_listing += f"\n{nth}: {option_txt}"

			print("Would you like to:", options_listing)
			#user_reply_text = user_input_wrapper("Type In Your Choice Here: ")
			user_reply_text = user_input_wrapper(
				"Type In Your Choice Here: ",
				user_reply_script_json,
				record_user_replies_for_reply_filename,
				asking_how_to_handle_bot_error_p = True)


			user_reply_int = int(user_reply_text)
			choice_txt = options[user_reply_int]

			string_to_log_and_print = f"UserReply to BotError for {sys_quest_num_str} is: '{choice_txt}'\n"
			print(string_to_log_and_print)
			log(conversation_log_filepath, string_to_log_and_print)
			
			if choice_txt == "skip to next question":
				# TODO(2022-05-20T10:56:00PDT, ) log this.
				
				#users_reply = skip_to_next_question(user_input_json)
				# 2022-06-10T18:39:22PDT after a few days delete the immediately preceeding line
				# 2022-06-10T18:39:22PDT oce we are sure thyat users_reply_json really is the fix.
				users_reply = skip_to_next_question(users_reply_json, my_next_question_id)

				continue
				
			elif choice_txt == "edit the payload and post again":
				print("Okay, you chose to edit the payload and post again.")
				print()
				print("So, how do you go about editing the payload?")
				print()
				print("Well, what you need to do is take the value of @param user_input,")
				print("Next edit that value and bind that new value to @param users_reply (a string, not a dict)")
				print("And then continue from the error that we are about to enter")
				pdb.set_trace()
				continue
			
			elif choice_txt == "go into the debugger":
				print("Okay, we will enter the debugger so you can decide what to do.")
				# TODO(2022-05-20T10:55:36PDT, ) log this.
				pdb.set_trace()
				
			elif choice_txt == "quit":
				#exit()
				return("Program Done!!")
			
			else:
				print("Unexpected option, whats going on!?!?!")
				pdb.set_trace()

		if bot_output_json.get('questionId') is None:

			print("################################################################")
			print("### Bot did not return a 'questionId' when it responded to the #")
			print("### the last user input.  Thus, we have completed the question ##")
			print("### driver. ####################################################")

			# 2022-06-23T14:30:32PDT Because we are done
			# with the questionnaire, there are no more
			# user answers to record, thus we want to add
			# close bracket to indicate the end of a list
			# because we are done with writing to the
			# auto_mode script (which is a json list)

			if record_user_replies_for_reply_filename:
				with open(record_user_replies_for_reply_filename, 'a') as record_fobj:
					print("]", file = record_fobj)
				
			break
				
		else:
			users_reply, question_index_seq = \
				process_system_reply(bot_output_json,
					log_dir,
					conversation_log_filepath,
					user_reply_script_json,
					record_user_replies_for_reply_filename,
					issues_of_note_filepath)

	print("#################################################################")
	print("### We have exited the while loop of ############################")
	print("### @func question_and_answer_loop ##############################")
	print("#################################################################")	
	print("### This run of the AskMD Patient Simulator on ##################")	
	print(f"### Consult ID {consultation_id} ################################")
	print("### is Complete #################################################")
	print("#################################################################")		

#!! return(user_response_object_str, question_index_seq)


# 2022-05-24T11:25:18PDT looking for question_id

def post_users_reply(payload, log_dir, question_seq_index, conversation_log_filepath):
	# 2022-05-16T11:26:00PDT prolly delete question_seq_index are all things with this timestamp

	""" 

	We post a payload which is, I *think* a json formatted string
	that contains the user reply.  This function that returns what
	the bot 'says' in response, and a couple of other details.
	# 2022-06-10T18:16:17PDT renaming result_json to bot_output_json

	@return bot_output_json - what the bot says in response to the user's reply.

	@return payload_as_dict, question_seq_index

	# TODO(2022-06-22T19:46:18PDT, ) Work on this later
	#>>> bot_output_json = post_users_reply('{"consultationId": 14 }', log_dir = None, question_seq_index = 0, conversation_log_filepath = None)
	#>>> bot_output_json == (TargetResultForStartConsult14, 1)
	#True

	# If there is a diff, try this:
	# >>> the_diff = DeepDiff(result, Result_from_start_Consult14)
	# >>> the_diff_pretty = json.dumps(the_diff, indent=4, sort_keys=True)
	# >>> print(the_diff_pretty)

	"""
	
	if STEP_SLOWLY_2:
		print("In @func post_users_reply: To make test case for this fn we want to know what the args are when this is called so that we can specify them in the test case")
		pdb.set_trace()
		
	print("################################################################")
	print("### Just Entered @fun post_users_reply ################################")
	print("################################################################")
	print()
	
	payload_as_dict = json.loads(payload)
	question_id = payload_as_dict.get('questionId', "NoQuestionIdSpecified")
	
	print(f"#### Payload for User Answer to Ques QuesSeq# {question_seq_index} QuesID# {question_id}")
	print("#### Payload (start of json object) ####")
	print()
	print(json.dumps(payload_as_dict, indent = 4, sort_keys = True))
	print()	
	print("#### Payload (end of json object) ####")

	print()
	#print("Just entered post_users_reply - is the input (payload) - see if you can get 'unable to move there or whatever'")
	# pdb.set_trace() commented out bc see 2022-05-12T08:49:02PDT
	#print("Just entered post_users_reply - is the input (payload) - see if you can get 'unable to move there or whatever'")	

	#url = 'https://api.dev.sharecare.com/consultation/next'
	# ... 2022-06-22T13:10:33PDT dev is dead, long live qa...
	url = 'https://api.qa.sharecare.com/consultation/next'
	
	headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

	post_response = requests.post(url, data=payload, headers=headers)
	#r = requests.post(url, data=payload, headers=headers)

	#post_response_status = post_response.status_code
	if post_response.status_code == 503:
		print("We are getting a status of 503, i.e. Service Unavailable")
		print("Here is what the response to the post looks like if we call print on it:")
		print(post_response.status)
		pdb.set_trace()

	if post_response.status_code not in [200, 500]:

		# We can skip past error of 500 bc usaully what we
		# want is the error message buried in the json and
		# that gets printed out to the operator elsewhere in
		# the code.
		
		print("post_response.status_code:", post_response.status_code)
		print("TODO this trace is a reminder to put in a test to make sure <to be filled in> is always the status")
		print("so that we can characterize the range and frequencies of the various statuses we'll get")
		pdb.set_trace()

	bot_output_json = json.loads(post_response.text)
	#bot_output_json = json.loads(r.text)
	#pdb.set_trace()
	#result_str = json.dumps(bot_output_json, indent=4, sort_keys=True)

	error_msg = bot_output_json.get('error')
	if error_msg:

		question_seq_index += 1
		if question_seq_index > 10:
			question_seq_index_str = "0" + str(question_seq_index)
		else:
			question_seq_index_str = str(question_seq_index)

		question_id = "NoID-BcBotError"
		
		error_report_string = \
			elif response_policy == "AnswerZero-UnlessBotError":

				if asking_how_to_handle_bot_error_p:

					print("STATUS: Okay the bot has thrown an error.")
					print("We are AUTO-MODE however the response_policy is 'AnswerZero-UnlessBotError'")
					print("(by 'BotError' we we mean the AskMD Consultation Service.  We do *not* mean the Sharecare ChatBot)")
					print("In other words the value for 'policyInAutoMode' specified in the file specified")
					print("by @param user_reply_script_json is 'AnswerZero-UnlessBotError'")
					print("Thus we need to ESCAPE OUT OF AUTO-MODE and,
					print("Ask you, the human operator, what to do")

					user_reply_txt = input(prompt_text)

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

	if record_user_replies_for_replay_filepath:
		with open(record_user_replies_for_replay_filepath, 'a') as record_fobj:
			user_turn_json = json.dumps({"user_reply_txt" : user_reply_txt})
			new_json_obj_to_write = user_turn_json + ","
			print(new_json_obj_to_write, file = record_fobj)

	return(user_reply_txt)

def handle_user_input(prompt_text):
	# NOTE THIS FUNCTION WAS ABANDOONED A LONG TIME BEFORE NOW
	# (2022-06-15T15:15:52EDT) see user_input_wrapper.  We still
	# might re-use the code below so might as well keep it for a
	# while.
	"""
	if user types n that means none of the above.
	if user types e that means enter debugger.
	if user types s that means list the sequence of questiojs and answers given so far in user friendly English
	if user types j that means see the json input that we are processing
	if the user types in p that means see what the users post was
	"""
	print("""In addition there are these 'meta' options:
	n none of the above options.p
	e that means enter debugger.
	s list sequence of questions and answers given so far in user friendly English (e.g. to faciliate replication on AskMD)
	j see the json input that we are processing	
	if the user types in p that means see what the users post was""")
	

	users_choice = input(prompt_text)
	if users_choice == 'e':
		pass

def detect_type_in_vs_multi_choice_anomaly(elements_that_have_no_type):

	"""
	@RETURN:

		'non_anomalous.'

		xor

		'anomalous.<followed by explanatory text>'
		

	The PURPOSE is to detect any time we have a sequence of
	response_items we *expect* it to be either:

	(1) a sequence of all TypeIn response objects followed by all
	MultiChoice Response Objects

	or

	(2) a sequence of all MultiChoice response objects followed by
	all TypeIn Response Objects

	Why?  Because it would seem funny if we have to render a
	type-in that is 'surrounded' by multi-choices.  I want to know
	if one of these happens bc I want to see how legacy AskMD
	website renders these to the end human user.

	Concretely, this function is looking for either:
	
		(1) a pattern where we have True initially changing to False and then Back to True.
		(1) a pattern where we have False initially changing to True and then Back to True.

	>>> detect_type_in_vs_multi_choice_anomaly([True])
	'non_anomalous.'

	>>> detect_type_in_vs_multi_choice_anomaly([False])
	'non_anomalous.'

	>>> detect_type_in_vs_multi_choice_anomaly([False, True, True])
	'non_anomalous.'

	>>> res1 = detect_type_in_vs_multi_choice_anomaly([False, True, False])
	>>> res1.startswith("anomalous.")
	True

	>>> res2 = detect_type_in_vs_multi_choice_anomaly([False, False, True, False])
	>>> res2.startswith("anomalous.")
	True

	>>> res3 = detect_type_in_vs_multi_choice_anomaly([False, False, False, True, False, False, False])
	>>> res3.startswith("anomalous.")
	True

	"""

	result = "presumed_non_anomalous."
	if elements_that_have_no_type[0] == True:
		for index, ele in enumerate(elements_that_have_no_type[1:]):
			if ele == False:
				if any(elements_that_have_no_type[index+1:]):
					result = f"anomalous. started at True at index={index} changed to False, and then there was a True after that in {elements_that_have_no_type}"

	elif elements_that_have_no_type[0] == False:
		for index, ele in enumerate(elements_that_have_no_type[1:]):
			if ele == True:
				#print("debug here")
				#pdb.set_trace()
				if not(all(elements_that_have_no_type[index+1:])):
					result = f"anomalous. started at False at index={index} changed to True, and then there was a False after that in {elements_that_have_no_type}"
	else:
		print("how did you get here?!?! (in @func detect_type_in_vs_multi_choice_anomaly)")
		pdb_set_trace()

	if result == "presumed_non_anomalous.":
		result = "non_anomalous."
	if result.split(".")[0] not in ["anomalous", "non_anomalous"]:
		print("hrm there is a bug in @func detect_type_in_vs_multi_choice_anomaly")
		pdb.set_trace()
	return(result)

################################################################	

def pretty_print_response_content_type_list(response_content_list):
	"""
	This is just to help debugging / monitoring

	#>>> pretty_print_response_content_type_list([MultiChoiceResponseObject, TypeInResponseObject])
	#["MultiChoice", "TypeIn"]

	#>>> pretty_print_response_content_type_list(["MultiChoiceResponseObject", "TypeInResponseObject"])
	#["MultiChoice", "TypeIn"]

	"""

	response_content_type_list = [ret_likely_response_mode_for_response_content(ele) for ele in response_content_list]
	
	#response_content_type_abbrev_list = [ele.rstrip("ResponseObject") for ele in response_content_type_list]
	
	# VERY weird that this does not give us TypeIn,	so, let's just give up on that approach
	# and try the following:

	# First, take note of this:
	# len("ResponseObject") => 14
	#
	# and thus do this...

	response_content_type_abbrev_list = [ele[0:-14] for ele in response_content_type_list]

	#print("response_content_type_list:", response_content_type_list)
	print("FLAG: response_content_type_abbrev_list:", response_content_type_abbrev_list)

################################################################	

def log(filepath, text):
	with open(filepath, 'a') as out_fobj:
		print(text, file=out_fobj)
		
def read_json_file(filepath):
	with open(filepath, 'r') as in_obj:
		json_data = json.load(in_obj)
		return(json_data)

def now_yyyy_mm_ddThhmm():
	"""return current time in a filename friendly format"""
	return(dt.datetime.now().strftime("%Y-%m-%dT%H%M"))

def now_yyyy_mm_ddThhmmss():
	"""return current time in a filename friendly format"""
	return(dt.datetime.now().strftime("%Y-%m-%dT%H%M%S"))


#process_system_reply(system_reply_to_quest21_consult_14_ankle_problem_began_last_24_hours)

#question_and_answer_loop({"consultationId": 14})

#question_and_answer_loop(start_conversation_with = "PickUpFromWhereYouLeftOff/consult-14-conv-01-QID-55-surgury-in-past-few-months.json", log_basedir = "../TstCoupProgLogs/")
#question_and_answer_loop(start_conversation_with = "PickUpFromWhereYouLeftOff/consult-14-conv-01-QID-55-surgury-in-past-few-months-female.json", log_basedir = "../TstCoupProgLogs/")

#question_and_answer_loop({"consultationId": 62}, log_basedir = "../TstCoupProgLogs/")


# 2022-05-19T12:56:31PDT trying shortest consult: stress managment
#question_and_answer_loop(155, log_basedir = "../TstCoupProgLogs/")

#question_and_answer_loop(start_conversation_with = "PickUpFromWhereYouLeftOff/consult_62_conv_Q1_QID_1_what_is_your_height.json", log_basedir = "../TstCoupProgLogs/")
# 2022-05-19T13:34:38PDT this dies early on, i forget why/



#question_and_answer_loop(start_conversation_with = "PickUpFromWhereYouLeftOff/consult_62_conv_Q1_QID_1_what_is_your_height_try2.json", log_basedir = "../TstCoupProgLogs/")



#question_and_answer_loop(14, log_basedir = "../TstCoupProgLogs/")

#question_and_answer_loop(62, log_basedir = "../TstCoupProgLogs/")
#question_and_answer_loop(1000, log_basedir = "../TstCoupProgLogs/")

#question_and_answer_loop(3, log_basedir = "../TstCoupProgLogs/")
#question_and_answer_loop(1001, log_basedir = "../TstCoupProgLogs/")
#question_and_answer_loop(1000, log_basedir = "../TstCoupProgLogs/")

#question_and_answer_loop(1003, log_basedir = "../TstCoupProgLogs/")

#question_and_answer_loop(14, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = None, record_user_replies_for_reply_filename = "test_record_14.01.json")

#question_and_answer_loop(14, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "test_record_14.01.json", record_user_replies_for_reply_filename = None)
#question_and_answer_loop(62, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "test_record_14.01.json", record_user_replies_for_reply_filename = None)

#question_and_answer_loop(3, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "test_record_14.01.json", record_user_replies_for_reply_filename = None)
#question_and_answer_loop(4, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "test_record_14.01.json", record_user_replies_for_reply_filename = None)
#question_and_answer_loop(6, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "test_record_14.01.json", record_user_replies_for_reply_filename = None)
#question_and_answer_loop(7, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "test_record_14.01.json", record_user_replies_for_reply_filename = None)

# Cpd-0008.json
# Cpd-0009.json
# Cpd-0011.json
# Cpd-0014.json
# Cpd-0015.json
# Cpd-0016.json

#for db in [8, 9, 11, 14, 15, 15]:
	# oops, repeated 15 caused a problem
#	question_and_answer_loop(db, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "test_record_14.01.json", record_user_replies_for_reply_filename = None)
	#sleep(1.3)
#	sleep(2)

# Cpd-0016.json

def run_patient_sim_script_over_consults(consults_descriptor, patient_sim_script_fpath, log_basedir = "../TstCoupProgLogs/"):


	"""

	@param log_basedir : you can just use the default.  But if you
	have a batch run and you want all the results to live in an
	exclusive dir, then you might say e.g.

	log_basedir = "../TstCoupProgLogs/CONSYS-299"

	"""
	
	list_of_db_numbers = obtain_db_numbers(consults_descriptor)

	if not(os.path.exists(patient_sim_script_fpath)):
		print("Error @param patient_sim_script_fpath points to a file that does not exist.")
		print("Maybe there is a typo in the value you have for @param patient_sim_script_fpath or you forgot to save a file at that location?")
		print("The value of @param patient_sim_script_fpath is:")
		print(patient_sim_script_fpath)
		pdb.set_trace()
	
	if not(os.path.exists(log_basedir)):
		os.mkdir(log_basedir)

	for just_the_db_number in list_of_db_numbers:

		print("################################################################")
		print("################################################################")
		print(f"# Calling question_and_answer_loop on CPD {just_the_db_number} #")
		print("################################################################")
		print("################################################################")

		question_and_answer_loop(just_the_db_number, log_basedir = log_basedir, patient_sim_script_fpath = patient_sim_script_fpath, record_user_replies_for_reply_filename = None)

		#!!! TODO uncomment this, remove the line above (2022-06-03T15:55:49PDT)
		# try:
		# 	question_and_answer_loop(just_the_db_number, log_basedir = log_basedir, patient_sim_script_fpath = patient_sim_script_fpath, record_user_replies_for_reply_filename = None)
		# except Exception as e:
		# 	print("################################################################")
		# 	print("################################################################")
		# 	print(f"# Exception when running CPD {just_the_db_number} #############")
		# 	print("# Exception is")
		# 	print(e)
		# 	print("################################################################")
		# 	print("################################################################")


def obtain_db_numbers(consults_descriptor):
	
	type_of_consult_descriptor = consults_descriptor.get('ConsultDescriptorType') 

	if type_of_consult_descriptor is None:
		print("ERROR: @param consults_descriptor is missing a value for 'ConsultDescriptorType'...")  
		print("...consults_descriptor is the argument to @func run_patient_sim_script_over_consults...")
		print("...it needs to be called with a value for the key 'ConsultDescriptorType'...")
		print("...as of 2022-06-03 its allowed values are 'PlainList', 'GlobExpression'...")
		pdb.set_trace()

	elif type_of_consult_descriptor == 'PlainList':
		list_of_cpd_numbers_to_return = consults_descriptor['ListOfCpdNumbers']

	elif type_of_consult_descriptor == 'EverythingInDir':
		dir_for_consults = consults_descriptor['DirForConsults']
		list_of_cpd_numbers_to_return = obtain_cpd_numbers_from_dir(dir_path)

	elif type_of_consult_descriptor == 'GlobExpression':
		dir_for_consults = consults_descriptor['DirForConsults']
		glob_expr = consults_descriptor['ActualGlobExpr']
		list_of_cpd_numbers_to_return = obtain_cpd_numbers_from_glob_expression(glob_expr, dir_for_consults)
		
	else:
		print("ERROR: @param invalid value for consults_descriptor 'ConsultDescriptorType'...")  
		print("...consults_descriptor is the argument to @func run_patient_sim_script_over_consults...")
		print("...it needs to be called with a value for the key 'ConsultDescriptorType'...")
		print("...as of 2022-06-03 its allowed values are 'PlainList', 'GlobExpression'...")

		pdb.set_trace()

	return(list_of_cpd_numbers_to_return)

def obtain_cpd_numbers_from_dir(dir_path):
	cpd_filename_list = os.listdir(mydir)
	cpd_filename_list.sort()
	return_list_of_cpd_numbers = []
	for cpd_filename in cpd_filename_list:
		with_front_stuff_removed = cpd_filename.lstrip("Cpd-0")
		# e.g. with_front_stuff_removed will be "1.json" if filename is "Cpd-0000000001.json"
		just_the_db_number = with_front_stuff_removed.rstrip(".json")
		just_the_db_number = int(just_the_db_number)
		return_list_of_cpd_numbers.append(just_the_db_number)
	return(return_list_of_cpd_numbers)


def obtain_cpd_numbers_from_glob_expression(glob_expr, dir_for_consults):
	print("Sorry Charlie this has not yet been implemented.")
	pdb.set_trace()

################
# Make output filenames pretty and standardized

def filename_str_for_bot_question(question_seq_index_str, question_id, expected_max_digits = 3):

	question_seq_index_str = add_padding_to_int_str(question_seq_index_str, expected_max_digits)
	question_id		= add_padding_to_int_str(question_id, expected_max_digits)

	return(f"Q{question_seq_index_str}-bot-quest-Id{question_id}.json")

def filename_str_for_user_reply(question_seq_index_str, question_id, expected_max_digits = 3):

	question_seq_index_str  = add_padding_to_int_str(question_seq_index_str, expected_max_digits)
	question_id		= add_padding_to_int_str(question_id, expected_max_digits)

	return(f"Q{question_seq_index_str}-usr-reply-Id{question_id}.json")

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

################

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

#question_and_answer_loop(76, log_basedir = "../TstCoupProgLogs/")
question_and_answer_loop(76, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "../PatientSimulatorScripts/dob_height_weight_then_all_zero_unless_error.json")

#question_and_answer_loop(14, log_basedir = "../TstCoupProgLogs/")

#question_and_answer_loop(101, log_basedir = "../TstCoupProgLogs/")

#question_and_answer_loop(14, log_basedir = "../TstCoupProgLogs/", patient_sim_script_fpath = "../PatientSimulatorScripts/first_try_auto_mode_policy_always_zero.json")

################################################################
# Use this to docttest specific functions, i.e.  Change to the first
# arg of run_docstring_examples

#if __name__ == '__main__':
#    import doctest
##    doctest.testmod()
#    doctest.run_docstring_examples(index_where_multi_choice_options_end, globals())

#print(index_where_multi_choice_options_end(TEST_RESPONSE_CONTENT_LIST_OF_MIXED_TYPE_01))
#print(index_where_multi_choice_options_end(TEST_RESPONSE_CONTENT_LIST_OF_MIXED_TYPE_01))

# handle_mixed_response_content_list(
# 	response_content_list = TEST_RESPONSE_CONTENT_LIST_OF_MIXED_TYPE_01,
# 	resp_section_num = 0,
# 	num_response_sections = 1,
# 	response_header = 'Did you stop taking any medication in the past few weeks?',
# 	user_reply_script_json = [],
# 	record_user_replies_for_reply_filename = None,
# 	findings_to_add = [],
# 	conversation_log_filepath = None,
# 	consult_id = 19,
# 	sys_quest_num_str = "QuesSeq# 23")

def test_process_system_reply_01():
	my_input_json = {'consultationId': 19, 'findings': [{'id': 99, 'keywords': [], 'mmp': None, 'note': None, 'present': True, 'state': 'PRESENT', 'text': None, 'uncertain': False, 'valueObject': {'format': 'DATE', 'formattedValue': {'day': 28, 'hour': 0, 'minute': 0, 'month': 12, 'second': 0, 'type': 'timestamp', 'year': 1988}, 'plural': None, 'string': False, 'value': '12/28/1988', 'valueType': 'DATE', 'valueTypeUnit': None}}, {'id': 41, 'keywords': [], 'mmp': None, 'note': None, 'present': True, 'state': 'PRESENT', 'text': None, 'uncertain': False, 'valueObject': {'format': 'DOUBLE', 'formattedValue': 33.0, 'plural': 'years', 'string': False, 'value': 33.0, 'valueType': 'TIMESPAN', 'valueTypeUnit': 1}}, {'id': 67, 'idForHumans': 'Fnd-null-GenNo-16645-Cpd-19-RecNum-67', 'state': 'PRESENT', 'valueObject': {'format': 'DOUBLE', 'myDisplayForDefaultUnit': 'inches', 'value': '71', 'valueType': 'LENGTH', 'valueTypeUnit': 4}}, {'id': 106, 'idForHumans': 'Fnd-null-GenNo-16647-Cpd-19-RecNum-106', 'state': 'PRESENT', 'valueObject': {'format': 'DOUBLE', 'myDisplayForDefaultUnit': 'pounds', 'value': '171', 'valueType': 'WEIGHT', 'valueTypeUnit': 2}}], 'myNextQuestionId': 23, 'questionId': 49, 'questionIndexSeq': 2}
	#my_input_str = json.dumps(input_json)

	my_question_seq_index = 2
	my_log_dir = "Tests/TestProcessSystemReply_01/"
	my_conversation_log_filepath = os.path.join(my_log_dir, CONVERSATION_FILENAME)
	my_record_user_replies_for_reply_filename = os.path.join(my_log_dir, "this_should_be_empty_i_think.json")
	my_issues_of_note_filepath = os.path.join(my_log_dir, ISSUES_OF_NOTE_FILENAME)

	return_val = process_system_reply(
		#json_input = my_input_str, 
		json_input = my_input_json,
		log_dir = my_log_dir,
		conversation_log_filepath = my_conversation_log_filepath,
		user_reply_script_json = None,
		record_user_replies_for_reply_filename = my_record_user_replies_for_reply_filename,
		issues_of_note_filepath = my_issues_of_note_filepath)

	return(result_val)


# TODO(2022-06-23T23:16:48PDT, ) finish debugging this test!!
#result = test_process_system_reply_01()
#print("################################################################")
#print(" OYE" * 42)
#print("here's the result of test_process_system_reply_01()")
#print(result)
#print("################################################################")