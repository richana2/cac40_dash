import boto3
import web_scraping_cac40 as raw_data
import os
import pandas as pd


###########################################################################################
def download_data_from_s3():
    """
    Download the raw data of cac40 providing of yahoo finance from my data lake aws S3.

    No return value.
    """
    try:
        s3_client = boto3.Session(
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
        )
        s3 = s3_client.resource('s3')
        s3.Bucket('cac40-raw-data').download_file(raw_data.filename, raw_data.filename)
    except Exception as e:
        raise e
###########################################################################################

def open_csv_file():
    """
    Open the raw data on csv file.

    Return a Dataframe of the csv file.
    """
    try:
        df = pd.read_csv(raw_data.filename)
        return df
    except Exception as e:
        raise e



if __name__ == '__main__':
    # first step : download the raw data from S3 bucket
    download_data_from_s3()  

    # second step : open the csv file
    raw_data = open_csv_file()
    
      