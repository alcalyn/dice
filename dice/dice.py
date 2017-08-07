from chall_cube.Cube import Cube
from chall_cube.device.Accelerometer import Accelerometer
from chall_cube.face.BlankFace import BlankFace
from face.gravity_path_face.GravityPathFace import GravityPathFace

accelerometer = Accelerometer()

faces = [
    BlankFace(),
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
