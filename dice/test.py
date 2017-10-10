import RPi.GPIO as GPIO
from chall_cube.Cube import Cube
from chall_cube.device.Accelerometer import Accelerometer
from chall_cube.device.Buzzer import Buzzer
from chall_cube.face.BlankFace import BlankFace
from face.strong_box_face.StrongBoxFace import StrongBoxFace
from face.gravity_path_face.GravityPathFace import GravityPathFace

GPIO.setmode(GPIO.BOARD)

accelerometer = Accelerometer()
buzzer = Buzzer(7)

faces = [
#    StrongBoxFace(buzzer, 11, 12),
    BlankFace(),
    BlankFace(),
    BlankFace(),
    BlankFace(),
    GravityPathFace(accelerometer, 12, 16, 18),
    BlankFace()
]

dice = Cube(faces)

print('Testing dice...')

dice.test()
GPIO.cleanup()

print('Dice tests stopped.')
