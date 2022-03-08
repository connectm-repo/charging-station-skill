from mycroft import MycroftSkill, intent_file_handler


class ChargingStation(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('station.charging.intent')
    def handle_station_charging(self, message):
        self.speak_dialog('station.charging')


def create_skill():
    return ChargingStation()

