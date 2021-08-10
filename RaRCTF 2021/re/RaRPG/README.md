# RaRPG

## Patching the binary
We patch the game binary so that the * moves 2 steps to the right whenever we press right arrow
![patch](patch.PNG)

## Getting the flag
We ran the binary using the following command LD_LIBRARY_PATH=$(pwd) ./client 193.57.159.27 60415,
then we move to the left wall and bypass it with the right key.

![flag](flag.PNG)
