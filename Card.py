__author__ = 'vinayneogi'

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



    def _createDictionary(self):
            colour = {1: 'S', 2: 'D', 3: 'C', 4: 'H'}
            value = {1: 'A', 10: 'T', 11: 'J', 12: 'Q', 13: 'K'}

            self.cardDictionary = {}

            for n in range(1, 5):
                for m in range(1,13):
                    valueToUse = str(m)
                    if value.has_key(m): valueToUse = value[m]

                    self.cardDictionary[valueToUse + colour[n]] = n*m









