from datetime import datetime
event_date = datetime.today().strftime('%Y-%m-%d')
expire_date = datetime.today().strftime('%Y-%m-%d')

event_date=datetime.strptime(event_date, '%Y-%m-%d')
expire_date=datetime.strptime(expire_date, '%Y-%m-%d')
print((expire_date-event_date).days)





import PyQt5.QtWidgets as QtWidgets
class EventPushButton(QtWidgets.QPushButton):
	def enterEvent(self, *args, **kwargs):
		self.setStyleSheet("QPushButton{background-color:rgb(255,255,0)}")
		print('enterenterenterenterenter')


