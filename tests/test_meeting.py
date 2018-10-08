from datetime import datetime

import pytest

from meeting_deconflictor.meeting import Meeting, TIME_FORMAT


class TestMeeting:

    def test_successful_creation(self):
        meeting = Meeting("6:00am", "7:00am")

        expected_start_time = datetime.strptime("6:00am", TIME_FORMAT)
        expected_end_time = datetime.strptime("7:00am", TIME_FORMAT)

        assert meeting.start_time == expected_start_time
        assert meeting.end_time == expected_end_time

    def test_throws_exception_on_start_time_after_end_time(self):
        with pytest.raises(ValueError) as ex:
            Meeting("7:00am", "6:00am")

        assert 'must be before' in str(ex)

    def test_throws_exception_on_start_time_equal_to_end_time(self):
        with pytest.raises(ValueError) as ex:
            Meeting("7:00am", "7:00am")

        assert 'must be before' in str(ex)

    def test_throws_exception_on_invalid_time(self):
        with pytest.raises(ValueError):
            Meeting("27:00am", "6:00am")

        with pytest.raises(ValueError):
            Meeting("7:00am", "x")

