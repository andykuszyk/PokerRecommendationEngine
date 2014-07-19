def CreateRecommendation(round):
    for card in round.GetHand():
        print "Card with rank " + str(card.GetRank()) + " and suit " + str(card.GetSuit())
    return Recommendation()
        
        
class Recommendation:
    def __init__(self):
        self._success = 0
        
    def GetSuccess(self):
        return self._success
    
    def SetSuccess(self,value):
        self._success = value
        
    def Description(self):
        return "Hello world"