import argparse
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

    @classmethod
    def generate_report_for_file(cls, meetings_filename):
        deconflictor = Deconflict(meetings_filename)
        conflicts = deconflictor.find_conflicts()

        print(conflicts)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process a meetings file and report conflicts')
    parser.add_argument('filename', type=str, help='Full path to meetings file to process')

    args = parser.parse_args()
    Deconflict.generate_report_for_file(args.filename)
