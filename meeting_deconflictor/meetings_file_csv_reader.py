import csv

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

        meetings = []
        with open(self.meetings_filename) as input_times_file:
            input_reader = csv.DictReader(input_times_file)
            for row in input_reader:
                meeting = Meeting(row['start'], row['end'])
                meetings.append(meeting)

        return meetings
