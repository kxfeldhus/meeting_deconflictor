import os

from meeting_deconflictor.deconflict import Deconflict
from meeting_deconflictor.meeting import Meeting
from meeting_deconflictor.meetings_file_csv_reader import MeetingsFileCsvReader

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.abspath(os.path.join(TEST_DIR, 'data'))


class TestMeetingsFileCsvReader:

    test_filename = os.path.join(TEST_DATA_DIR, 'times')
    reader = MeetingsFileCsvReader(test_filename)

    def test_read(self):
        meetings = self.reader.read()

        expected_meetings = [Meeting('8:15am', '8:30am'),
                             Meeting('9:00am', '10:00am'),
                             Meeting('9:30am', '10:30am'),
                             Meeting('10:45am', '1:00pm'),
                             Meeting('12:00pm', '1:00pm'),
                             Meeting('1:30pm', '3:00pm'),
                             Meeting('3:00pm', '3:30pm'),
                             Meeting('4:00pm', '5:00pm'),
                             Meeting('6:00pm', '7:00pm'),
                             Meeting('8:00pm', '9:00pm')]

        assert sorted(meetings) == sorted(expected_meetings)
