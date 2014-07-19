from Game import *
from Card import *
from RecommendationEngine import *
import abc

class CommandLineInterface:
    def Start(self):
        print "Welcome Vindy's Poker Recommendation Engine."
        print "Please enter a Game State:"
        numberOfPlayers = input("Number of players: ")
        bigBlind = input("Big blind: ")
        smallBlind = input("Small blind: ")
        self._game = Game(numberOfPlayers,bigBlind,smallBlind)
        
        print "Your game state has been created, now please enter your hand for the first round:"
        self.AddHandToGame()
        
    def AddHandToGame(self):
        card1 = Card(input("Enter the code for card 1: "))
        card1 = Card(input("Enter the code for card 2: "))
        _game.CreateNewRound(card1,card2)
        GetCurrentRecommendation()
        
    def GetCurrentRecommendation(self):
        recommendation = RecommendationEngine.CreateRecommendation(self._game.GetCurrentRound())
        print recommendation.Description()
        
        