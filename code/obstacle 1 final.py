from machine import Pin, PWM
import time

# --- Setup ---
SERVO_PIN = 13
BTN_5_PIN = 14
BTN_8_PIN = 12

btn5 = Pin(BTN_5_PIN, Pin.IN, Pin.PULL_UP)
btn8 = Pin(BTN_8_PIN, Pin.IN, Pin.PULL_UP)

step = 0

def move_servo(direction, duration):
    # Force the pin to be an output before starting PWM
    temp_pin = Pin(SERVO_PIN, Pin.OUT)
    servo = PWM(temp_pin, freq=50)
   
    if direction == "open":
        print("Action: Spinning Forward")
        servo.duty(115)
    else:
        print("Action: Spinning Backward")
        servo.duty(40)
       
    time.sleep(duration)
   
    # Completely destroy the PWM object to stop the motor
    servo.deinit()
    # Explicitly pull the pin LOW so there is zero voltage
    temp_pin.value(0)
    print("Stopped and De-energized.")

print("--- System Ready ---")

while True:
    # Button 5 logic
    if btn5.value() == 0:
        print("Button 5 Pressed")
        step = 1
        time.sleep(0.3)

    # Button 8 logic
    if btn8.value() == 0:
        if step == 1:
            print("Sequence Correct! Moving now...")
           
            # Move forward 1 second
            move_servo("open", 1.0)
           
            time.sleep(0.5) # Short pause
           
            # Move backward 1 second
            move_servo("close", 1.0)
           
            while btn8.value() == 0:
                time.sleep(0.01)
        else:
            print("You must press Button 5 first!")
           
        step = 0
        time.sleep(0.3)

    time.sleep(0.05)