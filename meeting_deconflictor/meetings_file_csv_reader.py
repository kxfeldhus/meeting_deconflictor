import csv

from meeting_deconflictor.DayBounds import DayBounds
from meeting_deconflictor.meeting import Meeting


class MeetingsFileCsvReader:
    """ Read a meetings file in a CSV format.
        Must adhere to this sample format:
            start,end
            8:15am,8:30am
            9:00am,10:00am
    """

    def __init__(self, meetings_filename):
        self.meetings_filename = meetings_filename

    def read(self):
        """ Open the file, read the contents, and return a list of Meetings. """

        day_bounds = DayBounds()
        meetings = []
        with open(self.meetings_filename) as input_times_file:
            input_reader = csv.DictReader(input_times_file)

            # meetings = [Meeting(row['start'], row['end']) for row in input_reader]
            for row in input_reader:
                if row['start'] is not '' and row['end'] is '':
                    day_bounds.set_start_of_day(row['start'])
                elif row['start'] is '' and row['end'] is not '':
                    day_bounds.set_end_of_day(row['end'])
                else:
                    meeting = Meeting(row['start'], row['end'])
                    meetings.append(meeting)

        print(meetings)
        meetings = [meeting for meeting in meetings if day_bounds.meeting_valid_for_bound(meeting)]
        print(meetings)

        return meetings
