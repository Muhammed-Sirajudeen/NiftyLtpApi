# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import requests
from bs4 import BeautifulSoup
from flask_cors import CORS



# creating the flask app

def scrapper():
    
    url="https://www.nseindia.com/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    html_content = requests.get(url,headers=headers).text
    soup = BeautifulSoup(html_content, "html.parser")
    val=soup.find_all("span",{"class":"val ltp"})
    for i in val:
        value=i.get_text()
        return value
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


# creating an API object
api = Api(app)

# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class Hello(Resource):

	# corresponds to the GET request.
	# this function is called whenever there
	# is a GET request for this resource
    
    def get(self):
        value=scrapper()
        return jsonify({'message': value})
    



# another resource to calculate the square of a number



# adding the defined resources along with their corresponding urls
api.add_resource(Hello, '/')



# driver function
if __name__ == '__main__':

	app.run(debug = True)
