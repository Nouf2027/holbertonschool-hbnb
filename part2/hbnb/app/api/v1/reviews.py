from flask_restx import Namespace, Resource, fields
from flask import request
from app.services import facade

api = Namespace("reviews", description="Review operations")

review_model = api.model("Review", {
    "text": fields.String(required=True),
    "rating": fields.Integer(required=True),
    "user_id": fields.String(required=True),
    "place_id": fields.String(required=True),
})

@api.route("/")
class ReviewList(Resource):
    def post(self):
        data = request.get_json()
        review, error = facade.create_review(data)
        if error:
            return {"error": error}, 400
        return {
            "id": review.id,
            "text": review.text,
            "rating": review.rating,
            "user_id": review.user_id,
            "place_id": review.place_id
        }, 201

    def get(self):
        reviews = facade.get_all_reviews()
        return [
            {
                "id": r.id,
                "text": r.text,
                "rating": r.rating,
                "user_id": r.user_id,
                "place_id": r.place_id
            } for r in reviews
        ], 200

@api.route("/<review_id>")
class ReviewItem(Resource):
    def get(self, review_id):
        review = facade.get_review(review_id)
        if not review:
            return {"error": "Review not found"}, 404
        return {
            "id": review.id,
            "text": review.text,
            "rating": review.rating,
            "user_id": review.user_id,
            "place_id": review.place_id
        }, 200

    def put(self, review_id):
        data = request.get_json()
        review, error = facade.update_review(review_id, data)
        if error:
            return {"error": error}, 400
        return {"message": "Review updated successfully"}, 200

    def delete(self, review_id):
        deleted, error = facade.delete_review(review_id)
        if not deleted:
            return {"error": error}, 404
        return {"message": "Review deleted successfully"}, 200

