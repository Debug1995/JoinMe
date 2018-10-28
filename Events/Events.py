from SqlController import *
import datetime
class Events:
    def __init__(self, data):
        data_list = data.strip().split('***')
        self.EventID = data_list[0]
        self.title = data_list[1]
        self.tags = data_list[2]
        self.description = data_list[3]
        self.image = data_list[4]
        self.event_date = data_list[5]
        self.location = data_list[6]
        self.register_period = data_list[7]
        self.mydb = SqlController("root", "12345678", "JoinMe").sql_connector
        self.mycursor = self.mydb.cursor()
        self.expire_date = self.__caculateDate(self.event_date, self.register_period)

    def __caculateDate(self, initial_date, register_period):
        cur_date = [int(x) for x in initial_date.strip().split('-')]
        d1 = datetime.date(cur_date[0], cur_date[1], cur_date[2])
        d = d1 + datetime.timedelta(days=int(register_period))
        year = str(d.year)
        month = str(d.month).zfill(2)
        date = str(d.day).zfill(2)
        return year + '-' + month + '-' + date

    def postEvent(self):
        sql = "INSERT INTO Event " \
              "(Title, Tags, EventDate, Description, Image, Location, Expiretime) " \
              "VALUES " \
              "(%s, %s, %s, %s, %s, %s,%s)"
        val = (str(self.title), str(self.tags), str(self.event_date),
               str(self.description),str(self.image),str(self.location),str(self.expire_date))
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        self.mycursor.execute("SELECT @@identity")
        for x in self.mycursor:
            EventID = x[0]
        return EventID


    def edit(self, edit_data):
        edit_datalist = edit_data.strip().split('***')
        EventID = edit_datalist[0]
        title = edit_datalist[1]
        tags = edit_datalist[2]
        description = edit_datalist[3]
        image = edit_datalist[4]
        event_date = edit_datalist[5]
        location = edit_datalist[6]
        register_period = edit_datalist[7]
        expire_date = self.__caculateDate(event_date, register_period)
        sql = "UPDATE Event " \
              "SET Title = %s, Tags = %s, EventDate = %s, Description = %s, " \
              "Image = %s, Location = %s, ExpireTime = %s " \
              "WHERE EventID = %s"
        val = (title, tags, event_date, description, image,
               location, expire_date, EventID)
        self.mycursor.execute(sql, val)
        self.mydb.commit()

    def expire(self):
        today = datetime.date.today()
        cur_year = str(today.year)
        cur_month = str(today.month).zfill(2)
        cur_day = str(today.day).zfill(2)
        expire = cur_year+'-'+cur_month+'-'+cur_day
        sql = "DELETE FROM Event WHERE Expiretime < %s"
        val = (expire,)
        self.mycursor.execute(sql, val)
        self.mydb.commit()

    def removeUser(self, userID):
        sql = "DELETE FROM JoinTable WHERE JoinID = %s and EventID = %s"
        val = (str(userID), self.EventID)
        self.mycursor.execute(sql, val)
        self.mydb.commit()




data = '35***this is title***tag13 tag2 tag3***this is description***this is image url***2018-08-27***this is location***7'
editdata = '36***this is title***tag13 tag2 tag3***this is description***this is image url***2222-08-27***this is location***7'
userID = 14

#event.expire()


