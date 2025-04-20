import cv2
import pyttsx3
import time

# Initialize TTS engine
engine = pyttsx3.init()

# Load the face detection model (comes with OpenCV)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start camera
cap = cv2.VideoCapture(0)

last_spoken = 0  # Time tracker to prevent spam
cooldown = 3     # Seconds between voice alerts

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to grayscale for detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # If face detected and cooldown passed, speak
    if len(faces) > 0 and (time.time() - last_spoken) > cooldown:
        engine.say("Face detected")
        engine.runAndWait()
        last_spoken = time.time()

    # Show the video feed
    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
