import os
def getPredictiveValue(var,bin,sum) :
	path = 'Mini_project/data/'
	if(var == 0) :
		day = "Monday"
	if(var == 1) :
		day = "Tuesday"
	if(var == 2) :
		day = "Wednesday"
	if(var == 3) :
		day = "Thursday"
	if(var == 4) :
		day = "Friday"
	if(var == 5) :
		day = "Saturday"
	if(var == 6) :
		day = "Sunday"
	path = path + day
	path = path + '.txt'
	content = []
	with open(path) as f:
		content = f.readlines()
	counter = 0
	ret = 0.0
	BIN = 0;
	SUM = 1.0
	for line in content:
		counter += 1
		if counter == 1:
			continue
		words = line.split(",")
		BIN = int(words[0])
		EXPECTED_VALUE = float(words[1])
		if BIN == bin:
			ret = EXPECTED_VALUE
		SUM += EXPECTED_VALUE
	return ret * (1.0 * sum / SUM)
