from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class HouseDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_name = db.Column(db.String(100), nullable=False)
    aadhar_number = db.Column(db.String(12), nullable=False)
    length = db.Column(db.Float, nullable=False)
    breadth = db.Column(db.Float, nullable=False)
    area = db.Column(db.Float, nullable=False)
    roof_type = db.Column(db.String(50), nullable=False)
    year_of_construction = db.Column(db.Integer, nullable=False)
    drainage_type = db.Column(db.String(100), nullable=False)
    road_type = db.Column(db.String(100), nullable=False)
    electricity_connection_type = db.Column(db.String(100), nullable=False)
    house_type = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<HouseDetail {self.id}>'
