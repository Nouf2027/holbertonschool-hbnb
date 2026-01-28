from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity
from app.services import facade

api = Namespace("users", description="User operations")


user_in = api.model("UserIn", {
    "first_name": fields.String(required=True),
    "last_name": fields.String(required=True),
    "email": fields.String(required=True),
    "password": fields.String(required=True),  
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


user_created_out = api.model("UserCreatedOut", {
    "id": fields.String,
    "message": fields.String,
})


@api.route("/")
class UserList(Resource):
    @api.marshal_list_with(user_out, code=200)
    def get(self):
          """Get list of users"""
        users = facade.get_all_users()
        return [u.to_dict() for u in users], 200

    @api.expect(user_in, validate=True)
    @api.marshal_with(user_created_out, code=201)
    def post(self):
        user, error = facade.create_user(api.payload)
        if error:
            api.abort(400, error)

        
        return {"id": user.id, "message": "User created successfully"}, 201


@api.route("/<string:user_id>")
class UserResource(Resource):
    @api.marshal_with(user_out, code=200)
    def get(self, user_id):
           """Get user by ID"""
        user = facade.get_user(user_id)
        if not user:
            api.abort(404, "User not found")
        return user.to_dict(), 200

        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }, 200

        @jwt_required()
@api.expect(user_update, validate=True)
@api.marshal_with(user_out, code=200)
   @api.response(403, 'Unauthorized action')
    @api.response(400, 'Invalid update')

def put(self, user_id):
  """
        Update user:
        - Admin: can update any user (including email/password)
        - User: can update only himself (no email/password)
        """
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404

        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }, 200
  
    def put(self, user_id):
        user, error = facade.update_user(user_id, api.payload)
        if error:
            if "not found" in error.lower():
                api.abort(404, error)
            api.abort(400, error)
        return user.to_dict(), 200

 # Admin password update
        if is_admin and 'password' in data:
            user.hash_password(data['password'])

        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }, 200
