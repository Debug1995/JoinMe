from Constants.Constants import Tags
import datetime
import time

class EventModel:
    def __init__(self, eid, title, tags: [Tags], description, image, hosts: [str], attendees: [str], event_date,
                 location, register_period):
        self.eid = eid
        self.title = title
        self.tags = tags
        self.description = description
        self.image = image
        self.hosts = hosts
        self.attendees = attendees
        if self.validCheckDate(event_date):
            self.event_date = event_date
        else:
            today = datetime.date.today()
            year = str(today.year)
            month = str(today.month).zfill(2)
            date = str(today.day - 1).zfill(2)
            self.event_date = year + '-' + month + '-' + date
        self.location = location
        if self.validPeriod(register_period):
            self.register_period = register_period
        else:
            self.register_period = '1'
        #print(self.event_date, self.register_period)
        self.expire_date = self.calculate_date(self.event_date, self.register_period)

    def validPeriod(self, period):
        period = period.strip()
        if not period or len(period):
            return False
        for char in period:
            if not char.isdigit():
                return False
        return True

    def validCheckDate(self, date):
        date = date.strip()
        if len(date) != 10 or date[4] != '-' or date[7] != '-' or not date or len(date) == 0:
            return False
        check_string = date[:4] + date[5:7] + date[8:]
        for char in check_string:
            if not char.isdigit():
                return False
        print(date)
        try:
            time.strptime(date, "%Y-%m-%d")
            return True
        except:
            return False

    def calculate_date(self, initial_date, register_period):

        cur_date = [int(x) for x in initial_date.strip().split('-')]
        d1 = datetime.date(cur_date[0], cur_date[1], cur_date[2])
        d = d1 + datetime.timedelta(days=int(register_period))
        year = str(d.year)
        month = str(d.month).zfill(2)
        date = str(d.day-1).zfill(2)
        return year + '-' + month + '-' + date
