from datetime import datetime

from meeting_deconflictor.meeting import Meeting

TIME_FORMAT = "%H:%M%p"

class TestMeeting(object):

    def test_creation(self):
        start_time = datetime.strptime("6:00am", TIME_FORMAT)
        end_time = datetime.strptime("7:00am", TIME_FORMAT)
        meeting = Meeting(start_time, end_time)

        assert meeting.start_time == start_time
        assert meeting.end_time == end_time

