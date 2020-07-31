import imutils
import numpy as np
import cv2
import time
import os


class YoloVideo():

    def __init__(self, cap):
        self.cap = cap
        self.writer = None
        self.height = None
        self.width = None
        self.label = "person"
        self.color = (102, 220, 225)
        self.cfg = os.path.join(os.path.dirname(
            __file__), '../yolo/yolov3-tiny.cfg')
        self.weight = os.path.join(os.path.dirname(
            __file__), '../yolo/yolov3-tiny.weights')

    def count_person(self):

        yolo = cv2.dnn.readNetFromDarknet(self.cfg, self.weight)
        layer = yolo.getLayerNames()

        layer = [layer[i[0] - 1] for i in yolo.getUnconnectedOutLayers()]

        prop = cv2.CAP_PROP_FRAME_COUNT
        total = int(self.cap.get(prop))

        counter_dict = {}
        while True:
            grab, frame = self.cap.read()

            if not grab:
                break

            if self.width is None or self.height is None:
                self.height, self.width = frame.shape[:2]

            blob = cv2.dnn.blobFromImage(
                frame, 1/255.0, (416, 416), swapRB=True, crop=False)

            yolo.setInput(blob)
            layerOutput = yolo.forward(layer)

            boxes = []
            confidences = []
            classIDs = []

            for output in layerOutput:
                for detection in output:
                    scores = detection[5:]
                    classID = np.argmax(scores)
                    confidence = scores[classID]

                    if confidence > 0.5:

                        box = detection[0:4] * \
                            np.array([self.width, self.height,
                                      self.width, self.height])
                        (center_x, center_y, w, h) = box.astype("int")

                        x = int(center_x - (w/2))
                        y = int(center_y - (h/2))

                        boxes.append([x, y, int(w), int(h)])
                        confidences.append(float(confidence))
                        classIDs.append(classID)
            idxs = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.5)
            count_person = 0
            if len(idxs) > 0:
                for i in idxs.flatten():

                    if classIDs[i] == 0:
                        count_person += 1
            counter_dict[self.cap.get(cv2.CAP_PROP_POS_MSEC)] = count_person

        return counter_dict
