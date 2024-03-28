#!/bin/bash

# Send a POST request with a custom header to trigger the response
curl -s -X POST -H "x-HolbertonSchool-User-Id: 98" 0.0.0.0:5000/catch_me
