from flask import Flask, request, abort
from src.config.config import Config
from src.controllers.main_controller import MainController

app = Flask(__name__)

if __name__ == "__main__":
    config = Config()
    geo_controller = MainController(app)
    
    app.run()
    