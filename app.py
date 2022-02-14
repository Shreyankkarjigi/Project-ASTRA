from flask import *
from nasapy import Nasa
import requests
import json
import webbrowser

key="TJ0EVVNFCbMpoNkvtus5tcKaeGEpffq6b53DgBc9"
nasa=Nasa(key=key)


app = Flask('mars_discovery')

@app.route("/image_day")
def image_day():
    
    
    f = r"https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&count=1"
    data = requests.get(f)
    tt = json.loads(data.text)
        
    print(tt[0]["title"])
    webbrowser.open(tt[0]["url"])

    
@app.route("/")
def home():
    earth_date=request.args.get('date')
    print(earth_date)
    data=nasa.mars_rover(earth_date=earth_date)


    return render_template('home.html',earth_date=earth_date,data=data)



app.run(debug=True)

