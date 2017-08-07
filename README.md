Dice challenges
===============

Dice challenges for RaspberryPi cube.


## Install

Requires:

- Python 3.6
- pip
- I2C enabled (see https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c)

``` bash
# Clone the project
git clone git@github.com:alcalyn/dice.git
cd dice/

# Install dependencies and run dice
make
```


## Develop on chall-cube

Dice uses [chall-cube](https://github.com/alcalyn/chall-cube).

To develop on this library (or a fork) at same time:

``` bash
# Clone chall-cube in another folder
cd ../
git clone git@github.com:alcalyn/chall-cube.git

# Go back to dice folder
cd dice/

# Install chall-cube using cloned repository instead of dist package
pip install -e ../chall-cube/
```

Dice will now use the local chall-cube sources
instead of dist package.


## License

This project is under [AGPL-3.0 License](LICENSE).
