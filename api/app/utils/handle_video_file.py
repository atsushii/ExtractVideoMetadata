import os
from werkzeug.utils import secure_filename
import cv2
import magic


class HandleVideoFile():

    def __init__(self, upload_folder):
        self.upload_folder = upload_folder
        self.flag = True

    def convert_to_videp_capture(self, file):

        if not os.path.isdir(self.upload_folder):
            os.mkdir(self.upload_folder)

        filename = secure_filename(file.filename)

        if not os.path.isfile(self.upload_folder + "/" + filename):
            file.save(os.path.join(self.upload_folder, filename))

        if not "MP4" in magic.from_file(self.upload_folder + "/" + filename):
            self.flag = False

        cap = cv2.VideoCapture(self.upload_folder + "/" + filename)

        os.remove(self.upload_folder + "/" + filename)

        return cap, self.flag
