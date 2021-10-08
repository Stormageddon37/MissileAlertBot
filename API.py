import json, urllib.request
from datetime import datetime


class RedColorAlarmAPI:

    def __init__(self):
        # Alarms info
        self.data = urllib.request.urlopen("https://www.oref.org.il/WarningMessages/History/AlertsHistory.json").read()
        # Alerts list of dicts
        self.alerts_list = json.loads(self.data)

    def get_last_alert(self):
        '''returns the last alert as a dictionary'''
        # title:
        # data:
        # alertDate:
        self._update()
        return self.alerts_list[0]

    def get_all_alerts(self):
        self._update()
        return self.alerts_list

    def get_alert_by_index(self, index):
        self._update()
        return self.alerts_list(index)

    def get_all_alerts_by_city(self, name):
        self._update(self)
        temp_list = []
        for i in self.alerts_list:
            if i["data"] == name:
                temp_list.append(i)
        return temp_list

    def get_all_alerts_by_date(self, date):
        self._update()
        temp_list = []
        for i in self.alerts_list:
            alertdate = datetime.strptime(i["alertDate"], '%Y-%m-%d %H:%M:%S')
            if date.date() == alertdate.date():
                temp_list.append(i)
        return temp_list

    def get_all_alerts_by_time(self, time):
        self._update()
        temp_list = []
        for i in self.alerts_list:
            alerttime = datetime.strptime(i["alertDate"], '%Y-%m-%d %H:%M:%S')
            if time.time() == alerttime.time():
                temp_list.append(i)
        return temp_list

    def get_all_alerts_by_date_and_time(self, date_time):
        self._update()
        temp_list = []
        for i in self.alerts_list:
            alert_date_time = datetime.strptime(i["alertDate"], '%Y-%m-%d %H:%M:%S')
            if date_time.time() == alert_date_time.time() and date_time.date() == alert_date_time.date():
                temp_list.append(i)
        return temp_list

    def get_last_alerts(self, count):
        self._update()
        temp_list = []
        for i in range(count):
            temp_list.append(self.alerts_list[i])
        return temp_list

    def _update(self):
        # Alarms info
        self.data = urllib.request.urlopen("https://www.oref.org.il/WarningMessages/History/AlertsHistory.json").read()
        # Alerts list of dicts
        self.alerts_list = json.loads(self.data)