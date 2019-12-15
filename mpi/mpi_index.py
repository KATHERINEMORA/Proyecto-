from mpi4py import MPI
import numpy as np
import cv2
from time import sleep


def capture_video():
    cap = cv2.VideoCapture(0)
    j = 0
    while j < 200:
        ret, frame = cap.read()

        # comm.send(frame, dest=1, tag=0)
        comm.send(frame, dest=2)
        cv2.waitKey(40)
        j += 1

    cap.release()


def show_video():
    i = 0
    while i < 200:
        data_frame = comm.recv(source=2)

        if len(data_frame) > 0:
            i += 1

        cv2.imshow('Video Stream', data_frame)
        cv2.waitKey(20)


def detect_faces():
    k = 0
    while k < 200:
        img = comm.recv(source=0)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # detectar si hay caras
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # si las hay, dibuja rectangulos alrededor de ellas
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # enviar el frame para mostrarlo
        comm.send(img, dest=1)
        cv2.waitKey(40)
        k += 1


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    capture_video()
elif rank == 1:
    show_video()
    cv2.destroyAllWindows()
    print('Finished')
elif rank == 2:
    detect_faces()
