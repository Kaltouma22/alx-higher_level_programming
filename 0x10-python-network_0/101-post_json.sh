#!/bin/bash

# Check if the number of arguments is correct
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <URL> <filename>"
    exit 1
fi

# Read the file contents into a variable
file_contents=$(cat "$2")

# Send a JSON POST request with the file contents to the URL
response=$(curl -s -X POST -H "Content-Type: application/json" -d "$file_contents" "$1")

# Display the body of the response
echo "$response"
