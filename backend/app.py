from flask import Flask

from src.config.config import Config
from src.controllers.user_controller import UserController
from src.controllers.location_controller import LocationController

app = Flask(__name__)

if __name__ == "__main__":
    config = Config()
    user_controller = UserController(app)
    location_controller = LocationController(app, config)
    
    app.run()
    