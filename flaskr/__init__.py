from flask import Flask, jsonify
from flask_cors import CORS



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    CORS(app)
    # cors = CORS(app, resources={r"/api/*": {"origins": "*"}}) # resource  specific

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response
        
    @app.route('/')
    # @cross_origin() # route specific

    def hello():
        return jsonify({ 'message': 'Hello world'})

    @app.route('/smiley')
    def smiley():
        return ":)"


    return app
