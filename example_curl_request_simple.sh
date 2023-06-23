curl --location --request POST 'https://api.dev.sharecare.com/consultation/next' \
     --header 'Content-Type: application/json' \
     -o junk.txt \
--data-raw '
{

    "consultationId": 14
}'

