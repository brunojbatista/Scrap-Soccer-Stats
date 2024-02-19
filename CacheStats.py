from Library_v1.Storage.JsonStorage import JsonStorage
from Library_v1.Directory.Directory import Directory
from Library_v1.Utils.string import (
    create_regex_latin_str,
    slug_name
)
from Readings.Data.Match import Match
from Readings.Data.Featured import Featured
from Readings.Data.Stats import Stats

class CacheStats(JsonStorage):
    def __init__(self, date: str, hometeam: str, awayteam: str):
        self.date = date;
        self.hometeam = hometeam
        self.awayteam = awayteam
        self.id = f"{date}_{slug_name(self.hometeam)}_x_{slug_name(self.awayteam)}"
        self.filename = f"{self.id}.json"
        self.dir = Directory(f"Cache/Stats/{self.date}")
        self.dir.create()
        self.currentPath = self.dir.get_path()
        self.filepath = Directory.separator(f"{self.currentPath}/{self.filename}")
        self.json = JsonStorage(self.filepath, indent=4)

        # self.match: Match = None
        # self.featured: Featured = None
        # self.stats: Stats = None
        # self.hometeam = None
        # self.awayteam = None

    # def setMatch(self, match: Match):
    #     self.match = match;

    # def setFeatured(self, featured: Featured):
    #     self.featured = featured;

    # def setStats(self, stats: Stats):
    #     self.stats = stats;
        
    def read(self, ) -> dict:
        data = self.json.read()
        if data is None: return []
        return data
        
    # def checkMatch(self, ):
    #     if self.match is None: raise ValueError("Não há partida definida")

    # def hasId(self, ):
    #     self.checkMatch()
    #     data = self.read()
    #     if data is None: return False
    #     return self.match.getId() in data
    
    # def getMatch(self, ) -> Match:
    #     if not self.hasId(): return None
    #     data = self.read()
    #     matchData = data[self.match.getId()]['match']
    #     return Match(matchData['hometeam'], matchData['awayteam'], matchData['time'])
    
    # def setMatch(self, match: Match) -> bool:
    #     self.match = match
    #     if self.hasId(): 
    #         print("Partida já setada...")
    #         return False
    #     id = self.match.getId()
    #     data = self.read()
    #     if id not in data:
    #         data[id] = {
    #             "id": id,
    #             "match": None,
    #             "featured": None,
    #             "stats": [],
    #         }
    #     data[id]["match"] = self.match.get()
    #     self.json.write(data)
    #     return True
    
    # def setFeatured(self, featured: Featured) -> bool:
    #     if not self.hasId(): return False
    #     id = self.match.getId()
    #     data = self.read()
    #     data[id]["featured"] = featured.getAll()
    #     self.json.write(data)
    #     return True
    
    # def getFeatured(self, ) -> Featured:
    #     if not self.hasId(): return None
    #     data = self.read()
    #     featuredData = data[self.match.getId()]['featured']
    #     return Featured(featuredData)

    def getFilename(self, ):
        return self.filename
    
    def setStats(self, stats: Stats) -> bool:
        statsData = self.getStats()
        for stat in stats.getAll():
            statsData.setById(stat["id"], stat["values"])
        self.json.write(statsData.getAll())
        return True

    def getStats(self, ) -> Stats:
        data = self.read()
        return Stats(data)
        