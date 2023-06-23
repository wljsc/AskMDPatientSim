# test_finding_proxies.2022-09-02T0713.partial_attempt_to_save_to_log_file.py
#
# It is called partial attempt to save to log file because rather than
# printing output to standard output many of the functions but not all
# saved to the log file. It was getting hairy and is likely to
# introduce a bug and I am in a hurry to just restart the next test so
# I aborted that project for now and reverted to the prior version.
# The prior version is 

################################################################
# PURPOSE:
# 
# To assist with the testing of the finding proxy end point

# https://api.qa.sharecare.com/consultation/results/findings

# see the doc string under @func test_finding_proxy it gets to much of
# the heart of the matter.

# APPROACH:

# Initially,
#
# For each program that has the values CntFndgs for "ContributingFindings"
# fire a JSON for each combination of findings at the endpoint.
# Is there an error?  If so, the test fails.  If not, the test passes.
# Later we'll have more advanced tests.

################################################################
# RELATED FILES

# See test_finding_proxies_experiments.py for a developmental history
# of sorts, where I tried different runs as the code developed.  Could
# be a good way to discover different recipes / usage patterns /
# capabiliities.

################################################################
# IMPORTS

import os
import sys
import time
import glob
import json
from collections import defaultdict
from itertools import combinations

import pdb
import requests

import config
import utils

################################################################
# HISTORY


# test_finding_proxies.2022-09-02T0656.py version just as I was
  starting to print to a log file rather than to standard out

# 2022-07-09T22:17:00PDT test_finding_proxies.v01.py
# some functions are working,
# about the change the way contributing findings are collected - abstract it away

# Jul 14 20:41 test_finding_proxies.v02.py

# Jul 14 22:06 test_finding_proxies.v03.py

# Jul 17 21:37 test_finding_proxies.v04.py

# 2022 Aug 17 11:18 test_finding_proxies.v05.py

# after v05 we are starting to log times.

################################################################
# CONSTANTS (start of section)
################################################################

OneFindingPerGroup = "OneFindingPerGroup-EnumHack"
AllFindingsInOneGroup = "AllFindingsInOneGroup-EnumHack"
AllCombinations = "AllCombinations-EnumHack"
AllCombinationsUpTo5_CFs = "AllCombinationsUpTo5_CFs-EnumHack"
TooManyCombos_WarningMsg = "TOO MANY COMBINATIONS"
AtLeastOne = "AtLeastOne-TestingFindingProxyValidationMode"

# This finding proxy example was taken from: Program RecNum 74, Title
# 'appetite suppressant drug' in Cpd-007.json.  It's purpose is to
# support some doc tests in here

################
# CONSTANTS for Examples and Tests (start of section)
################

FINDING_PROXY_EXAMPLE = \
    {
      "RecNo": 74,
      "Title": "appetite suppressant drug",
      "SourceCode": "///////////////////////////////////////////////////////////////////////////////\r\n// This proxy will function as a present finding if one or both of the \r\n// defined findings are present.\r\n//\r\n// Uncertain responses are handled as absent.\r\n// \r\n// Template:  PXY#1\r\n// Version:   3.0\r\n// Created:   08/28/02\r\n// Modified:  10/26/06\r\n///////////////////////////////////////////////////////////////////////////////\r\n{\r\n      \r\n  \r\n  // define the findings\r\n\r\n  short nFnd_A = 175 ;             // uses appetite suppressant drug\r\n  short nFnd_B = 247;              // current medication: appetite suppressant drug\r\n  \r\n  \r\n  // exit true if one or both of the defined findings are present\r\n  \r\n  Fnd[nFnd_A] == FndP || Fnd[nFnd_B] == FndP;        \r\n  \r\n}\r\n\r\n",
      "IncludeContributingFindings": True,
      "ContributingFindings": [
        {
          "FindingNo": 175
        },
        {
          "FindingNo": 247
        }
      ]
    }


FINDING_PROXY_EXAMPLE_2_FROM_CPD_4_RECNUM_16 = \
    {
      "ContributingFindings": [
        {
          "FindingNo": 62
        },
        {
          "FindingNo": 258
        }
      ],
      "IncludeContributingFindings": True,
      "RecNo": 16,
      "SourceCode": "////////////////////////////////////////////////////////////////////////////////\n//          This is a STANDARD PROXY, it should not be edited. \n//          --------------------------------------------------\n// This proxy tests if either of two possible pregnancy related findings are \n// present within the Coupler. \n//\n// This proxy is sourced by the proxy template Coupler. If both findings\n// do not exist in your Coupler, request a customized version of this proxy from\n// the Couplet Services Group.\n//\n// Uncertain responses are handled as absent.\n//\n// Template:  PXY#24\n// Version:   1.2\n// Created:   08/20/04\n// Modified:  05/17/05\n////////////////////////////////////////////////////////////////////////////////\n{\n  // define the variables\n\n  int nResult = true;\n  int nFnd;\n\n  // test if the findings exist and if they are present, if at least one\n  // finding is found present, break from the test loop and vote true\n\n  do\n  {\n    nFnd = MapEntNo (23966,1);          // possible pregnancy\n    if (nFnd > 0 && Fnd[nFnd] == FndP)\n      break;\n\n    nFnd = MapEntNo (25051,1);          // currently pregnant\n    if (nFnd > 0 && Fnd[nFnd] == FndP)\n      break;\n\n    // no present findings have been found\n\n    nResult = false;\n\n  } while (false);\n\n  // exit based on nResult\n\n  exit (nResult);\n}\n",
      "Title": "known or possible pregnancy"
    }

TARGET_JSON_FOR_TEST_01 = \
	{
	    "consultationId": 155,
	    "findings": [
		{
	            "id": 62399,
	            "idForHumans": "Fnd-drinks alcohol when stressed-GenNo-62399-Cpd-155-RecNum-10",
		    "state": "PRESENT"
	        }
		]
	}

################
# CONSTANTS for Examples and Tests (start of section)
################

################################################################
# CONSTANTS (end of section)
################################################################
################################################################
# CODE (start of section)
################################################################

# TODO(2022-07-12T08:22:29PDT, )  maybe replace 'cpd' with 'consult' for less confusing terminology.

def test_all_cpds_all_finding_proxies(json_dump_dir, grouping_type, error_log_filepath, test_all_cpds_except_these = None):

	# TODO(2022-07-14T08:19:56PDT, )  make error_log_filepath optional

	try:
		with open(error_log_filepath, 'x') as test_output_fobj:
			print('', file=test_output_fobj)
			
	except FileExistsError:
		print("The log file already exists.  Please call @func test_all_cpds_all_finding_proxies again with a different log file")
		print("We don't want you to accidentially stomp on a pre-existing log file")
		print(f"The log file you used is: {error_log_filepath}")
		sys.exit()
		

	cpd_nums = get_all_cpd_nums_from_dir(json_dump_dir, remove_these_cpd_nums = test_all_cpds_except_these)
	 	
	for cpd_num in cpd_nums:

		cpd_num_str = utils.add_padding_to_int_str(str(cpd_num), 4)
		# RE the above line, if cpd_num is 4, then cpd_num_str will be '0004'
		
		cpd_file_base_name = f"Cpd-{cpd_num_str}.json"

		print("################################################################", file=test_output_fobj)
		print(f"#### {utils.now_yyyy_mm_ddThhmmss()} Beginning {cpd_file_base_name} ####", file=test_output_fobj)
		print("################################################################", file=test_output_fobj)
		
		cpd_filepath = os.path.join(json_dump_dir, cpd_file_base_name)
		
		start_time_for_this_cpd_in_secs = round(time.time(), 2)		
		test_finding_proxies_in_cpd_file(cpd_filepath, grouping_type, test_output_fobj)
		end_time_for_this_cpd_in_secs = round(time.time(), 2)
		
		print("################################################################", test_output_fobj)
		print(f"#### {utils.now_yyyy_mm_ddThhmmss()} Finished {cpd_file_base_name} ####", test_output_fobj)
		duration_for_this_cpd_in_secs = round(end_time_for_this_cpd_in_secs - start_time_for_this_cpd_in_secs, 2)
		print(f"#### Duration of EntireConsult {cpd_file_base_name}: {duration_for_this_cpd_in_secs} (secs)", test_output_fobj)
		print("################################################################", test_output_fobj)

def test_finding_proxies_in_cpd_file(cpd_filepath, grouping_type, error_log_fileobj):
	"""

	@param grouping_type see @func compute_finding_groups.  As of
	2022-07-19 values include OneFindingPerGroup,
	AllFindingsInOneGroup, AllCombinations,
	AllCombinationsUpTo5_CFs

	"""
	# TODO renameget_fnd_proxies_and_contributing_fnds_from_cpd_json_file so that it's clear it deals with mere record numbers, NOT json
	#!pdb.set_trace()	
	proxy_rec_nums_by_cntrbg_fnd_rec_nums = get_fnd_proxies_and_contributing_fnds_from_cpd_json_file(cpd_filepath)
	with open(cpd_filepath, 'r') as fobj:
		consult_json = json.load(fobj)
		consult_id = consult_json["Configuration"]["Number"]
		for proxy_record_number in proxy_rec_nums_by_cntrbg_fnd_rec_nums:
			fnd_proxy_json = retrieve_program_json_from_cpd(proxy_record_number, consult_json)
			print("################################################################", file = error_log_fileobj)
			print(f"#### {utils.now_yyyy_mm_ddThhmmss()} Starting test_finding_proxy on Program RecNum: {proxy_record_number} from Cpd {consult_id} ####", file = error_log_fileobj)
			print("################################################################", file = error_log_fileobj)

			start_time_in_secs = round(time.time(), 2)
			test_finding_proxy(fnd_proxy_json, consult_json, grouping_type, error_log_fileobj = error_log_fileobj)
			end_time_in_secs = round(time.time(), 2)			
			duration_in_secs = round(end_time_in_secs - start_time_in_secs, 2)

			print("################################################################", file = error_log_fileobj)
			print(f"#### {utils.now_yyyy_mm_ddThhmmss()} Completed test_finding_proxy on Program RecNum: {proxy_record_number} from Cpd {consult_id} ####", file = error_log_fileobj)
			print(f"#### Duration WholeProxy: {duration_in_secs} (secs) of Cpd {consult_id} ProgRecNum: {proxy_record_number}", file = error_log_fileobj)
			print("################################################################", file = error_log_fileobj)

			

def test_finding_proxy(fnd_proxy_json, consult_json, grouping_type, error_log_fileobj, validation_mode = True, if_post_exception_log_retry_and_continue_p = True):
	"""

	This function is probably the 'heart' of this whole file.

	Given a finding proxy, FP, from the given consult_json, it
	computes a bunch of groupings for the contributing findings
	for this FP.  The groupings are specified by @param
	grouping_type.  

	A naive grouping might be 'compute all combinations' (naive bc
	the number of combinations is 2^n where n is the number of
	contributing findings).  

	Sometimes we don't have to be so exhaustive.  E.g., Sometimes
	a grouping like 'just try each contributing finding on its
	own' is good enough for the current level of testing desired.
	See @func compute_finding_groups for a definition of each kind
	of grouping_type.  See OneFindingPerGroup.

	There might be some useful tricks you can use if, after a run,
	you grep the contents of the file in the form of @param error_log_fileobj

	@param validation_mode:

	This parameter controls how this testing system analyzes the
	output from the findnig proxy endpoint.

	If @param validation_mode is None, then:

	This function only really cares if the output has an 'error'
	key.  Thus, it is the weakest form of validation.  We are just
	making sure finding proxy programs do not error out.  If there
	is no error, we are not detecting if the 'deduction' that the
	finding proxy programs make (i.e. the new finding proxy(ies)
	that get added to the finding list) are correct.

	If @param validation_mode is AtLeastOne, then this verifies
	that at least one of the groupings of contributing findings
	fired at the end point, cause the current finding proxy
	(i.e. the one identified by @param fnd_proxy_json) to be added
	to the finding list.  More than likely, other finding proxies
	will also get added to the finding list.  All such additions
	should be logged (TODO where/how?) but there is only a
	validation failure if the current finding proxy does not get
	added.

	"""
	#pdb.set_trace()	
	contributing_fnd_ids = ret_contributing_finding_ids_of_program(fnd_proxy_json)

	# 'all_combos' and 'combos' should be replaced with stuff like
	# 'groupings' why?  bc at first I thought I was gonna do all
	# combinations of the elements of a set.  But actually, I
	# don't always want to do all combinations.  Sometimes I might
	# wanna sample from all combos (e.g. if combinatoric
	# explosion), sometimes I might want to just do one
	# contributing finding at a time.
	
	all_combos_of_contributing_finding_ids = compute_finding_groups(contributing_fnd_ids, grouping_type)
	
	findings_added_across_all_combos = {}

	consult_id = consult_json["Configuration"]["Number"]
	consult_name = consult_json["Configuration"]["FullTopic"]
	program_rec_num = fnd_proxy_json["RecNo"]
	program_title = fnd_proxy_json.get('Title', 'ProgramHasNoTitle')
	
	potential_error_msg_txt = f'ConsultID: {consult_id} ProgRecNum: {program_rec_num} ("{program_title}")  ("{consult_name}")'
	potential_error_msg_txt_4grep = f' CPD | {consult_id} | PRN |  {program_rec_num} | "{program_title}" | "{consult_name}" | CFS '
	# CPD - means couplet database, dunno why they call it CPD
	# PRN - means program record number
	# CFS - means contributing findings
	
	error_report_obj = [potential_error_msg_txt, potential_error_msg_txt_4grep]

	for combo_of_fnd_ids in all_combos_of_contributing_finding_ids:

		################
		# Add the contributing findings for this combo to the
		# context described in potential_error_msg_txt_4grep
		
		potential_error_msg_txt_4grep = error_report_obj[1]
		combo_of_fnd_ids.sort()
		combo_of_fnd_ids_str = str(combo_of_fnd_ids)
		combo_of_fnd_ids_str = combo_of_fnd_ids_str.strip("[")
		combo_of_fnd_ids_str = combo_of_fnd_ids_str.strip("]")
		#!print("wtf")
		#!pdb.set_trace()
		potential_error_msg_txt_4grep += f"| {combo_of_fnd_ids_str} "
		error_report_obj[1] = potential_error_msg_txt_4grep

		
		contributing_fnds_json = compose_post_with_findings(combo_of_fnd_ids, consult_json)
		contributing_fnds_json_str = json.dumps(contributing_fnds_json, indent=4, sort_keys=True)

		print(f"FirstTry: test_finding_proxy ({utils.now_yyyy_mm_ddThhmmss()}) combo_of_fnd_ids: {combo_of_fnd_ids} Cpd: {consult_id} RecNum: {program_rec_num}", file = error_log_fileobj)

		################		
		# The Moment Of Truth: Here is where we actually hit the the endpoint!! (START OF SECTION)

		if if_post_exception_log_retry_and_continue_p:

			try:
				start_time_in_secs = round(time.time(), 2)
				bot_reply_to_post, error_report_string = post_contributing_findings(contributing_fnds_json_str, error_report_obj)
				end_time_in_secs = round(time.time(), 2)
			except Exception as exception_message:
				end_time_in_secs = round(time.time(), 2)
				duration_in_secs = round(end_time_in_secs - start_time_in_secs, 2)
				print(f"#### Duration of ProxyFindingCombination {duration_in_secs} (secs): {consult_id}: ProgRecNum: {program_rec_num} FndCombo: {combo_of_fnd_ids}: {duration_in_secs} (First Post Try Failed)", file = error_log_fileobj)
				print("################################################################", file = error_log_fileobj)
				print("# First Post Try Failed )-: )-: )-: ######################################", file = error_log_fileobj)
				print("# Exception Message Text: (START OF SECTION) ###################", file = error_log_fileobj)
				print(exception_message, file = error_log_fileobj)
				print("# Exception Message Text: (END OF SECTION) ######################", file = error_log_fileobj)
				print("################################################################", file = error_log_fileobj)

				print("################################################################", file = error_log_fileobj)
				print(f"SecondTry: test_finding_proxy ({utils.now_yyyy_mm_ddThhmmss()}) combo_of_fnd_ids: {combo_of_fnd_ids} Cpd: {consult_id} RecNum: {program_rec_num}", file = error_log_fileobj)
				try:
					start_time_in_secs = round(time.time(), 2)
					bot_reply_to_post, error_report_string = post_contributing_findings(contributing_fnds_json_str, error_report_obj)
					end_time_in_secs = round(time.time(), 2)

				except Exception as exception_message:
					end_time_in_secs = round(time.time(), 2)
					duration_in_secs = round(end_time_in_secs - start_time_in_secs, 2)

					print(f"#### Duration of ProxyFindingCombination {duration_in_secs} (secs): {consult_id}: ProgRecNum: {program_rec_num} FndCombo: {combo_of_fnd_ids}: {duration_in_secs} (Second Post Try Failed)", file = error_log_fileobj)
					print("################################################################", file = error_log_fileobj)
					print("# Second Post Try Failed )-: )-: )-: ###########################", file = error_log_fileobj)
					print("# Exception Message Text: (START OF SECTION) ###################", file = error_log_fileobj)
					print(exception_message, file = error_log_fileobj)
					print("# Exception Message Text: (END OF SECTION) ######################", file = error_log_fileobj)
					print("################################################################", file = error_log_fileobj)
					
				else:
					duration_in_secs = round(end_time_in_secs - start_time_in_secs, 2)
					print(f"#### Duration of ProxyFindingCombination {duration_in_secs} (secs): {consult_id}: ProgRecNum: {program_rec_num} FndCombo: {combo_of_fnd_ids}: {duration_in_secs} (Second Post Successful)", file = error_log_fileobj)

			else:
				duration_in_secs = round(end_time_in_secs - start_time_in_secs, 2)
				print(f"#### Duration of ProxyFindingCombination {duration_in_secs} (secs): {consult_id}: ProgRecNum: {program_rec_num} FndCombo: {combo_of_fnd_ids}: {duration_in_secs} (First Post Successful)", file = error_log_fileobj)


		# The Moment Of Truth: Here is where we actually hit the the endpoint!! (END OF SECTION)
		################		



		error_msg_in_endpoint_reply = bot_reply_to_post.get('error')

		# TODO(2022-07-18T11:31:09PDT, ) I'm pretty sure that I don't want
		# to implement this block.  Instead I will have the 'if error_msg' branch below
		# handle the error logging and the else branch handle the non-error logging.
		# So, wait a day or so and then if still don't want to then delete this commented blob
		# if error_p(bot_reply_to_post):
		# 	log_error(bot_reply_to_post)
		# else:
		# 	log_non_error(bot_reply_to_post)


		if error_msg_in_endpoint_reply:
			print("error", file = error_log_fileobj)
			# 2022-09-02T07:00:37PDT Commented out This:...
			#
			# with open(error_log_filepath, 'a') as f_obj:
			# 	print("################################################################", file=f_obj)
			# 	print(error_report_string, file=f_obj)
			# 	print("################################################################", file=f_obj)
			##TODO(2022-07-14T08:17:40PDT, ) maybe make whether we go into debugger a toggle via a param
			##!pdb.set_trace()
			#
			# ....2022-09-02T07:00:37PDT and added this:
			
			print("################################################################", file = error_log_fileobj)
			print(error_report_string, file = error_log_fileobj)
			print("################################################################", file = error_log_fileobj)
			

			
		elif validation_mode is not None:
		
			fnds_added = fnds_removed = None
			
			fnds_added, fnds_removed = fnds_diff(contributing_fnds_json, bot_reply_to_post)

			if fnds_added != []:
				print("Weird fnds_added is nonempty!", file = error_log_fileobj)
				#pdb.set_trace()
			if fnds_removed != []:
				print("Weird fnds_removed is nonempty!", file = error_log_fileobj)
				#pdb.set_trace()
			

			# Currently (2022-07-19T09:14:39PDT) fp
                        # endpoint does not appear able to add
                        # findings when couplet programs 'deduce' they
                        # should be added.  Thus, until this is
                        # supported (by Wed Jul 20?) we want to signal
                        # alarm bells if there is a diff.

			# 2022-08-16T07:41:54PDT updating this to only send a flag, i.e.
			#	print("Weird fnds_removed is nonempty!")
			# and not enter the debugger

		
			
		# 	if fnds_removed:
		# 		log_fnds_removed(fnds_removed, cpd, combo, user_json, bot_reply_to_post)
		# 	if fnds_added:
		#		fnd_combo_id = ret_fnd_combo_id(fnd_combo)
		# 		findings_added_across_all_combos[fnd_combo_id] = fnds_added



def compose_post_with_findings(combo_of_fnd_ids, consult_json, allow_valued_findings_p = False):
	"""

	PURPOSE: Roughly speaking, to compose, synthesize, write or
	spell out a json object with a particular finding list.

	More precisely, given a group of finding ids (specified in
	@param combo_of_fnd_ids) such that those ids are record
	numbers of the findings in the current consult database
	(i.e. @param consult_json) , create a json object to post on
	the findings endpoint (most likely, by calling @func
	post_contributing_findings)

	@param consult_json is a json object created by loading a cpd
	file - e.g. for consult id #4, the filename would be
	Cpd-0004.json).

	Set up the test:
	>>> TEST_CPD_0155_FILEPATH = "UnitTestStuff/TestJsonDumpDir2/Cpd-0155.json"
	>>> with open(TEST_CPD_0155_FILEPATH, 'r') as fobj: TEST_CPD_0155_JSON = json.load(fobj)

	Run the test:
	>>> output_json = compose_post_with_findings([10], TEST_CPD_0155_JSON)
	>>> TARGET_JSON_FOR_TEST_01 == output_json
	True

	"""
	if allow_valued_findings_p:
		print("Sorry, I do not (yet!!) no how to handle valued findings")
		pdb.set_trace()

	findings_list_for_json_payload = []

	consult_id = consult_json["Configuration"]["Number"]

	for fnd_rec_num_id in combo_of_fnd_ids:
		fnd_cpd_json = retrieve_fnd_json_from_cpd(fnd_rec_num_id, consult_json)
		fnd_name = fnd_cpd_json["Name"]
		fnd_entity_num = fnd_cpd_json["EntNo"]
		id_for_humans = utils.pretty_fnd_id(fnd_name, fnd_entity_num, consult_id, fnd_rec_num_id)
		fnd_payload_json = {"id" : fnd_entity_num, "state": "PRESENT", "idForHumans" : id_for_humans}
		findings_list_for_json_payload.append(fnd_payload_json)

	json_payload = {"consultationId" : consult_id, "findings" : findings_list_for_json_payload}

	return(json_payload)

def fnds_diff(user_json, bot_reply_to_post_json):

	"""Computes the diff between the finding list in user_json
	(whihc is posted to the finding proxy service) and the
	finding list bot_reply_to_post.

	@return two values

		- fnds_added is a sorted lists the findings ids that
                  were not in the user_json's finding list but were in
                  the finding list of bot_reply_to_post.

		- fnds_removed is a sorted lists the findings ids that
                  were in the user_json's finding list but were not in
                  the finding list of bot_reply_to_post.
	"""

	#tmp = bot_reply_to_post_json.get('findings')
	#tmp = bot_reply_to_post_json.get('categories').get('findings')

	# TODO(2022-07-19T13:52:22PDT, ) CAUTION THIS IF/ELSE iS A TEMP HACK!!!
	
	# if tmp is not None:
	# 	print("This is a temporary thing!!! There should be a JIRA that should say findings list returned from finding proxy endpoint should have a finding list.  We are doing this 'make sure the bug is still here' thing to verify that this bug is true for all finding proxies")
	# 	pdb.set_trace()
	# else:
	# 	return(None, None)

	#print("just making sure this gets called and works 2022-07-19T09:28:41PDT")
	#pdb.set_trace()

	user_json_fnds = user_json['findings']
	user_json_fnd_ids = [fnd['id'] for fnd in user_json_fnds]

	#bot_reply_to_post_json_fnds = bot_reply_to_post_json['findings']
	#bot_reply_to_post_json_fnd_ids = [fnd['id'] for fnd in bot_reply_to_post_json_fnds]
	bot_reply_to_post_json_fnd_ids = extract_list_of_finding_ids(bot_reply_to_post_json)

	fnds_removed = set(user_json_fnd_ids).difference(set(bot_reply_to_post_json_fnd_ids))
	fnds_added   = set(bot_reply_to_post_json_fnd_ids).difference(set(user_json_fnd_ids))

	fnds_removed = sorted(list(fnds_removed))
	fnds_added = sorted(list(fnds_added))

	return(fnds_removed, fnds_added)

def extract_list_of_finding_ids(bot_reply_to_post_json):
	list_finding_ids_across_cats = []
	cats = bot_reply_to_post_json['categories']
	for cat in cats:
		finding_list_of_cat = cat['findings']

		# TODO(2022-07-21T09:29:19PDT, ) there is a JIRA from
		# Jesse a few days before today in which he says 'id'
		# should be replaced with 'entityId' or s.t.

		list_finding_ids_of_cat = [fnd['id'] for fnd in finding_list_of_cat]
		list_finding_ids_across_cats += list_finding_ids_of_cat
	return(list_finding_ids_across_cats)

			

def finding_in_cpd_is_valued_p(fnd_cpd_json):

	"""In @file test_question_driver.py there is @fun
	ret_likely_response_mode_for_response_content.

	That function and the present function are kind of analogs of
	each other.
	
	This function wants to tell you the type of a finding in a CPD file.

	'That' function (i.e. @fun
	ret_likely_response_mode_for_response_content) wants to tell
	you the type of finding when you see a finding come to you in
	a response from the bot e.g. during question driver.

	"""
	
	value_type = fnd_cpd_json.get("ValueType")
	value_type_units = fnd_cpd_json.get("ValueTypeUnits")
	if value_type_units and value_type is None:
		print("This is a very strange and unexpected case and should be investigated more.")
		print("Specifically, have I been wrongly assuming how valued findings are represented??")
		print("If so, then modify the code based on more correct assumptions, *if*necessary*")
		pdb.set_trace()
	if value_type is not None:
		print("Hey value_type is not None!  Just letting you know so you can inspect")
		print(f"ValueType is {ValueType}, ValueTypeUnits is {ValueTypeUnits}.")
		print("You probably want to hit c to contine on but you may wish to inspect more deeply.")
		pdb.set_trace()
		return(True)
	else:
		return(False)
		

# TODO(2022-07-11T18:55:13PDT, ) TARGET_FINDING_REC_NO_10_IN_CPD_155
# in a couple of days unless it is needed.
#
# TARGET_FINDING_REC_NO_10_IN_CPD_155 = \
# 	{
# 	      "DisplayWeight": 240,
# 	      "EntNo": 62399,
# 	      "Name": "drinks alcohol when stressed",
# 	      "RecNo": 10
# 	}

TARGET_FINDING_REC_NO_2_IN_CPD_4 = \
    {
      "DisplayWeight": 860,
      "EntNo": 306,
      "Name": "difficulty swallowing",
      "RecNo": 2
    }


def retrieve_fnd_json_from_cpd(fnd_record_number_id, cpd_json):
	"""

	Gets the json finding object whose record number is @param
	fnd_record_number_id in the json object @param cpd_json.

	Set up the test:
	>>> TEST_CPD_004_FILEPATH = "UnitTestStuff/TestJsonDumpDir/Cpd-0004.json"
	>>> with open(TEST_CPD_004_FILEPATH, 'r') as fobj: TEST_CPD_004_JSON = json.load(fobj)

	Run the test:
	>>> json_obj_result = retrieve_fnd_json_from_cpd(2, TEST_CPD_004_JSON)
	>>> json_obj_result == TARGET_FINDING_REC_NO_2_IN_CPD_4
	True
	"""
	
	findings_in_cpd = cpd_json['Findings']
	matching_fnd_objs = [fnd_obj for fnd_obj in findings_in_cpd if fnd_obj['RecNo'] == fnd_record_number_id]
	if len(matching_fnd_objs) != 1:
		print("This is very strange.  It appears that more than one finding object has the same record number.")
		cpd_record_number = cpd_json['Number']
		print("Specifically in cpd_json number {cpd_record_number}, fnd_record_number_id {fnd_record_number_id} there are {len(matching_fnd_objs)} that have that record number!!!")
		pdb.set_trace()
	else:
		return(matching_fnd_objs[0])

def retrieve_program_json_from_cpd(program_record_number, cpd_json):
	"""

	Gets the json program object whose record number is @param
	program_record_number in the json object @param cpd_json.

	Set up the test:
	>>> TEST_CPD_004_FILEPATH = "UnitTestStuff/TestJsonDumpDir/Cpd-0004.json"
	>>> with open(TEST_CPD_004_FILEPATH, 'r') as fobj: TEST_CPD_004_JSON = json.load(fobj)

	Run the test:
	>>> json_obj_result = retrieve_program_json_from_cpd(16, TEST_CPD_004_JSON)
	>>> json_obj_result == FINDING_PROXY_EXAMPLE_2_FROM_CPD_4_RECNUM_16
	True
	"""
	
	programs_in_cpd = cpd_json['Programs']
	matching_program_objs = [pgm_obj for pgm_obj in programs_in_cpd if pgm_obj['RecNo'] == program_record_number]
	if len(matching_program_objs) != 1:
		print("This is very strange.  It appears that more than one program object has the same record number.")
		cpd_record_number = cpd_json['Number']
		print("Specifically in cpd_json number {cpd_record_number}, program_record_number_id {program_record_number_id} there are {len(matching_program_objs)} that have that record number!!!")
		pdb.set_trace()
	else:
		return(matching_program_objs[0])


TODO(2022-09-02T07:13:17PDT , ) finishgin adding th eprint for the error file obj.  or mayb ejot.  maybe give up
def post_contributing_findings(payload, error_report_obj):

	# TODO(2022-07-13T07:25:23PDT, ) easy -
	# potential_error_msg_txt should be renamed to s.t. like
	# post_context_description_txt bc it really does descript the
	# context in terms of CPD and finding proxy rec num and
	# contirbuting findings.  it should be printed not only if
	# there is an error but every time the post happens.  And
	# seems we can use the same post function in
	# test_question_driver.py too, maybe?

	# CAUTION: this might wanna be merged or partially merged with @fun post_users_reply
	# the post function in @file test_question_driver.py

	""" 

	We post a payload which is a json formatted string, which
	consists of a set stateemnts about findings are present.

	The end point should respond with a finding list.  The finding
	list should have all of the original findings plus one or more
	additional findings assuming the current finding proxy under
	examination runs correctly.

	@return bot_output_json - what the bot says in response to
	this post.

	@return payload_as_dict

	result = post_contributing_findings(TEST_PAYLOAD_1)

	"""
	
	# if STEP_SLOWLY_2:
	# 	print("In @func  post_contributing_findings")
	# 	pdb.set_trace()
		
	print("################################################################")
	print("### Just Entered @fun post_users_reply ################################")
	print("################################################################")
	print()
	
	payload_as_dict = json.loads(payload)
	
	print(f"#### Contributing Findings Payload TODO consider spelling out human readable findings list here? ####")
	print("#### Payload (start of json object) ####")
	print()
	print(json.dumps(payload_as_dict, indent = 4, sort_keys = True))
	print()	
	print("#### Payload (end of json object) ####")

	print()

	# url = 'https://api.dev.sharecare.com/consultation/next'
	# ... 2022-06-22T13:10:33PDT dev is dead, long live qa...
	# url = 'https://api.qa.sharecare.com/consultation/next'
	
	headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

	post_response = requests.post(url = config.FINDING_PROXY_ENDPOINT, data=payload, headers=headers)

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
	
	#pdb.set_trace()
	#result_str = json.dumps(bot_output_json, indent=4, sort_keys=True)

	error_msg = bot_output_json.get('error')
	error_report_string = None

	potential_error_msg_txt = error_report_obj[0]
	potential_error_msg_txt_4grep = error_report_obj[1]
	
	if error_msg:
		
		error_report_string = \
f"""################################################################
Dag Nabit! Finding Service Returns JSON with an error.  

The context in which the error was obtained: {potential_error_msg_txt}

The text of the error is:

{error_msg}

################################################################
Here is the payload that was posted to the service that resulted in the error:
<START OF PAYLOAD>

{payload}

<END OF PAYLOAD>
################################################################
Here is something to help you tally stats over a run using simple grep commands:

| 4GREP | {error_msg} | {potential_error_msg_txt_4grep} |

################################################################"""

# TODO(2022-07-18T09:14:32PDT, ) currently the above 4GREP line looks like this...
# <START QUOTE>
# | 4GREP | TypeError: funcRef is not a function |  CPD | 27 | PRN |  6 | "waist circumference over 40 inches (man) or 35 (woman)" | "Healthy Weight Management" | CFS | 8 | 9 | 53  |
# <END QUOTE>
# but that is wrong.  The last bit should be more like
# | CFS | 8 9 53 |
# or
# | CFS | 8, 9, 53 |
# Need to debug..  Maybe first just conver teh list to a string and dont worry about trimming [ and ] etc

		print(error_report_string)

	################################################################
	# LEGACY_STUFF_1 COPIED FROM @FUNC POST_USERS_REPLY (START OF SECTION)
	#
	# 	if log_dir is not None:

	# 		print("Sorry I have not been programmed to handle a log dir yet!!!")
		
	# 		out_filename = filename_str_for_bot_question(question_seq_index_str, question_id)
			
	# 		out_fpath = os.path.join(log_dir, out_filename)
	# 		with open(out_fpath, 'w') as out_obj:
	# 			print(error_report_string, file=out_obj)

	# 		# What to say in the CONVERSATION_FILENAME file
	# 		if CONVERSATION_INVARIANT_MODE_P:
	# 			sys_quest_num_str = f"QuesSeq# {question_seq_index}"			
	# 		else:
	# 			sys_quest_num_str = f"QuesSeq# {question_seq_index} QuesID# {question_id}"
	# 		string_to_log_and_print = f"{sys_quest_num_str} ResponseHeader: BotError"
	# 		print(string_to_log_and_print)
	# 		log(conversation_log_filepath, string_to_log_and_print)
	# LEGACY_STUFF_1 COPIED FROM @FUNC POST_USERS_REPLY (START OF SECTION)	
	################################################################

	# print("################")

	print("Bot JSON Response To Contributing Findings Post (start of section)")

	print()
	pretty_bot_output_json_str = json.dumps(bot_output_json, indent=4, sort_keys=True)
	print(pretty_bot_output_json_str)
	print()

	print("Bot JSON Response To Users Post (end of section)")
	print("################")

	################################################################
	# LEGACY_STUFF_2 COPIED FROM @FUNC POST_USERS_REPLY (START OF SECTION)

	# TODO(2022-07-11T17:52:26PDT, ) decide if / how to adapt this
	# for current purposes.  As of 2022-07-17T21:46:10PDT, it is
	# likely that this is all deltable garbage.

	# if log_dir is not None:
	# 	if error_msg:

	# 		# TODO(2022-06-01T22:13:10PDT, ) does the
	# 		# error get logged like other stuff?  i am
	# 		# pretty sure the nag is no longer needed, it
	# 		# already logs the error - soewhere else,
	# 		# right?
			
	# 		pass

	# 	else:

	# 		question_seq_index = bot_output_json['questionIndexSeq']
			
	# 		question_id = bot_output_json.get('questionId', "NO_QUES_ID_BC_NO_MORE_QUESTIONS")
	
	# 		if question_seq_index > 10:
	# 			question_seq_index_str = "0" + str(question_seq_index)
	# 		else:
	# 			question_seq_index_str = str(question_seq_index)

	# 		out_filename = filename_str_for_bot_question(question_seq_index_str, question_id)
			
	# 		out_fpath = os.path.join(log_dir, out_filename)
	# 		with open(out_fpath, 'w') as out_obj:
	# 			print(pretty_bot_output_json_str, file=out_obj)
	# LEGACY_STUFF_2 COPIED FROM @FUNC POST_USERS_REPLY (END OF SECTION)	
	################################################################


	#### return from post_users_reply
	return(bot_output_json, error_report_string)
	#### return from post_users_reply



def compute_finding_groups(finding_ids, grouping_type):
	
	if grouping_type == OneFindingPerGroup:
		groupings = [[x] for x in finding_ids]
	elif grouping_type == AllFindingsInOneGroup:
		groupings = [finding_ids]
	elif grouping_type == AllCombinations:
		print("Sorry I do not yet know how to compute AllCombinations - it's just too explosive.  But see AllCombinationsUpTo5")
		pdb.set_trace()
	elif grouping_type == AllCombinationsUpTo5_CFs:
		# 2 ** 5 is 32.  
		groupings = ret_all_combinations_unless_too_many(mylist, max_number_of_combos_to_return = 32)
	else:
		print(f"Unrecognized grouping type: {grouping_type}")
		pdb.set_trace()
	return(groupings)


def survey_number_contr_findings(json_dump_dir, threshold = None):

	"""PURPOSE for each consult, for each finding proxy program of
	that consult, print out how many contributing findings that
	finding proxy has.

	The proximate cause for writing this was to explore for what
	finding proxies we might have a combinatorial explosion.

	Specifically, to see what kind of n we are dealing with in
	terms of number of contributing findings.  Our plan (at least
	circa 2022-07-09) is to present all combinations of
	contributing findings to the end point.  Given n contributing
	findings it's basic (college) math that the number of
	combinations is 2^n.  So, as n gets to be like 20 or 50, the
	amount of compute required to generate or progress all
	combinations gets to be prohibitive.

	If threshold is None then the output is like this...

	>>> test_dump_dir = "UnitTestStuff/TestJsonDumpDir/"
	>>> survey_number_contr_findings(test_dump_dir)
	Cpd-0004.json: [16, 12, 8, 8, 7, 6, 6, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
	Cpd-0062.json: [11, 3, 2, 1, 1]
	Cpd-0610.json: [31, 18, 7, 4, 3, 1, 1, 1]

	If the threshold is 11 then output is like this...

	>>> survey_number_contr_findings(test_dump_dir, 11)
	Cpd-0004.json: [16, 12]
	Cpd-0062.json: []
	Cpd-0610.json: [31, 18]

	...In other words, for Cpd-0004.json there only 2 finding
	proxies that have more than 11 contributing findings.  One of
	the fp's has 16 contributing findings, the other one has 12.

	"""

	cpd_nums = get_all_cpd_nums_from_dir(json_dump_dir)
	 	
	for cpd_num in cpd_nums:
	
		cpd_num_str = utils.add_padding_to_int_str(str(cpd_num), 4)
		# RE the above line, if cpd_num is 4, then cpd_num_str will be '0004'
		
		cpd_file_base_name = f"Cpd-{cpd_num_str}.json"

		fpath = os.path.join(json_dump_dir, cpd_file_base_name)

		fnd_proxies_by_ctbg_fnds = get_fnd_proxies_and_contributing_fnds_from_cpd_json_file(fpath)

		number_of_contributing_fnds_for_fnd_proxy = []

		for k in fnd_proxies_by_ctbg_fnds:
			nmbr_of_contributing_fnds_for_this_proxy = len(fnd_proxies_by_ctbg_fnds[k])
			number_of_contributing_fnds_for_fnd_proxy.append(nmbr_of_contributing_fnds_for_this_proxy)

		number_of_contributing_fnds_for_fnd_proxy.sort(reverse=True)
		
		if threshold:
			number_of_contributing_fnds_for_fnd_proxy = [n for n in number_of_contributing_fnds_for_fnd_proxy if n > threshold]

		print(f"{cpd_file_base_name}: {number_of_contributing_fnds_for_fnd_proxy}")
			
		# if threshold:
		# 	num_of_ctbg_fnds_for_fnd_proxy_above_threshold = []
		# else:
		# 	num_of_ctbg_fnds_for_fnd_proxy_above_threshold = None
			
		# for k in fnd_proxies_by_ctbg_fnds:
		# 	nmbr_of_contributing_fnds_for_this_proxy = len(fnd_proxies_by_ctbg_fnds[k])
		# 	if threshold and (nmbr_of_contributing_fnds_for_this_proxy > threshold):
		# 		num_of_ctbg_fnds_for_fnd_proxy_above_threshold.append(nmbr_of_contributing_fnds_for_this_proxy)
		# 	number_of_contributing_fnds_for_fnd_proxy.append(nmbr_of_contributing_fnds_for_this_proxy)
			
		# number_of_contributing_fnds_for_fnd_proxy.sort(reverse=True)
		# #if number_of_contributing_fnds_for_fnd_proxy:

		# if num_of_ctbg_fnds_for_fnd_proxy_above_threshold:
		# 	print(f"{cpd_file_base_name}: {num_of_ctbg_fnds_for_fnd_proxy_above_threshold}")
		# else:
		# 	print(f"{cpd_file_base_name}: {number_of_contributing_fnds_for_fnd_proxy}")
		

def get_all_cpd_nums_from_dir(mydir = config.JSON_DUMP_DIRECTORY_PATH, remove_these_cpd_nums = None):

	"""

	PURPOSE: to all you to grab all the consult ids in a given
	json dump directory.  Optionally, to get all of them except
	those in the specified list (i.e. @param
	remove_these_cpd_nums)

	@param mydir is assumed to be a dir containing the JSON dumps of the
	consult dbs.  This function returns a sorted list which should
	contain all and only database id numbers of all consults.

	For example, in ...

	>>> test_dump_dir = "UnitTestStuff/TestJsonDumpDir/"

	...you will only these 3 filenames: Cpd-0004.json, Cpd-0062.json, Cpd-0610.json

	Thus this fun should return [4, 62, 610]

	>>> get_all_cpd_nums_from_dir(test_dump_dir)
	[4, 62, 610]

	>>> get_all_cpd_nums_from_dir(test_dump_dir, remove_these_cpd_nums = [62, 4])
	[610]

	"""
	all_dirs = glob.glob(os.path.join(mydir, "Cpd-*.json"))
	all_dirs_basenames = [os.path.basename(d) for d in all_dirs]
	all_cpds = [d.rstrip(".json") for d in all_dirs_basenames]
	all_cpds = [d.lstrip("Cpd-") for d in all_cpds]
	all_cpds = [d.lstrip("0") for d in all_cpds]
	all_cpds = [int(c) for c in all_cpds]
	if remove_these_cpd_nums:
		all_remaining_cpds = set(all_cpds).difference(set(remove_these_cpd_nums))
		all_cpds = list(all_remaining_cpds)
		
	all_cpds.sort()
	return(all_cpds)

#print(get_all_cpd_nums_from_dir("UnitTestStuff/TestJsonDumpDir/"))

def get_fnd_proxies_and_contributing_fnds_from_cpd_json_file(json_filepath):

	# DocString with DocTest
	
	"""
	@Returns a dict.

	The keys of that dict are the record numbers of Programs in
	@param json_filepath.  Each such program is a finding proxy.

	For each key, the value is the list of finding record numbers
	that are the contributing findings for that program.

	>>> result = get_fnd_proxies_and_contributing_fnds_from_cpd_json_file("UnitTestStuff/TestJsonDumpDir/Cpd-0062.json")

	>>> target = {7: [34], 14: [77, 104, 283], 23: [34], 27: [12, 13, 14, 15, 49, 98, 150, 168, 248, 410, 411], 79: [171, 263]}

	>>> result == target
	True

	"""

	# Actual Code
	
	with open(json_filepath, "r") as json_content:
		  cpd_json = json.load(json_content)
	programs_json_list = cpd_json.get('Programs')
	if programs_json_list is None:
		print("Error?  This is Highly unexpected. Is there a bug? Why would we have a such that there is nothing for the 'Programs' key?")
		pdb.set_trace()
	elif not(isinstance(programs_json_list, list)):
		print("Huh?  Why in the world would @param programs_json_list NOT be a list?.  Better pdb.set_trace() to find out.")
		pbd.set_trace()
	else:
		dict_of_fnds_proxy_vs_cont_findings = defaultdict(list)
		for program_json in programs_json_list:
			#contrib_fnds_list = program_json.get('ContributingFindings')
			contrib_fnd_ids_list = ret_contributing_finding_ids_of_program(program_json)
			prog_rec_num = program_json['RecNo']
			if len(contrib_fnd_ids_list) > 0:
				dict_of_fnds_proxy_vs_cont_findings[prog_rec_num] = contrib_fnd_ids_list
			
	return(dict_of_fnds_proxy_vs_cont_findings)

def ret_contributing_finding_ids_of_program(program_json):

	""" 

	Given a program, if it has any contributing findings, then
	return a list of the ids of the findings that are contributing
	findings.

	>>> ret_contributing_finding_ids_of_program(FINDING_PROXY_EXAMPLE)
	[175, 247]
	"""
	
	contrib_fnds_list = program_json.get('ContributingFindings', [])
	contrib_fnds_id_list = []
	
	for contributing_fnd in contrib_fnds_list:

		if not(list(contributing_fnd.keys()) == ['FindingNo']):

			# Not sure if having more than 'FindingNo' is
			# a pathology but want to know if it happens.
			# That's why we halt here.

			print("Hrm, this is somewhat unexpected.  We have a an element of 'ContributingFindings' that has more than just the key 'FindingNo'")
			pdb.set_trace()
		else:
			prog_rec_num = program_json['RecNo']
			contrib_fnds_id_list.append(contributing_fnd['FindingNo'])
	contrib_fnds_id_list.sort()
	return(contrib_fnds_id_list)

################################################################
# Generating Combinations

def ret_all_combinations_unless_too_many(mylist, max_number_of_combos_to_return):
	"""

	Given the list [a,b,c] compute all combinations of elements as
	seen in the doc test examples.  The human caller of this fn
	needs to decide how many hits of the end point that their
	patience can tolerate.  E.g. if they can tolerate no more than
	100 minutes for the set of contributing findings in @mylist,
	and it takes 1 minute per group of findings hitting the
	endpoint, then max_number_of_combos_to_return should be set to
	100. (Obviously in 'real life', it's MUCH shorter than 1
	minute, and the average human doesn't want to think in terms
	of just one finding proxies grouping of contributing findings
	but...

	Anyway, here's sort of an illustration of the above paragraph...

	>>> ret_all_combinations_unless_too_many(['a','b','c'], 500)
	[(), ('a',), ('b',), ('c',), ('a', 'b'), ('a', 'c'), ('b', 'c'), ('a', 'b', 'c')]

	TODO a little better to remove the (), eh?

	>>> ret_all_combinations_unless_too_many(['a','b','c'], 4)
	'TOO MANY COMBINATIONS!! Actual number was 8 but maximum allowed is 4'
	
	"""
	len_list = len(mylist)
	number_combos = 2 ** len_list
	
	if number_combos > max_number_of_combos_to_return:
		return_value = f"{TooManyCombos_WarningMsg}!! Actual number was {number_combos} but maximum allowed is {max_number_of_combos_to_return}"
	else:
		list_combinations = list()
		for n in range(len(mylist) + 1):
		    list_combinations += list(combinations(mylist, n))
		return_value = list_combinations

	return(return_value)
	


################################################################
# CODE (end of section)
################################################################
