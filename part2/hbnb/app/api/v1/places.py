from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace("places", description="Places endpoints")

place_in = api.model("PlaceIn", {
    "name": fields.String(required=True),
    "description": fields.String(required=False),
    "price_per_night": fields.Float(required=True),
    "latitude": fields.Float(required=True),
    "longitude": fields.Float(required=True),
    "owner_id": fields.String(required=True),
})

place_update = api.model("PlaceUpdate", {
    "name": fields.String(required=False),
    "description": fields.String(required=False),
    "price_per_night": fields.Float(required=False),
    "latitude": fields.Float(required=False),
    "longitude": fields.Float(required=False),
    "owner_id": fields.String(required=False),
})

place_out = api.model("PlaceOut", {
    "id": fields.String,
    "name": fields.String,
    "description": fields.String,
    "price_per_night": fields.Float,
    "latitude": fields.Float,
    "longitude": fields.Float,
    "owner_id": fields.String,
})


@api.route("/")
class PlaceList(Resource):
    @api.marshal_list_with(place_out, code=200)
    def get(self):
        places = facade.get_all_places()
        return [p.to_dict() for p in places], 200

    @api.expect(place_in, validate=True)
    @api.marshal_with(place_out, code=201)
    def post(self):
        place, error = facade.create_place(api.payload)
        if error:
            if "owner not found" in error.lower():
                api.abort(404, error)
            api.abort(400, error)
        return place.to_dict(), 201


@api.route("/<string:place_id>")
class PlaceItem(Resource):
    @api.marshal_with(place_out, code=200)
    def get(self, place_id):
        place = facade.get_place(place_id)
        if not place:
            api.abort(404, "Place not found")
        return place.to_dict(), 200

    @api.expect(place_update, validate=True)
    @api.marshal_with(place_out, code=200)
    def put(self, place_id):
        place, error = facade.update_place(place_id, api.payload)
        if error:
            if "place not found" in error.lower() or "owner not found" in error.lower():
                api.abort(404, error)
            api.abort(400, error)
        return place.to_dict(), 200


@api.route("/<string:place_id>/reviews")
class PlaceReviewList(Resource):
    def get(self, place_id):
        reviews, error = facade.get_reviews_by_place(place_id)
        if error:
            api.abort(404, error)
        return [r.to_dict() for r in reviews], 200
