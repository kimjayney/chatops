from flask import Flask  
from flask_restx import Api, Resource   
from dotenv import load_dotenv
load_dotenv(verbose=True)

app = Flask(__name__)  
api = Api(app)   
from slackapi import SlackAPI
import os
token = os.getenv("SLACK_TOKEN")
slack = SlackAPI(token)

from bots.pfsense import Pfsenses
api.add_namespace(Pfsenses, '/pfsense')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=81) 