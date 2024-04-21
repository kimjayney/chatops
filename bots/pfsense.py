from flask import request
from flask_restx import Resource, Api, Namespace 
Pfsenses = Namespace('pfsense')

@Pfsenses.route('') 
class SetIPAddr(Resource):
    def get(self): 
        return request.args.get("text")
 