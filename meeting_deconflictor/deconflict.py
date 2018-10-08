import argparse

from meeting_deconflictor.meetings_file_csv_reader import MeetingsFileCsvReader


class Deconflict:
    """ This class holds the core conflict detection logic. """

    def __init__(self, reader):
        # Accept a reader so we can easily switch between different reader formats, like xml or json.
        self.reader = reader

    def find_conflicts(self):
        """ Read the file and return a List of meetings with conflicts. """
        meetings = self.reader.read()

        # Meetings must be sorted by start_time in order to detect conflicts with adjacent meetings.
        sorted_meetings = sorted(meetings)
        conflicted_meetings = []

        # Starting with the first meeting and going to the n-1 meeting to avoid overrun.
        for i in range(len(sorted_meetings)-1):

            # We are always checking the current meeting to the next meeting until we hit the next to last one.
            current_meeting = sorted_meetings[i]
            next_meeting = sorted_meetings[i+1]

            # Core overlap detection.  If the end time of the current meeting is after the start time of the next
            #  meeting then we have a conflict.
            if current_meeting.end_time > next_meeting.start_time:
                conflicted_meetings.extend([current_meeting, next_meeting])

        return conflicted_meetings

    @classmethod
    def generate_report_for_file(cls, reader):
        deconflictor = Deconflict(reader)
        conflicts = deconflictor.find_conflicts()

        print(conflicts)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process a meetings file and report conflicts')
    parser.add_argument('filename', type=str, help='Full path to meetings file to process')
    args = parser.parse_args()

    # Just a simple CSV reader for now, we could easily expand to support other formats based on arguments.
    csv_reader = MeetingsFileCsvReader(args.filename)
    Deconflict.generate_report_for_file(csv_reader)
