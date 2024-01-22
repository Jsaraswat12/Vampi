from flask import Response
from flask import Flask, jsonify, Response, request, json
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from models.user_model import *
from app import vuln


# Initialize Flask app
app = Flask(__name__)

# Initialize Limiter
limiter = Limiter(get_remote_address, app=app, default_limits=["2 per day", "2 per hour"])


@limiter.limit("10 per hour") 
def populate_db():
    db.drop_all()
    db.create_all()
    User.init_db_users()
    response_text = '{ "message": "Database populated." }'
    response = Response(response_text, 200, mimetype='application/json')
    return response

def basic():
    response_text = '{ "message": "VAmPI the Vulnerable API", "help": "VAmPI is a vulnerable on purpose API. It was ' \
                    'created in order to evaluate the efficiency of third party tools in identifying vulnerabilities ' \
                    'in APIs but it can also be used in learning/teaching purposes.", "vulnerable":' + "{}".format(vuln) + "}"
    response = Response(response_text, 200, mimetype='application/json')
    return response
