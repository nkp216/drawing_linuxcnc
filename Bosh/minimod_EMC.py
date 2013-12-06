#!/usr/bin/python
import linuxcnc
import minimalmodbus
import time
vfd_sinus = minimalmodbus.Instrument('/dev/ttyACM0', 1)
vfd_sinus.serial.baudrate = 19200
s = linuxcnc.stat()
try:
    while 1:
	s.poll()
	#spindle speed
	if s.spindle_speed < 0:
		set_rpm = ((s.spindle_speed * -1)/0.30)
	else :
		set_rpm = (s.spindle_speed/(0.30))

	vfd_sinus.write_register(1, 251, 0)
	# on/off spindle
	onoff = vfd_sinus.read_register(1, 0)
	bin_onoff = bin(onoff)
	spindle_cmd = s.mcodes[2]
	if spindle_cmd == 3 :
		set_onoff = int(bin_onoff[2:12] + '0' + '1'+ '0', 2)
	
	if spindle_cmd == 4 :
		set_onoff = int(bin_onoff[2:12] + '1' + '0'+ '0', 2)
	
	if spindle_cmd == 5 :
		set_onoff = int(bin_onoff[2:12] + '0' + '0'+ '1', 2)
	else: 
		set_onoff = 0
	vfd_sinus.write_register(2, set_onoff, 0)
	time.sleep(0.1)	
except KeyboardInterrupt:
    raise SystemExit
