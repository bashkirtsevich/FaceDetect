import cv2
import sys

# Get user supplied values
imagePath = 'python.jpg'
cascPath = 'haarcascade_frontalface_default.xml'
smilePath = 'haarcascade_smile.xml'
eyePath = 'haarcascade_eye.xml'

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)
smileCascade = cv2.CascadeClassifier(smilePath)
eyeCascade = cv2.CascadeClassifier(eyePath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.05,
    minNeighbors=8,
    minSize=(55, 55)
    #flags=cv2.CV_HAAR_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]

    smile = smileCascade.detectMultiScale(
        roi_gray,
        scaleFactor=1.7,
        minNeighbors=2,
        minSize=(25, 25)
    )

    # Set region of interest for smiles
    for (x, y, w, h) in smile:
        print "Found", len(smile), "smiles!"
        cv2.rectangle(roi_color, (x, y), (x+w, y+h), (255, 0, 0), 1)

    eyes = eyeCascade.detectMultiScale(
        roi_gray#,
        #scaleFactor=1.7,
        #minNeighbors=1,
        #minSize=(17, 17)
    )
    for (ex,ey,ew,eh) in eyes:
        print "Found", len(eyes), "eyes!"
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),1)

cv2.imshow("Faces found", image)
cv2.waitKey(0)
