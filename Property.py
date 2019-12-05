class Property(object):
    def __init__(self, name, cost, rent, h1, h2, h3, h4, hotel, houseCost, color, setRank, rank):
        self.name = name
        self.cost = cost
        self.rent = rent
        self.h1 = h1
        self.h2 = h2
        self.h3 = h3
        self.h4 = h4
        self.hotel = hotel
        self.houseCost = houseCost
        self.double = False
        self.numHouse = 0
        self.selected = False
        self.color = color
        self.setRank = setRank
        self.rank = rank
        
    def __str__(self):
        return self.name
        
    def __repr__(self):
        return self.name
        
