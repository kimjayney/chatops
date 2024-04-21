from flask import request
from flask_restx import Resource, Api, Namespace 
Pfsenses = Namespace('pfsense')
import os
import requests
@Pfsenses.route('', doc=False ) 
class SetIPAddr(Resource):
    def post(self):  
        if request.args.get("secret") == os.getenv("BOT_PFSENSE_SECRET"):
            response = requests.post(os.getenv("BOT_PFSENSE_URL"), auth=(os.getenv("BOT_PFSENSE_ID"), os.getenv("BOT_PFSENSE_PW"))).json()

            if len(response["data"]["token"]) > 0:
                headers = {
                    'Accept': 'application/json',
                    'Authorization': "Bearer {}".format(response["data"]["token"]),
                    'Content-Type': 'application/json'
                }
                data = {
                    "address": [request.args.post("text")],
                    "apply": True,
                    "descr": "string",
                    "detail": ["string"],
                    "id": "LTE_IP",
                    "name": "LTE_IP",
                    "type": "host"
                }
                result = requests.put(os.getenv("BOT_PFSENSE_API_IPADD"), json=data, headers=headers).json()
                print (result ) 
                return result
            else:
                return 400
            
        else:
            return 403
