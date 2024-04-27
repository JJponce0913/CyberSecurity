#!/bin/bash

# Define the server address and port
SERVER="chals.swampctf.com"
PORT="60001"

# Send each number to the server using Netcat
for number in 203 1256 1218 1967 4644; do
    echo "Sending: $number"
    echo "$number" | nc $SERVER $PORT
done
