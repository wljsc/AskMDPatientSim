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

