import random

class SimpleIA:
    def __init__(self):
        self.greetings = ['Hi there!', 'Hello!', 'Greetings!']
        self.weather_responses = ['It is sunny today', 'Expect some rain later', 'It will be cloudy all day']
        self.usb_responses = ['Make sure the USB cable is properly plugged into the computer', 'Check if the USB drivers are installed', 'Try using a different USB port']

    def respond(self, user_input):
        if 'weather' in user_input:
            return random.choice(self.weather_responses)
        elif 'usb' in user_input:
            return random.choice(self.usb_responses)
        else:
            return random.choice(self.greetings)
