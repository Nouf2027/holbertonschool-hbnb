from flask_restx import Namespace, Resource, fields
from flask import request
from app.services import facade

api = Namespace("reviews", description="Review operations")

review_in = api.model("ReviewIn", {
    "text": fields.String(required=True),
    "rating": fields.Integer(required=True),
    "user_id": fields.String(required=True),
    "place_id": fields.String(required=True),
})

review_update = api.model("ReviewUpdate", {
    "text": fields.String(required=False),
    "rating": fields.Integer(required=False),
})

review_out = api.model("ReviewOut", {
    "id": fields.String,
    "text": fields.String,
    "rating": fields.Integer,
    "user_id": fields.String,
    "place_id": fields.String,
})

def _status_from_error(msg: str) -> int:
    if msg in ("User not found", "Place not found", "Review not found"):
        return 404
    return 400

@api.route("/")
class ReviewList(Resource):
    @api.marshal_list_with(review_out, code=200)
    def get(self):
        reviews = facade.get_all_reviews()
        return [r.to_dict() for r in reviews], 200

    @api.expect(review_in, validate=True)
    @api.marshal_with(review_out, code=201)
    def post(self):
        data = request.get_json(silent=True) or {}
        review, error = facade.create_review(data)
        if error:
            return {"error": error}, _status_from_error(error)
        return review.to_dict(), 201


@api.route("/<string:review_id>")
class ReviewItem(Resource):
    @api.marshal_with(review_out, code=200)
    def get(self, review_id):
        review = facade.get_review(review_id)
        if not review:
            api.abort(404, "Review not found")
        return review.to_dict(), 200

    @api.expect(review_update, validate=True)
    @api.marshal_with(review_out, code=200)
    def put(self, review_id):
        data = request.get_json(silent=True) or {}
        review, error = facade.update_review(review_id, data)
        if error:
            return {"error": error}, _status_from_error(error)
        return review.to_dict(), 200

    @api.response(204, "Review deleted successfully")
    @api.response(404, "Review not found")
    def delete(self, review_id):
        deleted, error = facade.delete_review(review_id)
        if not deleted:
            api.abort(404, error)
        return "", 204
