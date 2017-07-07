from chall_cube.Cube import Cube
from chall_cube.face.BlankFace import BlankFace
from chall_cube.face.BlockingFace import BlockingFace
from chall_cube.sensor.Accelerometer import Accelerometer
from dice.face.GravityPathFace import GravityPathFace

accelerometer = Accelerometer()

faces = [
    BlankFace(),
    BlockingFace(),
    BlankFace(),
    BlankFace(),
    GravityPathFace(accelerometer),
    BlankFace()
]

dice = Cube(faces)

dice.start()
