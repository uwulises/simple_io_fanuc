import RPi.GPIO as GPIO
import time
import socket

UDP_IP = "192.168.1.5"
UDP_PORT = 4712

GPIO.setmode(GPIO.BCM)
INPUT_PIN = 17  # Example: using GPIO 17

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    GPIO.setup(INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    last_state = None  # Track last signal state

    while True:
        current_state = GPIO.input(INPUT_PIN)

        if current_state != last_state:  # Only send when state changes
            if current_state == GPIO.LOW:
                print("Button Pressed!")
                msg = "StartMotor"
            else:
                print("Button Released.")
                msg = "StopMotor"

            sock.sendto(msg.encode(), (UDP_IP, UDP_PORT))
            last_state = current_state  # Update last state

        time.sleep(0.5)  # Small delay for stability

except KeyboardInterrupt:
    print("\nExiting program.")
finally:
    GPIO.cleanup()



