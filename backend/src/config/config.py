import os
import shutil

import yaml

        
class Config:
    def __init__(self) -> None:
        config = None
        if not os.path.exists("config.yaml"):
            shutil.copyfile("templates/config.yaml", "config.yaml")
        with open("config.yaml", "r") as config_file:
            config = yaml.load(config_file, Loader=yaml.FullLoader)
        
        self.radius = config["common"]["radius"]