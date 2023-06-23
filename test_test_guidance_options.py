from test_guidance_options import post_findings_to_guidance_options
import json

def foo():
	"""
	>>> from UnitTestStuff.test_guidance_options_01 import INPUT_FOR_TEST_O1_OF_POST_FINDINGS_TO_GUIDANCE_OPTIONS
	>>> TEST_INPUT_01_JSON = INPUT_FOR_TEST_O1_OF_POST_FINDINGS_TO_GUIDANCE_OPTIONS
	>>> TEST_INPUT_01_STR = json.dumps(TEST_INPUT_01_JSON)
	>>> post_findings_to_guidance_options(TEST_INPUT_01_STR, log_dir = None)
	################################################################
	### Just Entered @fun post_findings_to_guidance_options ###############
	################################################################

#### Payload (start of json object) ####

{
    "consultationId": 320,
    "findings": [
        {
            "entNo": 12100,
            "keywords": [],
            "present": true,
            "state": "PRESENT",
            "text": "female",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 31314,
            "keywords": [
                {
                    "name": "AgeRange",
                    "parameters": "0 yr, 18 yr"
                }
            ],
            "present": true,
            "state": "PRESENT",
            "text": "date of birth",
            "type": "FINDING",
            "uncertain": false,
            "valueObject": {
                "value": "2/13/2013",
                "valueType": "DATE"
            }
        },
        {
            "entNo": 26479,
            "keywords": [],
            "present": true,
            "state": "PRESENT",
            "text": "age",
            "type": "FINDING",
            "uncertain": false,
            "valueObject": {
                "value": 9.0,
                "valueType": "TIMESPAN",
                "valueTypeUnit": 1
            }
        },
        {
            "entNo": 51747,
            "keywords": [],
            "present": false,
            "state": "ABSENT",
            "text": "headache occurs around the time of menstrual period",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 44430,
            "keywords": [],
            "present": false,
            "state": "ABSENT",
            "text": "menstrual periods stopped in the past few months",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 62256,
            "keywords": [],
            "present": false,
            "state": "ABSENT",
            "text": "menstrual bleeding pattern or flow changed in past few month",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 62499,
            "keywords": [],
            "present": false,
            "state": "ABSENT",
            "text": "tampon use in the past 5 days",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 25051,
            "keywords": [],
            "present": false,
            "state": "ABSENT",
            "text": "pregnant currently",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 23966,
            "keywords": [],
            "mmp": 4201,
            "present": false,
            "state": "ABSENT",
            "text": "possibly pregnant",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 42763,
            "keywords": [],
            "present": false,
            "state": "ABSENT",
            "text": "childbirth in the past 6 weeks",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 1428,
            "keywords": [],
            "present": false,
            "state": "ABSENT",
            "text": "drinks alcohol",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 46071,
            "keywords": [],
            "present": false,
            "state": "ABSENT",
            "text": "uses cannabis",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 42305,
            "keywords": [],
            "present": false,
            "state": "ABSENT",
            "text": "uses cocaine",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 44647,
            "keywords": [],
            "present": false,
            "state": "ABSENT",
            "text": "uses other recreational drugs",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 42797,
            "keywords": [],
            "present": false,
            "state": "ABSENT",
            "text": "has injected recreational drugs",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 51605,
            "keywords": [],
            "present": false,
            "state": "ABSENT",
            "text": "has had sex in the past few months",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 64726,
            "keywords": [],
            "present": false,
            "state": "ABSENT",
            "text": "bulging at soft spaces (fontanelles) on top of head",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 66518,
            "keywords": [],
            "present": false,
            "state": "ABSENT",
            "text": "no bulging at soft spaces (fontanelles) on top of head",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 16645,
            "keywords": [
                {
                    "name": "ChildHeight"
                },
                {
                    "name": "Range",
                    "parameters": "12 in, 96 in"
                }
            ],
            "present": true,
            "state": "PRESENT",
            "text": "height",
            "type": "FINDING",
            "uncertain": false,
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
                    "name": "BodyWeight"
                },
                {
                    "name": "Range",
                    "parameters": "5 lb, 999 lb"
                }
            ],
            "present": true,
            "state": "PRESENT",
            "text": "weight",
            "type": "FINDING",
            "uncertain": false,
            "valueObject": {
                "value": 29.48350405,
                "valueType": "WEIGHT",
                "valueTypeUnit": 6
            }
        },
        {
            "entNo": 4769,
            "keywords": [],
            "present": true,
            "state": "PRESENT",
            "text": "body mass index (BMI)",
            "type": "FINDING",
            "uncertain": false,
            "valueObject": {
                "value": 18.279809070618143,
                "valueType": "ABSOLUTE_NUMBER"
            }
        },
        {
            "entNo": 65442,
            "keywords": [],
            "present": true,
            "state": "PRESENT",
            "text": "headache began in the past 24 hours",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 60772,
            "keywords": [],
            "present": true,
            "state": "PRESENT",
            "text": "headache occurs continuously",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 55859,
            "keywords": [],
            "present": false,
            "state": "ABSENT",
            "text": "headache lasts less than 1 minute",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 55855,
            "keywords": [],
            "present": false,
            "state": "ABSENT",
            "text": "headache lasts for minutes",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 65449,
            "keywords": [],
            "present": false,
            "state": "ABSENT",
            "text": "headache lasts for hours",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 17496,
            "keywords": [],
            "present": false,
            "state": "ABSENT",
            "text": "headache lasts most of the day to several days",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 61869,
            "keywords": [],
            "present": true,
            "state": "PRESENT",
            "text": "headache problem is getting worse",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 65448,
            "keywords": [],
            "present": true,
            "state": "PRESENT",
            "text": "headache all over the head",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 5237,
            "keywords": [],
            "present": false,
            "state": "ABSENT",
            "text": "pain behind the eye",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 2131,
            "keywords": [],
            "present": false,
            "state": "ABSENT",
            "text": "headache in the forehead area",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 2755,
            "keywords": [],
            "present": false,
            "state": "ABSENT",
            "text": "headache over the temple",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 2132,
            "keywords": [],
            "present": false,
            "state": "ABSENT",
            "text": "headache over the back of the head",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 61864,
            "keywords": [],
            "present": false,
            "state": "ABSENT",
            "text": "other headache location",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 61866,
            "keywords": [
                {
                    "name": "Range",
                    "parameters": "1,10;1"
                }
            ],
            "present": true,
            "state": "PRESENT",
            "text": "headache severity (1-10)",
            "type": "FINDING",
            "uncertain": false,
            "valueObject": {
                "value": "0",
                "valueType": "ABSOLUTE_NUMBER"
            }
        },
        {
            "entNo": 5096,
            "keywords": [],
            "present": true,
            "state": "PRESENT",
            "text": "sudden headache that is one of worst of child's life",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 59391,
            "keywords": [],
            "mmp": 3215,
            "present": true,
            "state": "PRESENT",
            "text": "headache preceded by an aura",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 43027,
            "keywords": [],
            "present": true,
            "state": "PRESENT",
            "text": "bump, blow, or jolt to the head or neck in past few weeks",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 65473,
            "keywords": [],
            "present": true,
            "state": "PRESENT",
            "text": "lost consciousness with injury or accident in past few days",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 65451,
            "keywords": [],
            "present": true,
            "state": "PRESENT",
            "text": "headache treatment previously tried",
            "type": "FINDING",
            "uncertain": false,
            "valueObject": {
                "value": "0",
                "valueType": "ABSOLUTE_STRING"
            }
        },
        {
            "entNo": 22553,
            "keywords": [],
            "present": true,
            "state": "PRESENT",
            "text": "fainting during or after standing up",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 1168,
            "keywords": [],
            "present": true,
            "state": "PRESENT",
            "text": "facial pain",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 58408,
            "keywords": [],
            "mmp": 4027,
            "present": true,
            "state": "PRESENT",
            "text": "travel or residence in Southern Africa in the past",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 1222,
            "keywords": [],
            "present": true,
            "state": "PRESENT",
            "text": "runny or stuffy nose",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 2506,
            "keywords": [],
            "present": true,
            "state": "PRESENT",
            "text": "snoring",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 269,
            "keywords": [],
            "present": true,
            "state": "PRESENT",
            "text": "nausea",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 356,
            "keywords": [],
            "present": true,
            "state": "PRESENT",
            "text": "joint pain",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 1136,
            "keywords": [],
            "present": true,
            "state": "PRESENT",
            "text": "flushing (reddening of the skin with a feeling of warmth)",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 42684,
            "keywords": [],
            "present": true,
            "state": "PRESENT",
            "text": "fever",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 42912,
            "keywords": [],
            "present": true,
            "state": "PRESENT",
            "text": "has had malaria",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 51747,
            "keywords": [],
            "present": true,
            "state": "PRESENT",
            "text": "headache occurs around the time of menstrual period",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 64745,
            "keywords": [],
            "present": true,
            "state": "PRESENT",
            "text": "sleeps with parent",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 64429,
            "keywords": [],
            "present": true,
            "state": "PRESENT",
            "text": "swallowed untreated water in the past few weeks",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 45246,
            "keywords": [],
            "present": true,
            "state": "PRESENT",
            "text": "mosquito bite in the past few weeks",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 64519,
            "keywords": [],
            "present": true,
            "state": "PRESENT",
            "text": "bird exposure in the past few weeks",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 58402,
            "keywords": [],
            "present": true,
            "state": "PRESENT",
            "text": "travel or residence outside of the US and Canada in the past",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 58864,
            "keywords": [],
            "present": true,
            "state": "PRESENT",
            "text": "has been in a developing country in the past",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 59383,
            "keywords": [
                {
                    "name": "HideIfAbsent",
                    "parameters": "58864"
                }
            ],
            "present": true,
            "state": "PRESENT",
            "text": "travel or residence in developing country in past few months",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 42728,
            "keywords": [],
            "present": true,
            "state": "PRESENT",
            "text": "current medication: hydralazine",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 64731,
            "keywords": [],
            "mmp": 4779,
            "present": true,
            "state": "PRESENT",
            "text": "current medication: ADHD drug",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 28426,
            "keywords": [],
            "present": true,
            "state": "PRESENT",
            "text": "other current medication",
            "type": "FINDING",
            "uncertain": false,
            "valueObject": {
                "value": "0",
                "valueType": "ABSOLUTE_STRING"
            }
        },
        {
            "entNo": 44124,
            "keywords": [],
            "present": true,
            "state": "PRESENT",
            "text": "other current over-the-counter drug or supplement",
            "type": "FINDING",
            "uncertain": false,
            "valueObject": {
                "value": "0",
                "valueType": "ABSOLUTE_STRING"
            }
        },
        {
            "entNo": 60744,
            "keywords": [],
            "present": true,
            "state": "PRESENT",
            "text": "regularly take any type of headache or pain medication",
            "type": "FINDING",
            "uncertain": false
        },
        {
            "entNo": 46444,
            "keywords": [],
            "present": true,
            "state": "PRESENT",
            "text": "stopped taking a medication in the past few weeks",
            "type": "FINDING",
            "uncertain": false,
            "valueObject": {
                "value": "0",
                "valueType": "ABSOLUTE_STRING"
            }
        },
        {
            "entNo": 61875,
            "keywords": [],
            "present": true,
            "state": "PRESENT",
            "text": "other information that may be useful",
            "type": "FINDING",
            "uncertain": false,
            "valueObject": {
                "value": "0",
                "valueType": "ABSOLUTE_STRING"
            }
        }
    ]
}

#### Payload (end of json object) ####

Bot JSON Response To Contributing Findings Post (start of section)

{
    "consultationId": 320,
    "consultationName": "Headache in Children Diagnosis",
    "guidanceOptions": [
        {
            "guidanceOptions": [
                {
                    "activeType": 0,
                    "commentLists": [],
                    "entityId": 726,
                    "extensionData": [],
                    "findings": [],
                    "isPoptList": true,
                    "isRelSecondary": false,
                    "name": "Migraine",
                    "observedFindingCount": 0,
                    "planOptionCategories": [],
                    "recNo": "1",
                    "relType": "EVIDENCE",
                    "totalFindingCount": 0,
                    "types": [],
                    "uniqueTypes": []
                },
                {
                    "activeType": 0,
                    "commentLists": [],
                    "entityId": 3519,
                    "extensionData": [],
                    "findings": [],
                    "isPoptList": true,
                    "isRelSecondary": false,
                    "name": "Sinusitis",
                    "observedFindingCount": 0,
                    "planOptionCategories": [],
                    "recNo": "28",
                    "relType": "EVIDENCE",
                    "totalFindingCount": 0,
                    "types": [],
                    "uniqueTypes": []
                },
                {
                    "activeType": 0,
                    "commentLists": [],
                    "entityId": 60452,
                    "extensionData": [],
                    "findings": [],
                    "isPoptList": true,
                    "isRelSecondary": false,
                    "name": "Drug use-related headache",
                    "observedFindingCount": 0,
                    "planOptionCategories": [],
                    "recNo": "30",
                    "relType": "EVIDENCE",
                    "totalFindingCount": 0,
                    "types": [],
                    "uniqueTypes": []
                },
                {
                    "activeType": 0,
                    "commentLists": [],
                    "entityId": 9937,
                    "extensionData": [],
                    "findings": [],
                    "isPoptList": true,
                    "isRelSecondary": false,
                    "name": "Menstrual migraine",
                    "observedFindingCount": 0,
                    "planOptionCategories": [],
                    "recNo": "50",
                    "relType": "EVIDENCE",
                    "totalFindingCount": 0,
                    "types": [],
                    "uniqueTypes": []
                },
                {
                    "activeType": 0,
                    "commentLists": [],
                    "entityId": 66831,
                    "extensionData": [],
                    "findings": [],
                    "isPoptList": true,
                    "isRelSecondary": false,
                    "name": "Coronavirus disease 2019 (COVID-19)",
                    "observedFindingCount": 0,
                    "planOptionCategories": [],
                    "recNo": "6",
                    "relType": "EVIDENCE",
                    "totalFindingCount": 0,
                    "types": [],
                    "uniqueTypes": []
                },
                {
                    "activeType": 0,
                    "commentLists": [],
                    "entityId": 26256,
                    "extensionData": [],
                    "findings": [],
                    "isPoptList": true,
                    "isRelSecondary": false,
                    "name": "Medication-related headache",
                    "observedFindingCount": 0,
                    "planOptionCategories": [],
                    "recNo": "8",
                    "relType": "EVIDENCE",
                    "totalFindingCount": 0,
                    "types": [],
                    "uniqueTypes": []
                },
                {
                    "activeType": 0,
                    "commentLists": [],
                    "entityId": 14227,
                    "extensionData": [],
                    "findings": [],
                    "isPoptList": true,
                    "isRelSecondary": false,
                    "name": "Medication overuse headache",
                    "observedFindingCount": 0,
                    "planOptionCategories": [],
                    "recNo": "99",
                    "relType": "EVIDENCE",
                    "totalFindingCount": 0,
                    "types": [],
                    "uniqueTypes": []
                }
            ],
            "name": "Common Causes"
        },
        {
            "guidanceOptions": [
                {
                    "activeType": 0,
                    "commentLists": [],
                    "entityId": 1250,
                    "extensionData": [],
                    "findings": [],
                    "isPoptList": true,
                    "isRelSecondary": false,
                    "name": "Malaria",
                    "observedFindingCount": 0,
                    "planOptionCategories": [],
                    "recNo": "111",
                    "relType": "EVIDENCE",
                    "totalFindingCount": 0,
                    "types": [],
                    "uniqueTypes": []
                },
                {
                    "activeType": 0,
                    "commentLists": [],
                    "entityId": 1105,
                    "extensionData": [],
                    "findings": [],
                    "isPoptList": true,
                    "isRelSecondary": false,
                    "name": "Hydrocephalus",
                    "observedFindingCount": 0,
                    "planOptionCategories": [],
                    "recNo": "12",
                    "relType": "EVIDENCE",
                    "totalFindingCount": 0,
                    "types": [],
                    "uniqueTypes": []
                },
                {
                    "activeType": 0,
                    "commentLists": [],
                    "entityId": 691,
                    "extensionData": [
                        {
                            "name": "Emergent"
                        }
                    ],
                    "findings": [],
                    "isPoptList": true,
                    "isRelSecondary": false,
                    "name": "Takayasu arteritis",
                    "observedFindingCount": 0,
                    "planOptionCategories": [],
                    "recNo": "120",
                    "relType": "EVIDENCE",
                    "totalFindingCount": 0,
                    "types": [],
                    "uniqueTypes": []
                },
                {
                    "activeType": 0,
                    "commentLists": [],
                    "entityId": 60768,
                    "extensionData": [],
                    "findings": [],
                    "isPoptList": true,
                    "isRelSecondary": false,
                    "name": "New daily persistent headache",
                    "observedFindingCount": 0,
                    "planOptionCategories": [],
                    "recNo": "22",
                    "relType": "EVIDENCE",
                    "totalFindingCount": 0,
                    "types": [],
                    "uniqueTypes": []
                },
                {
                    "activeType": 0,
                    "commentLists": [],
                    "entityId": 644,
                    "extensionData": [
                        {
                            "name": "Emergent"
                        }
                    ],
                    "findings": [],
                    "isPoptList": true,
                    "isRelSecondary": false,
                    "name": "Meningitis",
                    "observedFindingCount": 0,
                    "planOptionCategories": [],
                    "recNo": "24",
                    "relType": "EVIDENCE",
                    "totalFindingCount": 0,
                    "types": [],
                    "uniqueTypes": []
                },
                {
                    "activeType": 0,
                    "commentLists": [],
                    "entityId": 756,
                    "extensionData": [],
                    "findings": [],
                    "isPoptList": true,
                    "isRelSecondary": false,
                    "name": "Lyme disease",
                    "observedFindingCount": 0,
                    "planOptionCategories": [],
                    "recNo": "45",
                    "relType": "EVIDENCE",
                    "totalFindingCount": 0,
                    "types": [],
                    "uniqueTypes": []
                },
                {
                    "activeType": 0,
                    "commentLists": [],
                    "entityId": 37482,
                    "extensionData": [],
                    "findings": [],
                    "isPoptList": true,
                    "isRelSecondary": false,
                    "name": "Cysticercosis",
                    "observedFindingCount": 0,
                    "planOptionCategories": [],
                    "recNo": "61",
                    "relType": "EVIDENCE",
                    "totalFindingCount": 0,
                    "types": [],
                    "uniqueTypes": []
                },
                {
                    "activeType": 0,
                    "commentLists": [],
                    "entityId": 891,
                    "extensionData": [
                        {
                            "name": "Emergent"
                        }
                    ],
                    "findings": [],
                    "isPoptList": true,
                    "isRelSecondary": false,
                    "name": "Intracranial mass",
                    "observedFindingCount": 0,
                    "planOptionCategories": [],
                    "recNo": "78",
                    "relType": "EVIDENCE",
                    "totalFindingCount": 0,
                    "types": [],
                    "uniqueTypes": []
                }
            ],
            "name": "Less Common Causes"
        }
    ]
}

Bot JSON Response To Users Post (end of section)
################
################################################################
### About To Exit @fun post_findings_to_guidance_options #######
################################################################
"""
