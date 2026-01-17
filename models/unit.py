from backend.extensions import db

class Unit(db.Model):
    __tablename__ = "units"

    id = db.Column(db.Integer, primary_key=True)
    unit_number = db.Column(db.String(50), nullable=False)
    tower_id = db.Column(db.Integer, db.ForeignKey("towers.id"))
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default="available")

    def __repr__(self):
        return f"<Unit {self.unit_number}>"