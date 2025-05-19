import cv2 #pip install opencv-python

# Load Haar cascade file
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
if face_cascade.empty():
    print("Error loading cascade file")
    exit()

# Load image
image = cv2.imread('1.png')
if image is None:
    print("Error loading image")
    exit()

# Resize image
img = cv2.resize(image, None, fx=0.3, fy=0.3)

# Convert to grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(imgGray, scaleFactor=1.1, minNeighbors=4, minSize=(30, 30))

# Draw rectangles
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Show result
cv2.imshow('Detected Faces', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
