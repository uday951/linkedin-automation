#!/bin/bash

# Hostinger VPS Setup Script for LinkedIn Automation

echo "🚀 Setting up LinkedIn Automation on Hostinger VPS..."

# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and pip
sudo apt install python3 python3-pip python3-venv -y

# Install Chrome and dependencies
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt update
sudo apt install google-chrome-stable -y

# Install additional dependencies
sudo apt install xvfb unzip curl -y

# Create project directory
mkdir -p ~/linkedin-automation
cd ~/linkedin-automation

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python packages
pip install --upgrade pip
pip install schedule python-dotenv requests google-generativeai flask gunicorn selenium webdriver-manager

echo "✅ Hostinger VPS setup complete!"
echo "📁 Project directory: ~/linkedin-automation"
echo "🔧 Next: Upload your project files and run the app"