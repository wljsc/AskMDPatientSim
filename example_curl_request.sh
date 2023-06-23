curl --location --request POST 'https://api.dev.sharecare.com/consultation/next' \
--header 'Content-Type: application/json' \
--data-raw '
{
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
        {
        "myfindingId": "finding-2-consultation-14 - swelling of both legs, ankles, or feet",
	"id": 2,
	"state": "PRESENT"
        }
    ]
}
'
