from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace("amenities", description="Amenity operations")

amenity_in = api.model("AmenityIn", {
    "name": fields.String(required=True, description="Name of the amenity"),
    "is_active": fields.Boolean(required=False, description="Amenity status"),
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
        amenity, error = facade.create_amenity(api.payload)
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
    @api.response(200, "Amenity updated successfully")
    def put(self, amenity_id):
        amenity, error = facade.update_amenity(amenity_id, api.payload)
        if error:
            if "not found" in error.lower():
                api.abort(404, error)
            api.abort(400, error)
        return {"message": "Amenity updated successfully"}, 200
