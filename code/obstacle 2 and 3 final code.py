from machine import Pin, PWM, SPI, ADC
from mfrc522 import MFRC522
from servo import Servo
import time

# delay to process it
print("Starting in 5 seconds...")
time.sleep(5)

# rfid card
spi = SPI(2, baudrate=1000000, polarity=0, phase=0,
          sck=Pin(18), mosi=Pin(23), miso=Pin(19))

rdr = MFRC522(spi=spi, gpioRst=Pin(22), gpioCs=Pin(5))

# -buzzer
buzzer = PWM(Pin(25))
buzzer.freq(1000)
buzzer.duty(0)

# servo
servo_rfid = Servo(Pin(13))   # RFID servo
servo_ldr  = Servo(Pin(27))   # LDR servo

# ldr
ldr = ADC(Pin(26))
ldr.atten(ADC.ATTN_11DB)

# uid code
correct_uid = [69, 250, 3, 7, 187]

# pirate theme
def pirates_sound():
    notes = [
        330,392,440,440,0,
        440,494,523,523,0,
        523,587,494,494,0,
        440,392,440,0
    ]

    durations = [
        0.12,0.12,0.25,0.12,0.12,
        0.12,0.12,0.25,0.12,0.12,
        0.12,0.12,0.25,0.12,0.12,
        0.12,0.12,0.35,0.12
    ]

    for i in range(len(notes)):
        if notes[i] == 0:
            buzzer.duty(0)
        else:
            buzzer.freq(notes[i])
            buzzer.duty(400)

        time.sleep(durations[i])
        buzzer.duty(0)
        time.sleep(0.02)

    buzzer.duty(0)

# error
def error_sound():
    buzzer.freq(400)
    buzzer.duty(400)
    time.sleep(1)
    buzzer.duty(0)

# positions
servo_rfid.write_angle(0)
servo_ldr.write_angle(0)
time.sleep(1)

print("System Ready")

# main loop
while True:

    # ldr runs always
    value = ldr.read()

    if value > 2000:
        servo_ldr.write_angle(150)
    else:
        servo_ldr.write_angle(0)


    #rfid
    stat, _ = rdr.request(rdr.REQIDL)

    if stat == rdr.OK:
        stat, uid = rdr.anticoll()

        if stat == rdr.OK:
            print("Card:", uid)

            if uid == correct_uid:
                print("Access Granted")

                # OPEN RFID SERVO
                servo_rfid.write_angle(170)
                time.sleep(1)

                # stop signal before sound
                servo_rfid.write_us(0)

                pirates_sound()

                time.sleep(5)

                # CLOSE
                servo_rfid.write_angle(0)
                time.sleep(1)
                servo_rfid.write_us(0)

            else:
                print("Wrong Card")
                error_sound()

    time.sleep(0.1)