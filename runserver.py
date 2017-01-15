from flask import Flask 
from flask import request,render_template
app  = Flask(__name__)

@app.route('/')
@app.route('/home/',methods = ['GET','POST'])
def home():
	return render_template('index.html',title = 'LNMIIT_LBapp | Home')

if __name__ == '__main__':
	app.run(debug=True)
