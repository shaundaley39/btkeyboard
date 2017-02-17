import json
import RPi.GPIO as GPIO
import os

class GPIO_Glove:
  def __init__( self, call_finger):
    script_dir = os.path.dirname(__file__)
    layout_file_path = os.path.join(script_dir, 'pinlayout.json')
    pin_layout = json.loads(open(layout_file_path).read())["pinlayout"]["zero"]["right"]
    self.call_finger = call_finger
    self.code_of_pin = pin_layout["fingers"]
    self.thumb = pin_layout["thumb"]
    self.palm = pin_layout["palm"]
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.thumb, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(self.palm, GPIO.OUT)
    pwm_out = GPIO.PWM(self.palm, 4000)      # create object red for PWM on port 24 at 100 Hertz  
    pwm_out.start(65)              # red fully on (65%)
    for p in self.code_of_pin.keys():
      pin = int(p)
      GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
      GPIO.add_event_detect(pin, GPIO.RISING, callback=self.call_both, bouncetime=300)

  def call_both(self, input_pin):
    self.call_finger(self.code_of_pin[  str(input_pin) ])
