from os.path import dirname
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
import os
import time

__author__ = 'smolino'

LOGGER = getLogger(__name__)


class communicationSkill(MycroftSkill):

    def __init__(self):
        super(communicationSkill, self).__init__(name="communicationSkill")

    def initialize(self):
        turnlighton_intent = IntentBuilder("turnlightonIntent").\
            require("turnlightonKeyword").build()
        self.register_intent(turnlighton_intent, self.handle_turnlighton_intent)

        turnlightoff_intent = IntentBuilder("turnlightoffIntent").\
            require("turnlightoffKeyword").build()
        self.register_intent(turnlightoff_intent, self.handle_turnlightoff_intent)

        turnswitchon_intent = IntentBuilder("turnswitchonIntent").\
            require("turnswitchonKeyword").build()
        self.register_intent(turnswitchon_intent, self.handle_turnswitchon_intent)

        turnswitchoff_intent = IntentBuilder("turnswitchoffIntent").\
            require("turnswitchoffKeyword").build()
        self.register_intent(turnswitchoff_intent, self.handle_turnswitchoff_intent)

        turnfanon_intent = IntentBuilder("turnfanonIntent").\
            require("turnfanonKeyword").build()
        self.register_intent(turnfanon_intent, self.handle_turnfanon_intent)

        turnfanoff_intent = IntentBuilder("turnfanoffIntent").\
            require("turnfanoffKeyword").build()
        self.register_intent(turnfanoff_intent, self.handle_turnfanoff_intent)

        turnlivingon_intent = IntentBuilder("turnlivingonIntent").\
            require("turnlivingonKeyword").build()
        self.register_intent(turnlivingon_intent, self.handle_turnlivingon_intent)

        turnlivingoff_intent = IntentBuilder("turnlivingoffIntent").\
            require("turnlivingoffKeyword").build()
        self.register_intent(turnlivingoff_intent, self.handle_turnlivingoff_intent)

        turnbedroomon_intent = IntentBuilder("turnbedroomonIntent").\
            require("turnbedroomonKeyword").build()
        self.register_intent(turnbedroomon_intent, self.handle_turnbedroomon_intent)

        turnbedroomoff_intent = IntentBuilder("turnbedroomoffIntent").\
            require("turnbedroomoffKeyword").build()
        self.register_intent(turnbedroomoff_intent, self.handle_turnbedroomoff_intent)

        turnbathroomon_intent = IntentBuilder("turnbathroomonIntent").\
            require("turnbathroomonKeyword").build()
        self.register_intent(turnbathroomon_intent, self.handle_turnbathroomon_intent)

        turnbathroomoff_intent = IntentBuilder("turnbathroomoffIntent").\
            require("turnbathroomoffKeyword").build()
        self.register_intent(turnbathroomoff_intent, self.handle_turnbathroomoff_intent)

        turnkitchenon_intent = IntentBuilder("turnkitchenonIntent").\
            require("turnkitchenonKeyword").build()
        self.register_intent(turnkitchenon_intent, self.handle_turnkitchenon_intent)

        turnkitchenoff_intent = IntentBuilder("turnkitchenoffIntent").\
            require("turnkitchenoffKeyword").build()
        self.register_intent(turnkitchenoff_intent, self.handle_turnkitchenoff_intent)

        turnlampon_intent = IntentBuilder("turnlamponIntent").\
            require("turnlamponKeyword").build()
        self.register_intent(turnlampon_intent, self.handle_turnlampon_intent)

        turnlampoff_intent = IntentBuilder("turnlampoffIntent").\
            require("turnlampoffKeyword").build()
        self.register_intent(turnlampoff_intent, self.handle_turnlampoff_intent)

    def handle_turnlighton_intent(self, message):
        os.system("ssh pi@192.168.1.3 /home/pi/bin/say_to_mycroft turn light on >> /dev/null &")
        self.speak_dialog("turnlighton")

    def handle_turnlightoff_intent(self, message):
        os.system("ssh pi@192.168.1.3 /home/pi/bin/say_to_mycroft turn light off >> /dev/null &")
        self.speak_dialog("turnlightoff")

    def handle_turnswitchon_intent(self, message):
        os.system("ssh pi@192.168.1.3 /home/pi/bin/say_to_mycroft turn switch on >> /dev/null &")
        self.speak_dialog("turnswitchon")

    def handle_turnswitchoff_intent(self, message):
        os.system("ssh pi@192.168.1.3 /home/pi/bin/say_to_mycroft turn switch off >> /dev/null &")
        self.speak_dialog("turnswitchoff")

    def handle_turnfanon_intent(self, message):
        os.system("ssh pi@192.168.1.3 /home/pi/bin/say_to_mycroft turn fan on >> /dev/null &")
        self.speak_dialog("turnfanon")

    def handle_turnfanoff_intent(self, message):
        os.system("ssh pi@192.168.1.3 /home/pi/bin/say_to_mycroft turn fan off >> /dev/null &")
        self.speak_dialog("turnfanoff")

    def handle_turnlivingon_intent(self, message):
        os.system("ssh pi@192.168.1.3 /home/pi/bin/say_to_mycroft turn living on >> /dev/null &")
        self.speak_dialog("turnlivingon")

    def handle_turnlivingoff_intent(self, message):
        os.system("ssh pi@192.168.1.3 /home/pi/bin/say_to_mycroft turn living off >> /dev/null &")
        self.speak_dialog("turnlivingoff")

    def handle_turnbedroomon_intent(self, message):
        os.system("ssh pi@192.168.1.3 /home/pi/bin/say_to_mycroft turn bedroom on >> /dev/null &")
        self.speak_dialog("turnbedroomon")

    def handle_turnbedroomoff_intent(self, message):
        os.system("ssh pi@192.168.1.3 /home/pi/bin/say_to_mycroft turn bedroom off >> /dev/null &")
        self.speak_dialog("turnbedroomoff")

    def handle_turnbathroomon_intent(self, message):
        os.system("ssh pi@192.168.1.3 /home/pi/bin/say_to_mycroft turn bathroom on >> /dev/null &")
        self.speak_dialog("turnbathroomon")

    def handle_turnbathroomoff_intent(self, message):
        os.system("ssh pi@192.168.1.3 /home/pi/bin/say_to_mycroft turn bathroom off >> /dev/null &")
        self.speak_dialog("turnbathroomoff")

    def handle_turnkitchenon_intent(self, message):
        os.system("ssh pi@192.168.1.3 /home/pi/bin/say_to_mycroft turn kitchen on >> /dev/null &")
        self.speak_dialog("turnkitchenon")

    def handle_turnkitchenoff_intent(self, message):
        os.system("ssh pi@192.168.1.3 /home/pi/bin/say_to_mycroft turn kitchen off >> /dev/null &")
        self.speak_dialog("turnkitchenoff")

    def handle_turnlampon_intent(self, message):
        os.system("ssh pi@192.168.1.3 /home/pi/bin/say_to_mycroft turn lamp on >> /dev/null &")
        self.speak_dialog("turnlampon")

    def handle_turnlampoff_intent(self, message):
        os.system("ssh pi@192.168.1.3 /home/pi/bin/say_to_mycroft turn lamp off >> /dev/null &")
        self.speak_dialog("turnlampoff")

    def stop(self):
        pass

def create_skill():
    return communicationSkill()
