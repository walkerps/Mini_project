import pandas as pd
import numpy as np
import os
import datetime

sub_dir = '/home/walker/Desktop/Mini_project/data'

for filename in os.listdir(sub_dir):
	filename_ = os.path.join(sub_dir,filename)
	df = pd.read_csv(filename_)

	df['Date'] = df['Date'] + 733408

	lene = len(df['Date'])
	date_array = np.zeros(lene)

	for ii,date in enumerate(df['Date']):
		date = int(date)
		date_array[ii] = date
		

	ordinal = np.zeros(lene)

	ordinal  = ordinal.astype(str)

	for ii in range(len(date_array)):
		ordinal[ii] = str(datetime.date.fromordinal(int(date_array[ii])))

	df.loc[:,'Date'] = [ordinal[ii] for ii in range(len(ordinal))]

	print df.info()
	
	df.to_csv(filename_,index = False)