from machine import Pin, PWM # create PWM object from a pin and set the frequency = 20Hz of slice associated with pin 3
# and duty cycle = 50%, duty_u16 sets the duty cycle as a ratio duty_u16 / 65535

pwm0 = PWM(Pin(3), freq=20, duty_u16=32768) 
pwm0.freq() # get the current frequency of slice 0
pwm0.duty_u16() # get the current duty cycle of channel A, range 0-65535

print(pwm0) # show the properties of the PWM object.