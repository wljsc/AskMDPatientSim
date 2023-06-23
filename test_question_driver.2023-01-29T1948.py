# test_question_driver.py
################################################################
# HOW TO RUN EXAMPLE

# See the bottom of this file for two commented examples of how to run it.

################################################################
# PURPOSE:

# The purpose of this file is to be the 'real code' that tests the
# question driver and point. You could call this the ask MD patient
# simulator because it tries to answer questions send the answer to
# the question driver endpoint and then get the next question.

# You will find some doctest here (see >>> in the """ comments right
# after certain def's).  However, you will not find much in the way of
# real calls to this code base.  To see such calls see the following:

# SEE ALSO: test_question_driver_experiments.py

# As of summer & early fall 2022 the *calls* to this code as it was
# developed and as it was use to find bugs in the question drive
# endpoint, over many test runs can be found in
# test_question_driver_experiments.py

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


# DONE(2022-06-22T11:28:04PDT, 2022-07-02T18:57:49PDT)
# handle_mixed_response_content_list now handles not just truly mixed
# type in and multiple choice, it also handles pure type in (aka
# Branch 1).  This completion is also documented at
# 2022-07-02T18:53:54PDT.  More testing is best however.  As the
# testing is concluding see the needed to be done at
# 2022-07-02T19:01:55PDT

# TODO(2022-07-02T19:04:20PDT, ) Following up on
# 2022-06-22T11:28:04PDT, @func handle_mixed_response_content_list
# should probably take over for all the branches, not just Branch 1.


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

# 2023-01-10T18:36:23PST
# About to modify to support test_end_to_end.py

# test_question_driver.2023-01-03T2211.py

# 2022-12-27T23:08:23MST Thinking about how to enable more flexible
# scripts.  I wanted to have compositional way that I
# would specify the auto mode scripts. E.g. not stuff like...

# sex_dob_height_weight_then_all_zero_unless_error_for_children.json
# sex_dob_height_weight_then_all_zero_unless_error.json
# dob_height_weight_then_all_zero_unless_error.json
# sex_dob_height_weight_then_random_unless_error.json

# ...but instead something like...

# [sex_dob_height_weight,		all_zero_unless_error]
# [sex_dob_height_weight_for_children,	all_zero_unless_error]
# [sex_dob_height_weight,		random_unless_error]
# [sex_dob_height_weight_for_children,	random_unless_error]    
# [dob_height_weight,			all_zero_unless_error]	
# [dob_height_weight, 			all_zero_unless_error]	
# [dob_height_weight, 			random_unless_error]	
# [dob_height_weight, 			random_unless_error]    


# Now, it looks like it's going to be a lot a lot of work to do this
# deep into the code. However a better strategy would be to have a
# compositional name of a script specified in a high-level function
# and only the high level Functions would be able to understand that
# conversational language. And then what they would do is they would
# write out the script in painstaking detail and that script would be
# saved into the log directories and then the low-level code would
# read from that automatically written script.

# test_question_driver.2022-12-27T2233.py

# saving this version - I doubt there were any recent changes but
# right now I am going to start documenting stuff, possibly working up
# to making a new way to have auto mode run.  You could specify a
# sequence of scripts.  But before I do that I need to re-understand the
# code better.

# test_question_driver.2022-12-19T1200.py

# just after the above version
# (test_question_driver.2022-12-19T1200.py) I started supporting this
# kind of functionality.  If there's an error, i.e. if the resposen
# from the bot has an error_msg in it (not really a throwing exception
# kind of thing) then IF WE ARE IN SCALE UP MODE, then we want to keep
# moving.  Do not insist on receiving input from the user.  Instead,
# raise an exception.  Use that error_msg (maybe with some extra
# dressing, like 'The bot responded and the response contained the
# following error message: {error_message}"....Yes use that possibly
# sklgithly dressed up error_msg and pass that as the error text in
# the exception.  That way the exception will be caught like other
# more "hard" exceptions that get thrown when the bot is called.
# I.e. they will get saved to that Error. file.

# so, the plan is like this:

# 1) add an optional error_msg text arg to the wrapper function, it
# defaults to None but is set when there's an error message.

# 2) add an arg to question_and_answer loop that says whether or not
# you want human to intervene if there's an error.  or, hrm, maybe
# not.  maybe i should have new policy.  keep
# AnswerZero-UnlessBotError the way it is.  but a new policy called
# e.g. AnswerZero-ButIfErrorLogAndContinue
# 

# test_question_driver.2022-12-13T2220.py

# test_question_driver.2022-12-07T1228.py

# test_question_driver.2022-11-15T1928.py

# 2022-11-08T20:05:04PST Changing from timestamp_in_log_dir_p to
# timestamp_in_log_dir


# test_question_driver.2022-11-08T2001.py this vesion to show that
# there's been no change between
# test_question_driver.2022-11-08T2001.py and
# test_question_driver.2022-10-24T1151.py

# test_question_driver.2022-10-24T1151.py
# saving this version as of 2022-11-08T20:01:02PST


# test_question_driver.2022-09-18T2320.py 
#
# Weeks later, i.e. as of 2022-10-09T12:16:45PDT, this
# test_question_driver.2022-09-18T2320.py was the latest version of
# the file.  Thus development on this file took a hiatus at that point.

# Update2022-09-17 this is a tag used to name updates that were
# started on 2022-09-17 but not nec copmleted on that date!!  These
# updates were done bc I needed to start re-runnig this code (to test
# the question driver endpoint) becuase I had let it lie for maybe 1
# to 2 months while I worked on the findin gproxy gtester.

# 2022-09-17T17:21:30PDT lots of moves
# - moved process_system_reply to test_question_driver_process_system_reply.py
# - moving much more. not worth explaining.

# 2022-09-17T13:32:54PDT test_question_driver.v24.py

# just starting to pull def of process_system_reply.py
# out and into here:
# test_question_driver_process_system_reply.py

# 2022-07-18T1632 test_question_driver.v23.py

# Much later (at 2022-09-16T09:26:15PDT) I am finally coming back to
# this (after focused work on test_finding_proxies.py and
# test_finding_proxies_experiments.py).  Thus, now (i.e. at the
# aforementioned 2022-09-16T09:26:15PDT) I saved the latest version of
# this file (as test_question_driver.v23.py).

# 2022-07-07T11:03:27PD Ttest_question_driver.v22.py

# we are part way through implementing
# RandomAnswerForMultiChoice-UnlessBotError there is a bug.  I am
# saving this version bc I want to refactor, in particular change the
# new @param number_of_choices of @func user_input_wrapper to actually
# be the choices for better localizing the implementaiton of
# RandomAnswerForMultiChoice-UnlessBotError into user_input_wrapper

# 2022-07-07T07:00:38PDT test_question_driver.v21.py

# Have made heavy use with perhaps not many code changes since prior
# version.

# In next version will start allowing for a new policy to answer randomly.

# 2022-07-02T18:53:54PDT test_question_driver.v20.py
#
# I believe I've recently finished merging
# Branch 1 (TypeIn only)
# into
# Branch 5 (Mixed - Multiple Choice and Give a type-in value for each response ele)
# I have not fully tested across all consutls
# It was a fairly big refactor.
#

# Because of this I have converted a TO DO whose creation time was
# 2022-06-22T11:28:04PDT to done, at 2022-07-02T18:57:49PDT.  As a a
# followon task @func handle_mixed_response_content_list should
# probably take over for all the branches and this is given a to do
# with creation time of 2022-07-02T19:04:20PDT

# 2022-07-02T08:57:30PDT test_question_driver.v19.py just starting a
# major change in which we split findings_to_add into several 'sub
# variables'. test_question_driver.v19.py is the version to go to if
# the major change is a bust.
#
# The major change is called Refactor2022-07-02T08:53:21PDT (see
# occurrences below)

# 2022-07-01T11:53:34PDT test_question_driver.v18.py ab out to make
# TypeIn be managed by what is currently called # "Big Branch 5: Mixed
# - Multiple Choice and Give a type-in value for each response ele"
# see 2022-07-01T11:45:28PDT

# 2022-06-24T15:22:59PDT test_question_driver.v17.py

# saving v17 bc we are just about to delete a lot of the history of
# experiments.  See the newly created test_question_driver_experiments.py

# Fixed 2022-06-24T13:51:24PDT the
# UnboundLocalError: local variable 'user_reply_txt' referenced before
# assignment
#
# When running this..
#question_and_answer_loop(19, log_basedir =
# "../TstCoupProgLogs/", patient_sim_script_fpath =
# "../PatientSimulatorScripts/dob_height_weight_then_all_zero_unless_error.json")

# 2022-06-24T07:31:43PDT MILESTONE auto mode has discovered its first
# real problem and prompted the need for a new resposne policy,
# i.e. "AnswerZero-UnlessBotError"

# ~ 2022-06-23 started supporting output to ISSUES_OF_NOTE_FILENAME .

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
import time
import random
import pdb

import utils
import config

from test_question_driver_process_system_reply import process_system_reply

################################################################
# Constants used to be defined here 

RUN_DURATION_LOG_FILENAME = "run_duration_log.tsv"
DURATION_LOG_SEP = "\t"

from constants import TRYING_TO_MIMIC_RegressionTestLogs2_P
from constants import MultipleChoice
from constants import Mixed_TypeInAndMultipleChoice
from constants import TypeIn
from constants import UserChoiceWasNoneOfTheAbove
from constants import MultiChoiceResponseObject
from constants import TypeInResponseObject
from constants import STEP_SLOWLY_P
from constants import STEP_SLOWLY_2
from constants import DIR_OF_CPD_FILES
from constants import CONVERSATION_FILENAME
from constants import ISSUES_OF_NOTE_FILENAME
from constants import TEST_RESPONSE_CONTENT_LIST_OF_MIXED_TYPE_01
from constants import TargetResultForStartConsult14
from constants import ASK_OPERATOR_HOW_TO_HANDLE_BOT_ERROR_STR
from constants import DEFAULT_SLEEP_DURATION_TO_MITIGATE_MAX_RETRIES_ERROR

################################################################

def question_and_answer_loop(
	start_conversation_with,
	log_basedir = None,
	patient_sim_script_fpath = None,
	record_user_replies_for_reply_filename = None,
	timestamp_in_log_dir = True,
	if_reply_script_UnlessError_means_LogAndContinue = False,
	ret_bot_reply_out_fpath_p = False,
	sleep_duration = DEFAULT_SLEEP_DURATION_TO_MITIGATE_MAX_RETRIES_ERROR):

	"""

	@param start_conversation_with should be json that sets the state
	for the users reply.  

	If you want to start at the very beginning of consult, then if
	the consult number is CONSULT_NUMBER then
	start_conversation_with simply be CONSULT_NUMBER.

	For example, if you want to start from the beginning of CPD 4,
	then call this function with:
	
		start_conversation_with = 4

	Else, you probably want to give it a 'set of answers from
	partway through a consult'.  Do this by passing in a filepath
	such that the filepath contains the json that encodes the 'set
	of answers from partway through a consult'.

	@param patient_sim_script_fpath if None, just operates as
	normal, or 'manual' mode.  I.e. the operator of this simulator
	gives answers to each question from the AskMD bot when prompted.

	For AUTO-MODE AUTO mode AutoMode, Automatic Mode (a.k.a REPLAY mode)
	then @param patient_sim_script_fpath needs to point to a json
	file.  This file specifies for each user turn, what should be
	the response.

	DO YOU WANT TO LOG THE RUN?

	@param log_basedir

	If this is None, there should be no logs.

	If not None, then @param log_basedir must be a dir path.  A directory
	dedicated to the logging of *this* run will be created.

	Here is how the name of that directory will be decided:

	If @timestamp_in_log_dir is False, then the name of
	said logging directory will *not* have the timestamp.  That
	is, it will just be...
	
	Consult-Cpd-{consultation_id}

	If @timestamp_in_log_dir is True, then the name of said
	logging directory will a timestamp which is the time the
	program is called.  Specifically, the name of that directory
	will be

	Consult.{now_yyyy_mm_ddThhmm()}-Cpd-{consultation_id}

	Else if @timestamp_in_log_dir does not equal True or False, is
	assumed to be a string and it will be used as a substring in
	the name of that directory.  I.e. the directory will be called

	Consult.{timestamp_in_log_dir}-Cpd-{consultation_id}


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

	@param if_reply_script_UnlessError_means_LogAndContinue this
	absurdly named param says IF you are using a reply script (aka
	"auto mode") and you are in a situation where the bot returns
	a message saying something like 'i had some kind of error
	happen' THEN do not halt auto mode for a human to inspect.
	No, march on.  Save stuff the same way you would if a hard
	exception would be thrown.  This is really to be used for
	scaling up stuff, i.e. see test_question_driver_scale_up.py

	@param sleep_duration this is how long it will sleep before
	and after posting to the endpoint.  The reason this was added
	circa early Jan 2023 was to try to minimize how often we were
	getting the 'Max retries exceeded with url:
	/consultation/next' error.


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
		
	consultation_id = str(initiate_conversation_json['consultationId'])
	# i bet this is the problem xxx
	# 2022-11-15T22:27:48PST pernicious bug from late night work - try getting rid of the str 

	print("################################################################")
	#print(f"##### Starting Dialog: Consult {initiate_conversation_json['consultationId']} ######")
	print(f"##### Starting Dialog: Consult {consultation_id} ######")
	print("################################################################")
	print(f"#### Current Time at Dialog Start Is: {now_yyyy_mm_ddThhmm()}")

	users_reply = json.dumps(initiate_conversation_json)
	
	# if log_basedir is not None:
	# 	if timestamp_in_log_dir == True:
	# 		sub_dir_for_this_run = f"Consult.{now_yyyy_mm_ddThhmm()}-Cpd-{consultation_id}"
	# 	elif timestamp_in_log_dir == False:
	# 		sub_dir_for_this_run = f"Consult-Cpd-{consultation_id}"
	# 	else:
	# 		sub_dir_for_this_run = f"Consult.{timestamp_in_log_dir}-Cpd-{consultation_id}"

	if log_basedir is not None:
		sub_dir_for_this_run = sub_dir_name_for_consult_test_run(timestamp_in_log_dir, consultation_id)
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

		log_of_post_durations_filepath = os.path.join(log_dir, RUN_DURATION_LOG_FILENAME)
		log_of_post_durations_fileobj = open(log_of_post_durations_filepath, 'w')
		column_headers = ["consultation_id", "question_id", "duration_secs", "start_time_legible", "end_time_legible"]
		column_headers_str = f"{DURATION_LOG_SEP}".join(column_headers)
		print(column_headers_str, file=log_of_post_durations_fileobj)


	else: 
		conversation_log_filepath = None
		issues_of_note_filepath = None
		log_of_post_durations_fileobj = None

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
		
		bot_output_json, question_seq_index = post_users_reply(users_reply, 
			log_dir, 
			question_index_seq, 
			conversation_log_filepath, 
			log_of_post_durations_fileobj,
			ret_bot_reply_out_fpath_p,
			sleep_duration = sleep_duration)

		users_reply_json = json.loads(users_reply)
		
		error_msg = bot_output_json.get('error')
		
		if error_msg:

			print()
			print("Ugh, we posted @param payload (i.e. json representation of user response and finding list) and the bot is returning an error!!!")
			print("you might want to look at the value of @param payload to see if something was formatted in an obviously bad way")
			print()
			print("Here is the error msg:")

			#question_id = users_reply_json['questionId']
			# 2022-11-15T22:29:54PST commented out the above and put the below maybe 30 min ago
			question_id = users_reply_json.get('questionId', "NoQuestionIdSpecified")
			# 2022-11-15T22:29:54PST RE pernicious bug from late night work - how could i have gotten so far 
			# runngin this for weeks and weeks and only now being required to put the get
			if config.CONVERSATION_INVARIANT_MODE_P:
				sys_quest_num_str = f"QuesSeq# {question_seq_index}"
			else:
				sys_quest_num_str = f"QuesSeq# {question_seq_index} QuesID# {question_id}"
				
			#string_to_log_and_print = f"BotReplies with Error to {sys_quest_num_str}\nBotError JSON is:\n{error_msg}\n"
			# 2023-01-23T07:37:20PST change from the above to the below to ease grabbing the error msg
			string_to_log_and_print = f"BotReplies with Error to {sys_quest_num_str}\nBotError JSON is: {error_msg.strip()}\n"
			
			utils.log(conversation_log_filepath, string_to_log_and_print)

			if issues_of_note_filepath:
				with open(issues_of_note_filepath, 'a') as issues_of_note_fobj:
					print("################################################################", file=issues_of_note_fobj)
					print(file=issues_of_note_fobj)
					print(sys_quest_num_str, file=issues_of_note_fobj)
					print(string_to_log_and_print, file=issues_of_note_fobj)
					print(file=issues_of_note_fobj)
					print("################################################################", file=issues_of_note_fobj)


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
				#print("We are now going to trace.  (Caution: I added this trace at 2022-10-24T11:50:48PDT long after main development on this code base.  It is possible (though more or less unlikely) that trace is *not* the right thing to do here)")
				#pdb.set_trace()		
				# 2022-12-04T22:48:55PST I got rid of the trace bc a trace will hold up a massive test run
				# Nowadays, when there is a problem like this, we just want to blow past it but thrown 
				# an exception so that a human can look a the test log and know to diagnos this one.
				raise Exception(f"""There is no next question.  Here is the value of users_reply_json:
				
				{json.dumps(users_reply_json, indent=4, sort_keys=True)}
				
				""")
			else:				
				options = ["skip to next question"] + options

			options_listing = ""
			for nth, option_txt in enumerate(options):
				options_listing += f"\n{nth}: {option_txt}"

			print("Would you like to:", options_listing)
			#user_reply_text = user_input_wrapper("Type In Your Choice Here: ")

			# There has been an error, we are seeking
			# input from the user about what to do.  If we
			# are in auto-mode, then the
			# user_reply_script_json should tell us what
			# to do.
			
			user_reply_text = utils.user_input_wrapper(
				"Type In Your Choice Here: ",
				user_reply_script_json,
				record_user_replies_for_reply_filename,
				asking_how_to_handle_bot_error_p = True,
				choices = options,
				error_msg = error_msg,
				if_reply_script_UnlessError_means_LogAndContinue = if_reply_script_UnlessError_means_LogAndContinue)


			user_reply_int = int(user_reply_text)
			choice_txt = options[user_reply_int]

			string_to_log_and_print = f"UserReply to BotError for {sys_quest_num_str} is: '{choice_txt}'\n"
			print(string_to_log_and_print)
			utils.log(conversation_log_filepath, string_to_log_and_print)
			
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

	if log_of_post_durations_fileobj:
		log_of_post_durations_fileobj.close()

	return(bot_output_json, question_index_seq)




# 2022-05-24T11:25:18PDT looking for question_id

def post_users_reply(payload,
	log_dir,
	question_seq_index,
	conversation_log_filepath,
	log_of_post_durations_fileobj,
	ret_bot_reply_out_fpath_p = False,
	sleep_duration = None):

	# CAUTION: this might wanna be merged or partially merged with
	# the post function in @file test_finding_proxies.py

	# 2022-05-16T11:26:00PDT prolly delete question_seq_index are all things with this timestamp

	""" 

	We post a payload which is, I *think* a json formatted string
	that contains the user reply.  This function that returns what
	the bot 'says' in response, and a couple of other details.
	# 2022-06-10T18:16:17PDT renaming result_json to bot_output_json

	@return bot_output_json, question_seq_index

	@return param bot_output_json - what the bot says in response to the user's reply.

	@param log_of_post_durations_fileobj is an output fileobject.
	It is where the duration of each post is stored so that we can
	analyze latency.

	@param ret_bot_reply_out_fpath_p: 

	Short for 'return bot's reply output filepath'

	Default false.  If true, this func (i.e. @func
	post_users_reply), we return not 2 (per usual) but 3 values.
	The third value will be @param bot_reply_out_fpath.  

	This optional return value was added late in the game to
	support @file test_end_to_end.py.  So it (test_end_to_end.py)
	wants to set this param to True, and legacy code doesn't know
	about it so it will be False, i.e. the default, for them....In
	other words they will receive just two return values.
	
	# TODO(2022-06-22T19:46:18PDT, ) Work on this later
	#>>> bot_output_json = post_users_reply('{"consultationId": 14 }', log_dir = None, question_seq_index = 0, conversation_log_filepath = None)
	#>>> bot_output_json == (TargetResultForStartConsult14, 1)
	#True

	# If there is a diff, try this:
	# >>> the_diff = DeepDiff(result, Result_from_start_Consult14)
	# >>> the_diff_pretty = json.dumps(the_diff, indent=4, sort_keys=True)
	# >>> print(the_diff_pretty)

	@param sleep_duration see arg sig for this functions caller,
	i.e. @func question_and_answer_loop

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
	consultation_id = payload_as_dict['consultationId']

	print(f"#### Payload for User Answer to Ques QuesSeq# {question_seq_index} QuesID# {question_id}")
	print("#### Payload (start of json object) ####")
	print()
	print(json.dumps(payload_as_dict, indent = 4, sort_keys = True))
	print()	
	print("#### Payload (end of json object) ####")

	print()

	#url = 'https://api.dev.sharecare.com/consultation/next'
	#
	# ... 2022-06-22T13:10:33PDT dev is dead, long live qa...
	#
	#url = 'https://api.qa.sharecare.com/consultation/next'
	#
	# 2022-12-06T22:09:16PST about time I replace the above with
	# the below!!!!
	#
	url = config.QUESTION_DRIVER_ENDPOINT
	
	headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}


	MAX_RETRIES_EXCEEDED_WITH_URL_STR =  f"For sleep {sleep_duration} seconds - hoping to easily prevent 'Max_retries_exceeded_with_url' error"
	
	# NOTE in trace the real error looks like...
	#
	#	'Max retries exceeded with url'
	# ...not...
	#
	#	'Max_retries_exceeded_with_url'
	#
	# ...as per the immediately above code.
	# At 2023-01-17T21:15:43PST we added the _'s to allow finding true errors via grep-like string search


	if sleep_duration and sleep_duration > 0:
		print(f"Just Before Post:", MAX_RETRIES_EXCEEDED_WITH_URL_STR)
		time.sleep(sleep_duration)
	
	if log_of_post_durations_fileobj:
		start_time_legible = utils.now_yyyy_mm_ddThhmmss(utc_offset_p = True)
		start_time = time.time()
	
	post_response = requests.post(url, data=payload, headers=headers)

	#print("2022-11-15T21:57:05PST think it has s.t. to do w coerce to string")
	#pdb.set_trace()

	if log_of_post_durations_fileobj:
		end_time = time.time()
		end_time_legible = utils.now_yyyy_mm_ddThhmmss(utc_offset_p = True)
		duration_secs = str(end_time - start_time)
		values = [str(consultation_id), str(question_id), duration_secs, start_time_legible, end_time_legible]
		#values = [consultation_id, question_id, duration_secs, start_time_legible, start_time_legible]
		row_of_data_as_str = f"{DURATION_LOG_SEP}".join(values)

		# chop of the superfluous last tab or comma 
		row_of_data_as_str = row_of_data_as_str.rstrip(DURATION_LOG_SEP)
		print(row_of_data_as_str, file=log_of_post_durations_fileobj)


	if sleep_duration and sleep_duration > 0:
		print(f"Just After Post:", MAX_RETRIES_EXCEEDED_WITH_URL_STR)
		time.sleep(sleep_duration)

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

		# print("TODO this trace is a reminder to put in a test to make sure <to be filled in> is always the status")
		# print("so that we can characterize the range and frequencies of the various statuses we'll get")
		# pdb.set_trace()

		# At 2022-11-08T20:49:50PST I commented out the above
		# trace message.  Why?  Well, I really need to scale
		# and hanging here and there will not let me continue
		# on if a trace is entered.  Sure, I'd like to follow
		# what it's asking me TODO.  But I'm not sure what it
		# is really asking and under one interpretation of
		# what it is asking the task is done (i.e. that inter
		# being, what we already check that as follows:
		# post_response.status_code not in [200, 500]:

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
f"""################################################################
Dag Nabit! We are getting an error.  Here it is:

{error_msg}

################################################################
Here is the payload that was posted to the bot that resulted in the error:

{payload}

################################################################"""


		print(error_report_string)
		
		if log_dir is not None:
		
			out_filename = utils.filename_str_for_bot_question(question_seq_index_str, question_id)
			
			out_fpath = os.path.join(log_dir, out_filename)
			with open(out_fpath, 'w') as out_obj:
				print(error_report_string, file=out_obj)

			# What to say in the CONVERSATION_FILENAME file
			if config.CONVERSATION_INVARIANT_MODE_P:
				sys_quest_num_str = f"QuesSeq# {question_seq_index}"			
			else:
				sys_quest_num_str = f"QuesSeq# {question_seq_index} QuesID# {question_id}"
			string_to_log_and_print = f"{sys_quest_num_str} ResponseHeader: BotError"
			print(string_to_log_and_print)
			utils.log(conversation_log_filepath, string_to_log_and_print)

		
	# TODO(2022-05-20T19:36:11PDT, ) if exiting this fnwith error, maybe log that fact?"

	print("################")

	if config.CONVERSATION_INVARIANT_MODE_P:
		sys_quest_num_str = f"QuesSeq# {question_seq_index} (ConsultID {payload_as_dict['consultationId']})"
	else:
		sys_quest_num_str = f"QuesSeq# {question_seq_index} QuesID# {question_id} (ConsultID {payload_as_dict['consultationId']})"

	print(f"Bot Response is {sys_quest_num_str}")

	print("Bot JSON Response To Users Post (start of section)")

	print()
	pretty_bot_output_json_str = json.dumps(bot_output_json, indent=4, sort_keys=True)
	print(pretty_bot_output_json_str)
	print()

	print("Bot JSON Response To Users Post (end of section)")
	print("################")
		
	if log_dir is not None:
		if error_msg:

			# TODO(2022-06-01T22:13:10PDT, ) does the
			# error get logged like other stuff?  i am
			# pretty sure the nag is no longer needed, it
			# already logs the error - soewhere else,
			# right?
			
			pass

		else:

			question_seq_index = bot_output_json['questionIndexSeq']
			
			question_id = bot_output_json.get('questionId', "NO_QUES_ID_BC_NO_MORE_QUESTIONS")

			# TODO (2022-12-13T22:17:11PST, )
			# NO_QUES_ID_BC_NO_MORE_QUESTIONS should be
			# replaced with a constant by the name
			# NO_QUES_ID_BC_NO_MORE_QUESTIONS and that
			# constant should be defined in config.  See
			# also 2022-12-13T22:18:27PST in
			# test_guidance_options.py
	
			if question_seq_index > 10:
				question_seq_index_str = "0" + str(question_seq_index)
			else:
				question_seq_index_str = str(question_seq_index)

			out_filename = utils.filename_str_for_bot_question(question_seq_index_str, question_id)
			
			bot_reply_out_fpath = os.path.join(log_dir, out_filename)
			with open(bot_reply_out_fpath, 'w') as out_obj:
				print(pretty_bot_output_json_str, file=out_obj)

	#### return from post_users_reply
	if ret_bot_reply_out_fpath_p:
		return(bot_output_json, question_seq_index, bot_reply_out_fpath)
	else:
		return(bot_output_json, question_seq_index)
	#### return from post_users_reply


# print("################################################################")
# print('################ {"consultationId": 14 } ################')
# print(json.dumps(post_users_reply('{"consultationId": 14 }'), indent=4, sort_keys=True))

# Comment This Out - some error
# answer_to_quest21_consult_14_How_long_ago_did_your_foot_or_ankle_problem_begin = \
# {
#     "myquestionId": "question-21-consultation-14-How long ago did your foot or ankle problem begin",
#     "questionId": "21",
#     "consultationId": 14,
#     "findings": [
#         {
#             "id": 18,
#             "valueObject": {
#                 "value": "71",
#                 "valueType": "LENGTH",
#                 "valueTypeUnit": 4,
#                 "format": "INT"
#             },
#             "state": "PRESENT"
#         },
#         {
#             "id": 12,
#             "valueObject": {
#                 "value": "205",
#                 "valueType": "WEIGHT",
#                 "valueTypeUnit": 2,
#                 "format": "INT"
#             },
#             "state": "PRESENT"
#         },
#         {
#             "id": 184,
#             "myfindingId": "male-finding-184",
#             "state": "PRESENT"
#         },
#         {
#             "id": 181,
#             "myfindingId": "date-of-birth-finding-181",
#             "valueObject": {
#                 "value": "12/29/1988",
#                 "valueType": "DATE",
#                 "format": "DATE"
#             },
#             "state": "PRESENT"
#         },
#         {
#             "id": "27",
#             "myFindingId": "past 24 hours finding-27-consultation-14",
#             "state": "PRESENT"
#         }
#     ]
# }



answer_to_quest21_consult_14_How_long_ago_did_your_foot_or_ankle_problem_begin = \
'{"questionId": 21, "consultationId": 14}'

# print('################################################################')
# print('################ System Reply To: How long ago did your foot or ankle problem begin ################')

# print(json.dumps(post_users_reply(answer_to_quest21_consult_14_How_long_ago_did_your_foot_or_ankle_problem_begin), indent=4, sort_keys=True))

# system_reply_to_quest21_consult_14_ankle_problem_began_last_24_hours = post_users_reply(answer_to_quest21_consult_14_How_long_ago_did_your_foot_or_ankle_problem_begin)

CONSTRUCT_FINDING_VALUE_OBJECT_DE_NOVO_P = False

################################################################
# 2022-09-17T13:37:49PDT the definiton of process_system_reply was
# removed from here and placed in
# test_question_driver_process_system_reply.py as part of
# Update2022-09-17

################################################################

# 2022-09-17T17:31:00PDT moved handle_mixed_response_content_list to
# test_question_driver_process_system_reply.py

################################################################

# 2022-09-18T23:20:09PDT moved
# solicit_user_ans_to_the_multiple_choice_question to
# test_question_driver_process_system_reply.py

################################################################

# 2022-09-17T17:25:40PDT moved index_where_multi_choice_options_end
# and it's _internal subroutine totest_question_driver_process_system_reply.py

################################################################

# 2022-09-17T21:20:05PDT moved
# ret_likely_response_mode_for_response_content to
# test_question_driver_process_system_reply.py

################################################################

# 2022-09-17T21:25:04PDT moved convert_user_type_in_val_to_finding to test_question_driver_process_system_reply.py

################################################################

# Can prolly comment this out
# def skip_to_next_question_bc_of_error_p(bot_reply):
# 	if (bot_reply.get('re_write_this_post_as_next_question')):
# 		return(True)
# 	else:
# 		return(False)	

def skip_to_next_question(user_input_json, my_next_question_id):

# skip_to_next_quesiton is a misnomer.  It really skips two questions.
# see
# [[file:~/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/diary-TestCoupletPrograms.org::Link-2022-05-25-Wed-22-36][this]]
# for the full explanation.  TODO we can probably do a real skip this question.

	"""This function is intended to be used if the bot has errored
	out and we want to somehow skip over the question that caused
	the bot to error out.  So, takes the original user_input which
	says it as a reply to question number N and makes it tell a
	lie.  It makes it say I am not for question number N, I am for
	question number N+1.  In this way it convinces the bot to skip
	to the next question.  user_input has to have the special
	'myNextQuestionId' added to it before being called so that it
	knows that record number of then nth +1 question.

	This function should not be called if there is no next
	question bc code inside the caller should prevent that from
	happening.

	"""

	user_input_json['questionId'] = user_input_json['myNextQuestionId']
	user_input_json['myNextQuestionId'] = "There is no next Question Id bc we've already skip / advanced to the next question!!!"
	user_response_str = json.dumps(user_input_json)

	return(user_response_str)

# 2022-10-22T11:57:01PDT Commented this out bc it is not used anywhere!
# def exit_if_no_more_questions(bot_reply):
# 	if bot_reply['questionId'] is None:
# 		if len(bot_reply['responseSections']) == 0:
# 			print("################################################################")
# 			print("# Congratulations, you answered the last question, we're done. #")
# 			print("################################################################")
# 			exit()
# 		else:
# 			print("################################################################")
# 			print("# Odd, reponseSections is the empty list, but questionId is None #")
# 			print("################################################################")
# 			print("Entering debugger so you can diagnose.")
# 			pdb.set_trace()
# 	if len(bot_reply['responseSections']) == 0:
# 		print("################################################################")
# 		print("# Odd, reponseSections is the empty list yet questionId is not None #")
# 		print("################################################################")
# 		print("Entering debugger so you can diagnose.")
# 		pdb.set_trace()
# 	else:
# 		return()

################################################################

# 2022-09-17T17:24:18PDT moved auto_mode_reply_txt_for_rnd_ans_case_01
# from here to utils.py

################################################################

# 2022-09-17T17:28:32PDT moved user_input_wrapper to utils.

################################################################

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

################################################################

# 2022-09-18T23:17:08PDT detect_type_in_vs_multi_choice_anomaly moved from here to test_question_driver_process_system_reply.py

################################################################	

# 2022-09-17T17:22:51PDT pretty_print_response_content_type_list was moved from here to test_question_driver_process_system_reply.py 

################################################################

def sub_dir_name_for_consult_test_run(timestamp_in_log_dir, consultation_id):
	if timestamp_in_log_dir == True:
		sub_dir_for_this_run = f"Consult.{now_yyyy_mm_ddThhmm()}-Cpd-{consultation_id}"
	elif timestamp_in_log_dir == False:
		sub_dir_for_this_run = f"Consult-Cpd-{consultation_id}"
	else:
		sub_dir_for_this_run = f"Consult.{timestamp_in_log_dir}-Cpd-{consultation_id}"
	return(sub_dir_for_this_run)

################################################################

def read_json_file(filepath):
	with open(filepath, 'r') as in_obj:
		json_data = json.load(in_obj)
		return(json_data)

def now_yyyy_mm_ddThhmm():
	"""return current time in a filename friendly format"""
	return(dt.datetime.now().strftime("%Y-%m-%dT%H%M"))

# TODO(2022-07-12T23:36:18PDT, ) WARNING there is a copy of @fun
# now_yyyy_mm_ddThhmmss() utils.py.  All these time utiliities shoudl
#  be moved there.

# def now_yyyy_mm_ddThhmmss():
# 	"""return current time in a filename friendly format"""
# 	return(dt.datetime.now().strftime("%Y-%m-%dT%H%M%S"))


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
	#time.sleep(1.3)
#	time.sleep(2)

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

		#TODO uncomment this, remove the line above (2022-06-03T15:55:49PDT)
		# 2022-07-02T10:23:44PDT on second thoughts, at the present stage of dev, I like it to completely stop when there is an error
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

################################################################

# 2022-09-17T17:32:34PDT moved 
# filename_str_for_bot_question
# filename_str_for_user_reply
# to utils.
################################################################

################
# 
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
# as of 2023-01-29T19:18:03PST it looks like this fn test_process_system_reply_01 is not called anywhere.
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

################################################################
# example call:
# question_and_answer_loop(
# 	start_conversation_with = 4,
# 	log_basedir = os.path.join(config.LOG_DIR_GENERIC, "QuestionDriverTests"),
# 	patient_sim_script_fpath = None,
# 	record_user_replies_for_reply_filename = "../PatientSimulatorScripts/cpd-4-first-try.json",
# 	timestamp_in_log_dir = True)

# question_and_answer_loop(
# 	start_conversation_with = 19,
# 	log_basedir = os.path.join(config.LOG_DIR_GENERIC, "QuestionDriverTests"),
# 	patient_sim_script_fpath = None,
# 	record_user_replies_for_reply_filename = "../PatientSimulatorScripts/cpd-19-first-try.json",
# 	timestamp_in_log_dir = True)

# 2022-12-06T22:29:41PST realized 182 needs sex first not dob first
# question_and_answer_loop(
# 	start_conversation_with = 182,
# 	log_basedir = os.path.join(config.LOG_DIR_GENERIC, "QuestionDriverTests"),
# 	#patient_sim_script_fpath = "../PatientSimulatorScripts/dob_height_weight_then_all_zero_unless_error.json",
# 	#patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_random_unless_error.json",
# 	#patient_sim_script_fpath = None,
# 	#record_user_replies_for_reply_filename = "../PatientSimulatorScripts/cpd-189-why-did-it-fail-in-scale-up.json",
# 	patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json",
# 	timestamp_in_log_dir = True)

# 2022-12-06T22:40:34PST realized 89 needs dob frist not sex first

# question_and_answer_loop(
# 	start_conversation_with = 89,
# 	log_basedir = os.path.join(config.LOG_DIR_GENERIC, "QuestionDriverTests"),
# 	#patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json",
# 	#record_user_replies_for_reply_filename = "../PatientSimulatorScripts/cpd-89-why-did-it-fail-in-scale-up.json",
# 	patient_sim_script_fpath = "../PatientSimulatorScripts/dob_height_weight_then_all_zero_unless_error.json",
# 	timestamp_in_log_dir = True)

# question_and_answer_loop(
# 	start_conversation_with = 183,
# 	log_basedir = os.path.join(config.LOG_DIR_GENERIC, "QuestionDriverTests"),
# 	#patient_sim_script_fpath = "../PatientSimulatorScripts/dob_height_weight_then_all_zero_unless_error.json",
# 	patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json",
# 	timestamp_in_log_dir = True)


# question_and_answer_loop(
# 	start_conversation_with = 308,
# 	log_basedir = os.path.join(config.LOG_DIR_GENERIC, "QuestionDriverTests"),
# 	patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error_for_children.json",
# 	timestamp_in_log_dir = True)

# question_and_answer_loop(
# 	start_conversation_with = 308,
# 	log_basedir = os.path.join(config.LOG_DIR_GENERIC, "QuestionDriverTests"),
# 	patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error_for_children.json",>
# 	timestamp_in_log_dir = True)

################################################################
# 2022-12-19T10:18:10PST diagnosing...
#
# invalid literal for int() with base 10: '12/5/1999'
#
# which occured in scale up testing of this
# 2022-12-14T093642.BirthSexFirst_Height_Weight_AllZeroUnlessError_NeedingAttention/Error.Consult.2022-12-14T093649-Cpd-26.txt

# question_and_answer_loop(
# 	start_conversation_with = 26,
# 	log_basedir = os.path.join(config.LOG_DIR_GENERIC, "QuestionDriverTests"),
#  	patient_sim_script_fpath = "../PatientSimulatorScripts/dob_height_weight_then_all_zero_unless_error.json",
# 	timestamp_in_log_dir = True)

# 2022-12-19T10:31:35PST moved 26 to using the correct script, i.e. dob_height_weight_then_all_zero_unless_error.json.
# as proven by the immediately above which was successful

# question_and_answer_loop(
# 	start_conversation_with = 62,
# 	log_basedir = os.path.join(config.LOG_DIR_GENERIC, "QuestionDriverTests"),
#  	patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json",
# 	timestamp_in_log_dir = True)

################################################################
# Scale up test shows

# invalid literal for int() with base 10: '12/5/1999'
# if we use sex_dob_height_weight_then_all_zero_unless_error.json

# question_and_answer_loop(
# 	start_conversation_with = 189,
# 	log_basedir = os.path.join(config.LOG_DIR_GENERIC, "QuestionDriverTests"),
# 	patient_sim_script_fpath = "../PatientSimulatorScripts/dob_height_weight_then_all_zero_unless_error.json",
# 	timestamp_in_log_dir = True)


# question_and_answer_loop(
# 	start_conversation_with = 6,
# 	log_basedir = os.path.join(config.LOG_DIR_GENERIC, "QuestionDriverTests"),
# 	patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json",
# 	timestamp_in_log_dir = True)

# 2022-12-19T11:06:33PST diagnosis, it needs a blood pressure, thus, make a new script, i.e. sex_dob_height_weight_blood_pressure_then_all_zero_unless_error.json

# question_and_answer_loop(
# 	start_conversation_with = 6,
# 	log_basedir = os.path.join(config.LOG_DIR_GENERIC, "QuestionDriverTests"),
# 	patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_blood_pressure_then_all_zero_unless_error.json",
# 	timestamp_in_log_dir = True)

# question_and_answer_loop(
# 	start_conversation_with = 7,
# 	log_basedir = os.path.join(config.LOG_DIR_GENERIC, "QuestionDriverTests"),
# 	patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json",
# 	timestamp_in_log_dir = True)


# question_and_answer_loop(
# 	start_conversation_with = 3,
# 	log_basedir = os.path.join(config.LOG_DIR_GENERIC, "QuestionDriverTests"),
#  	patient_sim_script_fpath = "../PatientSimulatorScripts/sex_dob_height_weight_then_all_zero_unless_error.json",
# 	timestamp_in_log_dir = True)

# 2023-01-10T22:37:23PST trying to reproduce an error found with 321.  not able to reproduce:
# see 2023-01-10T22:38:07PST in diary-TestCoupletPrograms.org
# 2023-01-11T11:08:55PST (The next day) this was a misguided unnecessary test.
# question_and_answer_loop(
# 	start_conversation_with = 321,
# 	log_basedir = os.path.join(config.LOG_DIR_GENERIC, "QuestionDriverTests"),
#  	patient_sim_script_fpath = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/GenDataForTestGuidOpt-FullScale/2023-01-10T070544.1st_w_random_answers/2023-01-10T072548.ChildrensConsults_not_suffering_Consys_322/Consult.2023-01-10T073515-Cpd-321/recording_of_user_replies_for_sim_script.manually_repaired.json",
# 	timestamp_in_log_dir = True)

# question_and_answer_loop(
# 	start_conversation_with = 7,
# 	log_basedir = os.path.join(config.LOG_DIR_GENERIC, "QuestionDriverTests"),
# 	timestamp_in_log_dir = True)

# question_and_answer_loop(
# 	start_conversation_with = 29,
# 	log_basedir = os.path.join(config.LOG_DIR_GENERIC, "QuestionDriverTests"),
# 	timestamp_in_log_dir = True)

# question_and_answer_loop(
# 	start_conversation_with = 7,
# 	log_basedir = os.path.join(config.LOG_DIR_GENERIC, "QuestionDriverTests"),
# 	patient_sim_script_fpath = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/PatientSimulatorScripts/cpd-7-sex-dob-hgt-wgt-blood-pressure-then-random-unless-error.json",
# 	timestamp_in_log_dir = True)

