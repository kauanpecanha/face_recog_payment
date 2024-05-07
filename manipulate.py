from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np
import requests

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("keras_Model.h5", compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()

# load the face detection model from cv2
facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# getting the image
sample = cv2.imread("./analyze/1.jpg")

# transforming the sample to a gray image for better detection
gray = cv2.cvtColor(sample, cv2.COLOR_BGR2GRAY)

# face detection
faces = facedetect.detectMultiScale(gray,1.3,5)

# for each face recognized at the gray picture
for x,y,w,h in faces:
    # cv2.rectangle(sample, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # crop of the specific area of the face
    crop_img=sample[y:y+h,x:x+h]
    
    # resizing the image in order to fit the model input dimensions
    image=cv2.resize(crop_img, (224,224))

# showing the face area
cv2.imshow("Face", crop_img)  

# Make the image a numpy array and reshape it to the models input shape.
image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

# normalizing the image
image = (image / 127.5) - 1

# Predicts the model
prediction = model.predict(image)
index = np.argmax(prediction)
class_name = class_names[index]
confidence_score = prediction[0][index]

# print(class_name)

# splits the string
splits = class_name.split()

# collecting the second string, as it is the customer's name
print(splits[1])

# writing it down into a txt file
with open("storage.txt", "w") as f:
    
    for i in range(1, len(splits)):
        f.write(f"{splits[i]}")
        f.write(" ")