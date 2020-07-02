```
LCD Pin : Raspberry Pi
VSS * GND
VDD * 5.0V
V0  * 
RS  : GPIO22
RW  : GND
E   : GPIO26
D0  -
D1  -
D2  -
D3  -
D4  : GPIO5
D5  : GPIO6 
D6  : GPIO13
D7  : GPIO19
A   * 5.0V
K   * GND
```

```
sudo apt-get update
sudo apt-get install -y build-essential python-dev python-smbus python-pip git
sudo pip install RPi.GPIO

cd ~/
git clone https://github.com/adafruit/Adafruit_Python_CharLCD.git
cd Adafruit_Python_CharLCD
sudo python setup.py install
```