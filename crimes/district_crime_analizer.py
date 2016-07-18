'''
Created on Jul 17, 2016

@author: eli
'''

if __name__ == '__main__':
    pass

import csv
import urllib.request
from heatmap_chart_helper import CreateHeatMap
from analize_crimes_csv import AnalizeCrimesCsv
from aws_s3_helper import AwsFileDownloader

URL = 'https://athena-dev-task.s3-eu-west-1.amazonaws.com/Crimes.csv'
CSV_FILE_NAME = "Crimes.csv"
BUCKET_NAME = "athena-dev-task"
PARSED_CSV_FILE_NAME = "districtCrimes.csv"


#s3_helper = AwsFileDownloader(BUCKET_NAME, CSV_FILE_NAME, CSV_FILE_NAME)
#s3_helper.download_file()

#urllib.request.urlretrieve (URL, CSV_FILE_NAME)
analize_crimes =  AnalizeCrimesCsv()
analize_crimes.parse_crimes_csv(CSV_FILE_NAME)
result_list = analize_crimes.dictionary_to_sorted_list()
show = CreateHeatMap(analize_crimes.get_district_list(), analize_crimes.get_crimes_list(), result_list)
  
analize_crimes.save_result_to_csv(PARSED_CSV_FILE_NAME)

