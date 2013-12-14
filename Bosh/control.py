import hal 
import glib
import linuxcnc
import subprocess
import pygtk
pygtk.require('2.0')

import gtk
import gtk.glade
import gobject

class HandlerClass:

    def on_button_press(self,widget,data=None):

    		
		f_result = open("/home/nkp/emc2-dev-80db2a2/nc_files/7.ngc","w")
		
		f_begin = open("/home/nkp/emc2-dev-80db2a2/nc_files/6.ngc","r")
		if f_begin:
			self.bline = f_begin.readlines()
			print self.bline
			

		st = ['F400','G1','X',str(self.velx.get_value()),'Y',str(self.vely.get_value()), '\n','G10','L20','P2','X0','Y0','Z0','\n','G55','\n',]
		self.gst =' '.join(st)
		f_result.write(self.gst)

		f_result.writelines(self.bline)
		f_result.close()
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
        
	
        
	self.vely = self.builder.get_object('hal_hscale1')
	self.velx = self.builder.get_object('hal_hscale2')

	




def get_handlers(halcomp,builder,useropts):
    return [HandlerClass(halcomp,builder,useropts)]
