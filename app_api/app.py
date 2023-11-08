from flask import Flask, request, Response
from datetime import datetime
import json

app = Flask(__name__)

#teste app
@app.route('/')
def hello():
    print ('hello flask')
    return 'OK'
    

@app.route('/api', methods=['POST'])
def get_app():
    now = str(datetime.now())[:19]
    
    # get body 
    body = request.get_json()
    # get header
    email = request.headers.get('X-email')
    # incluide email on body
    body['email'] = email
     
   
    json_object = json.dumps(body)
    with open(f"output/api_{now}.json", "w") as outfile:
        outfile.write(json_object)
   
       
    return 'CONGRATULATION INSERT API SUCCESS'

if __name__ == "__main__":
    app.run(host ='0.0.0.0', debug = True)



        
  