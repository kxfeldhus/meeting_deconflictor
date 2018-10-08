from datetime import datetime

TIME_FORMAT = "%I:%M%p"


class Meeting:

    def __init__(self, start_time, end_time):
        self.start_time = datetime.strptime(start_time, TIME_FORMAT)
        self.end_time = datetime.strptime(end_time, TIME_FORMAT)

    def __repr__(self):
        return f"Meeting('{self.start_time}', '{self.end_time}')"

    def __eq__(self, other):
        return self.start_time == other.start_time and self.end_time == other.end_time

    def __lt__(self, other):
        return self.end_time < other.end_time

    def __gt__(self, other):
        return self.end_time > other.end_time
