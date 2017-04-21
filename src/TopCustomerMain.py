﻿# Author : Sudhanshu Badoni
# Purpose : This program is main program which calls other class functions to find the LTV value.
# Name : TopCustomerMain.py
# language : python
# External Packages : SYS
# Date : 21-APR-2017

from  load_event import *;
from  TopXSimpleLTVCustomers import *
import sys 
class TopCustomerMain:

	if __name__ == '__main__':
		try:
			inp=raw_input("Enter : No. of customer required for LTV ?")
			event1=load_event();
			data=event1.event_update('/Users/sudhanshubadoni/Desktop/VIEW/Shutterfly/input/input.txt');
			TopXSimpleLTVCustomers1=TopXSimpleLTVCustomers()
			TopXSimpleLTVCustomers1.create_data_model(data);
			TopXSimpleLTVCustomers1.LTVcalculation_top_ct(int(inp));
		except:
			print "Cass TopCustomerMain: Error in the main ";
			sys.exit();