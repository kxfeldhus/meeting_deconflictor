import argparse

from meeting_deconflictor.meetings_file_csv_reader import MeetingsFileCsvReader


class Deconflict:
    """ This class holds the core conflict detection logic. """

    def __init__(self, reader):
        """ Accept a reader so we can easily switch between different reader formats, like xml or json.
            reader must implement a #read() method that returns a List of Meetings.
        """
        # TODO: Make sure the reader has a #read() method.

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
                conflicted_meetings.append((current_meeting, next_meeting))

        return conflicted_meetings

    @classmethod
    def generate_report_for_file(cls, reader):
        """ A utility method to be used as the primary entry point to generate a report from an input reader. """
        deconflictor = Deconflict(reader)
        conflicts = deconflictor.find_conflicts()

        Deconflict.report_conflicts(conflicts)

    @classmethod
    def report_conflicts(cls, conflicts):
        """ Print out the conflicts. This is a very simple example to iterate on.
            A future improvement would be to have different reporter classes that could
            report out in various ways and formats.  Like to stdout here, or to a file, or send an email, or publish to
            a web service.
        """
        print("Conflict Report:")
        for conflict1, conflict2 in conflicts:
            print(f'{conflict1} --- conflicts with --- {conflict2}')



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process a meetings file and report conflicts')
    parser.add_argument('filename', type=str, help='Full path to meetings file to process')
    args = parser.parse_args()

    # Just a simple CSV reader for now, we could easily expand to support other formats based on arguments.
    csv_reader = MeetingsFileCsvReader(args.filename)
    Deconflict.generate_report_for_file(csv_reader)
