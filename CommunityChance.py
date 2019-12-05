class CommunityChance(object):
    def __init__(self, name):
        self.name = name

class CommunityChanceCardMoney(CommunityChance):
    def __init__(self, name, action, message):
        super().__init__(name)
        self.action = action
        self.message = message
        
class CommunityChanceCardMovement(CommunityChance):
    def __init__(self, name, action, message):
        super().__init__(name)
        self.action = action
        self.message = message