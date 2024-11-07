import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


def read() -> tuple[str,str]:
    reader = SimpleMFRC522()
    
    try:
        print("\nReading Data...")
        id, text = reader.read()
        print(id)
        print(text)
        print("Done.\n")
        return (id, text)
    finally:
        GPIO.cleanup()
    return None