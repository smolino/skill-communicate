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

    def handle_turnlighton_intent(self, message):
        os.system("ssh pi@192.168.1.3 /home/pi/bin/say_to_mycroft turn light on >> /dev/null &")
        self.speak_dialog("turnlighton")

    def handle_turnlightoff_intent(self, message):
        os.system("ssh pi@192.168.1.3 /home/pi/bin/say_to_mycroft turn light off >> /dev/null &")
        self.speak_dialog("turnlightoff")
    def stop(self):
        pass


def create_skill():
    return communicationSkill()
