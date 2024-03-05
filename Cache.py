from Library_v1.Storage.JsonStorage import JsonStorage
from Library_v1.Directory.Directory import Directory
from Library_v1.Utils.string import (
    create_regex_latin_str,
    slug_name
)
from Readings.Data.Match import Match
from Readings.Data.Featured import Featured
from Readings.Data.Stats import Stats

class Cache(JsonStorage):
    def __init__(self, date: str):
        self.date = date;
        self.filename = f"{date}_cache.json"
        # self.dir = Directory()
        # self.currentPath = self.dir.get_path()
        self.dir = Directory(f"Cache")
        self.dir.create()
        self.currentPath = self.dir.get_path()
        self.filepath = Directory.separator(f"{self.currentPath}/{self.filename}")
        # self.filepath = self.dir.find_file(create_regex_latin_str(self.filename))
        # if self.filepath is None:
        #     self.filepath = Directory.get_realpath(f"{self.currentPath}//{self.filename}")
        self.json = JsonStorage(self.filepath, indent=4)

        self.match: Match = None
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
        if data is None: return {}
        return data
    
    def hasData(self, ) -> bool:
        return not self.json.read() is None
        
    def checkMatch(self, ):
        if self.match is None: raise ValueError("Não há partida definida")

    def hasId(self, ):
        self.checkMatch()
        data = self.read()
        if data is None: return False
        return self.match.getId() in data
    
    def getMatch(self, ) -> Match:
        if not self.hasId(): return None
        data = self.read()
        matchData = data[self.match.getId()]['match']
        return Match(matchData['hometeam'], matchData['awayteam'], matchData['time'])
    
    def setMatchRef(self, match: Match):
        self.match = match
    
    def setMatch(self, match: Match) -> bool:
        self.setMatchRef(match)
        if self.hasId(): 
            print("Partida já setada...")
            return False
        id = self.match.getId()
        data = self.read()
        if id not in data:
            data[id] = {
                "id": id,
                "match": None,
                "featured": None,
                "stats": None,
            }
        data[id]["match"] = self.match.get()
        self.json.write(data)
        return True
    
    def removeMatch(self, match: Match) -> bool:
        self.setMatchRef(match)
        if not self.hasId(): 
            print("Partida não existe mais...")
            return False
        id = self.match.getId()
        data = self.read()
        del data[id]
        self.json.write(data)
        return True
    
    def getMathes(self, ) -> list:
        data = self.read()
        return [Match(data[id]['match']['hometeam'], data[id]['match']['awayteam'], data[id]['match']['time']) for id in data]
    
    def setFeatured(self, featured: Featured) -> bool:
        if not self.hasId(): return False
        id = self.match.getId()
        data = self.read()
        data[id]["featured"] = featured.getAll()
        self.json.write(data)
        return True
    
    def getFeatured(self, ) -> Featured:
        if not self.hasId(): return None
        data = self.read()
        featuredData = data[self.match.getId()]['featured']
        return Featured(featuredData)
    
    def setStatsFilename(self, filename: str) -> bool:
        if not self.hasId(): return False
        data = self.read()
        id = self.match.getId()
        # statsData = self.getStats()
        # for stat in stats.getAll():
        #     statsData.setById(stat["id"], stat["values"])
        data[id]["stats"] = filename
        self.json.write(data)
        return True

    def getStatsFilename(self, ) -> str:
        if not self.hasId(): return None
        data = self.read()
        return data[self.match.getId()]['stats']
        # return Stats(statsData)