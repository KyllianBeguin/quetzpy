QUERY=$1
BEARER_TOKEN=YOUR_BEARER_TOKEN
rm ./data/json/data_$QUERY.json
curl "https://api.twitter.com/2/tweets/search/recent?query=$QUERY&tweet.fields=created_at&max_results=100" -H "Authorization: Bearer $BEARER_TOKEN" >> ./data/json/data_$QUERY.json
