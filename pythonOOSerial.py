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

def __init__(self,start = 0):
    """THis make the new generator and starts it at zero"""
    self.start = self.next = start

def __repr__(self):
    """the generator describes itself"""
    return f"Serial Gnerator with a Start of {self.start} and next of {self.next}"

def generate(self):
    """cycles the generator"""
    self.next += 1
    return self.next

def reset(self):
    """return the generator to starting"""
    self.next = self.start