from datetime import datetime


def format_time(datetime_obj: datetime):
    print("24h", datetime_obj.strftime("%H:%M"))
    print("12h", datetime_obj.strftime("%I:%M"))
