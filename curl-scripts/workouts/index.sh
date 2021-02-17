#!/bin/bash

curl "http://localhost:8000/workouts" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
