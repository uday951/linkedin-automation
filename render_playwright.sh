#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium

# Install system dependencies for Playwright
playwright install-deps