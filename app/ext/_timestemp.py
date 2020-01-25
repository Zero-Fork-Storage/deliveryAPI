from datetime import datetime
import time

def GetTimestemp():
    timestemp = time.mktime(datetime.today().timetuple())
    return timestemp