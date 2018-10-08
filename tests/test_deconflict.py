import os

from meeting_deconflictor.deconflict import Deconflict
from meeting_deconflictor.meeting import Meeting

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.abspath(os.path.join(TEST_DIR, 'data'))


class TestDeconflict:

    test_filename = os.path.join(TEST_DATA_DIR, 'times')
    deconflictor = Deconflict(test_filename)

    def test_deconflict(self):
        conflicted_meetings = self.deconflictor.find_conflicts()

        expected_meetings = [Meeting('9:00am', '10:00am'),
                             Meeting('9:30am', '10:30am'),
                             Meeting('10:45am', '1:00pm'),
                             Meeting('12:00pm', '1:00pm')]

        assert sorted(conflicted_meetings) == sorted(expected_meetings)



