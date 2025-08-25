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
g++ example/example.cpp -o example -I${PWD}/../include -L${PWD}/../lib -lzimmergripper -Wl,"-rpath,${PWD}../lib"
./example
~~~
###

### 3.2 Python
~~~
python3 example/zimmergripper.py libzimmergripper.so file path'
~~~
###