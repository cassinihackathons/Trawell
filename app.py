from dataclasses import dataclass
from flask import Flask
from src.config.config import Config
from src.controllers.main_controller import MainController
from src.controllers.user_controller import UserController

app = Flask(__name__)

if __name__ == "__main__":
    config = Config()
    geo_controller = MainController(app)
    user_controller = UserController(app, jason_config=config.jason)
    
    app.run()
    