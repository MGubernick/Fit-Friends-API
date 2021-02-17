#!/bin/bash

curl "http://localhost:8000/workouts" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "workout": {
      "title": "'"${TITLE}"'",
      "category": "'"${CAT}"'",
      "difficulty": "'"${DIF}"'",
      "description": "'"${DESC}"'"
    }
  }'

echo
