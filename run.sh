#!/bin/bash

a=1

while [ $a -le $2 ]
do
  bash twitter_query.sh $1
  python3 insert_scraped_data.py ./data/json/data_$1.json
  echo "Extraction n°$a"
  sleep $3
  ((a++))
done
