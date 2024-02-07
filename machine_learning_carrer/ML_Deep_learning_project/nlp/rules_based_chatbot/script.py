import re
import random

class AlienBot:
    negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
    random_questions = (
        "Why are you here? ",
        "Are there many humans like you? ",
        "What do you consume for sustenance? ",
        "Is there intelligent life on this planet? ",
        "Does Earth have a leader? ",
        "What planets have you visited? ",
        "What technology do you have on this planet? "
    )

    def __init__(self):
        self.alienbabble = {
            'describe_planet_intent': r'\b(planet|world)\b',
            'answer_why_intent': r'\b(why)\b',
            'cubed_intent': r'.*cube.*(\d+)'
        }

    def greet(self):
        self.name = input("Hello there, what's your name? ")
        will_help = input(f"Hi {self.name}, I'm Etcetera, an alien visiting your planet. Will you help me learn about your planet? ")
        if will_help.lower() in self.negative_responses:
            print("Ok, have a nice Earth day!")
            return
        self.chat()

    def make_exit(self, reply):
        for command in self.exit_commands:
            if command in reply:
                print("Ok, have a nice Earth day!")
                return True
        return False

    def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self, reply):
        for intent, regex_pattern in self.alienbabble.items():
            found_match = re.match(regex_pattern, reply)
            if found_match:
                return getattr(self, intent)(found_match.groups())
        return self.no_match_intent()

    def describe_planet_intent(self, match_groups):
        responses = (
            "My planet is a utopia of diverse organisms and species. ",
            "I am from Opidan, a planet in the Andromeda galaxy. "
        )
        return random.choice(responses)

    def answer_why_intent(self, match_groups):
        responses = (
            "I come in peace. ",
            "I am here to collect data on your planet and its inhabitants. ",
            "I heard the coffee is good. "
        )
        return random.choice(responses)

    def cubed_intent(self, match_groups):
        number = int(match_groups[0])
        cubed_number = number**3
        return f"The cube of {number} is {cubed_number}. Isn't that cool?"

    def no_match_intent(self):
        responses = (
            "Please tell me more. ",
            "Tell me more! ",
            "Why do you say that? ",
            "I see. Can you elaborate? ",
            "Interesting. Can you tell me more? ",
            "I see. How do you think? ",
            "Why? ",
            "How do you think I feel when you say that? "
        )
        return random.choice(responses)

# Create an instance of AlienBot and call greet method
alien_bot = AlienBot()
alien_bot.greet()
