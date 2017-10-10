import RPi.GPIO as GPIO
from time import sleep
from chall_cube.face.Face import Face
from shiftr_74HC595.shiftr_74HC595 import ShiftRegister


class GravityPathFace(Face):

    def __init__(self, accelerometer, ser, rclk, srclk):
        super().__init__()

        self.__accelerometer = accelerometer
        self.__ser = ser
        self.__rclk = rclk
        self.__srclk = srclk

    def request_stop(self):
        self.__has_stop_request = True

    def start(self):
        self.print('Running gravity path face.')

        self.__has_stop_request = False
        shift_register = ShiftRegister(self.__ser, self.__rclk, self.__srclk)

        PATH_0 = 2
        PATH_1 = 1
        PATH_2 = 3
        PATH_3 = 4
        MIDDLE_GREEN = 6
        MIDDLE_RED = 5

        paths = [
            [5, 1, 4, 5],
            [5, 4, 6, 3, 1, 5],
            [5, 3, 1, 2, 3, 5],
            [5, 6, 5, 4, 1, 3, 5]
        ]

        path_trackers = [-1] * 4
        path_resolved = [False] * 4
        path_leds = [PATH_0, PATH_1, PATH_2, PATH_3]

        shift_register.setOutputs([GPIO.LOW] * 8)
        shift_register.setOutput(MIDDLE_RED, GPIO.HIGH)

        for i in range(0, 4):
            shift_register.setOutput(path_leds[i], GPIO.HIGH)

        shift_register.latch()

        while not self.__has_stop_request:
            current_face = self.__accelerometer.get_current_face()
            self.print(current_face)

            for i in range(0, 4):
                if path_resolved[i]:
                    continue

                if -1 == path_trackers[i]:
                    if current_face == paths[i][0]:
                        path_trackers[i] = 0

                    continue

                if current_face == paths[i][path_trackers[i]]:
                    continue

                if current_face != paths[i][path_trackers[i] + 1]:
                    path_trackers[i] = -1
                    continue

                path_trackers[i] += 1

                if path_trackers[i] == len(paths[i]) - 1:
                    path_resolved[i] = True

                    shift_register.setOutput(path_leds[i], GPIO.LOW)
                    shift_register.latch()

                    if all(path_resolved):
                        shift_register.setOutput(MIDDLE_RED, GPIO.LOW)
                        shift_register.setOutput(MIDDLE_GREEN, GPIO.HIGH)
                        shift_register.latch()
                        break

            sleep(0.1)

    def test(self):
        self.__has_stop_request = False
        shift_register = ShiftRegister(self.__ser, self.__rclk, self.__srclk)

        PATH_0 = 2
        PATH_1 = 1
        PATH_2 = 3
        PATH_3 = 4
        MIDDLE_GREEN = 6
        MIDDLE_RED = 5

        self.__has_stop_request = False
        delay = 0.5

        while not self.__has_stop_request:
            self.print('off')
            shift_register.setOutputs([GPIO.LOW] * 8)
            shift_register.latch()
            sleep(delay)

            self.print('path 1')
            shift_register.setOutput(PATH_0, GPIO.HIGH);
            shift_register.latch()
            sleep(delay)

            self.print('path 2')
            shift_register.setOutput(PATH_1, GPIO.HIGH);
            shift_register.latch()
            sleep(delay)

            self.print('path 3')
            shift_register.setOutput(PATH_2, GPIO.HIGH);
            shift_register.latch()
            sleep(delay)

            self.print('path 4')
            shift_register.setOutput(PATH_3, GPIO.HIGH);
            shift_register.latch()
            sleep(delay)

            self.print('red')
            shift_register.setOutput(MIDDLE_RED, GPIO.HIGH);
            shift_register.latch()
            sleep(delay)

            self.print('green')
            shift_register.setOutput(MIDDLE_RED, GPIO.LOW);
            shift_register.setOutput(MIDDLE_GREEN, GPIO.HIGH);
            shift_register.latch()
            sleep(delay)

            shift_register.setOutputs([GPIO.LOW] * 8)
            shift_register.latch()
