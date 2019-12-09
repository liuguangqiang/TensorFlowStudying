# coding=UTF-8

import cv2
import sys

import face_recognition

imagePath = "test_face_detection.jpg"
image = face_recognition.load_image_file(imagePath)
face_locations = face_recognition.face_locations(image)

print(face_locations)

