import threading
import queue
import cv2
import pyttsx3
import time


class DetectionController:
    def __init__(self):
        self.running = False
        self.thread = None
        self.engine = pyttsx3.init()
        self.speak_delay = 2  # seconds
        self.voice_id = None
        self.speech_queue = queue.Queue()
        self.speech_thread = threading.Thread(target=self._speech_worker, daemon=True)
        self.speech_thread.start()

    def _speech_worker(self):
        while True:
            text = self.speech_queue.get()
            if text is None:
                break
            self.engine.say(text)
            self.engine.runAndWait()
            self.speech_queue.task_done()

    def set_voice(self, gender: str):
        voices = self.engine.getProperty('voices')
        for v in voices:
            if gender.lower() in v.name.lower():
                self.engine.setProperty('voice', v.id)
                self.voice_id = v.id
                return True
        return False

    def set_delay(self, seconds: float):
        self.speak_delay = seconds

    def get_status(self):
        return self.running

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._run_detection)
            self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()
            self.thread = None

    def _run_detection(self):
        CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
                   "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
                   "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
                   "sofa", "train", "tvmonitor"]

        net = cv2.dnn.readNetFromCaffe(
            'models/MobileNet-SSD/deploy.prototxt',
            'models/MobileNet-SSD/mobilenet_iter_73000.caffemodel'
        )

        cap = cv2.VideoCapture(0)
        last_spoken = {}

        try:
            while self.running:
                ret, frame = cap.read()
                if not ret:
                    break

                resized = cv2.resize(frame, (300, 300))
                blob = cv2.dnn.blobFromImage(resized, 0.007843, (300, 300), 127.5)
                net.setInput(blob)
                detections = net.forward()

                current_time = time.time()

                for i in range(detections.shape[2]):
                    confidence = detections[0, 0, i, 2]
                    if confidence > 0.5:
                        idx = int(detections[0, 0, i, 1])
                        label = CLASSES[idx]

                        if label not in last_spoken or current_time - last_spoken[label] > self.speak_delay:
                            print(f"Detected: {label}")
                            self.speech_queue.put(f"{label} ahead")
                            last_spoken[label] = current_time

                cv2.waitKey(1)
        finally:
            cap.release()
            cv2.destroyAllWindows()

controller = DetectionController()
