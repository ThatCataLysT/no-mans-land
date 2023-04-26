#!/bin/bash

# Set variables
version=$(<fabricver.txt)
api=https://meta.fabricmc.net/v2/versions/loader

# Get the fabric loader
latest_loader="$(jq -r '.[0].loader.version' floader.json)"

#Get the fabric installer
latest_installer="$(jq -r '.[0].version' finstaller.json)"

# Construct download URL
download_url="$api"/"$version"/"$latest_loader"/"$latest_installer"/server/jar

# Download file
wget "$download_url" -O fabric.jar
