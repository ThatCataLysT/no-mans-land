#!/bin/bash

# Set variables
version=$(<paperver.txt)
api=https://papermc.io/api/v2

# Get the build number of the most recent build
latest_build="$(curl -sX GET "$api"/projects/paper/versions/"$version"/builds -H 'accept: application/json' | jq '.builds [-1].build')"

# Construct download URL
download_url="$api"/projects/paper/versions/"$version"/builds/"$latest_build"/downloads/paper-"$version"-"$latest_build".jar

# Download file
wget "$download_url" -O paper.jar
