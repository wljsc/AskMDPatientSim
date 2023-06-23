import json

################################################################

Result_from_start_Consult14 = \
json.loads("""{
    "extensionData": [
        {
            "name": "GenderDOB",
            "parameters": "null"
        }
    ],
    "findings": [],
    "mmp": null,
    "nextQuestionId": 10,
    "questionCountSeq": 27,
    "questionCountTot": null,
    "questionId": 68,
    "questionIndexSeq": 1,
    "responses": [
        {
            "entNo": "12100",
            "extensionData": [],
            "findingValue": {
                "defaultUnit": null,
                "format": "STRING",
                "type": "NONE",
                "units": []
            },
            "mmp": null,
            "name": "female",
            "respNo": "180"
        },
        {
            "entNo": "3066",
            "extensionData": [],
            "findingValue": {
                "defaultUnit": null,
                "format": "STRING",
                "type": "NONE",
                "units": []
            },
            "mmp": null,
            "name": "male",
            "respNo": "184"
        },
        {
            "entNo": "31314",
            "extensionData": [],
            "findingValue": {
                "defaultUnit": null,
                "format": "STRING",
                "type": "DATE",
                "units": []
            },
            "mmp": null,
            "name": "date of birth",
            "respNo": "181"
        }
	]
    ],
    "title": "Birth sex, date of birth"
}""")

################################################################
# Input - user response to question-29-consultation-14 Do you have any of these foot or ankle problems?"

# swelling in one foot or ankle

#         {
#             "text": "swelling in one foot or ankle",
#             "findingId": "finding-4-consultation-14",
#             "mmp": null
#         },


UserReply_to_Question28_Consult14_swelling_in_one_foot_or_ankle = \
json.loads("""{
"myquestionId": "question-29-consultation-14 Do you have any of these foot or ankle problems?",
"questionId": 29,
    "consultationId": 14,
    "findings": [
        {
            "id": 18,
            "valueObject": {
                "value": "71",
                "valueType": "LENGTH",
                "valueTypeUnit": 4,
                "format": "INT"
            },
            "state": "PRESENT"
        },
        {
            "id": 12,
            "valueObject": {
                "value": "205",
                "valueType": "WEIGHT",
                "valueTypeUnit": 2,
                "format": "INT"
            },
            "state": "PRESENT"
        },
        {
            "id": 184,
            "myfindingId": "male-finding-184",
            "state": "PRESENT"
        },
        {
            "id": 181,
            "myfindingId": "date-of-birth-finding-181",
            "valueObject": {
                "value": "12/29/1988",
                "valueType": "DATE",
                "format": "DATE"
            },
            "state": "PRESENT"
        },
        {
            "id": 27,
            "myFindingId": "past 24 hours finding-27-consultation-14",
            "state": "PRESENT"
        },
        {
            "id": 98,
            "myfindingId": "finding-98-consultation-14 all the time",
            "state": "PRESENT"
        },
        {
        "myfindingId": "finding-92-consultation-14 getting worse",
	"id": 92,
	"state": "PRESENT"
        },
        {
	"myfindingId": "finding-4-consultation-14 swelling in one foot or ankle",
        "id": 4,
	"state": "PRESENT"
        },
    ]
}""")