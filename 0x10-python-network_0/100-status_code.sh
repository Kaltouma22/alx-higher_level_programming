#!/bin/bash

# Send a request to the URL passed as an argument
response=$(curl -s -o /dev/null -w "%{http_code}" "$1")

# Display only the status code of the response
echo "$response"
