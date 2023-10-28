from flask import Flask,request, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/weatherapp",methods = ['GET','POST'])
def get_weatherdata():
    url = 'https://api.openweathermap.org/data/2.5/weather'
    param = {'q': request.form.get('city'),
    'appid':request.form.get('appid'),
    'units':request.form.get('units')}
    #response = requests.get(url=url,params=param,verify=False)
    #data = response.json()
    return f"data: {requests.get(url=url,params=param,verify=False).json()}"

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)