import RPi.GPIO as GPIO
import time
import threading

# Motor A (Left)
IN1 = 17
IN2 = 18
ENA = 24

# Motor B (Right)
IN3 = 22
IN4 = 23
ENB = 25

# Relay
RELAY_SPRAY = 27
RELAY_MOWER = 16

# State flags
autonomous_running = False
override_active = False

def setup():
    GPIO.setmode(GPIO.BCM)

    # Motors
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)
    GPIO.setup(ENA, GPIO.OUT)
    GPIO.setup(ENB, GPIO.OUT)
    GPIO.output(ENA, GPIO.HIGH)
    GPIO.output(ENB, GPIO.HIGH)

    # Relays — set HIGH immediately to prevent triggering on boot
    GPIO.setup(RELAY_SPRAY, GPIO.OUT)
    GPIO.setup(RELAY_MOWER, GPIO.OUT)
    GPIO.output(RELAY_SPRAY, GPIO.HIGH)
    GPIO.output(RELAY_MOWER, GPIO.HIGH)

def forward():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

def backward():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

def turn_left():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

def turn_right():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

def stop():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

def spray_on():
    GPIO.output(RELAY_SPRAY, GPIO.LOW)

def spray_off():
    GPIO.output(RELAY_SPRAY, GPIO.HIGH)

def mower_on():
    GPIO.output(RELAY_MOWER, GPIO.LOW)

def mower_off():
    GPIO.output(RELAY_MOWER, GPIO.HIGH)

def zigzag_pattern():
    # One zigzag pass: forward, turn, forward, turn back
    forward()
    time.sleep(2)
    stop()
    time.sleep(0.3)
    turn_right()
    time.sleep(0.6)
    stop()
    time.sleep(0.3)
    forward()
    time.sleep(2)
    stop()
    time.sleep(0.3)
    turn_left()
    time.sleep(0.6)
    stop()
    time.sleep(0.3)

def auto_run():
    global autonomous_running
    while autonomous_running:
        zigzag_pattern()
    stop()

def auto_on():
    global autonomous_running
    autonomous_running = True
    t = threading.Thread(target=auto_run)
    t.daemon = True
    t.start()

def auto_off():
    global autonomous_running
    autonomous_running = False
    stop()

def override_on():
    global override_active
    override_active = True

def override_off():
    global override_active
    override_active = False

def cleanup():
    global autonomous_running
    autonomous_running = False
    GPIO.output(RELAY_SPRAY, GPIO.HIGH)
    GPIO.output(RELAY_MOWER, GPIO.HIGH)
    GPIO.cleanup()
