from flask import Flask, request, render_template
import requests
app = Flask(__name__)


@app.route('/')
def webpage():
    return render_template('index.html')

@app.route('/weatherapp', methods = ['POST', 'GET'])
def weatherdata():

    city = request.form.get('city')
    units = request.form.get('units')
    appid = request.form.get('appid')

    api_url='https://api.openweathermap.org/data/2.5/weather'
    params = {'q':city, 'units':units, 'appid': appid}
    responce = requests.get(api_url, params=params)
    data = responce.json()
    feelslike = data['main']['feels_like']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    temp = data['main']['temp']
    city = data['name']
    possibility = data['weather']
    wind = data["wind"]

    return f'''City :{city} 
    Tempreture :{temp} 
    Feels Like Tempreture :{feelslike} 
    Humidity :{humidity} 
    Pressure :{pressure} 
    Wind :{wind} 
    Posibility :{possibility}'''

if __name__== '__main__':
    app.run(host='0.0.0.0', port= 5002)


