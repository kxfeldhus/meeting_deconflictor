import csv

from meeting_deconflictor.meeting import Meeting


class Deconflict:

    def __init__(self, meetings_filename):
        self.meetings_filename = meetings_filename

    def read_file(self):
        meetings = []
        with open(self.meetings_filename) as input_times_file:
            input_reader = csv.DictReader(input_times_file)
            for row in input_reader:
                meeting = Meeting(row['start'], row['end'])
                meetings.append(meeting)

        return meetings

    def find_conflicts(self):
        meetings = Deconflict.read_file(self)

        sorted_meetings = sorted(meetings)
        conflicted_meetings = []

        for i in range(len(sorted_meetings)-1):
            current_meeting = sorted_meetings[i]
            next_meeting = sorted_meetings[i+1]

            if current_meeting.end_time > next_meeting.start_time:
                conflicted_meetings.extend([current_meeting, next_meeting])

        return conflicted_meetings
