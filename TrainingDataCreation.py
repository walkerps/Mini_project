import pandas as pd
import numpy as np
from datetime import datetime

file = 'sum_of_device_reading.txt'

df = pd.read_csv(file)

print df.head(5)

file3 = 'weatherData.csv'

df2 = pd.read_csv(file3,header = None)

df2.columns =['Date','ind','rain','ind','maxt','ind','mint','gmin','soil']

print df2.head(5)

date_columns = df2['Date'].values

df2_date = [] 
df2_cleaned_date = []
for date in date_columns:
	df2_date.append(datetime.strptime(date,'%d-%b-%Y').date())

for date in df2_date:
	df2_cleaned_date.append(datetime.strftime(date,'%Y-%m-%d'))

print df2_cleaned_date

df2.Date = df2_cleaned_date

result_date_frame = pd.merge(df,df2,on = 'Date')

print result_date_frame.head(5)

print result_date_frame.info()

result_date_frame = result_date_frame.drop(['ind','ind','ind'],axis = 1)
maxt_median = result_date_frame['maxt'].median()
mint_median = result_date_frame['mint'].median()
gmin_median = result_date_frame['gmin'].median()
soil_median = result_date_frame['soil'].median()

result_date_frame.loc[(result_date_frame['maxt'].isnull(),'maxt')] = maxt_median
result_date_frame.loc[(result_date_frame['mint'].isnull(),'mint')] = mint_median
result_date_frame.loc[(result_date_frame['gmin'].isnull(),'gmin')] = gmin_median
result_date_frame.loc[(result_date_frame['soil'].isnull(),'soil')] = soil_median
print result_date_frame.info()
print df.describe()

file = 'Resulted_Data.csv'

df = pd.read_csv(file,index_col = False)

df = df.drop(['Date'],axis = 1)

print df.info()
print df.head(5)

df.to_csv('Training_data.csv',index = False)
