from flask import Flask, jsonify
import logging
import os

def create_app():
    app = Flask(__name__)
    
    # Set up logging directory
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    # Set up logging
    logging.basicConfig(filename='logs/app.log', level=logging.INFO, 
                        format='%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    
    @app.route('/')
    def home():
        app.logger.info("Home route accessed")
        return 'Hello, Docker!'
    
    @app.route('/health')
    def health():
        app.logger.info("Health check route accessed")
        return jsonify(status="UP"), 200
    
    return app
