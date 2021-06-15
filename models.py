class Calendar:
    def __init__(self, disposition, information, calendar):
        self.disposition = disposition
        self.information = information
        self. calenadar = calendar

class Weather(Calendar):
    def __init__(self, weather, location, calendar):
        self.weather = weather
        self.location = location
        super.__init__(self.calenadar)

class Order:
    def __init__(self, email, phone_number, name, location, information):
        self.email = email
        self.phone_number = phone_number
        self.name = name
        self.location = location
        self.information = information

class PostBoss:
    def __init__(self, information):
        self.information = information