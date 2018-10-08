class MockDataReader:
    """ A very simple test utility that can be passed into a Deconflict with known data. """

    def __init__(self, test_data):
        self.test_data = test_data

    def read(self):
        return self.test_data