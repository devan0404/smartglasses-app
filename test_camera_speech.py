import cv2
import pyttsx3

# Initialize speech engine
engine = pyttsx3.init()
engine.say("Starting camera. Hello world!")
engine.runAndWait()

# Start webcam
cap = cv2.VideoCapture(0)  # 0 is your default camera
if not cap.isOpened():
    engine.say("Camera not detected.")
    engine.runAndWait()
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Smart Glasses Preview", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
engine.say("Camera closed. Goodbye.")
engine.runAndWait()
