import asyncio
import os
from flask import Flask, request
from flask_cors import CORS
from variables import variables

class Endpoints:
    def __init__(self):
        self.db_request = None

    def main_endpoints(self):
        app = Flask(__name__)
        CORS(app)

        @app.route("/", methods=['GET'])
        def main_page():
            return {"message": "site was started"}

        # server send the request user status about, response is True or False
        # /is_user_active?{user_id}
        @app.route(variables.is_user_active_endpoint, methods=['GET'])
        def is_user_active():
            # check user status in bot
            user_id = request.args.get('user_id')
            active = True
            return {"response": active}

        @app.route(variables.provide_message_to_user_endpoint, methods=['POST'])
        def provide_message_to_user():
            data = request.json
            message = data['message']
            user_id = data['user_id']
            return {"response": "good"}

        @app.route(variables.impossible_to_cancel_order_endpoints, methods=['GET'])
        def impossible_to_cancel_order():
            return {"response": "good"}




        app.run(host='127.0.0.1', port=int(os.environ.get('PORT', 5000)))

if __name__ == '__main__':
    ep = Endpoints()
    ep.main_endpoints()
