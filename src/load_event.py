# Author : Sudhanshu Badoni
# Purpose : This program will be used to load the 'json' file from input directory.
# Name : load_event.py
# language : python
# Packages : JSON,SYS
# Date : 21-APR-2017


import json as js;
import sys ;

class load_event:
			
	def __init__(self):
		# Constructor to initialize the class
		print "Class load_event: Initialized class";
		
	def event_update(self,data_file):
		# event_update : This function will be used to load the JSON data file .

		try:
			with open(data_file)  as df:
			 		json_source = df.read()
					data = js.loads('{}'.format(json_source))
		except:
			print "Class load_event: Error in reading the JSON Data file ";
			sys.exit();
			
		return data;
			
			

	
		

