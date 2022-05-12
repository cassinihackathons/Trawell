from mimetypes import init
import os
import shutil

import yaml

class DatabaseConfig:
    def __init__(self, node) -> None:
        self.address = node["address"]
        
class Config:
    def __init__(self) -> None:
        config = None
        if not os.path.exists("config.yaml"):
            shutil.copyfile("templates/config.yaml", "config.yaml")
        with open("config.yaml", "r") as config_file:
            config = yaml.load(config_file, Loader=yaml.FullLoader)
        
        self.database = DatabaseConfig(config["database"])