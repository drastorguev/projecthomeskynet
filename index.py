from flask import Flask, render_template
import requests
import json
from apikeys import metofficekey
import time

def clean5date(thismessydate):
    thiscleandate1 = time.strptime(str(thismessydate),'%Y-%m-%d'+'Z')
    thiscleandate2 = time.strftime("%A, %d-%b-%y", thiscleandate1)
    return thiscleandate2

app = Flask(__name__)

app.jinja_env.globals.update(clean5date=clean5date)

@app.route('/')
def hello_world():
    return 'Project Home Skynet is live!'

@app.route('/weather')
def gettingweather():
    returneddata1 = requests.get('http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/350928?res=3hourly&key='+metofficekey).content
    returneddata2 = json.loads(returneddata1)
    cleandate1 = time.strptime(str(returneddata2['SiteRep']['DV']['dataDate']),'%Y-%m-%d'+'T'+'%H:%M:%S'+'Z')
    cleandate2 = time.strftime("%A, %d %B %Y at %H:%M", cleandate1)
    forlocation = str(returneddata2['SiteRep']['DV']['Location']['name']).title() +', ' + str(returneddata2['SiteRep']['DV']['Location']['country']).title()
    dailydata = returneddata2['SiteRep']['DV']['Location']['Period']
    return render_template('weather.html', cleandate2=cleandate2, forlocation=forlocation, dailydata=dailydata )
