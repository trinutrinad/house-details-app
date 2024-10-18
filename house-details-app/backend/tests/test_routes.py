import unittest
from app import create_app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_house(self):
        response = self.client.post('/houses', json={
            'owner_name': 'John Doe',
            'aadhar_number': '123456789012',
            'length': 30,
            'breadth': 40,
            'roof_type': 'Concrete',
            'year_of_construction': 2020,
            'drainage_type': 'Sewage',
            'road_type': 'Paved',
            'electricity_connection': 'Yes',
            'house_type': 'Living'
        })
        self.assertEqual(response.status_code, 201)
