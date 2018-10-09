import os

from meeting_deconflictor.deconflict import Deconflict
from meeting_deconflictor.meeting import Meeting
from tests.util.mock_data_reader import MockDataReader

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.abspath(os.path.join(TEST_DIR, 'data'))


class TestDeconflict:

    def test_deconflict(self):
        # A nominal set of data taken from the test file.
        test_data = [Meeting('8:15am', '8:30am'),
                     Meeting('9:00am', '10:00am'),
                     Meeting('9:30am', '10:30am'),
                     Meeting('10:45am', '1:00pm'),
                     Meeting('12:00pm', '1:00pm'),
                     Meeting('1:30pm', '3:00pm'),
                     Meeting('3:00pm', '3:30pm'),
                     Meeting('4:00pm', '5:00pm'),
                     Meeting('6:00pm', '7:00pm'),
                     Meeting('8:00pm', '9:00pm')]

        test_data_reader = MockDataReader(test_data)
        deconflictor = Deconflict(test_data_reader)
        conflicted_meetings = deconflictor.find_conflicts()

        expected_meetings = [(Meeting('9:00am', '10:00am'),
                              Meeting('9:30am', '10:30am')),
                             (Meeting('10:45am', '1:00pm'),
                              Meeting('12:00pm', '1:00pm'))]

        assert sorted(conflicted_meetings) == sorted(expected_meetings)

    def test_deconflict_inner_bounded(self):
        # Make sure we find a conflict when one meeting is fully within the times of another.
        test_data = [Meeting('10:00am', '11:00am'),
                     Meeting('10:01am', '10:59am')]
        test_data_reader = MockDataReader(test_data)
        deconflictor = Deconflict(test_data_reader)
        conflicted_meetings = deconflictor.find_conflicts()

        expected_meetings = [(Meeting('10:00am', '11:00am'),
                              Meeting('10:01am', '10:59am'))]

        assert sorted(conflicted_meetings) == sorted(expected_meetings)

    def test_deconflict_no_meetings(self):
        # Make sure we handle when no meetings are provided.
        test_data = []
        test_data_reader = MockDataReader(test_data)
        deconflictor = Deconflict(test_data_reader)
        conflicted_meetings = deconflictor.find_conflicts()

        expected_meetings = []

        assert conflicted_meetings == expected_meetings
