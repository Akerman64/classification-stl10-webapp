import unittest
import os
from io import BytesIO
from app import app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        self.upload_folder = app.config['UPLOAD_FOLDER']

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'STL-10 Image Classifier', response.data)

    def test_image_upload_prediction(self):
        # Create a dummy image
        data = {
            'file': (BytesIO(b'my dummy image data'), 'test.jpg')
        }
        response = self.app.post('/', data=data, content_type='multipart/form-data', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # Check if predictions are displayed (Mock mode or Real mode)
        # In mock mode, we expect some class names to appear
        # We can check for "Top 3 Predictions"
        self.assertIn(b'Top 3 Predictions', response.data)

if __name__ == '__main__':
    unittest.main()
