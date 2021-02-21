#!/bin/bash

curl "http://localhost:8000/favorites" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "favorite": {
      "workout_id": "'"${WKID}"'",
      "user_id": "'"${USID}"'"
    }
  }'

echo
