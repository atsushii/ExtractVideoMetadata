import unittest
from app import create_app, db
import os
import magic
from app.utils.validate_uploaded_file import ValidateUploadedVideo


class TestVideoValidator(unittest.TestCase):
    """
    Test uploaded file validation
    """

    def setUp(self):
        print("setup")
        app = create_app()
        self.client = app.test_client()

        self.validator = ValidateUploadedVideo()

        # create test video data
        test_video = os.path.join(
            "/api/app/tests/video_data/Pexels Videos 2432402.mp4")

        self.test_video = magic.from_file(test_video).lower().split()[2]

        # create test csv data
        test_csv = os.path.join(
            "/api/app/tests/video_data/test.csv")

        self.test_csv = magic.from_file(test_csv).lower().split()[2]

        # create test img data
        test_img = os.path.join(
            "/api/app/tests/video_data/test_img.jpg")

        self.test_img = magic.from_file(test_img).lower().split()[2]

        # initialize test data
        db.create_all()

    def tearDown(self):
        print("tearDown")
        # delete test db
        db.session.remove()
        db.drop_all()

    def test_validator(self):
        """
        Test uploaded file validator
        """

        # test if uploaded file extention is mp4
        flag = self.validator.validator(
            self.test_video)

        self.assertTrue(flag)

        # test if uploaded file extention is csv
        flag = self.validator.validator(
            self.test_csv)

        self.assertFalse(flag)

        # test if uploaded file extention is jpg
        flag = self.validator.validator(
            self.test_img)

        self.assertFalse(flag)
