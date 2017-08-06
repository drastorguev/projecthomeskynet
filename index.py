from flask import Flask, render_template
import requests
import json
from apikeys import metofficekey


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Project Home Skynet is live!'

@app.route('/weather')
def gettingweather():
    returneddata1 = requests.get('http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/350928?res=3hourly&key='+metofficekey).content
    returneddata2 = json.loads(returneddata1)
    asofdate = str(returneddata2['SiteRep']['DV']['dataDate']).title()
    forlocation = str(returneddata2['SiteRep']['DV']['Location']['name']).title() +', ' + str(returneddata2['SiteRep']['DV']['Location']['country']).title()
    dailydata = returneddata2['SiteRep']['DV']['Location']['Period']
    return render_template('weather.html', asofdate=asofdate, forlocation=forlocation, dailydata=dailydata)
