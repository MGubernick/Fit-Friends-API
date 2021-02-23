#!/bin/bash

curl "http://localhost:8000/secret-user-path/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
