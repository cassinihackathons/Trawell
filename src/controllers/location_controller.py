import json
import random
from flask import jsonify, request
from src.config.config import Config


class LocationController:
    def __init__(self, app, config: Config) -> None:
        self.config = config

        @app.route('/location/attraction', methods=['GET'])
        def location_attraction_route(): return self.location_attraction()

    def location_attraction(self):
        '''
            Gets location of the nearest attraction.
            Get params:
                - long: <float>
                - lat: <float>
        '''
        data = None
        with open('data.json') as json_file:
            data = json.load(json_file)
        if data is None:
            return jsonify({"error":"database error"}), 500
        
        attrations = data["attractions"]
        near_attractions = []
        chosen_attraction = None
        for attraction in attrations:
            if ((float(attraction["long"]) - float(request.args["long"]))**2 + (float(attraction["lat"]) - float(request.args["lat"]))**2)**0.5 < self.config.radius:
                near_attractions.append(attraction)

        # TODO: fix! can return really far object if radius is too small!
        if(len(near_attractions) > 0):
            chosen_attraction = random.choice(near_attractions)
        else:
            chosen_attraction = random.choice(attraction)

        return jsonify({"attraction": chosen_attraction}), 200
