from flask import Blueprint, request, jsonify
from backend.extensions import db
from models.user import User
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return jsonify(msg="User registered")

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()
    if not user:
        return jsonify(msg="Invalid credentials"), 401

    token = create_access_token(identity={"id": user.id, "role": user.role})
    return jsonify(access_token=token)
