#!/bin/bash

curl "http://localhost:8000/workouts/${ID}" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}" \


echo
