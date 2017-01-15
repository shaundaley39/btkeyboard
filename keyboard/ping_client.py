#!/usr/bin/python
#
# YAPTB Bluetooth keyboard emulation service
# keyboard copy client. 
# Reads local key events and forwards them to the btk_server DBUS service
#
# Adapted from www.linuxuser.co.uk/tutorials/emulate-a-bluetooth-keyboard-with-the-raspberry-pi
#
#
import os #used to all external commands
import sys # used to exit the script
import dbus
import dbus.service
import dbus.mainloop.glib
import time
import keystates # maps characters and actions to keyboard keodes

#Define a client to listen to local key events
class Keyboard( name ):
	def __init__(self):
		self.name = name
		print "setting up DBus Client"	
		self.bus = dbus.SystemBus()
		self.btkservice = self.bus.get_object('org.yaptb.btkbservice','/org/yaptb/btkbservice')
		self.iface = dbus.Interface(self.btkservice,'org.yaptb.btkbservice')	

		print "getting connection from slave glove"
		#keep trying 
#		have_dev=False
#		while have_dev==False:
#			try:
				#try and get a keyboard - should always be event0 as
				#we're only plugging one thing in
#				self.dev = InputDevice("/dev/input/event0")
#				have_dev=True
#			except OSError:
#				print "Keyboard not found, waiting 3 seconds and retrying"
#				time.sleep(3)
#			print "found a keyboard"

	#poll for keyboard events
	def event_loop(self):
		while True:
			time.sleep(3)
                        self.send_action("NEWTAB")
			self.send_action("H")
                        self.send_action("e")
                        self.send_action("l")
                        self.send_action("l")
                        self.send_action("o")
                        self.send_action(" ")
                        self.send_action("W")
                        self.send_action("o")
                        self.send_action("r")
                        self.send_action("l")
                        self.send_action("d")
                        self.send_action("!")
                        self.send_action(" ")
			for c in self.name:
				self.send_action(c)

        def send_action(self, action):
		self.send_state( keystates.getcode (action ))
		self.send_state( keystates.getcode( "DEFAULT" ))

        def send_state(self, state):
                bin_str=""
                element=state[2]
                for bit in element:
                        bin_str += str(bit)
                self.iface.send_keys(int(bin_str,2), state[4:10]  )

if __name__ == "__main__":

	print "Setting up keyboard"

	kb = Keyboard( sys.argv[1] )

	print "starting event loop"
	kb.event_loop()
