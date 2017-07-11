Dice challenges
===============

Dice challenges for RaspberryPi cube.


## Install

Requires git, Docker and docker-compose.

``` bash
# Clone the project
git clone git@github.com:alcalyn/dice.git
cd dice/

# Only for RaspberryPi:
cp docker/docker-compose.rpi.yml docker-compose.override.yml

# Only to develop on AMD64:
cp docker/docker-compose.amd64.yml docker-compose.override.yml

# Install dependencies and run dice
make
```


## License

This project is under [AGPL-3.0 License](LICENSE).
