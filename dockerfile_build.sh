#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Install system dependencies
apt-get update
apt-get install -y wget gnupg unzip curl

# Install Chrome
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
apt-get update
apt-get install -y google-chrome-stable

# Verify Chrome installation
google-chrome --version || echo "Chrome installation failed"

# Set Chrome binary path
export CHROME_BIN=/usr/bin/google-chrome-stable