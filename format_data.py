import pandas as pd
import numpy as np

def Import_DataSets(files):
	df_list = []

	for file in files:
		df = pd.read_excel(file, dtype = 'str')
		df_list.append(df)

	return df_list


def Get_Number_Of_Starbuck_In_ZipCode(data_sets):

	zip_code_counts = []

	for data in data_sets:
		data['Zip']=data['Zip'].str[:5]

	for data in data_sets:
		zipcode_series = data.groupby('Zip')['Zip'].count()
		zipcode = pd.DataFrame({'Zip':zipcode_series.index, 'Count':zipcode_series.values})
		zipcode = zipcode[zipcode.Zip != 'nan']
		zip_code_counts.append( zipcode )

	return zip_code_counts


def Save_Files(file_list):
	file_name = 'count'
	file_count = 0
	file_type = '.csv'

	for file in file_list:
		file.to_csv(file_name + file_type, sep=',', index = False, )
		file_name = file_name + str(file_count)
		file_count = int(file_count) + 1



def Main():
	files = ["June 2012 Starbucks_Locations_in_the_US dataset.xlsx", "November 2013 All_Starbucks_Locations_in_the_US dataset.xlsx", "Cleaned_Starbucks_2017.xls"]
	data_sets = Import_DataSets(files)

	zip_code_counts = Get_Number_Of_Starbuck_In_ZipCode(data_sets)

	for zip_code in zip_code_counts:
		print (zip_code.shape)

	Save_Files(zip_code_counts)

Main()
