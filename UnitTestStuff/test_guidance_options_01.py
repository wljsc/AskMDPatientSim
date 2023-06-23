# test_guidance_options_01.py

# INPUT_FOR_TEST_O1_OF_POST_FINDINGS_TO_GUIDANCE_OPTIONS Was derived
# at 2022-09-28T07:33:14PDT via a copy-n-edit of
# Q040-bot-quest-IdNO_QUES_ID_BC_NO_MORE_QUESTIONS.json
# from ... TestCoupletPrograms/TstCoupProgLogs/Consult.2022-09-27T2232-Cpd-320/



# INPUT_FOR_TEST_O1_OF_POST_FINDINGS_TO_GUIDANCE_OPTIONS = \
# {
#     "consultationId": 320,
#     "findings": [
#         {
#             "entNo": 12100,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "female",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 31314,
#             "keywords": [
#                 {
#                     "name": "AgeRange",
#                     "parameters": "0 yr, 18 yr"
#                 }
#             ],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "date of birth",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": {
#                 "value": "2/13/2013",
#                 "valueType": "DATE",
#                 "valueTypeUnit": null
#             }
#         },
#         {
#             "entNo": 26479,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "age",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": {
#                 "value": 9.0,
#                 "valueType": "TIMESPAN",
#                 "valueTypeUnit": 1
#             }
#         },
#         {
#             "entNo": 51747,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": false,
#             "state": "ABSENT",
#             "text": "headache occurs around the time of menstrual period",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 44430,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": false,
#             "state": "ABSENT",
#             "text": "menstrual periods stopped in the past few months",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 62256,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": false,
#             "state": "ABSENT",
#             "text": "menstrual bleeding pattern or flow changed in past few month",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 62499,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": false,
#             "state": "ABSENT",
#             "text": "tampon use in the past 5 days",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 25051,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": false,
#             "state": "ABSENT",
#             "text": "pregnant currently",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 23966,
#             "keywords": [],
#             "mmp": 4201,
#             "note": null,
#             "present": false,
#             "state": "ABSENT",
#             "text": "possibly pregnant",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 42763,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": false,
#             "state": "ABSENT",
#             "text": "childbirth in the past 6 weeks",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 1428,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": false,
#             "state": "ABSENT",
#             "text": "drinks alcohol",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 46071,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": false,
#             "state": "ABSENT",
#             "text": "uses cannabis",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 42305,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": false,
#             "state": "ABSENT",
#             "text": "uses cocaine",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 44647,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": false,
#             "state": "ABSENT",
#             "text": "uses other recreational drugs",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 42797,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": false,
#             "state": "ABSENT",
#             "text": "has injected recreational drugs",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 51605,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": false,
#             "state": "ABSENT",
#             "text": "has had sex in the past few months",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 64726,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": false,
#             "state": "ABSENT",
#             "text": "bulging at soft spaces (fontanelles) on top of head",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 66518,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": false,
#             "state": "ABSENT",
#             "text": "no bulging at soft spaces (fontanelles) on top of head",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 16645,
#             "keywords": [
#                 {
#                     "name": "ChildHeight",
#                     "parameters": null
#                 },
#                 {
#                     "name": "Range",
#                     "parameters": "12 in, 96 in"
#                 }
#             ],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "height",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": {
#                 "value": 1.27,
#                 "valueType": "LENGTH",
#                 "valueTypeUnit": 6
#             }
#         },
#         {
#             "entNo": 16647,
#             "keywords": [
#                 {
#                     "name": "BodyWeight",
#                     "parameters": null
#                 },
#                 {
#                     "name": "Range",
#                     "parameters": "5 lb, 999 lb"
#                 }
#             ],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "weight",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": {
#                 "value": 29.48350405,
#                 "valueType": "WEIGHT",
#                 "valueTypeUnit": 6
#             }
#         },
#         {
#             "entNo": 4769,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "body mass index (BMI)",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": {
#                 "value": 18.279809070618143,
#                 "valueType": "ABSOLUTE_NUMBER",
#                 "valueTypeUnit": null
#             }
#         },
#         {
#             "entNo": 65442,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "headache began in the past 24 hours",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 60772,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "headache occurs continuously",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 55859,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": false,
#             "state": "ABSENT",
#             "text": "headache lasts less than 1 minute",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 55855,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": false,
#             "state": "ABSENT",
#             "text": "headache lasts for minutes",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 65449,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": false,
#             "state": "ABSENT",
#             "text": "headache lasts for hours",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 17496,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": false,
#             "state": "ABSENT",
#             "text": "headache lasts most of the day to several days",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 61869,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "headache problem is getting worse",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 65448,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "headache all over the head",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 5237,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": false,
#             "state": "ABSENT",
#             "text": "pain behind the eye",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 2131,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": false,
#             "state": "ABSENT",
#             "text": "headache in the forehead area",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 2755,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": false,
#             "state": "ABSENT",
#             "text": "headache over the temple",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 2132,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": false,
#             "state": "ABSENT",
#             "text": "headache over the back of the head",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 61864,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": false,
#             "state": "ABSENT",
#             "text": "other headache location",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 61866,
#             "keywords": [
#                 {
#                     "name": "Range",
#                     "parameters": "1,10;1"
#                 }
#             ],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "headache severity (1-10)",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": {
#                 "value": "0",
#                 "valueType": "ABSOLUTE_NUMBER",
#                 "valueTypeUnit": null
#             }
#         },
#         {
#             "entNo": 5096,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "sudden headache that is one of worst of child's life",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 59391,
#             "keywords": [],
#             "mmp": 3215,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "headache preceded by an aura",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 43027,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "bump, blow, or jolt to the head or neck in past few weeks",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 65473,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "lost consciousness with injury or accident in past few days",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 65451,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "headache treatment previously tried",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": {
#                 "value": "0",
#                 "valueType": "ABSOLUTE_STRING",
#                 "valueTypeUnit": null
#             }
#         },
#         {
#             "entNo": 22553,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "fainting during or after standing up",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 1168,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "facial pain",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 58408,
#             "keywords": [],
#             "mmp": 4027,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "travel or residence in Southern Africa in the past",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 1222,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "runny or stuffy nose",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 2506,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "snoring",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 269,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "nausea",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 356,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "joint pain",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 1136,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "flushing (reddening of the skin with a feeling of warmth)",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 42684,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "fever",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 42912,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "has had malaria",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 51747,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "headache occurs around the time of menstrual period",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 64745,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "sleeps with parent",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 64429,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "swallowed untreated water in the past few weeks",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 45246,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "mosquito bite in the past few weeks",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 64519,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "bird exposure in the past few weeks",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 58402,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "travel or residence outside of the US and Canada in the past",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 58864,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "has been in a developing country in the past",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 59383,
#             "keywords": [
#                 {
#                     "name": "HideIfAbsent",
#                     "parameters": "58864"
#                 }
#             ],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "travel or residence in developing country in past few months",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 42728,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "current medication: hydralazine",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 64731,
#             "keywords": [],
#             "mmp": 4779,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "current medication: ADHD drug",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 28426,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "other current medication",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": {
#                 "value": "0",
#                 "valueType": "ABSOLUTE_STRING",
#                 "valueTypeUnit": null
#             }
#         },
#         {
#             "entNo": 44124,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "other current over-the-counter drug or supplement",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": {
#                 "value": "0",
#                 "valueType": "ABSOLUTE_STRING",
#                 "valueTypeUnit": null
#             }
#         },
#         {
#             "entNo": 60744,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "regularly take any type of headache or pain medication",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": null
#         },
#         {
#             "entNo": 46444,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "stopped taking a medication in the past few weeks",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": {
#                 "value": "0",
#                 "valueType": "ABSOLUTE_STRING",
#                 "valueTypeUnit": null
#             }
#         },
#         {
#             "entNo": 61875,
#             "keywords": [],
#             "mmp": null,
#             "note": null,
#             "present": true,
#             "state": "PRESENT",
#             "text": "other information that may be useful",
#             "type": "FINDING",
#             "uncertain": false,
#             "valueObject": {
#                 "value": "0",
#                 "valueType": "ABSOLUTE_STRING",
#                 "valueTypeUnit": null
#             }
#         }
#     ],
#     "questionId": 13
# }

INPUT_FOR_TEST_O1_OF_POST_FINDINGS_TO_GUIDANCE_OPTIONS = \
{
    "consultationId": 320,
    "findings": [
        {
            "entNo": 12100,
            "keywords": [],
            "present": True,
            "state": "PRESENT",
            "text": "female",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 31314,
            "keywords": [
                {
                    "name": "AgeRange",
                    "parameters": "0 yr, 18 yr"
                }
            ],
            "present": True,
            "state": "PRESENT",
            "text": "date of birth",
            "type": "FINDING",
            "uncertain": False,
            "valueObject": {
                "value": "2/13/2013",
                "valueType": "DATE",
            }
        },
        {
            "entNo": 26479,
            "keywords": [],
            "present": True,
            "state": "PRESENT",
            "text": "age",
            "type": "FINDING",
            "uncertain": False,
            "valueObject": {
                "value": 9.0,
                "valueType": "TIMESPAN",
                "valueTypeUnit": 1
            }
        },
        {
            "entNo": 51747,
            "keywords": [],
            "present": False,
            "state": "ABSENT",
            "text": "headache occurs around the time of menstrual period",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 44430,
            "keywords": [],
            "present": False,
            "state": "ABSENT",
            "text": "menstrual periods stopped in the past few months",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 62256,
            "keywords": [],
            "present": False,
            "state": "ABSENT",
            "text": "menstrual bleeding pattern or flow changed in past few month",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 62499,
            "keywords": [],
            "present": False,
            "state": "ABSENT",
            "text": "tampon use in the past 5 days",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 25051,
            "keywords": [],
            "present": False,
            "state": "ABSENT",
            "text": "pregnant currently",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 23966,
            "keywords": [],
            "mmp": 4201,
            "present": False,
            "state": "ABSENT",
            "text": "possibly pregnant",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 42763,
            "keywords": [],
            "present": False,
            "state": "ABSENT",
            "text": "childbirth in the past 6 weeks",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 1428,
            "keywords": [],
            "present": False,
            "state": "ABSENT",
            "text": "drinks alcohol",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 46071,
            "keywords": [],
            "present": False,
            "state": "ABSENT",
            "text": "uses cannabis",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 42305,
            "keywords": [],
            "present": False,
            "state": "ABSENT",
            "text": "uses cocaine",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 44647,
            "keywords": [],
            "present": False,
            "state": "ABSENT",
            "text": "uses other recreational drugs",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 42797,
            "keywords": [],
            "present": False,
            "state": "ABSENT",
            "text": "has injected recreational drugs",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 51605,
            "keywords": [],
            "present": False,
            "state": "ABSENT",
            "text": "has had sex in the past few months",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 64726,
            "keywords": [],
            "present": False,
            "state": "ABSENT",
            "text": "bulging at soft spaces (fontanelles) on top of head",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 66518,
            "keywords": [],
            "present": False,
            "state": "ABSENT",
            "text": "no bulging at soft spaces (fontanelles) on top of head",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 16645,
            "keywords": [
                {
                    "name": "ChildHeight",
                },
                {
                    "name": "Range",
                    "parameters": "12 in, 96 in"
                }
            ],
            "present": True,
            "state": "PRESENT",
            "text": "height",
            "type": "FINDING",
            "uncertain": False,
            "valueObject": {
                "value": 1.27,
                "valueType": "LENGTH",
                "valueTypeUnit": 6
            }
        },
        {
            "entNo": 16647,
            "keywords": [
                {
                    "name": "BodyWeight",
                },
                {
                    "name": "Range",
                    "parameters": "5 lb, 999 lb"
                }
            ],
            "present": True,
            "state": "PRESENT",
            "text": "weight",
            "type": "FINDING",
            "uncertain": False,
            "valueObject": {
                "value": 29.48350405,
                "valueType": "WEIGHT",
                "valueTypeUnit": 6
            }
        },
        {
            "entNo": 4769,
            "keywords": [],
            "present": True,
            "state": "PRESENT",
            "text": "body mass index (BMI)",
            "type": "FINDING",
            "uncertain": False,
            "valueObject": {
                "value": 18.279809070618143,
                "valueType": "ABSOLUTE_NUMBER",
            }
        },
        {
            "entNo": 65442,
            "keywords": [],
            "present": True,
            "state": "PRESENT",
            "text": "headache began in the past 24 hours",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 60772,
            "keywords": [],
            "present": True,
            "state": "PRESENT",
            "text": "headache occurs continuously",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 55859,
            "keywords": [],
            "present": False,
            "state": "ABSENT",
            "text": "headache lasts less than 1 minute",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 55855,
            "keywords": [],
            "present": False,
            "state": "ABSENT",
            "text": "headache lasts for minutes",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 65449,
            "keywords": [],
            "present": False,
            "state": "ABSENT",
            "text": "headache lasts for hours",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 17496,
            "keywords": [],
            "present": False,
            "state": "ABSENT",
            "text": "headache lasts most of the day to several days",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 61869,
            "keywords": [],
            "present": True,
            "state": "PRESENT",
            "text": "headache problem is getting worse",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 65448,
            "keywords": [],
            "present": True,
            "state": "PRESENT",
            "text": "headache all over the head",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 5237,
            "keywords": [],
            "present": False,
            "state": "ABSENT",
            "text": "pain behind the eye",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 2131,
            "keywords": [],
            "present": False,
            "state": "ABSENT",
            "text": "headache in the forehead area",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 2755,
            "keywords": [],
            "present": False,
            "state": "ABSENT",
            "text": "headache over the temple",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 2132,
            "keywords": [],
            "present": False,
            "state": "ABSENT",
            "text": "headache over the back of the head",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 61864,
            "keywords": [],
            "present": False,
            "state": "ABSENT",
            "text": "other headache location",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 61866,
            "keywords": [
                {
                    "name": "Range",
                    "parameters": "1,10;1"
                }
            ],
            "present": True,
            "state": "PRESENT",
            "text": "headache severity (1-10)",
            "type": "FINDING",
            "uncertain": False,
            "valueObject": {
                "value": "0",
                "valueType": "ABSOLUTE_NUMBER",
            }
        },
        {
            "entNo": 5096,
            "keywords": [],
            "present": True,
            "state": "PRESENT",
            "text": "sudden headache that is one of worst of child's life",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 59391,
            "keywords": [],
            "mmp": 3215,
            "present": True,
            "state": "PRESENT",
            "text": "headache preceded by an aura",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 43027,
            "keywords": [],
            "present": True,
            "state": "PRESENT",
            "text": "bump, blow, or jolt to the head or neck in past few weeks",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 65473,
            "keywords": [],
            "present": True,
            "state": "PRESENT",
            "text": "lost consciousness with injury or accident in past few days",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 65451,
            "keywords": [],
            "present": True,
            "state": "PRESENT",
            "text": "headache treatment previously tried",
            "type": "FINDING",
            "uncertain": False,
            "valueObject": {
                "value": "0",
                "valueType": "ABSOLUTE_STRING",
            }
        },
        {
            "entNo": 22553,
            "keywords": [],
            "present": True,
            "state": "PRESENT",
            "text": "fainting during or after standing up",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 1168,
            "keywords": [],
            "present": True,
            "state": "PRESENT",
            "text": "facial pain",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 58408,
            "keywords": [],
            "mmp": 4027,
            "present": True,
            "state": "PRESENT",
            "text": "travel or residence in Southern Africa in the past",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 1222,
            "keywords": [],
            "present": True,
            "state": "PRESENT",
            "text": "runny or stuffy nose",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 2506,
            "keywords": [],
            "present": True,
            "state": "PRESENT",
            "text": "snoring",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 269,
            "keywords": [],
            "present": True,
            "state": "PRESENT",
            "text": "nausea",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 356,
            "keywords": [],
            "present": True,
            "state": "PRESENT",
            "text": "joint pain",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 1136,
            "keywords": [],
            "present": True,
            "state": "PRESENT",
            "text": "flushing (reddening of the skin with a feeling of warmth)",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 42684,
            "keywords": [],
            "present": True,
            "state": "PRESENT",
            "text": "fever",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 42912,
            "keywords": [],
            "present": True,
            "state": "PRESENT",
            "text": "has had malaria",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 51747,
            "keywords": [],
            "present": True,
            "state": "PRESENT",
            "text": "headache occurs around the time of menstrual period",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 64745,
            "keywords": [],
            "present": True,
            "state": "PRESENT",
            "text": "sleeps with parent",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 64429,
            "keywords": [],
            "present": True,
            "state": "PRESENT",
            "text": "swallowed untreated water in the past few weeks",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 45246,
            "keywords": [],
            "present": True,
            "state": "PRESENT",
            "text": "mosquito bite in the past few weeks",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 64519,
            "keywords": [],
            "present": True,
            "state": "PRESENT",
            "text": "bird exposure in the past few weeks",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 58402,
            "keywords": [],
            "present": True,
            "state": "PRESENT",
            "text": "travel or residence outside of the US and Canada in the past",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 58864,
            "keywords": [],
            "present": True,
            "state": "PRESENT",
            "text": "has been in a developing country in the past",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 59383,
            "keywords": [
                {
                    "name": "HideIfAbsent",
                    "parameters": "58864"
                }
            ],
            "present": True,
            "state": "PRESENT",
            "text": "travel or residence in developing country in past few months",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 42728,
            "keywords": [],
            "present": True,
            "state": "PRESENT",
            "text": "current medication: hydralazine",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 64731,
            "keywords": [],
            "mmp": 4779,
            "present": True,
            "state": "PRESENT",
            "text": "current medication: ADHD drug",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 28426,
            "keywords": [],
            "present": True,
            "state": "PRESENT",
            "text": "other current medication",
            "type": "FINDING",
            "uncertain": False,
            "valueObject": {
                "value": "0",
                "valueType": "ABSOLUTE_STRING",
            }
        },
        {
            "entNo": 44124,
            "keywords": [],
            "present": True,
            "state": "PRESENT",
            "text": "other current over-the-counter drug or supplement",
            "type": "FINDING",
            "uncertain": False,
            "valueObject": {
                "value": "0",
                "valueType": "ABSOLUTE_STRING",
            }
        },
        {
            "entNo": 60744,
            "keywords": [],
            "present": True,
            "state": "PRESENT",
            "text": "regularly take any type of headache or pain medication",
            "type": "FINDING",
            "uncertain": False,
        },
        {
            "entNo": 46444,
            "keywords": [],
            "present": True,
            "state": "PRESENT",
            "text": "stopped taking a medication in the past few weeks",
            "type": "FINDING",
            "uncertain": False,
            "valueObject": {
                "value": "0",
                "valueType": "ABSOLUTE_STRING",
            }
        },
        {
            "entNo": 61875,
            "keywords": [],
            "present": True,
            "state": "PRESENT",
            "text": "other information that may be useful",
            "type": "FINDING",
            "uncertain": False,
            "valueObject": {
                "value": "0",
                "valueType": "ABSOLUTE_STRING",
            }
        }
    ],
}

TARGET_OUTPUT_FOR_TEST_O1_OF_POST_FINDINGS_TO_GUIDANCE_OPTIONS = {'consultationId': 320, 'consultationName': 'Headache in Children Diagnosis', 'guidanceOptions': [{'name': 'Common Causes', 'guidanceOptions': [{'name': 'Migraine', 'entityId': 726, 'recNo': '1', 'observedFindingCount': 0, 'totalFindingCount': 0, 'isPoptList': True, 'isRelSecondary': False, 'relType': 'EVIDENCE', 'extensionData': [], 'findings': [], 'planOptionCategories': [], 'commentLists': [], 'activeType': 0, 'types': [], 'uniqueTypes': []}, {'name': 'Sinusitis', 'entityId': 3519, 'recNo': '28', 'observedFindingCount': 0, 'totalFindingCount': 0, 'isPoptList': True, 'isRelSecondary': False, 'relType': 'EVIDENCE', 'extensionData': [], 'findings': [], 'planOptionCategories': [], 'commentLists': [], 'activeType': 0, 'types': [], 'uniqueTypes': []}, {'name': 'Drug use-related headache', 'entityId': 60452, 'recNo': '30', 'observedFindingCount': 0, 'totalFindingCount': 0, 'isPoptList': True, 'isRelSecondary': False, 'relType': 'EVIDENCE', 'extensionData': [], 'findings': [], 'planOptionCategories': [], 'commentLists': [], 'activeType': 0, 'types': [], 'uniqueTypes': []}, {'name': 'Menstrual migraine', 'entityId': 9937, 'recNo': '50', 'observedFindingCount': 0, 'totalFindingCount': 0, 'isPoptList': True, 'isRelSecondary': False, 'relType': 'EVIDENCE', 'extensionData': [], 'findings': [], 'planOptionCategories': [], 'commentLists': [], 'activeType': 0, 'types': [], 'uniqueTypes': []}, {'name': 'Coronavirus disease 2019 (COVID-19)', 'entityId': 66831, 'recNo': '6', 'observedFindingCount': 0, 'totalFindingCount': 0, 'isPoptList': True, 'isRelSecondary': False, 'relType': 'EVIDENCE', 'extensionData': [], 'findings': [], 'planOptionCategories': [], 'commentLists': [], 'activeType': 0, 'types': [], 'uniqueTypes': []}, {'name': 'Medication-related headache', 'entityId': 26256, 'recNo': '8', 'observedFindingCount': 0, 'totalFindingCount': 0, 'isPoptList': True, 'isRelSecondary': False, 'relType': 'EVIDENCE', 'extensionData': [], 'findings': [], 'planOptionCategories': [], 'commentLists': [], 'activeType': 0, 'types': [], 'uniqueTypes': []}, {'name': 'Medication overuse headache', 'entityId': 14227, 'recNo': '99', 'observedFindingCount': 0, 'totalFindingCount': 0, 'isPoptList': True, 'isRelSecondary': False, 'relType': 'EVIDENCE', 'extensionData': [], 'findings': [], 'planOptionCategories': [], 'commentLists': [], 'activeType': 0, 'types': [], 'uniqueTypes': []}]}, {'name': 'Less Common Causes', 'guidanceOptions': [{'name': 'Malaria', 'entityId': 1250, 'recNo': '111', 'observedFindingCount': 0, 'totalFindingCount': 0, 'isPoptList': True, 'isRelSecondary': False, 'relType': 'EVIDENCE', 'extensionData': [], 'findings': [], 'planOptionCategories': [], 'commentLists': [], 'activeType': 0, 'types': [], 'uniqueTypes': []}, {'name': 'Hydrocephalus', 'entityId': 1105, 'recNo': '12', 'observedFindingCount': 0, 'totalFindingCount': 0, 'isPoptList': True, 'isRelSecondary': False, 'relType': 'EVIDENCE', 'extensionData': [], 'findings': [], 'planOptionCategories': [], 'commentLists': [], 'activeType': 0, 'types': [], 'uniqueTypes': []}, {'name': 'Takayasu arteritis', 'entityId': 691, 'recNo': '120', 'observedFindingCount': 0, 'totalFindingCount': 0, 'isPoptList': True, 'isRelSecondary': False, 'relType': 'EVIDENCE', 'extensionData': [{'name': 'Emergent'}], 'findings': [], 'planOptionCategories': [], 'commentLists': [], 'activeType': 0, 'types': [], 'uniqueTypes': []}, {'name': 'New daily persistent headache', 'entityId': 60768, 'recNo': '22', 'observedFindingCount': 0, 'totalFindingCount': 0, 'isPoptList': True, 'isRelSecondary': False, 'relType': 'EVIDENCE', 'extensionData': [], 'findings': [], 'planOptionCategories': [], 'commentLists': [], 'activeType': 0, 'types': [], 'uniqueTypes': []}, {'name': 'Meningitis', 'entityId': 644, 'recNo': '24', 'observedFindingCount': 0, 'totalFindingCount': 0, 'isPoptList': True, 'isRelSecondary': False, 'relType': 'EVIDENCE', 'extensionData': [{'name': 'Emergent'}], 'findings': [], 'planOptionCategories': [], 'commentLists': [], 'activeType': 0, 'types': [], 'uniqueTypes': []}, {'name': 'Lyme disease', 'entityId': 756, 'recNo': '45', 'observedFindingCount': 0, 'totalFindingCount': 0, 'isPoptList': True, 'isRelSecondary': False, 'relType': 'EVIDENCE', 'extensionData': [], 'findings': [], 'planOptionCategories': [], 'commentLists': [], 'activeType': 0, 'types': [], 'uniqueTypes': []}, {'name': 'Cysticercosis', 'entityId': 37482, 'recNo': '61', 'observedFindingCount': 0, 'totalFindingCount': 0, 'isPoptList': True, 'isRelSecondary': False, 'relType': 'EVIDENCE', 'extensionData': [], 'findings': [], 'planOptionCategories': [], 'commentLists': [], 'activeType': 0, 'types': [], 'uniqueTypes': []}, {'name': 'Intracranial mass', 'entityId': 891, 'recNo': '78', 'observedFindingCount': 0, 'totalFindingCount': 0, 'isPoptList': True, 'isRelSecondary': False, 'relType': 'EVIDENCE', 'extensionData': [{'name': 'Emergent'}], 'findings': [], 'planOptionCategories': [], 'commentLists': [], 'activeType': 0, 'types': [], 'uniqueTypes': []}]}]}