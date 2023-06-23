# summarize_test_question_driver_scale_up_results.sh
# PURPOSE

# A hacky, not guarantted to be full way of seeig a top level view of the result of a run of test_question_driver_scale_up.py

MY_DIR=/Users/william.jarrold/ShCr/AskMD/Resources/Couplet/TestCoupletPrograms/Logs-Generic/GenDataForTestGuidOpt-FullScale/$1

echo TODO: put post_response.status_code if not nominal in summary report

echo "################################################################"
echo "Here are the error files:"

ls $MY_DIR/*/Err*

echo "################################################################"
echo "Max retries exceeded with url"

grep "Max retries exceeded with url" $MY_DIR/*/Err*

echo "################################################################"
echo "Here are the read timed out ones:"

grep "Read timed out" $MY_DIR/*/Err*

echo "################################################################"
echo "Here are the bot error ones"

grep "BotError JSON" $MY_DIR/*/*/conversation_text.org

echo "################################################################"
echo "Here's the number of Questions (technically lines w BotSubQuestion in conversation_text.org (close to tot number questions): "
# This was devised here...
#grep status 2023-02-12T141528.run_class_09_just_time_to_go_through_everything_again/*/*/conversation_text.org | wc -l
# ...and now it is generalized
grep BotSubQuestion $MY_DIR/*/*/conversation_text.org | wc -l

echo "################################################################"
# This was devised here...
#grep post_response.status_code 2023-02-12T141528.run_class_09_just_time_to_go_through_everything_again/*/*/conversation_text.org | awk '{print $2}' | sort | uniq -c | sort -nr
# ...and now it is generalized
echo "for each post_response.status_code how many times did that occur:"
echo "NUM: CODE:"
grep post_response.status_code $MY_DIR/*/*/conversation_text.org | awk '{print $2}' | sort | uniq -c | sort -nr


echo "################################################################"
echo "number of run groups"

ls -d $MY_DIR/*/ | wc -l


echo "number of run groups with GuidanceOptionsResults"

ls -d $MY_DIR/*/GuidanceOptionsResults/ | wc -l

#echo "Guidance Option Result Dirs"
# ls -d $MY_DIR/*/GuidanceOptionsResults/*/
# too much screen spew.
################################################################
#ls -d $MY_DIR/*/* | wc -l

# TODO check the run duration logs:
# wc -l */*/run_duration_log.tsv

echo TODO make sure that Total Duration Of Scale Up Run gets saved in a nice easy to find place


