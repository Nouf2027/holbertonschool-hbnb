from flask import request
from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace("amenities", description="Amenity operations")

amenity_in = api.model("AmenityIn", {
    "name": fields.String(required=True, description="Name of the amenity"),
    "is_active": fields.Boolean(required=False, description="Amenity active flag"),
})

amenity_out = api.model("AmenityOut", {
    "id": fields.String,
    "name": fields.String,
    "is_active": fields.Boolean,
})

@api.route("/")
class AmenityList(Resource):
    @api.marshal_list_with(amenity_out, code=200)
    def get(self):
        amenities = facade.get_all_amenities()
        return [a.to_dict() for a in amenities], 200

    @api.expect(amenity_in, validate=True)
    @api.marshal_with(amenity_out, code=201)
    def post(self):
        data = request.get_json(silent=True) or {}
        amenity, error = facade.create_amenity(data)
        if error:
            api.abort(400, error)
        return amenity.to_dict(), 201

@api.route("/<string:amenity_id>")
class AmenityResource(Resource):
    @api.marshal_with(amenity_out, code=200)
    def get(self, amenity_id):
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            api.abort(404, "Amenity not found")
        return amenity.to_dict(), 200

    @api.expect(amenity_in, validate=True)
    @api.marshal_with(amenity_out, code=200)
    def put(self, amenity_id):
        data = request.get_json(silent=True) or {}
        amenity, error = facade.update_amenity(amenity_id, data)
        if error:
            if error == "Amenity not found":
                api.abort(404, error)
            api.abort(400, error)
        return amenity.to_dict(), 200
