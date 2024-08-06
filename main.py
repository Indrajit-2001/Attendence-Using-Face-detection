import cv2
import numpy as np
import face_recognition

Ritu = face_recognition.load_image_file('FaceDetection/Ritu.jpg') #loading the image
Ritu = cv2.cvtColor(Ritu,cv2.COLOR_BGR2RGB) #converting the image colored to rgb
RituTest = face_recognition.load_image_file('FaceDetection/Indrajit.jfif')
RituTest = cv2.cvtColor(RituTest,cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(Ritu)[0]
encodeRitu = face_recognition.face_encodings(Ritu)[0]
cv2.rectangle(Ritu,(faceLoc[0],faceLoc[3]),(faceLoc[1],faceLoc[2]),(255,0,255),2)



faceLocTest = face_recognition.face_locations(RituTest)[0]
encodeRituTest = face_recognition.face_encodings(RituTest)[0]
cv2.rectangle(RituTest,(faceLocTest[0],faceLocTest[3]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)

result = face_recognition.compare_faces([encodeRitu],encodeRituTest)
faceDis= face_recognition.face_distance([encodeRitu],encodeRituTest)

print(result,faceDis)
print("Running the code")
cv2.imshow('Rituparna Singh',Ritu)
cv2.imshow('Rituparna Singh Test',RituTest)
cv2.waitKey(0)
