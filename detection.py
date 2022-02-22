from pyexpat import model
import cv2 as cv
from threading import Thread, Lock


class Detection:

    # threading properties
    stopped = True
    lock = None
    # properties
    cascade = None
    screenshot = None
    confidence = 0
    model = None

    def __init__(self, model_file_path):
        # create a thread lock object
        self.lock = Lock()
        self.model = cv.imread(model_file_path, cv.IMREAD_UNCHANGED)

    def update(self, screenshot):
        self.lock.acquire()
        self.screenshot = screenshot
        self.lock.release()

    def start(self):
        self.stopped = False
        t = Thread(target=self.run)
        t.start()

    def stop(self):
        self.stopped = True

    def run(self):
        #print("DIOBO")
        # TODO: you can write your own time/iterations calculation to determine how fast this is
        while not self.stopped:
            if not self.screenshot is None:
                # do object detection
                min_val, confidence, min_loc, max_loc = cv.minMaxLoc(cv.matchTemplate(self.screenshot, self.model, cv.TM_CCOEFF_NORMED))
                # lock the thread while updating the results
                self.lock.acquire()
                self.confidence = confidence
                self.lock.release()
