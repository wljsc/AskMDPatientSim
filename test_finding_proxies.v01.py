################################################################
# PURPOSE:
# 
# To assist with the testing of the finding proxy end point

# https://api.qa.sharecare.com/consultation/results/findings

# APPROACH:

# Initially,
# For each program that has the values CntFndgs for "ContributingFindings"
# fire a JSON for each combination of findings at the endpoint.
# Is there an error?  If so, the test fails.  If not, the test passes.
# Later we'll have more advanced tests.

################################################################
# IMPORTS

import os
import glob
import json
from collections import defaultdict
import pdb

import utils

################################################################
# HISTORY

# 2022-07-09T22:17:00PDT test_finding_proxies.v01.py
# some functions are working,
# about the cahnge the way contributing findings are collected - abstract it away


################################################################
# CONSTANTS

# This finding proxy example was taken from: Program RecNum 74, Title
# 'appetite suppressant drug' in Cpd-007.json.  It's purpose is to
# support some doc tests in here

FINDING_PROXY_EXAMPLE = \
    {
      "RecNo": 74,
      "Title": "appetite suppressant drug",
      "SourceCode": "///////////////////////////////////////////////////////////////////////////////\r\n// This proxy will function as a present finding if one or both of the \r\n// defined findings are present.\r\n//\r\n// Uncertain responses are handled as absent.\r\n// \r\n// Template:  PXY#1\r\n// Version:   3.0\r\n// Created:   08/28/02\r\n// Modified:  10/26/06\r\n///////////////////////////////////////////////////////////////////////////////\r\n{\r\n      \r\n  \r\n  // define the findings\r\n\r\n  short nFnd_A = 175 ;             // uses appetite suppressant drug\r\n  short nFnd_B = 247;              // current medication: appetite suppressant drug\r\n  \r\n  \r\n  // exit true if one or both of the defined findings are present\r\n  \r\n  Fnd[nFnd_A] == FndP || Fnd[nFnd_B] == FndP;        \r\n  \r\n}\r\n\r\n",
      "IncludeContributingFindings": true,
      "ContributingFindings": [
        {
          "FindingNo": 175
        },
        {
          "FindingNo": 247
        }
      ]
    }



################################################################
# CODE

def test_finding_proxies_in_cpd_file(cpd_fpath):
	proxies_by_cntrbg_fnds = get_fnd_proxies_and_contributing_fnds_from_cpd_json_file(cpd_fpath)
	for proxy in proxies_by_cntrbg_fnds:
		test_finding_proxy(fnd_proxy)

def test_finding_proxy(fnd_proxy):
	"""
	"""	
	contributing_fnds = ret_contributing_fnds_of_proxy(fnd_proxy)
	
	all_combos_of_contributing_findings = compute_all_combos(contributing_fnds)
	
	findings_added_across_all_combos = {}

	for fnd_combo in all_combos_of_contributing_findings:

		user_json = compose_post_with_findings(fnd_combo, cdp_num)
		bot_reply_to_post = post(user_json)
	
		if error_p(bot_reply_to_post):
			log_error(bot_reply_to_post)
		else:
			log_non_error(bot_reply_to_post)
			
		# TODO this is for later after we find out which ones fail
		# else:
		# 	fnds_added, fnds_removed = fnds_diff(user_json, bot_reply_to_post)
			
		# 	if fnds_removed:
		# 		log_fnds_removed(fnds_removed, cpd, combo, user_json, bot_reply_to_post)
		# 	if fnds_added:
		#		fnd_combo_id = ret_fnd_combo_id(fnd_combo)
		# 		findings_added_across_all_combos[fnd_combo_id] = fnds_added


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
		

def get_all_cpd_nums_from_dir(mydir):

	"""

	@mydir is assumed to be a dir containing the JSON dumps of the
	consult dbs.  This function returns a sorted list which should
	contain all and only database id numbers of all consults.

	For example, in ...

	>>> test_dump_dir = "UnitTestStuff/TestJsonDumpDir/"

	...you will only these 3 filenames: Cpd-0004.json, Cpd-0062.json, Cpd-0610.json

	Thus this fun should return [4, 62, 610]

	>>> get_all_cpd_nums_from_dir(test_dump_dir)
	[4, 62, 610]

	"""
	all_dirs = glob.glob(os.path.join(mydir, "Cpd-*.json"))
	all_dirs_basenames = [os.path.basename(d) for d in all_dirs]
	all_cpds = [d.rstrip(".json") for d in all_dirs_basenames]
	all_cpds = [d.lstrip("Cpd-") for d in all_cpds]
	all_cpds = [d.lstrip("0") for d in all_cpds]
	all_cpds = [int(c) for c in all_cpds]
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
		for prog in programs_json_list:
			#contrib_fnds_list = prog.get('ContributingFindings')
			contrib_fnds_list = ret_cont_fnds_of_program(program_json)

			if contrib_fnds_list is not None:
				for contributing_fnd in contrib_fnds_list:
					if not(list(contributing_fnd.keys()) == ['FindingNo']):
						print("Hrm, this is somewhat unexpected.  We have a an element of 'ContributingFindings' that has more than just the key 'FindingNo'")
						pdb.set_trace()
					else:
						prog_rec_num = prog['RecNo']
						dict_of_fnds_proxy_vs_cont_findings[prog_rec_num].append(contributing_fnd['FindingNo'])
	return(dict_of_fnds_proxy_vs_cont_findings)

def ret_cont_fnds_ids_of_program(program_json):
	""" 
	>>> ret_cont_fnds_ids_of_program(FINDING_PROXY_EXAMPLE)
	[175, 247]

	contrib_fnds_list = prog.get('ContributingFindings')
	contrib_fnds_id_list = []

	for contributing_fnd in contrib_fnds_list:

		if not(list(contributing_fnd.keys()) == ['FindingNo']):

			# Not sure if having more than 'FindingNo' is
			# a pathology but want to know if it happens.
			# That's why we halt here.

			print("Hrm, this is somewhat unexpected.  We have a an element of 'ContributingFindings' that has more than just the key 'FindingNo'")
			pdb.set_trace()
		else:
			prog_rec_num = prog['RecNo']
			contrib_fnds_id_list.append(contributing_fnd['FindingNo'])
	contrib_fnds_id_list.sort()
	return(contrib_fnds_id_list)

	

#print(survey_number_contr_findings("UnitTestStuff/TestJsonDumpDir/"))

#survey_number_contr_findings("/Users/william.jarrold/ShCr/AskMD/Code/Packages/Consultation.API7/Consultation.API/app-data/couplet/consults/2022-02-04-Draft13.fixed")

#survey_number_contr_findings("/Users/william.jarrold/ShCr/AskMD/Code/Packages/Consultation.API7/Consultation.API/app-data/couplet/consults/2022-02-04-Draft13.fixed", 15)
#survey_number_contr_findings("/Users/william.jarrold/ShCr/AskMD/Code/Packages/Consultation.API7/Consultation.API/app-data/couplet/consults/2022-02-04-Draft13.fixed", 20)
			
# (((2^15 / 10) / 60) / 60) = 0.91022222222

# Threshold of 15 means like 26 are over it excluding 148
# Threshold of 20 means like 10 are over it excluding 148

# Cpd-148 has 41 over threshold of 20