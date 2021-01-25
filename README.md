# NEMA 17 Python Tests with Raspberry Pi
Python codes for controlling a NEMA 17 stepper motor with a DRV8825 driver and Raspberry Pi computer

#

### - NEMA 17, DRV8825, and Raspberry Pi Wiring - 

The NEMA 17 can be wired to the Raspberry Pi via the DRV8825 driver and GPIO pins:

![NEMA-17 RPi Wiring](https://static1.squarespace.com/static/59b037304c0dbfb092fbe894/t/600dfdf5643aa169878cacac/1611529729165/nema17_rpi_drv8825_drawing.png?format=1500w)
#

The RpiMotorLib is used to control the motor, which can be installed via the following command:

```
pi@raspberrypi:~ $ sudo pip3 install rpimotorlib
```

Example output from nema17_test.py:

![NEMA-17 Test](https://static1.squarespace.com/static/59b037304c0dbfb092fbe894/t/600ef8b8a0e8fa2c29a3d8a1/1611593925474/nema17_rpi_demo.gif?format=1000w)
