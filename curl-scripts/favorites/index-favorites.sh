#!/bin/bash

curl "http://localhost:8000/favorites" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
