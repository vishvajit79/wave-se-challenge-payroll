import unittest
import json

from models import db
from server import server


class TestUpload(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = server.test_client()

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_upload(self):
        """ The POST on `/upload` should fail as no file is provided """
        response = self.client.post('/v1/upload')

        self.assertEqual(response.status_code, 400)
        response_json = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_json, {'message': {
                         'file': 'The csv file for number of hours worked per day per employee'}})
