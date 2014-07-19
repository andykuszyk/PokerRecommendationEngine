class RecommendationEngine:
    def CreateRecommendation(round):
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