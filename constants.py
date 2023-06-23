################################################################
# CONSTANTS (start of section)

TRYING_TO_MIMIC_RegressionTestLogs2_P = True

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

# CONVERSATION_INVARIANT_MODE_P used to be defined here but at 2022-09-17T21:06:09PDT
# it was moved to config.


########
#
# DIR_OF_CPD_FILES =
# "/Users/william.jarrold/ShCr/AskMD/Code/Packages/Consultation.API7/Consultation.API/app-data/couplet/consults/2022-02-04-Draft13"
#
# 2022-06-14T11:57:23EDT changing the above to this (i.e. adding
# .fixed)

DIR_OF_CPD_FILES = "/Users/william.jarrold/ShCr/AskMD/Code/Packages/Consultation.API7/Consultation.API/app-data/couplet/consults/2022-02-04-Draft13.fixed"

#
########

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

################################
# Define ASK_OPERATOR_HOW_TO_HANDLE_BOT_ERROR_STR <start of section>

# Defining this here merely to increase the readability of the function that calls it.
# i.e. @func user_input_wrapper

ASK_OPERATOR_HOW_TO_HANDLE_BOT_ERROR_STR =\
"""

STATUS: Okay the bot has thrown an error.

We are AUTO-MODE however the response_policy is 'AnswerZero-UnlessBotError'

(Aside: by 'BotError' we we mean the AskMD Consultation Service.
We do *not* mean the Sharecare ChatBot)")

In other words the value for 'policyInAutoMode' specified in the file specified")
by @param user_reply_script_json is 'AnswerZero-UnlessBotError'")

Thus we need to ESCAPE OUT OF AUTO-MODE and ask you the human operator what to do.

So, see the options you were prompted for above and chose one.

"""

# Define ASK_OPERATOR_HOW_TO_HANDLE_BOT_ERROR_STR <end of section>
################################

DEFAULT_SLEEP_DURATION_TO_MITIGATE_MAX_RETRIES_ERROR = 0.2
# 2023-02-11T23:57:55PST cheanging the sleep to 0.2 sec now that I am trying to set max retries to 10 w 1 sec backoff
# DEFAULT_SLEEP_DURATION_TO_MITIGATE_MAX_RETRIES_ERROR = 1
# 2023-02-11T15:05:05PST changed from 3 to 1 bc trying "timeout = 1"
#DEFAULT_SLEEP_DURATION_TO_MITIGATE_MAX_RETRIES_ERROR = 3
# 2023-01-10T22:24:41PST Set this to 2 seconds.  A few days before 
# now the sleep was just hard-coded.
#
# See diary-TestCoupletPrograms.org 2023-01-03T22:12:17PST trying
#  again - got a bunch of the max tries bug before - trying now with a
#  2 sec sleep before and after
# 
# 


# CONSTANTS (end of section)
################################################################
