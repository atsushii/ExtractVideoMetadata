import os
from werkzeug.utils import secure_filename
import cv2
import magic
from app.utils.validate_uploaded_file import ValidateUploadedVideo


class HandleVideoFile():
    """
    Convert to VideoCapture object by OpenCV.
    """

    def __init__(self, upload_folder):
        """
        Constructor
        param: upload_folder: it is temporary  use for saving the video file
        """
        self.upload_folder = upload_folder
        self.flag = True

    def convert_to_videp_capture(self, file):
        """
        Convert to VideoCapture by OpenCV to extract metadata.
        param: file: Uploaded video file by a user
        """

        # Make directory which saves uploaded file
        if not os.path.isdir(self.upload_folder):
            os.mkdir(self.upload_folder)

        filename = secure_filename(file.filename)

        # Save file
        if not os.path.isfile(self.upload_folder + "/" + filename):
            file.save(os.path.join(self.upload_folder, filename))

        # Check uploaded file is valid
        validator = ValidateUploadedVideo()
        self.flag = validator.validator(magic.from_file(
            self.upload_folder + "/" + filename).lower().split()[2])

        cap = cv2.VideoCapture(self.upload_folder + "/" + filename)

        os.remove(self.upload_folder + "/" + filename)

        return cap, self.flag
