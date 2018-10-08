from datetime import datetime

from meeting_deconflictor.meeting import Meeting, TIME_FORMAT


class TestMeeting:

    def test_creation(self):
        meeting = Meeting("6:00am", "7:00am")

        expected_start_time = datetime.strptime("6:00am", TIME_FORMAT)
        expected_end_time = datetime.strptime("7:00am", TIME_FORMAT)

        assert meeting.start_time == expected_start_time
        assert meeting.end_time == expected_end_time

