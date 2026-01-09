from flask import request
from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace("places", description="Place operations")

# Input model (validation + swagger docs)
place_model = api.model("Place", {
    "name": fields.String(required=True, description="Name of the place"),
    "description": fields.String(required=False, description="Description of the place"),
    "owner_id": fields.String(required=True, description="UUID of the owner (User)"),
    # Some projects use price_per_night, others use price — we accept both
    "price_per_night": fields.Float(required=False, description="Price per night"),
    "price": fields.Float(required=False, description="Price per night (alias)"),
    "latitude": fields.Float(required=False, description="Latitude (-90 to 90)"),
    "longitude": fields.Float(required=False, description="Longitude (-180 to 180)"),
    "amenities": fields.List(fields.String, required=False, description="List of Amenity UUIDs")
})


@api.route("/")
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, "Place successfully created")
    @api.response(400, "Invalid input data")
    def post(self):
        """Register a new place"""
        data = request.get_json() or {}
        try:
            created = facade.create_place(data)
            return created, 201
        except ValueError as e:
            return {"error": str(e)}, 400

    @api.response(200, "List of places retrieved successfully")
    def get(self):
        """Retrieve a list of all places"""
        places = facade.get_all_places()
        return places, 200


@api.route("/<string:place_id>")
class PlaceResource(Resource):
    @api.response(200, "Place details retrieved successfully")
    @api.response(404, "Place not found")
    def get(self, place_id):
        """Get place details by ID"""
        place = facade.get_place(place_id)
        if not place:
            return {"error": "Place not found"}, 404
        return place, 200

    @api.expect(place_model)
    @api.response(200, "Place updated successfully")
    @api.response(404, "Place not found")
    @api.response(400, "Invalid input data")
    def put(self, place_id):
        """Update a place's information"""
        data = request.get_json() or {}
        try:
            updated = facade.update_place(place_id, data)
            if not updated:
                return {"error": "Place not found"}, 404
            return {"message": "Place updated successfully"}, 200
        except ValueError as e:
            return {"error": str(e)}, 400
