# -*- coding: utf-8 -*-
import pandas as pd
import yfinance as yf
from datetime import date
import boto3
import os


def cac40scraping(start, end):
    try:
      cac40Info = pd.read_html('https://en.wikipedia.org/wiki/CAC_40')[4]
      d = yf.download(
        list(cac40Info.Ticker),
        start = start,
        end = end
      )
      return d
    except Exception as e:
      print(e)
      print('Failed to download the data from yfinance.')
      return None

def save_to_S3(filename, date, bucket):
  try:
    s3 = boto3.client('s3')
    
    s3.upload_file(filename, bucket, date + '/' + filename)
  except Exception as e:
    print(e)
    print('Failed to upload the data to S3.')
    

if __name__ == '__main__':
  #################################Scraping####################################
  start = '2020-01-01'
  end =  date.today().strftime("%Y-%m-%d")
  filename = 'CAC40_raw_data_' + start + '_to_' + end +'.csv'
  
  data = cac40scraping(start, end)
  data.to_csv(filename)
  #############################################################################
  
  #################################Upload to S3################################
  save_to_S3(filename, end, 'cac40-raw-data')
  #############################################################################
  