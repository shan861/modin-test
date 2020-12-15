import json
from flask import Flask,request,jsonify

import os 

app = Flask(__name__)

i
@app.route('/')
def hello():    
    return "APP is running!"

@app.route('/test')
def ask():
    q=request.args['q']
    
    import modin.pandas as pd

    df = pd.read_csv("GL_Data.csv")
   
    print(len(df))
    //output = json.dumps(result, default=set_default)
    return str(len(df))


if __name__=='__main__':
    app.run() 




