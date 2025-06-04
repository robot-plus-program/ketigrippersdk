***
## Environment

### Linux Version : Ubuntu 20.04, 22.04, 24.04
***

## 1. Update OS
~~~
sudo apt-get update && sudo apt-get upgrade
~~~

## 2. Install dependency libraries
~~~
sudo apt-get install libmodbus*

sudo apt install python3-pip python3-dev
pip3 install pymodbus
~~~

## 3. Run example
### 3.1 C++
~~~
g++ src/sample.cpp -o sample -Iinclude -Llib/22.04 -lzimmergripper -Wl,"-rpath,lib/22.04"
./sample
~~~
###

### 3.2 Python
~~~
edit "gripper = KetiZimmer('libzimmergripper.so file path')"
python3 scripts/zimmergripper.py
~~~
###