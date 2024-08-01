from flask import Flask, request, jsonify
from flask_cors import CORS

from semester import get_1st,get_2nd,get_3rd,get_4th
from main import get_result

app = Flask(__name__)
CORS(app)

app.add_url_rule('/result' , 'get_result' ,get_result ,methods=['GET'])
app.add_url_rule('/1st' , 'get_1st' ,get_1st ,methods=['GET'])
app.add_url_rule('/2nd' , 'get_2nd' ,get_2nd ,methods=['GET'])
app.add_url_rule('/3rd' , 'get_3rd' ,get_3rd ,methods=['GET'])
app.add_url_rule('/4th' , 'get_4th' ,get_4th ,methods=['GET'])




if __name__ == '__main__':
    app.run(debug=True)
