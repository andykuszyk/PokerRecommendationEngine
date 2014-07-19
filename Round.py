class Round:

    def __init__(self, card1, card2):
        self._hand = [card1, card2]
        
    def AddFlop(self,card1,card2,card3):
        self._hand.append(card1)
        self._hand.append(card2)
        self._hand.append(card3)
    
    def AddTurnOrRiver(self,card1):
        self._hand.append(card1)
        
    def GetHand(self):
        return self._hand    
    
