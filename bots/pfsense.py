from flask import request
from flask_restx import Resource, Api, Namespace 
Pfsenses = Namespace('pfsense')
import os

@Pfsenses.route('') 
class SetIPAddr(Resource):
    def get(self):  
        if request.args.get("secret") == os.getenv("BOT_PFSENSE_SECRET"):
            return request.args.get("text")
        else:
            return 403
 