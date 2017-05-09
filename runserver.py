from flask import Flask 
from flask import request,render_template
from datetime import datetime
import calendar
import pickle
from predictvalue import getPredictiveValue

app  = Flask(__name__)

@app.route('/')
@app.route('/home/',methods = ['GET','POST'])
def home():
	return render_template('index.html',title = 'LNMIIT_LBapp | Home')

@app.route('/myModel',methods = ['GET','POST'])
def myModel():
	_date = request.form.get('date')
	_time = request.form.get('time')
	_maxtemp = str(request.form.get('maxtemp'))
	_mintemp =str(request.form.get('mintemp'))
	_rain = str(request.form.get('rain'))
	_gmin = str(request.form.get('gmin'))
	_soil = str(request.form.get('soil'))

	time_dict = {'12:30 AM':1,'01:00 AM':2,'01:30 AM':3,'02:00 AM':4,'02:30 AM':5,'03:00 AM':6,'03:30 AM':7,'04:00 AM':8,'04:30 AM':9,'05:00 AM':10,'05:30 AM':11,'06:00 AM':12,'06:30 AM':13,'07:00 AM':14,'07:30 AM':15,'08:00 AM':16,'08:30 AM':17,'09:00 AM':18,'09:30 AM':19,'10:00 AM':20,'10:30 AM':21,'11:00 AM':22,'11:30 AM':23,'12:00 PM':24,'12:30 PM':25,'01:00 PM':26,'01:30 PM':27,'02:00 PM':28,'02:30 PM':29,'03:00 PM':30,'03:30 PM':31,'04:00 PM':32,'04:30 PM':33,'05:00 PM':34,'05:30 PM':35,'06:00 PM':36,'06:30 PM':37,'07:00 PM':38,'07:30 PM':39,'08:00 PM':40,'08:30 PM':41,'09:00 PM':42,'09:30 PM':43,'10:00 PM':44,'10:30 PM':45,'11:00 PM':46,'11:30 PM':47,'12:00 AM':48}
	date_object = datetime.strptime(_date,'%m/%d/%Y').date()
	day = calendar.day_name[date_object.weekday()]
	day_dict = {'Monday':0,'Tuesday':1,'Wednesday':2,'Thursday':3,'Friday':4,'Saturday':5,'Sunday':6}
	date_string = datetime.strftime(date_object,'%Y-%m-%d')
	time_value = time_dict[_time]

	test_set = [float(_rain),float(_maxtemp),float(_mintemp),float(_gmin),float(_soil)]
	#test_set = [_rain,_maxtemp,_mintemp,_gmin,_soil]
	loaded_model = pickle.load(open('dataModel.sav','rb'))
	result = loaded_model.predict(test_set)
	var = day_dict[day]
	value_result = getPredictiveValue(var,time_value,result)
	result_value = float(value_result/3000)

	return render_template('model.html',title = 'LNMIIT_LBapp | Prediction' ,prediction = result_value)

if __name__ == '__main__':
	app.run(debug=True)
