from flask import Flask,request
import pandas as pd
import numpy as np
from latlon_to_bng import WGS84toOSGB36 #bng-latlon
import pickle
import json

DISTANCE_THRESHOLD = 10000

df = pd.read_csv('Data.csv')
with open('NeuralNetModel.pickle', 'rb') as handle:
    model = pickle.load(handle)


app = Flask(__name__)
def getTimeRange(t):
    if (t>=2200 and t<2400) or (t>=0 and t<600):
        return 0
    if (t>-600 and t<1400):
        return 1
    return 2

def getLocationRisk(params):
    lat = float(params.get('lat'))
    lon = float(params.get('lon'))
    easting,northing = WGS84toOSGB36(lat,lon)
    df1 = df.copy()
    df1['dist'] = np.sqrt( (df.Easting-easting)**2 + (df.Northing-northing)**2)/1000    
    df2 = df1.copy()
    df1 = df1[df1.dist<10]
    df2 = df2[df2.dist<100]
    score = df1.dist.count()/(df2.dist.count()+1.0)
    return score

@app.route('/getConditionRisk/',methods=['GET'])
def getConditionRisk():
    time = int(request.args.get('time'))
    surface = int(request.args.get('surface'))
    age = int(request.args.get('age'))
    sex = int(request.args.get('sex'))
    veh = int(request.args.get('veh'))    
    time = getTimeRange(time)
    response = {}
    response['severeRisk'] = str(model.predict_proba([[time,surface,age,sex,veh]])[0][0]*100)
    response['locationRisk'] = getLocationRisk(request.args)*100
    return json.dumps(response)

if __name__=='__main__':
    app.run()