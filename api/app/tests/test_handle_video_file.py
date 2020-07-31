import unittest
from app import create_app, db
import os
from werkzeug.datastructures import FileStorage
from app.utils.handle_video_file import HandleVideoFile


class TestHandleVideoFile(unittest.TestCase):

    def setUp(self):
        print("setup")
        app = create_app()
        self.client = app.test_client()

        self.handle_video_file = HandleVideoFile("/api/uploads")

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

    def test_convertor(self):

        response, flag = self.handle_video_file.convert_to_videp_capture(
            self.test_video)

        self.assertTrue(flag)

        response, flag = self.handle_video_file.convert_to_videp_capture(
            self.test_csv)

        self.assertFalse(flag)

        response, flag = self.handle_video_file.convert_to_videp_capture(
            self.test_img)

        self.assertFalse(flag)
