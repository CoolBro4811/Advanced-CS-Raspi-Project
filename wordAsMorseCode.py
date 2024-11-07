import RPi.GPIO as GPIO
import time

class wordAsMorseCode:
    def __init__(self) -> None:
        self.buzzerPin = 4
        self.letters = []

    def addLetter(self, word : list[int]) -> None:
        self.letters.append(word)

    def playWord(self) -> None:
        print("Playing word.")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.buzzerPin, GPIO.OUT)
        GPIO.output(self.buzzerPin, False)
        for letter in self.letters:
            for t in letter:
                GPIO.output(self.buzzerPin, GPIO.HIGH)
                print(t)
                time.sleep(t/20)
                GPIO.output(self.buzzerPin, GPIO.LOW)
                time.sleep(1/20)

        GPIO.output(self.buzzerPin, GPIO.LOW)
