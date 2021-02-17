#!/bin/bash

curl "http://localhost:8000/myworkouts" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
