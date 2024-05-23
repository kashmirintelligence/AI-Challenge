#!/bin/bash

# URLs for the datasets
ECL_URL="https://drive.google.com/uc?export=download&id=1tK3Ub3Gu5mvXa5U4Y4jGO_r5YUbW5u93"
WTH_URL="https://drive.google.com/uc?export=download&id=1to-HCS5_nHb_fxxRmyveES7ABplFyoYV"

# Output filenames
ECL_FILE="ECL.csv"
WTH_FILE="WTH.csv"

# Download the datasets
echo "Downloading ECL dataset..."
wget --no-check-certificate -O $ECL_FILE $ECL_URL

echo "Downloading WTH dataset..."
wget --no-check-certificate -O $WTH_FILE $WTH_URL

echo "Download completed!"
