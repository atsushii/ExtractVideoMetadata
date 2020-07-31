import unittest
from app import create_app, db
from werkzeug.datastructures import FileStorage
import os
import json


class TestEndPoint(unittest.TestCase):
    """
    Test endpoint.
    """

    def setUp(self):
        print("setup")
        app = create_app()
        self.client = app.test_client()

        # target route
        self.target_route = "/fetch_video_information"

        # create test video data
        test_video = os.path.join(
            "/api/app/tests/video_data/Pexels Videos 2432402.mp4")

        self.test_video = FileStorage(stream=open(test_video, "rb"),
                                      filename="Pexels Videos 2432402.mp4")
        # create test csv data
        test_csv = os.path.join(
            "/api/app/tests/video_data/test.csv")

        self.test_csv = FileStorage(stream=open(test_csv, "rb"),
                                    filename="test.csv")

        # create test img data
        test_img = os.path.join(
            "/api/app/tests/video_data/test_img.jpg")

        self.test_img = FileStorage(stream=open(test_img, "rb"),
                                    filename="test_img.jpg")

        # initialize test data
        db.create_all()

    def tearDown(self):
        print("tearDown")
        # delete test db
        db.session.remove()
        db.drop_all()

    def test_fetch_video_information(self):
        """
        Test fetching metadata correctly
        """

        # Test if uploaded file is video
        response = self.client.post(self.target_route,
                                    data={"data": self.test_video},
                                    content_type="multipart/form-data")
        data = json.loads(response.data.decode('utf-8'))["metadata"][0]

        assert response.status_code == 200
        self.assertIn("create_time", data)
        self.assertIn("duration", data)
        self.assertIn("filename", data)
        self.assertIn("height", data)
        self.assertIn("mime_type", data)
        self.assertIn("width", data)

        # Test if uploaded file is CSV
        response = self.client.post(self.target_route,
                                    data={"data": self.test_csv},
                                    content_type="multipart/form-data")

        assert response.status_code == 400

        # Test if uploaded file is image
        response = self.client.post(self.target_route,
                                    data={"data": self.test_img},
                                    content_type="multipart/form-data")

        assert response.status_code == 400


if __name__ == "__main__":
    unittest.main()
