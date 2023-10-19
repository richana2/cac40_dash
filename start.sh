#!/bin/bash

# 1. EXTRACT : Scrap the data from the api yfinance and add raw data to S3 bucket
echo "Scraping data from yfinance api..."
python3 web_scraping_cac40.py

echo "Scraping done !"
sleep 3

# 2. TRANSFORM : process the data 
echo "Processing data..."
python3 process.py

echo "Processing done !"
sleep 3

# 3. LOAD : load the data to postgresql
echo "Loading data to postgresql..."
python3 load.py

echo "Loading done !"
sleep 3
# 4. BI : Create a dashboard plotly
echo "Creating dashboard..."
python3 dashboard.py


