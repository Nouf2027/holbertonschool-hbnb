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

    @jwt_required()
    @api.expect(user_update, validate=True)
    @api.marshal_with(user_out, code=200)
    @api.response(403, 'Unauthorized action')
    @api.response(400, 'Invalid update')
    def put(self, user_id):
        """
        Update user:
        Admin: can update any user (email,password)
        User: can update only himself (no email,password)
        """
        user = facade.get_user(user_id)
        if not user:
            api.abort(404, "User not found")

        claims = get_jwt()
        is_admin = claims.get('is_admin', False)
        current_user_id = get_jwt_identity()

        data = api.payload or {}

        if not is_admin:
            if user_id != current_user_id:
                return {'error': 'Unauthorized action'}, 403
            if 'email' in data or 'password' in data:
                return {'error': 'You cannot modify email or password.'}, 400

        if is_admin and 'email' in data:
            existing_user = facade.get_user_by_email(data['email'])
            if existing_user and existing_user.id != user_id:
                return {'error': 'Email already registered'}, 400

        updated_user, err = facade.update_user(user_id, data)
        if err:
            if 'not found' in err.lower():
                api.abort(404, err)
            api.abort(400, err)

        # allow admin to set password via model method if present
        if is_admin and 'password' in data:
            if hasattr(updated_user, 'hash_password'):
                updated_user.hash_password(data['password'])

        return updated_user.to_dict(), 200
