import boto3
#import me my module web_scraping_cac40
import web_scraping_cac40 as raw_data
import os

import sys
from pathlib import Path
 
lib_path = Path(__file__).parent.parent / "Python/Exercice python"
lib_path = lib_path.resolve()
sys.path.insert(0, str(lib_path))

def download_data_from_s3():
    try:
        s3_client = boto3.Session(
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
        )
        s3 = s3_client.resource('s3')
        s3.Bucket('cac40-raw-data').download_file(raw_data.filename, raw_data.end + '/' +raw_data.filename)
    except Exception as e:
        print(e)
        print('Failed to download the data from S3.')
        return None


if __name__ == '__main__':
    #################################Download from S3############################
    download_data_from_s3()
    #############################################################################
    