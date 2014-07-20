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
        return self._rounds[len(self._rounds)-1]
    
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
    
class Card:

    def __init__(self,cardCode):

        rankDictionary = {'A': 1, 'T': 10, 'J': 11, 'Q': 12, 'K': 13}

        if cardCode[0] in rankDictionary.keys():
            self._rank = rankDictionary[cardCode[0]]
        else:
            self._rank = cardCode[0]

        self._suit = cardCode[1]


    def GetRank(self):
        return self._rank

    def GetSuit(self):
        return self._suit
    
