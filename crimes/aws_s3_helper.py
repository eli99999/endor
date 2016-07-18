'''
Created on Jul 18, 2016

@author: eli
'''
import boto
import boto.s3.connection

class AwsFileDownloader:
   
    def download_file(self, bucket_name, bucket_path, local_path):
        
        AWS_ACCESS_KEY_ID = '...'
        AWS_SECRET_ACCESS_KEY = '...'

        # connect to the bucket
        conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
        bucket = conn.get_bucket(bucket_name)
        
        # go through the list of files
        key = bucket.get_key(bucket_path)
        key.get_contents_to_filename(local_path)