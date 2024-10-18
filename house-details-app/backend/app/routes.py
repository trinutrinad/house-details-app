from flask import Flask, request, jsonify
from app import db
from app.models import HouseDetail

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///houses.db'  # Use your database URI
db.init_app(app)

@app.route('/api/houses', methods=['POST'])
def add_house():
    data = request.json
    new_house = HouseDetail(
        owner_name=data['ownerName'],
        aadhar_number=data['aadharNumber'],
        length=data['length'],
        breadth=data['breadth'],
        area=data['area'],
        roof_type=data['roofType'],
        year_of_construction=data['yearOfConstruction'],
        drainage_type=data['drainageType'],
        road_type=data['roadType'],
        electricity_connection_type=data['electricityConnectionType'],
        house_type=data['houseType']
    )
    db.session.add(new_house)
    db.session.commit()
    return jsonify({'message': 'House details saved successfully!'}), 201
