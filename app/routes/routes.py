import uuid
from flask import request, jsonify, Blueprint
from app.models.models import Users, db

users = Blueprint('users', __name__)


@users.route("/")
def index():
    return "Welcome User!"


@users.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    new_user = Users(
        public_id=str(uuid.uuid4()),
        first_name=data["first_name"],
        last_name=data["last_name"],
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"Message": "User Added"})


@users.route("/users", methods=["GET"])
def get_all_users():
    get_users = Users.query.all()
    output = []
    for user in get_users:
        user_data = {
            "public_id": user.public_id,
            "first_name": user.first_name,
            "last_name": user.last_name
        }
        output.append(user_data)

    return jsonify({"users": output})


@users.route("/users/<public_id>", methods=["GET"])
def get_single_user(public_id):

    user = Users.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({"message": "User Not Found"})
    else:
        user_data = {
            "public_id": user.public_id,
            "first_name": user.first_name,
            "Last_name" : user.last_name
        }

    return jsonify({"user": user_data})


@users.route("/users/<public_id>", methods=["DELETE"])
def delete_single_user(public_id):
    user = Users.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({"message": "User Not Found"})
    else:
        db.session.delete(user)
        db.session.commit()
    return jsonify({"message": "User has been deleted"})
