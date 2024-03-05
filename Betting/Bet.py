from Readings.Data.Match import Match
from Readings.Data.Featured import Featured
from Readings.Data.Stats import Stats

class Bet():
    def __init__(self, matchTab: str, sizeTab: str, classification: str, match: Match, featured: Featured, stat: Stats, name: str) -> None:
        self.match = match
        self.featured = featured
        self.stat = stat
        self.matchTab = matchTab
        self.sizeTab = sizeTab
        self.classification = classification
        self.name = name
        self.methods = {}

    def getMatch(self, ) -> Match:
        return self.match

    def getFeatured(self, ) -> Featured:
        return self.featured

    def getStat(self, ) -> Stats:
        return self.stat
    
    def getClassification(self, ) -> str:
        return self.classification
    
    def getClassification(self, ) -> str:
        return self.classification
    
    def getName(self, ) -> str:
        return self.name

    def hasClassification(self, ):
        # print(f">> hasClassification:")
        oddHome = self.featured.getOddHome()
        oddAway = self.featured.getOddAway()
        # print(f"oddHome: {oddHome}")
        # print(f"oddAway: {oddAway}")
        if self.classification == 'Super Favorito':
            if oddHome > 1 and oddHome < 1.5:
                return True
            else:
                return False
        elif self.classification == 'Favorito':
            if oddHome >= 1.5 and oddHome < 2:
                return True
            else:
                return False
        elif self.classification == 'Equilibrado':
            if oddHome >= 2 and oddHome < 4 and oddAway >= 2 and oddAway < 4:
                return True;
            else:
                return False;
        elif self.classification == 'Zebra':
            if oddHome >= 4:
                return True;
            else:
                return False;
