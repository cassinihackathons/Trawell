from flask import Flask
from flask_cors import CORS

from src.config.config import Config
from src.controllers.user_controller import UserController
from src.controllers.location_controller import LocationController

app = Flask(__name__)
CORS(app)

if __name__ == "__main__":
    config = Config()
    user_controller = UserController(app)
    location_controller = LocationController(app, config)
    
    app.run(host=config.deploy.host, port=config.deploy.port)
    