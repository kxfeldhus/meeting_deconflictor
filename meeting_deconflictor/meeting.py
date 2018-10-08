from datetime import datetime

TIME_FORMAT = "%I:%M%p"  # Format for times that drops the date.


class Meeting:
    """ This class holds the data, validation, and the sorting logic for a Meeting. """

    def __init__(self, start_time, end_time):
        """ A new Meeting object, will throw a ValueError on bad time values. """
        start_time = datetime.strptime(start_time, TIME_FORMAT)
        end_time = datetime.strptime(end_time, TIME_FORMAT)

        if Meeting.validate_time_args(start_time, end_time):
            self.start_time = start_time
            self.end_time = end_time
        else:
            raise ValueError(f"start time of {start_time} must be before {end_time}")

    @staticmethod
    def validate_time_args(start_time, end_time):
        """ Validate that the start time is before the end time of a meeting """

        return start_time < end_time

    def __repr__(self):
        start_time = datetime.strftime(self.start_time, TIME_FORMAT)
        end_time = datetime.strftime(self.end_time, TIME_FORMAT)
        return f"Meeting('{start_time}', '{end_time}')"

    def __eq__(self, other):
        return self.start_time == other.start_time and self.end_time == other.end_time

    def __lt__(self, other):
        return self.start_time < other.start_time

    def __gt__(self, other):
        return self.start_time > other.start_time
