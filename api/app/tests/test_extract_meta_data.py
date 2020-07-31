from app import create_app, db
import unittest
import os
import cv2
from werkzeug.datastructures import FileStorage
from app.utils.extract_meta import ExtractMetaData
from datetime import datetime


class TestExtractMetaData(unittest.TestCase):

    def setUp(self):
        print("setup")
        app = create_app()
        self.client = app.test_client()

        # create test video data
        test_video = os.path.join(
            "/api/app/tests/video_data/Pexels Videos 2432402.mp4")

        test_video = FileStorage(stream=open(test_video, "rb"),
                                 filename="Pexels Videos 2432402.mp4",
                                 content_type="multipart/form-data")
        # create VideoCapture
        cap = cv2.VideoCapture(
            "/api/app/tests/video_data/Pexels Videos 2432402.mp4")

        self.extract_meta = ExtractMetaData(
            test_video, cap)

        # create test video data
        test_video2 = os.path.join(
            "/api/app/tests/video_data/video123.mp4")

        test_video2 = FileStorage(stream=open(test_video2, "rb"),
                                  filename="video123.mp4",
                                  content_type="multipart/form-data")
        # create VideoCapture
        cap2 = cv2.VideoCapture(
            "/api/app/tests/video_data/video123.mp4")

        self.extract_meta2 = ExtractMetaData(
            test_video2, cap2)

        # initialize test data
        db.create_all()

    def tearDown(self):
        print("tearDown")
        # delete test db
        db.session.remove()
        db.drop_all()

    def test_extract_filename(self):
        response = self.extract_meta.extract_filename()

        self.assertEqual("Pexels Videos 2432402.mp4", response)

        response = self.extract_meta2.extract_filename()

        self.assertEqual("video123.mp4", response)

    def test_timestamp(self):
        response = self.extract_meta.create_timestamp()

        self.assertEqual(datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"), response)

    def test_extract_minetype(self):
        response = self.extract_meta.extract_mimetype()
        self.assertEqual("multipart/form-data", response)

        response = self.extract_meta2.extract_mimetype()
        self.assertEqual("multipart/form-data", response)

    def test_extract_duration(self):
        response = self.extract_meta.extract_duration()
        self.assertIsInstance(response, str)

        response = self.extract_meta2.extract_duration()
        self.assertIsInstance(response, str)

    def test_extract_width_and_height(self):
        width, height = self.extract_meta.extract_width_and_height()
        self.assertIsInstance(width, float)
        self.assertIsInstance(height, float)

        width, height = self.extract_meta2.extract_width_and_height()
        self.assertIsInstance(width, float)
        self.assertIsInstance(height, float)

    def test_create_meta_data(self):
        response = self.extract_meta.create_meta_data()
        self.assertIsInstance(response, list)
        self.assertEqual(len(response[0]), 6)

        response = self.extract_meta2.create_meta_data()
        self.assertIsInstance(response, list)
        self.assertEqual(len(response[0]), 6)
