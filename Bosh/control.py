import hal
import glib
import time
import linuxcnc
import subprocess

class HandlerClass:

    def on_button_press(self,widget,data=None):
		f = open("/home/nkp/emc2-dev-80db2a2/nc_files/7.ngc","w")
		f.write('m2')
		f.close()
		self.stat.poll()
		if self.stat.interp_state == linuxcnc.INTERP_IDLE :
			self.linuxcnc.reset_interpreter()
			self.linuxcnc.mode(linuxcnc.MODE_AUTO)
			subprocess.call(["axis-remote","/home/nkp/emc2-dev-80db2a2/nc_files/7.ngc"])

    def __init__(self, halcomp,builder,useropts):
	self.linuxcnc = linuxcnc.command()
	self.stat = linuxcnc.stat()
        self.halcomp = halcomp
        self.builder = builder



def get_handlers(halcomp,builder,useropts):
    return [HandlerClass(halcomp,builder,useropts)]
