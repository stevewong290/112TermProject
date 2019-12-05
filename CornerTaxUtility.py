class CornerSpace(object):
    def __init__(self, name):
        self.name = name

class Tax(object):
    def __init__(self, name, tax):
        self.name = name
        self.tax = tax
        
class Utilities(object):
    def __init__(self, name, cost, rank):
        self.name = name
        self.cost = cost
        self.double = False
        self.rank = rank