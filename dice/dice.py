import RPi.GPIO as GPIO
from chall_cube.Cube import Cube
from chall_cube.device.Accelerometer import Accelerometer
from chall_cube.face.BlankFace import BlankFace
from face.strong_box_face.StrongBoxFace import StrongBoxFace
from face.gravity_path_face.GravityPathFace import GravityPathFace

GPIO.setmode(GPIO.BOARD)

accelerometer = Accelerometer()

faces = [
    StrongBoxFace(),
    BlankFace(),
    BlankFace(),
    BlankFace(),
    GravityPathFace(accelerometer),
    BlankFace()
]

dice = Cube(faces)

print('Starting dice...')

dice.start()

print('Dice end.')

GPIO.cleanup()
