import Round.Round as Round

class Game:
    
    def __init__(self,numberOfPlayers, bigBlind, smallBlind):
        self._numberOfPlayers = numberOfPlayers
        self._bigBlind = bigBlind
        self._smallBlind = smallBlind
        self._rounds = []
                
    def GetNumberOfPlayers(self):
        return _numberOfPlayers
    
    def CreateNewRound(self,card1,card2):
        self._rounds.append(Round(card1, card2))
        
    def GetCurrentRound(self):
        return self._rounds[self._rounds.count()-1]