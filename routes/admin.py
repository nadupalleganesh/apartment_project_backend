from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.booking import Booking
from backend.extensions import db

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/bookings")
@jwt_required()
def view_bookings():
    return jsonify([b.status for b in Booking.query.all()])

@admin_bp.route("/booking/<int:id>/approve", methods=["PUT"])
@jwt_required()
def approve(id):
    booking = Booking.query.get(id)
    booking.status = "APPROVED"
    db.session.commit()
    return jsonify(msg="Approved")
