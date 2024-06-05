from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import logging
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Set up logging directory
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    # Set up logging
    logging.basicConfig(filename='logs/app.log', level=logging.INFO, 
                        format='%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    
    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    @app.route('/')
    def home():
        app.logger.info("Home route accessed")
        return 'Hello, Docker!'
    
    @app.route('/health')
    def health():
        app.logger.info("Health check route accessed")
        return jsonify(status="UP"), 200
    
    return app
