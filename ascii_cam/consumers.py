import json
from channels.generic.websocket import WebsocketConsumer

import cv2
import math


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

        vid = cv2.VideoCapture(0)

        gs_string = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`.                           '
        rgs_string = gs_string[::-1]
        while True:
            ret, frame = vid.read()
            resized_frame = cv2.resize(frame, (110, 110))
            matrix = list()
            for row in range(len(resized_frame)):
                hor = list()
                for col in range(len(resized_frame[row])):
                    pixel = resized_frame[row][col]
                    rgb_plus = pixel[0] + pixel[1] + pixel[2]
                    ascii_pixel = math.ceil((rgb_plus / 765) * len(gs_string))
                    ascii_val = rgs_string[ascii_pixel]
                    hor.append(ascii_val)
                hor_string = ' '.join(hor)
                hor_div = f'<div>{hor_string}</div>'
                matrix.append(hor_div)
            matrix_string = "".join(matrix)
            self.send(text_data=json.dumps({
                'type': 'connection established',
                'message': 'You are now connected',
                'stream': matrix_string
            }))
