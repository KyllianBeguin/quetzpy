QUERY=$1
BEARER_TOKEN='AAAAAAAAAAAAAAAAAAAAAKv%2FeQEAAAAAIMy9q%2Bu%2Fjb5TYOVikG37lSKpEYU%3Dsyk09zEyzIPJZ2M0wZTX73EzbqU5VkaFrrYCpCxxCkr7MvXVue'
rm ./data/json/data_$QUERY.json
curl "https://api.twitter.com/2/tweets/search/recent?query=$QUERY&tweet.fields=created_at&max_results=100" -H "Authorization: Bearer $BEARER_TOKEN" >> ./data/json/data_$QUERY.json
