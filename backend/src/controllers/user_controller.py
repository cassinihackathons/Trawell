from flask import jsonify, request
import uuid
import georinex as gr
import os

class UserController:
    def __init__(self, app) -> None:

        @app.route('/user/location', methods=['POST'])
        def location_route(): return self.location()
        
    def location(self):
        gnss_data = request.json["gnss"]
        ret_data = {}
        file_path = f'tmp/{uuid.uuid1()}.rnx'
        
        with open(file_path, "w") as file:
            file.write(gnss_data)
            
        if os.path.exists(file_path):
            obs  = gr.load(file_path)
            position = obs.position
            ret_data = {"longitude":position[0], "latitude":position[1], "atlitude":position[2]}
            os.remove(file_path)

        return jsonify(ret_data), 200
                
