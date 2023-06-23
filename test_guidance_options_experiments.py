# test_guidance_options_experiments.py
# 2022-11-09T09:50:19PST

import os

################################################################
from config import LOG_DIR_FULL_SCALE_TEST_GUIDANCE_OPTIONS

# at 2023-01-10T19:56:32PST this is:
# "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/GenDataForTestGuidOpt-FullScale"

################################################################

#from test_guidance_options import test_guidance_options_from_many_dirs
#from test_guidance_options import test_guidance_options_full_scale

import test_guidance_options as tgo

#test_log_basedir = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/GenDataForTestGuidOpt/2022-11-08T2242.ChildrensConsults_not_suffering_Consys_322/"
#test_guidance_options_from_many_dirs(dir_of_dirs = test_log_basedir, verbose_p = True)

#test_log_basedir = "/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/GenDataForTestGuidOpt/2022-11-08T1034.BirthSexFirst_Height_Weight_AllZeroUnlessError_Okay"
#test_guidance_options_from_many_dirs(dir_of_dirs = test_log_basedir, verbose_p = True)

#test_guidance_options_full_scale(os.path.join(LOG_DIR_FULL_SCALE_TEST_GUIDANCE_OPTIONS, "2022-12-19T120104"))

#tgo.test_guidance_options_full_scale(os.path.join(LOG_DIR_FULL_SCALE_TEST_GUIDANCE_OPTIONS, "2023-01-03T221146.1st_w_random_answers"))

# tgo.test_guidance_options_full_scale(os.path.join(LOG_DIR_FULL_SCALE_TEST_GUIDANCE_OPTIONS, "2023-01-10T070544.1st_w_random_answers"))
# 2023-01-10T1958 last file write date just before commenting out the above line

################################################################
#

# tgo.test_guidance_options_full_scale(os.path.join(LOG_DIR_FULL_SCALE_TEST_GUIDANCE_OPTIONS, "2023-01-10T232657.run_004_w_random_answers"))

# 2023-01-17T21:23:24PST Why did I choose 2023-01-10T232657.run_004_w_random_answers?
#

# because I think it was the next consult service run that was not fed
# through guidance options.  I believe the last time guidance options
# were tested was on "2023-01-10T070544.1st_w_random_answers".

# So, what was the next real run of consult service?  Well do this...

# (env) william.jarrold@SC7618 GenDataForTestGuidOpt-FullScale % ls
# ls
# <... cut out a bunch of lines ...> 
# 2022-12-28T000447.1st_w_random_answers
# 2023-01-03T221146.1st_w_random_answers
# 2023-01-10T070544.1st_w_random_answers
# 2023-01-10T232500.run_004_w_random_answers
# 2023-01-10T232540.run_004_w_random_answers
# 2023-01-10T232554.run_004_w_random_answers
# 2023-01-10T232657.run_004_w_random_answers
# 2023-01-17T101224.run_004_w_random_answers

# So it had to be one of the 2023-01-10 runs that needed to be tested
# with Guidance Options.  which one?  Well look at the sizes, I bet it
# was a stirng of failed runs that lasted just a short bit, finally
# where one succeeded, likely the last one and that should have a LOT
# more content.  That's what I faintly remember.  So, what do dir
# sizes for 2023-01-10 look like?

# (env) william.jarrold@SC7618 GenDataForTestGuidOpt-FullScale % du -skh 2023-01-10T23*/
# du -skh 2023-01-10T23*/
# 80K	2023-01-10T232500.run_004_w_random_answers/
# 16K	2023-01-10T232540.run_004_w_random_answers/
# 20K	2023-01-10T232554.run_004_w_random_answers/
# 31M	2023-01-10T232657.run_004_w_random_answers/

# Clearly 2023-01-10T232657.run_004_w_random_answers/ fits this pattern and MUST be the next one.

# (just I had though before verifying all of this) bc the 10th of jan was a tuesay.  I started a run
# on tuesday hoping it would be done in time before the meeting on wed.

# So, that is why I did
#### tgo.test_guidance_options_full_scale(os.path.join(LOG_DIR_FULL_SCALE_TEST_GUIDANCE_OPTIONS, "2023-01-10T232657.run_004_w_random_answers"))
# immedateily above.

################################################################

#tgo.test_guidance_options_full_scale(os.path.join(LOG_DIR_FULL_SCALE_TEST_GUIDANCE_OPTIONS, "2023-01-31T195050.run_007_w_random_answers/"))

# tgo.test_guidance_options_full_scale(os.path.join(LOG_DIR_FULL_SCALE_TEST_GUIDANCE_OPTIONS, "2023-01-31T195050.run_007_w_random_answers/"), reverse_order_p = True)
# The purpose of the above was to see if I could reproduce this error:
# "error":"Collection contains no element matching the predicate."} Error

# That I had been getting around 2023-02-06.  As of
# 2023-02-07T21:52:28PST I have not been able to reproduce it, however
# the above only has like 2 consutls.  Whathappened to the others?

#tgo.test_guidance_options_full_scale(os.path.join(LOG_DIR_FULL_SCALE_TEST_GUIDANCE_OPTIONS, "2023-02-06T115937.run_class_08_focused_col_contains_no_ele_matching_pred"), reverse_order_p = True)

#tgo.test_guidance_options_full_scale(os.path.join(LOG_DIR_FULL_SCALE_TEST_GUIDANCE_OPTIONS, "2023-02-06T115937.run_class_08_focused_col_contains_no_ele_matching_pred"), reverse_order_p = True, sync_to_health_profile_p=False)
# 2023-02-07T22:56:04PST trying this for jesse

#tgo.test_guidance_options_full_scale(os.path.join(LOG_DIR_FULL_SCALE_TEST_GUIDANCE_OPTIONS, "2023-02-07T110247.run_class_09_just_time_to_go_through_everything_again"), reverse_order_p = True, sync_to_health_profile_p=False)

#tgo.test_guidance_options_full_scale(os.path.join(LOG_DIR_FULL_SCALE_TEST_GUIDANCE_OPTIONS, "2023-02-12T141528.run_class_09_just_time_to_go_through_everything_again"), reverse_order_p = True, sync_to_health_profile_p=False)
# 2023-02-12T195849

tgo.test_guidance_options_full_scale(os.path.join(LOG_DIR_FULL_SCALE_TEST_GUIDANCE_OPTIONS, "2023-02-12T141528.run_class_09_just_time_to_go_through_everything_again"), reverse_order_p = True, sync_to_health_profile_p=True)
# 2023-02-12T22:18:30PST
