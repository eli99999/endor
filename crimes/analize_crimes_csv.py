'''
Created on Jul 18, 2016

@author: eli
'''

import csv
import urllib.request
 

class AnalizeCrimesCsv:
    '''
    classdocs
    '''
    crimes_heat_dictionary = {}
    crimes_dictionary ={}
    crime_count = 0

    def add_crime_district_to_main_dictionary(self, crime, district):
        if district and crime :
            crime_typeid = self.get_crime_typeid(crime)
            if district in self.crimes_heat_dictionary:
                dist_crime_dictionary =  self.crimes_heat_dictionary.get(district)
                self.add_crime_to_district_dictionary(dist_crime_dictionary, crime_typeid)
            else:
                dist_crime_dictionary = {}
                self.crimes_heat_dictionary[district] = self.add_crime_to_district_dictionary(dist_crime_dictionary, crime_typeid)
        
    def add_crime_to_district_dictionary(self, dist_crime_dictionary, crime_typeid):
        if crime_typeid in dist_crime_dictionary:
            dist_crime_dictionary[crime_typeid] = dist_crime_dictionary.get(crime_typeid)+1
        else :
            dist_crime_dictionary[crime_typeid] = 1
        return dist_crime_dictionary
            
    def get_crime_typeid(self ,crime):
        if  crime in self.crimes_dictionary :
            return self.crimes_dictionary.get(crime)
        else:
            global crime_count
            self.crimes_dictionary[crime] = self.crime_count
            self.crime_count = self.crime_count +1
            return self.crimes_dictionary.get(crime)
    
    def save_result_to_csv(self, save_file_name):
        crimes_list = self.get_crimes_list()
        writer = csv.writer(open(save_file_name,'w', newline=''))
        crimes_list.insert(0, "district")
        writer.writerow(crimes_list)
        for key in sorted(self.crimes_heat_dictionary):
            rowvalues = self.crimes_heat_dictionary[key]
            rowlist = list(rowvalues.values())
            rowlist.insert(0, key)
            writer.writerow(rowlist)
           
    def parse_crimes_csv(self ,file_name): 
        cr = csv.reader(open(file_name, "r"))
        first_line = True
        for row in cr:
            if first_line:
                first_line = False
                continue
            self.add_crime_district_to_main_dictionary(row[5] ,row[11])
        
    def dictionary_to_sorted_list(self):
        result = []  
        for key in sorted(self.crimes_heat_dictionary):
            for i in range(0, self.crime_count):
                if i not in self.crimes_heat_dictionary[key]:
                    self.crimes_heat_dictionary[key][i]=0
            result.append(list(self.crimes_heat_dictionary[key].values()))
        return result
     
    def get_district_list(self):
        return self.crimes_heat_dictionary.keys()
    
    def get_crimes_list(self):
        return sorted(self.crimes_dictionary.keys(), key=self.crimes_dictionary.get) 