#!/bin/bash

curl "http://localhost:8000/one-user/${ID}" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}" \


echo
