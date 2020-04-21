from flask import Flask, jsonify,request
from .models import setup_db, Plant
from flask_cors import CORS



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    # cors = CORS(app, resources={r"/api/*": {"origins": "*"}}) # resource  specific

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response
        
    @app.route('/plants')
    # @cross_origin() # route specific
    def get_plants():
        page=request.args.get('page',1 ,type=int)
        start=(page-1)*4 # Display the first 4 plants in the database
        end=start + 4
        plants = Plant.query.all()
        formatted_plants = [plant.format() for plant in plants]

        return jsonify({
            'success': True,
            'plants': formatted_plants[start:end],
            'total_plants':len(formatted_plants)
        })

    def hello():
        return jsonify({ 'message': 'Hello world'})

    @app.route('/smiley')
    def smiley():
        return ":)"


    return app
