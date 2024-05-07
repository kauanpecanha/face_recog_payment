from flask import Flask, request 
import json 

# Setup flask server 
app = Flask(__name__) 

# Setup url route which will calculate 
# total sum of array. 
@app.route('/', methods = ['GET']) 
def returnMoney():
    
    return json.dumps({"result": "10201"})

if __name__ == "__main__": 
	app.run(port=5000)
