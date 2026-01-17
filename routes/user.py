from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.unit import Unit
from models.booking import Booking
from backend.extensions import db

user_bp = Blueprint("user", __name__)

@user_bp.route("/units")
@jwt_required()
def get_units():
    units = Unit.query.all()
    return jsonify([u.unit_number for u in units])

@user_bp.route("/book", methods=["POST"])
@jwt_required()
def book_unit():
    user = get_jwt_identity()
    booking = Booking(
        user_id=user["id"],
        unit_id=request.json["unit_id"],
        status="PENDING"
    )
    db.session.add(booking)
    db.session.commit()
    return jsonify(msg="Booking requested")
