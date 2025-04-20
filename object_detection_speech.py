import cv2
import pyttsx3
import time

# Load the pre-trained model (MobileNet SSD)
net = cv2.dnn.readNetFromCaffe(
    'models/MobileNet-SSD/deploy.prototxt',
    'models/MobileNet-SSD/mobilenet_iter_73000.caffemodel'
)

# Initialize TTS
engine = pyttsx3.init()

# Classes the model can detect
CLASSES = [
    "background", "aeroplane", "bicycle", "bird", "boat",
    "bottle", "bus", "car", "cat", "chair",
    "cow", "diningtable", "dog", "horse", "motorbike",
    "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"
]

last_spoken = {}
cooldown = 4  # seconds between saying same object

# Start camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize and prepare input
    h, w = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
                                 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > 0.5:
            idx = int(detections[0, 0, i, 1])
            label = CLASSES[idx]
            box = detections[0, 0, i, 3:7] * [w, h, w, h]
            (startX, startY, endX, endY) = box.astype("int")

            # Draw box
            cv2.rectangle(frame, (startX, startY), (endX, endY),
                          (0, 255, 0), 2)
            cv2.putText(frame, label, (startX, startY - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

            # Speak label if cooldown passed
            now = time.time()
            if label not in last_spoken or (now - last_spoken[label]) > cooldown:
                engine.say(f"{label} detected")
                engine.runAndWait()
                last_spoken[label] = now

    # Show video
    cv2.imshow("Object Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

net = cv2.dnn.readNetFromCaffe(
    'models/MobileNet-SSD/deploy.prototxt',
    'models/MobileNet-SSD/mobilenet_iter_73000.caffemodel'
)

