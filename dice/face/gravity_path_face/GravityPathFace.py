from time import sleep
from chall_cube.face.Face import Face
from gpiocrust import Header, OutputPin


class GravityPathFace(Face):

    def __init__(self, accelerometer):
        super().__init__()

        self.__accelerometer = accelerometer
        self.__has_stop_request = False

    def request_stop(self):
        self.__has_stop_request = True

    def start(self):
        self.print('Running gravity path face.')

        with Header() as header:
            led_middle_red = OutputPin(8, value=1)
            led_middle_green = OutputPin(10, value=0)
            led_paths = [
                OutputPin(12, value=1),
                OutputPin(16, value=1),
                OutputPin(18, value=1),
                OutputPin(22, value=1)
            ]

            while not self.__has_stop_request:
                led_middle_red.value = 1 - led_middle_red.value

                current_face = self.__accelerometer.get_current_face()

                self.print('Current face: %d' % current_face)

                sleep(1.2)
