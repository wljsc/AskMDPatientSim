################################################################
# PURPOSE (start of section)

# Purpose is to contain all of the parameters releavnt to
# configuration to make this code very easy to port to different
# contexts / configurations etc.

# NOTE that this file was created a while after much of the coding
# happened.  As a result, as of 2022-07-11, many relevant
# configuration parameters may be burried in other files.

# PURPOSE (end of section)
################################################################
# HISTORY of this file (start of section)
# put newest on top

# 2022-07-11T17:45:05PDT created this file, i.e. config.py

# HISTORY of this file (end of section)
################################################################
# IMPORTS

import os


################################################################
# CONSTANTS (start of section)

QUESTION_DRIVER_ENDPOINT = "https://api.qa.sharecare.com/consultation/next"

FINDING_PROXY_ENDPOINT = "https://api.qa.sharecare.com/consultation/results/findings"

#GUIDANCE_OPTIONS_ENDPOINT = "https://api.dev.sharecare.com/consultation/results/guidance-options"
# 2023-02-01T12:32:20PST replaced the above with the below
GUIDANCE_OPTIONS_ENDPOINT = "https://api.qa.sharecare.com/consultation/results/guidance-options"

JSON_DUMP_DIRECTORY_PATH = "/Users/william.jarrold/ShCr/AskMD/Code/Packages/Consultation.API7/Consultation.API/app-data/couplet/consults/2022-02-04-Draft13.fixed"

# TODO move the next line to a local config
LOG_DIR_GENERIC				 = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/"

LOG_DIR_TEST_GUIDANCE_OPTIONS		 = os.path.join(LOG_DIR_GENERIC, "GenDataForTestGuidOpt/")
LOG_DIR_FULL_SCALE_TEST_GUIDANCE_OPTIONS = os.path.join(LOG_DIR_GENERIC, "GenDataForTestGuidOpt-FullScale")
LOG_DIR_AD_HOC_TEST_GUIDANCE_OPTIONS	 = os.path.join(LOG_DIR_GENERIC, "AdHocGuidOptTests")


################################################################

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

################################################################

