"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start, counter=0):
        self.start = start
        self.counter = counter

    def __repr__(self):
        return f"<SerialGenerator start={self.start}>"

    def generate(self):
        '''Returns a serial number and increments itself each time'''
        number = self.start + self.counter
        self.counter += 1
        return number

    def reset(self):
        '''Resets the serial number back to start'''
        self.counter = 0
