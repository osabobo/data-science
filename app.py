from  simple import simple_interest
from flask import Flask, request, jsonify

app = Flask(__name__)



@app.route("/") 
def hello():
    return "This is my first API!"; 

@app.route('/post', methods=["GET","POST"])
def interest_score():
     input_json = request.get_json(force=True) 
     principal= input_json["principal"]
     rate= input_json["rate"]
     period= input_json["period"]
     interest=simple_interest(principal,rate,period)
     return jsonify(interest)

if __name__ == "__main__":
    app.run()
