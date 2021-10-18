from datetime import datetime


def get_release_date(release_str):
    date = release_str.split(': ')[1]
    return datetime.strptime(date, "%d %B %Y")
