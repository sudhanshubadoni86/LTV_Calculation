# Author : Sudhanshu Badoni
# Purpose : This program will be used calculate LTV value for each customer and then .
# Name : TopXSimpleLTVCustomers.py
# language : python
# Packages : OPERATOR,SYS
# Date : 21-APR-2017

import operator;
import sys ;

class TopXSimpleLTVCustomers:
	# Class variables 
	
	cust=list();
	site=list();
	order=list();
	image=list();
	custlist=list();
	Err=0;
	ErrNo='';
	f_output=open('/Users/sudhanshubadoni/Desktop/VIEW/Shutterfly/output/output.txt','w+');
	
	def __init__(self):
		# Constructor to initialize the class
		print "Class TopXSimpleLTVCustomers: Initialized the TopXSimpleLTVCustomers Class";
		
	
	def create_data_model(self,data):
		# This function creates separate data model based on  type for Customer,Site_visit,Image and order.

		try:
			for i in range(0,len(data)):
				if(data[i]['type']=='CUSTOMER'):
						self.cust.append(data[i]);
						print "\n Class TopXSimpleLTVCustomers: Customer JSON Data : ",self.cust;	
				elif (data[i]['type']=='SITE_VISIT'):
						self.site.append(data[i]);
						print "\n Class TopXSimpleLTVCustomers: SITE JSON Data : ",self.site;	
				elif (data[i]['type']=='IMAGE'):
						self.image.append(data[i]);
						print "\n Class TopXSimpleLTVCustomers: IMAGE JSON Data : ",self.image;	
				elif (data[i]['type']=='ORDER'):
						self.order.append(data[i]);
						print "\n Class TopXSimpleLTVCustomers: ORDER JSON Data : ",self.order;
		except:
			print "\n Class TopXSimpleLTVCustomers: Error in Creating the data model";
			sys.exit();
			
	
	def	LTVcalculation_top_ct(self,no_cust):
		# This function makes other function calls to find the customer Life time value(LTV) 
		# and also writes the output to the file in output directory .
		try:
			c_ltv={}
			cst_exp_per_visit = self.customer_exp_per_visit();
			dict_site_dys= self.LTV_time_frame();
			unique_cust=set(map(lambda x:x['key'],self.cust));
			for cstmer in self.custlist:
				cltv=0
				
				
				#Formula to calculate the customer LTV value
				#	52	* (customer expenditure per visit (sum(total_amount)/no.of visits) * Total number of visits) * 10
				
				cltv=52*(cst_exp_per_visit[cstmer]*dict_site_dys[cstmer])*10;
				c_ltv[cstmer]=cltv;
			
			#Sorting the dictionary to pick top customers by LTV
			sorted_c_ltv = sorted(c_ltv.items(), key=operator.itemgetter(1),reverse=1)
			
			if(len(sorted_c_ltv)<no_cust):
				rnge=len(sorted_c_ltv);
			else:
				rnge=no_cust;
		except:
			print "\n Class TopXSimpleLTVCustomers-LTVcalculation_top_ct: Error in calculating the LTV value";
			sys.exit();
		
		try:
			# File Writing logic 
			self.f_output.write("******************************************************");
			self.f_output.write("\n");
			for i in range(0,rnge):
				self.f_output.write("Customer No :	");
				self.f_output.write(str(sorted_c_ltv[i][0]));
				self.f_output.write("\nCustomer LTV Value :	");
				self.f_output.write(str(sorted_c_ltv[i][1]));
				self.f_output.write("\n");
				self.f_output.write("******************************************************");
				self.f_output.write("\n");
			self.f_output.close();	
		except:
			self.f_output.close();
			print "\n Class TopXSimpleLTVCustomers-LTVcalculation_top_ct: Error in Writing the file";
			sys.exit();
		

	 		


	def customer_exp_per_visit(self):
		# This function calculates the customer expenditure per visit 

		dict_sum_site={}
		self.custlist=set(map(lambda x:x['key'],self.cust));
		try:	
			for cst in self.custlist:
				sum=0;
				count=0;
				for st in range(0,len(self.order)):
					if(cst==self.order[st]['customer_id']):
						sum=sum+float((self.order[st]['total_amount']).split(' ')[0]);
						
				for sr in range(0,len(self.site)):
					if(cst==self.site[sr]['customer_id']):
						count=count+1
				 
				
				try:
					dict_sum_site[cst]=sum/count;
				except:
					dict_sum_site[cst]=0
		except:
		 	print "\n Class TopXSimpleLTVCustomers-customer_exp_per_visit:Error in calculating the customer expenditure per visit";
			sys.exit();
			
		return dict_sum_site;
			
	def LTV_time_frame(self):
		# This function calculates the no.of customer visits  

		dict_site_days={}
		try:
			for cst1 in self.custlist:
				tm=0;
				for se in range(0,len(self.site)):
					if(cst1==self.site[se]['customer_id']):
						tm=tm+1;
							
				dict_site_days[cst1]=tm;
		except:
			print "\n Class TopXSimpleLTVCustomers-LTV_time_frame:Error in finding the time frame";
			sys.exit();
			
		return(dict_site_days);	
