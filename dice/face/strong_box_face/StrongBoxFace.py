import RPi.GPIO as GPIO
from time import sleep
from chall_cube.face.Face import Face
from chall_cube.device.Buzzer import Buzzer


class StrongBoxFace(Face):

    def __init__(self):
        super().__init__()

    def request_stop(self):
        self.__has_stop_request = True

    def start(self):
        self.print('Running strong box face.')

        buzzer = Buzzer(7)
        buzzer.hz(440.0, 0.5)
        buzzer.hz(262.0, 1.0)
        buzzer.hz(494.0, 0.5)
