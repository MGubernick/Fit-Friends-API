#!/bin/bash

curl "http://localhost:8000/favorites/${ID}" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
