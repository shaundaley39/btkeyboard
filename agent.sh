#!/usr/bin/expect -f

spawn "bluetoothctl"
expect "#"
send "agent on\r"
expect "Agent registered"
send "default-agent\r"
expect "Default agent request successful"
send "scan on\r"
expect "Discovery started"
expect "agent"
expect "Confirm passkey"
send "yes\r"       
expect "#" ;# this shows up and if the connection with the computer isn't initialised, both top level expects timeout and this gets send.

