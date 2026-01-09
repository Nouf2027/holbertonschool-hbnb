

from flask_restx import Namespace, Resource
from flask import request
from app.services.facade import HBnBFacade

api = Namespace("places", description="Places endpoints")
facade = HBnBFacade()

@api.route("/")
class PlaceList(Resource):
    def get(self):
        places = facade.get_all_places()
        return [p.to_dict() for p in places], 200

    def post(self):
        data = request.get_json()
        place, error = facade.create_place(data)
        if error:
            return {"error": error}, 400
        return place.to_dict(), 201

@api.route("/<place_id>")
class PlaceItem(Resource):
    def get(self, place_id):
        place = facade.get_place(place_id)
        if not place:
            return {"error": "Place not found"}, 404
        return place.to_dict(), 200

    def put(self, place_id):
        data = request.get_json()
        place, error = facade.update_place(place_id, data)
        if error:
            return {"error": error}, 400
        return place.to_dict(), 200
