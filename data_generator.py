import sklearn as sk 
import pandas as pd 
import numpy as np 
import os
sub_dir = '/home/walker/Desktop/Mini_project/data'
lines_per_file = 1000000

smallfile  = None
for fileno,filename in enumerate(os.listdir('/home/walker/Desktop/Mini_project/data')):
	with open(os.path.join(sub_dir,filename)) as bigfile:
		for lineno,line in enumerate(bigfile):
			if lineno%lines_per_file == 0:
				if smallfile:
					smallfile.close()
				small_filename = 'small_file__{}_{}.txt'.format(fileno+1,lineno+lines_per_file)
				smallfile = open(small_filename,"w")
			smallfile.write(line)
		if smallfile:
			smallfile.close()
