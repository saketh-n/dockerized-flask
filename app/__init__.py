from flask import Flask, jsonify
import logging

def create_app():
    app = Flask(__name__)

    # Set up logging
    logging.basicConfig(level=logging.INFO)
    
    @app.route('/')
    def home():
        return 'Hello, Docker!'
    
    @app.route('/health')
    def health():
        return jsonify(status="UP"), 200
    
    return app
