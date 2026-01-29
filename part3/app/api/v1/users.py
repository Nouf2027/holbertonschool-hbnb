from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity
from app.services import facade

api = Namespace("users", description="User operations")

# --- Models ---

user_in = api.model("UserIn", {
    "first_name": fields.String(required=True),
    "last_name": fields.String(required=True),
    "email": fields.String(required=True),
    "password": fields.String(required=True),  
})

# Model for user update ,Added password here so Admins can send it if needed
user_update = api.model("UserUpdate", {
    "first_name": fields.String(required=False),
    "last_name": fields.String(required=False),
    "email": fields.String(required=False),
     "password": fields.String(required=False), 
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
# --- Endpoints ---

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
          """
        Update user:
     Admin: can update any user (email,password)
     User: can update only himself (no email,password)
        """

claims = get_jwt()
        is_admin = claims.get('is_admin', False)
        current_user_id = get_jwt_identity()

        data = api.payload

        # inflied admin  restrictions
        if not is_admin:
            if user_id != current_user_id:
                return {'error': 'Unauthorized action'}, 403

            if 'email' in data or 'password' in data:
                return {'error': 'You cannot modify email or password.'}, 400

# check Admin email  
        if is_admin and 'email' in data:
            existing_user = facade.get_user_by_email(data['email'])
            if existing_user and existing_user.id != user_id:
                return {'error': 'Email already registered'}, 400

        user = facade.update_user(user_id, data)
        if not user:
            return {'error': 'User not found'}, 404
 # Admin password update
        if is_admin and 'password' in data:
            user.hash_password(data['password'])

        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }, 200
