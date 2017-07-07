from time import sleep
from chall_cube.face.Face import Face


class GravityPathFace(Face):

    def __init__(self, accelerometer):
        self.accelerometer = accelerometer

    def start(self):
        print('Running gravity path face.')

        while True:
            current_face = self.accelerometer.get_current_face()

            print('Current face: %d' % current_face)

            sleep(0.8)
