clear
QUERY='PekinExpress'
BEARER_TOKEN='YOUR_TOKEN'
curl "https://api.twitter.com/2/tweets/search/recent?query=$QUERY&tweet.fields=created_at&max_results=100" -H "Authorization: Bearer $BEARER_TOKEN" >> data_$QUERY.json
