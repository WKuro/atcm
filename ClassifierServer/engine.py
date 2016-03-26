#-----------------------------------------------------------
# Author : Le Thai An EEIT2015 and Nguyen The Viet CS2015
# Organization: Vietnamese-German University
# Date created: 26-3-2016
# Place: Binh Duong Conference Center, Binh Duong New City, Vietnam
#-----------------------------------------------------------

import cv2
import json
import numpy as np
import time
import socket
import pygame
import struct
from pygame.locals import *
import threading

class StreamHandler(threading.Thread):
    def __init__(self, tcp_addr, BUFFER_SIZE=1024):
        threading.Thread.__init__(self)

        self.temp_array = np.zeros((1, 76800), dtype=np.float32)

        self.BUFFER_SIZE = BUFFER_SIZE
        self.total_frames = 0
        self.__state = True

        self.server = socket.socket()
        self.server.bind(tcp_addr)
        self.server.listen(0)

        self.connection = self.server.accept()[0].makefile('rb')
    def run(self):
        stream_bytes =''
        cv2.startWindowThread()
        cv2.namedWindow('Traffic', cv2.CV_WINDOW_AUTOSIZE)
        try:
            while self.__state:
                stream_bytes += self.connection.read(self.BUFFER_SIZE)
                first = stream_bytes.find('\xff\xd8')
                last = stream_bytes.find('\xff\xd9')
                if first != -1 and last != -1:
                    jpg = stream_bytes[first:last + 2]
                    stream_bytes = stream_bytes[last+2:]
                    image = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.CV_LOAD_IMAGE_GRAYSCALE)
                    self.temp_array = image.reshape(1, 76800).astype(np.float32)
                    self.total_frames +=1
        finally:
            cv2.destroyAllWindows()

    def stop_handle(self):
        self.__state=False

class ClientStream:
    def __init__(self, tcp_addr, size, fps):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, size[0])
        self.cap.set(4, size[1])
        self.cap.set(5, fps)

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(tcp_addr)
        self.__state = True

        self.connection = self.client.makefile('wb')

    def stream(self):
        try:
            while self.__state:
                completed, frame = self.cap.read()
                ret, jpeg = cv2.imencode('.jpg', frame)
                self.connection.write(jpeg.tobytes())
        finally:
            self.connection.close()
            self.client.close()

    def stop_stream(self):
        self.__state =False
