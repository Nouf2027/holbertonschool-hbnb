from flask_restx import Namespace, Resource
from flask import request
from app.services import facade

api = Namespace("places", description="Places endpoints")


@api.route("/")
class PlaceList(Resource):
    def get(self):
        places = facade.get_all_places()
        return [p.to_dict() for p in places], 200

    def post(self):
        data = request.get_json(silent=True) or {}
        place, error = facade.create_place(data)
        if error:
            # Reference error: owner must exist
            if error == "Owner not found":
                return {"error": error}, 404
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
        data = request.get_json(silent=True) or {}
        place, error = facade.update_place(place_id, data)
        if error:
            if error == "Place not found":
                return {"error": error}, 404
            if error == "Owner not found":
                return {"error": error}, 404
            return {"error": error}, 400
        return place.to_dict(), 200


@api.route("/<place_id>/reviews")
class PlaceReviewList(Resource):
    def get(self, place_id):
        reviews, error = facade.get_reviews_by_place(place_id)
        if error:
            return {"error": error}, 404

        return [
            {
                "id": r.id,
                "text": r.text,
                "rating": r.rating,
                "user_id": r.user_id,
                "place_id": r.place_id
            } for r in reviews
        ], 200
