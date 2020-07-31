from datetime import datetime
import cv2


class ExtractMetaData():
    """
    Extract metadata from uploaded video.
    """

    def __init__(self, video, cap):
        """
        Constructor
        :param video: uploaded video
        :param cap: uploaded video as caption object
        """
        self.video = video
        self.cap = cap

    def create_meta_data(self):
        """
        Collect all of result from each functions
        """
        filename = self.extract_filename()
        create_time = self.create_timestamp()
        mime_type = self.extract_mimetype()
        duration = self.extract_duration()
        width, height = self.extract_width_and_height()

        meta_data = [
            {"filename": filename,
             "create_time": create_time,
             "mime_type": mime_type,
             "duration": duration,
             "width": width,
             "height": height}
        ]

        return meta_data

    def extract_filename(self):
        """
        Extract filename
        """
        filename = self.video.filename
        return filename

    def create_timestamp(self):
        """
        Create timestamp
        """
        create_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return create_time

    def extract_mimetype(self):
        """
        Extract minetype
        """
        mime_type = self.video.mimetype
        return mime_type

    def extract_duration(self):
        """
        Extract duration
        """
        fps = self.cap.get(cv2.CAP_PROP_FPS)
        frame = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = frame / fps

        return f"{duration} s"

    def extract_width_and_height(self):
        """
        Extract width and height of frames
        """

        width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        return width, height
