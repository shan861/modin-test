import json
from flask import Flask,request,jsonify
import modin.pandas as pd
import pandas as pdn

import timeit
import time

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
    stop = timeit.default_timer()

    count=len(df)
    
    print('Time modin pd taken: ', stop - start) 
    #output = json.dumps(result, default=set_default)
    s = time.time()
    df = pd.concat([df for _ in range(5)])
    e = time.time()
    print("Pandas Concat Time = {}".format(e-s))


    return str(count)

@app.route('/normal-pd')
def normalpd():
    #q=request.args['q'] 
    start = timeit.default_timer() 
    dfn = pdn.read_csv("GL_Data.csv")
    stop = timeit.default_timer()

    count=len(dfn)
    
    print('Time normal pd taken: ', stop - start) 
    #output = json.dumps(result, default=set_default)
    return str(count)

@app.route('/test_modin')
def test_modin():
    #q=request.args['q'] 

   

    ### Read in the data with Modin    

    s = time.time()
    df = pd.read_csv("GL_Data.csv")
    e = time.time()
    print("Modin Loading Time = {}".format(e-s))    


    df = pd.read_csv("GL_Data.csv")
    s = time.time()
    df = pd.concat([df for _ in range(5)])
    e = time.time()
    print("Modin Concat Time = {}".format(e-s))



    count=len(df)
    return str(count)

@app.route('/test_normal')
def test_normal():
    #q=request.args['q'] 

    ### Read in the data with Pandas   

    s = time.time()
    df = pdn.read_csv("GL_Data.csv")
    e = time.time()
    print("Pandas Loading Time = {}".format(e-s))

   

    df = pdn.read_csv("GL_Data.csv")
    s = time.time()
    df = pdn.concat([df for _ in range(5)])
    e = time.time()
    print("Pandas Concat Time = {}".format(e-s))  



    count=len(df)
    return str(count)


@app.route('/largefile')
def largefile():
     df = pd.read_csv("GL_Data.csv")  
     df = pd.concat([df] * 15)
     df.to_csv('big_csv.csv')

     count=len(df)
     return str(count)


@app.route('/largefile_modin')
def large_modin():
    #q=request.args['q'] 

   

    ### Read in the data with Modin    

    s = time.time()
    df = pd.read_csv("big_csv.csv")
    e = time.time()
    print("Modin Loading Time = {}".format(e-s))    


    df = pd.read_csv("big_csv.csv")
    s = time.time()
    df = pd.concat([df for _ in range(5)])
    e = time.time()
    print("Modin Concat Time = {}".format(e-s))



    count=len(df)
    return str(count)

@app.route('/largefile_pandas')
def large_normal():
    #q=request.args['q'] 

    ### Read in the data with Pandas   

    s = time.time()
    df = pdn.read_csv("big_csv.csv")
    e = time.time()
    print("Pandas Loading Time = {}".format(e-s))

   

    df = pdn.read_csv("big_csv.csv")
    s = time.time()
    df = pdn.concat([df for _ in range(5)])
    e = time.time()
    print("Pandas Concat Time = {}".format(e-s))  



    count=len(df)
    return str(count)


if __name__=='__main__':
    app.run() 




