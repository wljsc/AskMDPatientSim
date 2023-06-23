################################################################
# IMPORTS

import config
import test_finding_proxies as tfp
import os



################################################################

#print(survey_number_contr_findings("UnitTestStuff/TestJsonDumpDir/"))

#survey_number_contr_findings("/Users/william.jarrold/ShCr/AskMD/Code/Packages/Consultation.API7/Consultation.API/app-data/couplet/consults/2022-02-04-Draft13.fixed")

#survey_number_contr_findings("/Users/william.jarrold/ShCr/AskMD/Code/Packages/Consultation.API7/Consultation.API/app-data/couplet/consults/2022-02-04-Draft13.fixed", 15)
#survey_number_contr_findings("/Users/william.jarrold/ShCr/AskMD/Code/Packages/Consultation.API7/Consultation.API/app-data/couplet/consults/2022-02-04-Draft13.fixed", 20)
			
# (((2^15 / 10) / 60) / 60) = 0.91022222222

# Threshold of 15 means like 26 are over it excluding 148
# Threshold of 20 means like 10 are over it excluding 148

# Cpd-148 has 41 over threshold of 20

# import doctest
#if __name__ == "__main__":
#     import doctest
#     #doctest.testmod()
#     #doctest.run_docstring_examples(retrieve_fnd_json_from_cpd, globals())
#     doctest.run_docstring_examples(retrieve_program_json_from_cpd, globals())
#     doctest.run_docstring_examples(compose_post_with_findings, globals())

# test_finding_proxies_in_cpd_file("UnitTestStuff/TestJsonDumpDir/Cpd-0004.json")

#test_finding_proxies_in_cpd_file("UnitTestStuff/TestJsonDumpDir/Cpd-0004.json", tfp.AllFindingsInOneGroup)

#test_all_cpds_all_finding_proxies(config.JSON_DUMP_DIRECTORY_PATH, tfp.AllFindingsInOneGroup)

#test_finding_proxies_in_cpd_file(os.path.join(config.JSON_DUMP_DIRECTORY_PATH, "Cpd-0016.json"), tfp.AllFindingsInOneGroup)

#test_all_cpds_all_finding_proxies(config.JSON_DUMP_DIRECTORY_PATH, tfp.AllFindingsInOneGroup, test_all_cpds_except_these = [3,4,6,7,8,9,11,14,15,16])
#test_all_cpds_all_finding_proxies(config.JSON_DUMP_DIRECTORY_PATH, tfp.AllFindingsInOneGroup, test_all_cpds_except_these = [3,4,6,7,8,9,11,14,15,16,17,19,20,24,26,27])
# tfp.test_all_cpds_all_finding_proxies(
# 	config.JSON_DUMP_DIRECTORY_PATH,
# 	tfp.AllFindingsInOneGroup,
# 	error_log_filepath = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/FindingProxyTests/error_log.2022-07-14T08:21:11PDT.txt",
# 	test_all_cpds_except_these = [3,4,6,7,8,9,11,14,15,16,17,19,20,24,26,27,28,29,32])

# tfp.test_all_cpds_all_finding_proxies(
# 	config.JSON_DUMP_DIRECTORY_PATH,
# 	tfp.OneFindingPerGroup,
# 	error_log_filepath = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/FindingProxyTests/error_log.OneFindingPerGroup.2022-07-14T2128.txt",
# 	test_all_cpds_except_these = [])

# tfp.test_finding_proxies_in_cpd_file(
# 	os.path.join(config.JSON_DUMP_DIRECTORY_PATH, "Cpd-0027.json"),
# 	grouping_type = tfp.OneFindingPerGroup,
# 	error_log_filepath = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/FindingProxyTests/junk_test.txt")

# First test of 
# tfp.test_finding_proxies_in_cpd_file(
# 	"UnitTestStuff/TestJsonDumpDir/Cpd-0004.json",
# 	grouping_type = tfp.AllFindingsInOneGroup,
# 	error_log_filepath = "../Logs-Generic/FindingProxyTests/test_2022-07-19.txt")


# VerifyThatBotNeverAddsFindings
# we have a tmp hack that we are verifying that for all proxies in all consuls finding prox endpoint never adds any findings.

# tfp.test_all_cpds_all_finding_proxies(
# 	config.JSON_DUMP_DIRECTORY_PATH,
# 	tfp.OneFindingPerGroup,
# 	error_log_filepath = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/FindingProxyTests/error_log.VerifyThatBotNeverAddsFindings.OneFindingPerGroup.2022-07-19T13:57:22PDT.txt",
#  	test_all_cpds_except_these = [])
#
# The above died on 29 with this error...
#
# requests.exceptions.ConnectionError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
#
# 


################
# Need to re-run the above and but do is starting at 29, skip over the stuff before that.

# print([cpd for cpd in tfp.get_all_cpd_nums_from_dir() if cpd < 29])
# [3, 4, 6, 7, 8, 9, 11, 14, 15, 16, 17, 19, 20, 24, 26, 27, 28]

# ALL_CPDS_WITH_ID_LESS_THAN_29 = [cpd for cpd in tfp.get_all_cpd_nums_from_dir() if cpd < 29]

# tfp.test_all_cpds_all_finding_proxies(
# 	config.JSON_DUMP_DIRECTORY_PATH,
# 	tfp.OneFindingPerGroup,
# 	error_log_filepath = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/FindingProxyTests/error_log.VerifyThatBotNeverAddsFindings.OneFindingPerGroup.From29-onward.2022-07-19T1702.txt",
#  	test_all_cpds_except_these = ALL_CPDS_WITH_ID_LESS_THAN_29)

# ALL_CPDS_WITH_ID_LESS_THAN_148 = [cpd for cpd in tfp.get_all_cpd_nums_from_dir() if cpd < 148]

# tfp.test_all_cpds_all_finding_proxies(
# 	config.JSON_DUMP_DIRECTORY_PATH,
# 	tfp.OneFindingPerGroup,
# 	error_log_filepath = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/FindingProxyTests/error_log.VerifyThatBotNeverAddsFindings.OneFindingPerGroup.From148-onward.2022-07-19T2223.txt",
#  	test_all_cpds_except_these = ALL_CPDS_WITH_ID_LESS_THAN_148)

# ALL_CPDS_WITH_ID_LESS_THAN_148 = [cpd for cpd in tfp.get_all_cpd_nums_from_dir() if cpd < 148]

# tfp.test_all_cpds_all_finding_proxies(
# 	config.JSON_DUMP_DIRECTORY_PATH,
# 	tfp.OneFindingPerGroup,
# 	error_log_filepath = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/FindingProxyTests/error_log.VerifyThatBotNeverAddsFindings.OneFindingPerGroup.From148-onward.2022-07-20T09:35:12PDT.txt",
#  	test_all_cpds_except_these = ALL_CPDS_WITH_ID_LESS_THAN_148)

# 2022-07-21T09:21:20PDT FINALLY replaced
#
# 	user_json_fnds = user_json[findings']
# ...with...
# 	user_json_fnds = user_json['categories'][findings']
# See "DOH!" in teams with Miachael / Vijay 2022-07-20
#
# So, testing it
#tfp.test_finding_proxies_in_cpd_file("UnitTestStuff/TestJsonDumpDir/Cpd-0004.json", tfp.AllFindingsInOneGroup, "junk.txt")
# seemed to work

# ALL_CPDS_WITH_ID_LESS_THAN_148 = [cpd for cpd in tfp.get_all_cpd_nums_from_dir() if cpd < 148]

# tfp.test_all_cpds_all_finding_proxies(
# 	config.JSON_DUMP_DIRECTORY_PATH,
# 	tfp.OneFindingPerGroup,
# 	#error_log_filepath = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/FindingProxyTests/error_log.VerifyThatBotNeverAddsFindings.OneFindingPerGroup.StartAfresh.2022-07-21T0948.txt",
# 	# oops, misnamed bc I did not actually start afresh bc I acciednetally icluded the test_all_cpds_except_these = ALL_CPDS_WITH_ID_LESS_THAN_148)
# 	# So afte the run I did this
# 	# unix %mv error_log.VerifyThatBotNeverAddsFindings.OneFindingPerGroup.StartAfresh.2022-07-21T0948.txt error_log.VerifyThatBotNeverAddsFindings.OneFindingPerGroup.StartAfreshButFrom148.2022-07-21T0948.txt
# 	#
# 	error_log_filepath = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/FindingProxyTests/error_log.VerifyThatBotNeverAddsFindings.OneFindingPerGroup.StartAfreshButFrom148.2022-07-21T0948.txt",
#  	test_all_cpds_except_these = ALL_CPDS_WITH_ID_LESS_THAN_148)

ALL_CPDS_WITH_ID_LESS_THAN_148 = [cpd for cpd in tfp.get_all_cpd_nums_from_dir() if cpd < 148]

# 2022-07-21T13:04:47PDT started the below
# tfp.test_all_cpds_all_finding_proxies(
# 	config.JSON_DUMP_DIRECTORY_PATH,
# 	tfp.OneFindingPerGroup,
# 	error_log_filepath = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/FindingProxyTests/error_log.VerifyThatBotNeverAddsFindings.OneFindingPerGroup.DoesItHangOn148Again.2022-07-21T1304.txt",
#  	test_all_cpds_except_these = ALL_CPDS_WITH_ID_LESS_THAN_148)

# 2022-07-21T14:46:54PDT

# the above died on CPD 148 but a different program.  Michale just
# increased number of instances from 1 to a range from 2 to 5.  hope
# that will fix the throwing of the http.client.RemoteDisconnected:
# Remote end closed connection without response

# 2022-07-21T1448 
# (Long after, i.e. at 2022-08-16T06:57:32PDT, this timestamp was put here based on file's last write date )
# tfp.test_all_cpds_all_finding_proxies(
# 	config.JSON_DUMP_DIRECTORY_PATH,
# 	tfp.OneFindingPerGroup,
# 	error_log_filepath = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/FindingProxyTests/error_log.VerifyThatBotNeverAddsFindings.OneFindingPerGroup.DoesItHangOn148AgainNowScaledOut.2022-07-21T1447.txt",
#  	test_all_cpds_except_these = ALL_CPDS_WITH_ID_LESS_THAN_148)

# tfp.test_all_cpds_all_finding_proxies(
# 	config.JSON_DUMP_DIRECTORY_PATH,
# 	tfp.OneFindingPerGroup,
# 	error_log_filepath = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/FindingProxyTests/error_log.OneFindingPerGroup.AreAllIssuesResolved.2022-08-16T0659.txt",
#  	test_all_cpds_except_these = [])

ALL_CPDS_WITH_ID_LESS_THAN_24 = [cpd for cpd in tfp.get_all_cpd_nums_from_dir() if cpd < 24]

# had to do this bc it seemed to hang here: see 2022-08-16T16:04:54PDT weird hang? in file:diary-TestCoupletPrograms.org

# print("################################################################")
# print("ALL_CPDS_WITH_ID_LESS_THAN_24")
# print(ALL_CPDS_WITH_ID_LESS_THAN_24)
#print("################################################################")

# tfp.test_all_cpds_all_finding_proxies(
# 	config.JSON_DUMP_DIRECTORY_PATH,
# 	tfp.OneFindingPerGroup,
# 	error_log_filepath = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/FindingProxyTests/error_log.OneFindingPerGroup.AreAllIssuesResolved.2022-08-16T0659.Cpd24_onward.txt",
#  	test_all_cpds_except_these = ALL_CPDS_WITH_ID_LESS_THAN_24)

################################################################

# got another problem see 2022-08-16T23:02:12PDT got this again(?) requests.exceptions.ConnectionError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
# in diary-TestCoupletPrograms.org
ALL_CPDS_WITH_ID_LESS_THAN_98 = [cpd for cpd in tfp.get_all_cpd_nums_from_dir() if cpd < 98]

# print("################################################################")
# print("ALL_CPDS_WITH_ID_LESS_THAN_98")
# print(ALL_CPDS_WITH_ID_LESS_THAN_98)
# print("################################################################")


# tfp.test_all_cpds_all_finding_proxies(
# 	config.JSON_DUMP_DIRECTORY_PATH,
# 	tfp.OneFindingPerGroup,
# 	error_log_filepath = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/FindingProxyTests/error_log.OneFindingPerGroup.AreAllIssuesResolved.2022-08-16T0659.Cpd98_onward.txt",
#  	test_all_cpds_except_these = ALL_CPDS_WITH_ID_LESS_THAN_98)

# got yes another problem see 2022-08-16T235737 RecNum: 29 from Cpd 148 http.client.RemoteDisconnected: Remote end closed connection without response
# in diary-TestCoupletPrograms.org

# ALL_CPDS_WITH_ID_LESS_THAN_148 = [cpd for cpd in tfp.get_all_cpd_nums_from_dir() if cpd < 148]

# print("################################################################")
# print("ALL_CPDS_WITH_ID_LESS_THAN_148")
# print(ALL_CPDS_WITH_ID_LESS_THAN_148)
# print("################################################################")


# tfp.test_all_cpds_all_finding_proxies(
# 	config.JSON_DUMP_DIRECTORY_PATH,
# 	tfp.OneFindingPerGroup,
# 	error_log_filepath = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/FindingProxyTests/error_log.OneFindingPerGroup.AreAllIssuesResolved.2022-08-16T0659.Cpd148_onward.txt",
#  	test_all_cpds_except_these = ALL_CPDS_WITH_ID_LESS_THAN_148)

# tfp.test_all_cpds_all_finding_proxies(
# 	config.JSON_DUMP_DIRECTORY_PATH,
# 	tfp.OneFindingPerGroup,
# 	error_log_filepath = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/FindingProxyTests/error_log.OneFindingPerGroup.AreAllIssuesResolved.2022-08-16T0659.Cpd148_onward.try_2.txt",
#  	test_all_cpds_except_these = ALL_CPDS_WITH_ID_LESS_THAN_148)

# ALL_CPDS_WITH_ID_LESS_THAN_149 = [cpd for cpd in tfp.get_all_cpd_nums_from_dir() if cpd < 149]

# print("################################################################")
# print("ALL_CPDS_WITH_ID_LESS_THAN_149")
# print(ALL_CPDS_WITH_ID_LESS_THAN_149)
# print("################################################################")


# tfp.test_all_cpds_all_finding_proxies(
# 	config.JSON_DUMP_DIRECTORY_PATH,
# 	tfp.OneFindingPerGroup,
# 	error_log_filepath = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/FindingProxyTests/error_log.OneFindingPerGroup.AreAllIssuesResolved.2022-08-16T0659.Cpd149_onward",
#  	test_all_cpds_except_these = ALL_CPDS_WITH_ID_LESS_THAN_149)

ALL_CPDS_EXCEPT_148 = [cpd for cpd in tfp.get_all_cpd_nums_from_dir() if cpd != 148]

print("################################################################")
print("ALL_CPDS_EXCEPT_148")
print(ALL_CPDS_EXCEPT_148)
print("################################################################")

# tfp.test_all_cpds_all_finding_proxies(
# 	config.JSON_DUMP_DIRECTORY_PATH,
# 	tfp.OneFindingPerGroup,
# 	error_log_filepath = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/FindingProxyTests/error_log.OneFindingPerGroup.Cpd148Only.FirstWithDurationMeasured.txt",
#  	test_all_cpds_except_these = ALL_CPDS_EXCEPT_148)


# tfp.test_all_cpds_all_finding_proxies(
# 	config.JSON_DUMP_DIRECTORY_PATH,
# 	tfp.OneFindingPerGroup,
# 	error_log_filepath = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/FindingProxyTests/error_log.OneFindingPerGroup.Cpd148Only.First-w-OneRetryIfFail.txt",
#  	test_all_cpds_except_these = ALL_CPDS_EXCEPT_148)

# tfp.test_all_cpds_all_finding_proxies(
# 	config.JSON_DUMP_DIRECTORY_PATH,
# 	tfp.OneFindingPerGroup,
# 	error_log_filepath = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/FindingProxyTests/error_log.OneFindingPerGroup.Cpd148Only.2nd-w-OneRetryIfFail.txt",
#  	test_all_cpds_except_these = ALL_CPDS_EXCEPT_148)

# tfp.test_all_cpds_all_finding_proxies(
# 	config.JSON_DUMP_DIRECTORY_PATH,
# 	tfp.OneFindingPerGroup,
# 	error_log_filepath = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/FindingProxyTests/error_log.OneFindingPerGroup.Cpd148Only.3rd-w-OneRetryIfFail.txt",
#  	test_all_cpds_except_these = ALL_CPDS_EXCEPT_148)

# The above had a bug if there were two failures.  I fixed that and added some logging info in the below:

# tfp.test_all_cpds_all_finding_proxies(
# 	config.JSON_DUMP_DIRECTORY_PATH,
# 	tfp.OneFindingPerGroup,
#  	error_log_filepath = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/FindingProxyTests/error_log.OneFindingPerGroup.Cpd148Only.4th-w-OneRetryIfFail.txt",
#  	test_all_cpds_except_these = ALL_CPDS_EXCEPT_148)

# dunno why the above failed changed if to elif
# tfp.test_all_cpds_all_finding_proxies(
# 	config.JSON_DUMP_DIRECTORY_PATH,
# 	tfp.OneFindingPerGroup,
#  	error_log_filepath = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/FindingProxyTests/error_log.OneFindingPerGroup.Cpd148Only.5th-w-OneRetryIfFail.txt",
#  	test_all_cpds_except_these = ALL_CPDS_EXCEPT_148)

# tfp.test_all_cpds_all_finding_proxies(
# 	config.JSON_DUMP_DIRECTORY_PATH,
# 	tfp.OneFindingPerGroup,
#  	error_log_filepath = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/FindingProxyTests/error_log.junk_for_debugging.txt",
#  	test_all_cpds_except_these = ALL_CPDS_EXCEPT_148)

# tfp.test_all_cpds_all_finding_proxies(
# 	config.JSON_DUMP_DIRECTORY_PATH,
# 	tfp.OneFindingPerGroup,
#  	error_log_filepath = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/FindingProxyTests/error_log.OneFindingPerGroup.Cpd148Only.6th-w-OneRetryIfFail.txt",
#  	test_all_cpds_except_these = ALL_CPDS_EXCEPT_148)

# The above died when we had a non 200 post_reponse.status_code.  So I
# decided to fix that in a princpled way (and knock off a TODO from
# Vijay) so the new hopefully workign substantial refacotr is here:

# tfp.test_all_cpds_all_finding_proxies(
# 	config.JSON_DUMP_DIRECTORY_PATH,
# 	tfp.OneFindingPerGroup,
#  	error_log_filepath = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/FindingProxyTests/error_log.OneFindingPerGroup.Cpd148Only.7th-w-OneRetryIfFail.txt",
#  	test_all_cpds_except_these = ALL_CPDS_EXCEPT_148)

# maybe the mosts salient change is that if there is a non 200
# responise, then we retry one time.  and if again, we contine on to
# the next combination of contributing findings.

# 2022-09-06T08:24:27PDT the above was a failure bc I did not add a print statement to the print_4_grep function

# tfp.test_all_cpds_all_finding_proxies(
# 	config.JSON_DUMP_DIRECTORY_PATH,
# 	tfp.OneFindingPerGroup,
#  	error_log_filepath = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/FindingProxyTests/error_log.OneFindingPerGroup.Cpd148Only.8th-w-OneRetryIfFail.txt",
#  	test_all_cpds_except_these = ALL_CPDS_EXCEPT_148)

# 2022-09-08T11:45:49PDT the above was the first complete run!!!

# 2022-09-08T11:46:06PDT hopefully the below has better and final logging for the 4grep hack.
# trying again to get stats on where the slowness is

# tfp.test_all_cpds_all_finding_proxies(
# 	config.JSON_DUMP_DIRECTORY_PATH,
# 	tfp.OneFindingPerGroup,
#  	error_log_filepath = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/FindingProxyTests/error_log.OneFindingPerGroup.Cpd148Only.9th-w-OneRetryIfFail.txt",
#  	test_all_cpds_except_these = ALL_CPDS_EXCEPT_148)

# tfp.test_all_cpds_all_finding_proxies(
# 	config.JSON_DUMP_DIRECTORY_PATH,
# 	tfp.OneFindingPerGroup,
#  	error_log_filepath = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/FindingProxyTests/error_log.OneFindingPerGroup.Cpd148Only.10th-w-OneRetryIfFail.txt",
#  	test_all_cpds_except_these = ALL_CPDS_EXCEPT_148)

# above had to do bc forced shutdown bc of sysadmi want me to install new vesion of os.
# belo machine rebooted, dunno wny.

tfp.test_all_cpds_all_finding_proxies(
	config.JSON_DUMP_DIRECTORY_PATH,
	tfp.OneFindingPerGroup,
 	error_log_filepath = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/FindingProxyTests/error_log.OneFindingPerGroup.Cpd148Only.11th-w-OneRetryIfFail.txt",
 	test_all_cpds_except_these = ALL_CPDS_EXCEPT_148)


