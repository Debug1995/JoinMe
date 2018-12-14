from datetime import datetime
event_date = datetime.today().strftime('%Y-%m-%d')
expire_date = datetime.today().strftime('%Y-%m-%d')

event_date=datetime.strptime(event_date, '%Y-%m-%d')
expire_date=datetime.strptime(expire_date, '%Y-%m-%d')
print((expire_date-event_date).days)
