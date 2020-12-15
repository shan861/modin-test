import json
from flask import Flask,request,jsonify
import modin.pandas as pd
import pandas as pdn

import timeit

import os 

app = Flask(__name__)


@app.route('/')
def hello():    
    return "APP is running!"

@app.route('/modin-pd')
def modinpd():
    #q=request.args['q']  
    start = timeit.default_timer()
    df = pd.read_csv("GL_Data.csv")
    count=len(df)
    stop = timeit.default_timer()
    print('Time modin pd taken: ', stop - start) 
    #output = json.dumps(result, default=set_default)
    return str(count)

@app.route('/normal-pd')
def normalpd():
    #q=request.args['q'] 
    start = timeit.default_timer() 
    dfn = pdn.read_csv("GL_Data.csv")
    count=len(dfn)
    stop = timeit.default_timer()
    print('Time normal pd taken: ', stop - start) 
    #output = json.dumps(result, default=set_default)
    return str(count)


if __name__=='__main__':
    app.run() 




