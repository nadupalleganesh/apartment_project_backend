from backend.extensions import db

class Booking(db.Model):
    __tablename__ = "bookings"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    unit_id = db.Column(db.Integer, db.ForeignKey("units.id"))
    booking_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Booking {self.id}>"