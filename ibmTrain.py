# ibmTrain.py
# 
# This file produces 11 classifiers using the NLClassifier IBM Service
# 
# TODO: You must fill out all of the functions in this file following 
# 		the specifications exactly. DO NOT modify the headers of any
#		functions. Doing so will cause your program to fail the autotester.
#
#		You may use whatever libraries you like (as long as they are available
#		on CDF). You may find json, request, or pycurl helpful.
#

###IMPORTS###################################
#TODO: add necessary imports
import itertools
import io
###HELPER FUNCTIONS##########################

def convert_training_csv_to_watson_csv_format(input_csv_name, group_id, output_csv_name): 
	# Converts an existing training csv file. The output file should
	# contain only the 11,000 lines of your group's specific training set.
	#
	# Inputs:
	#	input_csv - a string containing the name of the original csv file
	#		ex. "my_file.csv"
	#
	#	output_csv - a string containing the name of the output csv file
	#		ex. "my_output_file.csv"
	#
	# Returns:
	#	None
	
	#TODO: Fill in this function
	class0 = (int(group_id)*5500,(int(group_id)+1)*5500-1)
	class1 = (800000+(int(group_id)*5500),800000+(int(group_id)+1)*5500-1)
	filtered = []
	outf = open(output_csv_name,'w')
	f = open(input_csv_name,'r') 
	strlist = f.read().strip().split("\n")
	for i in strlist[class0[0]:class0[1]]:
		tokens = i.split(",")
		classif = tokens[0][1:-1]
		twtText = ",".join(tokens[5:])
		singleTweet = twtText[1:-1]+","+classif
		filtered.append(singleTweet)
	for i in strlist[class1[0]:class1[1]]:
		tokens = i.split(",")
		classif = tokens[0][1:-1]
		twtText = ",".join(tokens[5:])
		singleTweet = twtText[1:-1]+","+classif
		filtered.append(singleTweet)
	for i in filtered:
		outf.write(i+"\n")
	
	outf.close()
	f.close()
	
		
	
def extract_subset_from_csv_file(input_csv_file, n_lines_to_extract, output_file_prefix='ibmTrain'):
	# Extracts n_lines_to_extract lines from a given csv file and writes them to 
	# an outputfile named ibmTrain#.csv (where # is n_lines_to_extract).
	#
	# Inputs: 
	#	input_csv - a string containing the name of the original csv file from which
	#		a subset of lines will be extracted
	#		ex. "my_file.csv"
	#	
	#	n_lines_to_extract - the number of lines to extract from the csv_file, as an integer
	#		ex. 500
	#
	#	output_file_prefix - a prefix for the output csv file. If unspecified, output files 
	#		are named 'ibmTrain#.csv', where # is the input parameter n_lines_to_extract.
	#		The csv must be in the "watson" 2-column format.
	#		
	# Returns:
	#	None
	
	#TODO: Fill in this function
	f = open(input_csv_file,'r') 	
	outf = open(output_file_prefix + str(n_lines_to_extract) + ".csv",'w')
	num_class0 = 0
	num_class1 = 0
	for line in f:
		if int(line[-2]) == 0 and num_class0 < n_lines_to_extract:
			outf.write(line)
			num_class0 +=1
		elif int(line[-2]) == 4 and num_class0 < n_lines_to_extract:
			outf.write(line)
			num_class1 +=1
			
	
	return
	
def create_classifier(username, password, n, input_file_prefix='ibmTrain'):
	# Creates a classifier using the NLClassifier service specified with username and password.
	# Training_data for the classifier provided using an existing csv file named
	# ibmTrain#.csv, where # is the input parameter n.
	#
	# Inputs:
	# 	username - username for the NLClassifier to be used, as a string
	#
	# 	password - password for the NLClassifier to be used, as a string
	#
	#	n - identification number for the input_file, as an integer
	#		ex. 500
	#
	#	input_file_prefix - a prefix for the input csv file, as a string.
	#		If unspecified data will be collected from an existing csv file 
	#		named 'ibmTrain#.csv', where # is the input parameter n.
	#		The csv must be in the "watson" 2-column format.
	#
	# Returns:
	# 	A dictionary containing the response code of the classifier call, will all the fields 
	#	specified at
	#	http://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/natural-language-classifier/api/v1/?curl#create_classifier
	#   
	#
	# Error Handling:
	#	This function should throw an exception if the create classifier call fails for any reason
	#	or if the input csv file does not exist or cannot be read.
	#
	
	#TODO: Fill in this function
	f = open(input_file_prefix + str(n) + ".csv",'w')	
	url = "https://gateway.watsonplatform.net/natural-language-classifier/api/v1/classifiers"
	training_metadata ={"language":"en","name":"Classifier "+str(n)}
	
	
	
	return
	
if __name__ == "__main__":
	
	#### STEP 1: Convert csv file into two-field watson format
	#input_csv_name = '<ADD FILENAME HERE>'
	input_csv_name = '/u/cs401/A1/tweets/training.1600000.processed.noemoticon.csv'
	
	##DO NOT CHANGE THE NAME OF THIS FILE
	#output_csv_name 'training_11000_watson_style.csv'
	output_csv_name ='training_11000_watson_style.csv'
	#convert_training_csv_to_watson_csv_format(input_csv_name,output_csv_name)
	
	
	### STEP 2: Save 11 subsets in the new format into ibmTrain#.csv files
	
	#TODO: extract all 11 subsets and write the 11 new ibmTrain#.csv files
	#
	# you should make use of the following function call:
	#
	# n_lines_to_extract = 500
	# extract_subset_from_csv_file(input_csv,n_lines_to_extract)
	n_lines_to_extract = 500
	extract_subset_from_csv_file(input_csv,n_lines_to_extract)
	### STEP 3: Create the classifiers using Watson
	
	#TODO: Create all 11 classifiers using the csv files of the subsets produced in 
	# STEP 2
	# 
	#
	# you should make use of the following function call
	 n = 500
	username = '<ADD USERNAME>'
	password = '<ADD PASSWORD>'
	create_classifier(username, password, n, input_file_prefix='ibmTrain')
	pass
