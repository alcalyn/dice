import random
from time import sleep
from chall_cube.face.Face import Face
from ky040.KY040 import KY040


class StrongBoxFace(Face):

    def __init__(self, buzzer, pin_clock, pin_data):
        super().__init__()

        self.__buzzer = buzzer
        self.__pin_clock = pin_clock
        self.__pin_data = pin_data

        self.__has_stop_request = False

    def request_stop(self):
        self.__has_stop_request = True

    def start(self):
        self.print('Running strong box face.')

        self.success = False
        self.counter = 0
        self.combo = 0
        self.secret = None
        self.direction = 1
        self.lastSecret = None

        def rotaryChange(rotation):
            if self.success:
                return

            if None == self.secret:
                self.secret = random.randint(1, 20)
                self.counter = 0
                self.combo = 0

            self.counter += 1 if rotation else -1
            self.print("counter=%s combo=%s secret=%s direction=%s lastSecret=%s" % (self.counter, self.combo, self.secret, self.direction, self.lastSecret))

            if self.secret == self.counter or (0 == self.combo and self.secret == -self.counter):
                if 0 == self.combo:
                    self.direction = -1 if self.counter > 0 else 1
                else:
                    self.direction *= -1

                self.__buzzer.hz_async(800.0, 0.2)
                self.combo += 1
                self.lastSecret = self.counter
                self.secret = self.counter + random.randint(1, 20) * self.direction

            elif self.combo > 0:
                if (1 == self.direction and self.counter < self.lastSecret) or (-1 == self.direction and self.counter > self.lastSecret):
                    self.__buzzer.hz_async(300.0, 0.6)
                    self.combo = 0
                    self.secret = None
                    self.lastSecret = None

            if self.combo >= 8:
                for i in range(6, 20):
                    self.__buzzer.hz(i * 100.0, 0.1)

                self.success = True

        ky040 = KY040(self.__pin_clock, self.__pin_data, rotaryCallback=rotaryChange, rotaryBouncetime=40)
        ky040.start()

        try:
            while not self.success and not self.__has_stop_request:
                sleep(1)
        finally:
            ky040.stop()
            self.print("Strong box open, face solved.")
