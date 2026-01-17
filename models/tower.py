from backend.extensions import db

class Tower(db.Model):
    __tablename__ = "towers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Tower {self.name}>"