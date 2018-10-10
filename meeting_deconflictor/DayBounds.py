from datetime import datetime

from meeting_deconflictor.meeting import TIME_FORMAT


class DayBounds:
    start_of_day = None
    end_of_day = None

    # def __init__(self):
    #     self.start_of_day# = datetime.strptime(start_time, TIME_FORMAT)
    #     self.end_of_day# = datetime.strptime(end_time, TIME_FORMAT)

    def set_start_of_day(self, time):
        self.start_of_day = datetime.strptime(time, TIME_FORMAT)

    def set_end_of_day(self, time):
        self.end_of_day = datetime.strptime(time, TIME_FORMAT)

    def meeting_valid_for_bound(self, meeting):
        return meeting.start_time >= self.start_of_day and meeting.end_time <= self.end_of_day
