from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace("users", description="User operations")

user_in = api.model("UserIn", {
    "first_name": fields.String(required=True),
    "last_name": fields.String(required=True),
    "email": fields.String(required=True),
})

user_update = api.model("UserUpdate", {
    "first_name": fields.String(required=False),
    "last_name": fields.String(required=False),
    "email": fields.String(required=False),
})

user_out = api.model("UserOut", {
    "id": fields.String,
    "first_name": fields.String,
    "last_name": fields.String,
    "email": fields.String,
})

@api.route("/")
class UserList(Resource):
    @api.marshal_list_with(user_out, code=200)
    def get(self):
        users = facade.get_all_users()
        return [u.to_dict() for u in users], 200

    @api.expect(user_in, validate=True)
    @api.marshal_with(user_out, code=201)
    def post(self):
        data = api.payload
        if facade.get_user_by_email(data["email"]):
            api.abort(400, "Email already registered")
        user = facade.create_user(data)
        return user.to_dict(), 201

@api.route("/<string:user_id>")
class UserResource(Resource):
    @api.marshal_with(user_out, code=200)
    def get(self, user_id):
        user = facade.get_user(user_id)
        if not user:
            api.abort(404, "User not found")
        return user.to_dict(), 200

    @api.expect(user_update, validate=True)
    @api.marshal_with(user_out, code=200)
    def put(self, user_id):
        data = api.payload
        user = facade.get_user(user_id)
        if not user:
            api.abort(404, "User not found")
        if "email" in data and data["email"] != user.email:
            if facade.get_user_by_email(data["email"]):
                api.abort(400, "Email already registered")
        updated = facade.update_user(user_id, data)
        return updated.to_dict(), 200
