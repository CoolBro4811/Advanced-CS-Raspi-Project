import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

def write(text : str) -> None:
    reader = SimpleMFRC522()

    try:
        reader.write(text)
        print("Data written.\n")
        return
    finally:
        GPIO.cleanup()
    return


def writeInput() -> tuple[str, str]:
    text = input("Enter the data that will be stored on the RFID card/chip:\n")

    write(text)

    print("Finished, exiting...\n")