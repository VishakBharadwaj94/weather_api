from flask import Flask,render_template,redirect,url_for,request
from functions import weather_info
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/weather',methods=['GET','POST'])
def weather():
	if request.method == 'POST':
		city = request.form['city']
		units = request.form['units']
		info = weather_info(city,units)
		return render_template('home.html',info=info)
	return redirect(url_for('home'))


app.run(debug=True)