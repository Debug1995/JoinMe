from Controller.EventController import *


class EventModel:
    def __init__(self, eid, title, tags, description, image, hosts, attendees, event_date, location, register_period):
        self.eid = eid
        self.title = title
        self.tags = tags
        self.description = description
        self.image = image
        self.hosts = hosts
        self.attendees = []
        self.event_date = []
        self.location = location
        self.register_period = register_period
        self.expire_date = calculate_date(event_date, register_period)
