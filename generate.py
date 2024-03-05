from Library_v1.Utils.string import (
    slug_name,
    default_space,
)

from Readings.Data.Stats import Stats
from Cache import Cache
from CacheStats import CacheStats

from Readings.Data.Featured import Featured
from Readings.Data.Stats import Stats

import sys

class Generate():
    def __init__(self) -> None:
        self.typeReadings = []

    def addTypeReading(self, matchTab: str = '5 jogos', sizeTab = 'Casa/Visitante'):
        self.typeReadings.append((matchTab, sizeTab))

    def getFilename(self, date: str, matchTab: str = '5 jogos', sizeTab = 'Casa/Visitante'):
        return slug_name(f"{date}_{matchTab}_{sizeTab}")

    def getHeaders(self, ):
        FEATURED = Featured.getHeaders()
        STATS = Stats.getHeaders()
        return [*FEATURED, *STATS]

    def getValues(self, featured: Featured, stats: Stats, matchTab: str, sizeTab: str):
        FEATURED = Featured.getHeaders()
        featuredMap = featured.getMap()
        STATS = Stats.getHeaders()
        statsMap = stats.getMap(matchTab, sizeTab)
        values = []
        for statName in FEATURED:
            values.append(featuredMap[statName])
        for statName in STATS:
            values.append(statsMap[statName])
        return values

    def saveContent(self, date: str, matchTab: str, sizeTab: str, content: str):
        filename = f"{self.getFilename(date, matchTab, sizeTab)}.txt"
        file = open(filename, "a", encoding="utf-8")
        file.write(f"{content}\n")
        file.close()
        file = None

    def clearContent(self, date: str, matchTab: str, sizeTab: str):
        filename = f"{self.getFilename(date, matchTab, sizeTab)}.txt"
        with open(filename,'w') as file:
            pass

    def execute(self, date: str):

        # headers = self.getHeaders()
        # print(f"headers: {headers}")

        for matchTab, sizeTab in self.typeReadings:
            print(f"-"*50)
            filename = self.getFilename(date, matchTab, sizeTab)
            print(f"filename: {filename}")
            self.clearContent(date, matchTab, sizeTab)
            cache = Cache(date)
            if not cache.hasData():
                print(f"A data '{date}' informada não tem registro")
                continue
            matches = cache.getMathes()
            # print(f"matches: {matches}")
            for match in matches:
                print(f"="*30)
                cache.setMatchRef(match)
                featured = cache.getFeatured()
                statsFilename = cache.getStatsFilename()
                cacheStats = CacheStats(date, match.getHometeam(), match.getAwayteam())
                stats = cacheStats.getStats()
                print(f"featured: {featured}")
                print(f"statsFilename: {statsFilename}")
                print(f"stats: {stats}")
                # stats = cache.getFeatured()
                values = self.getValues(featured, stats, matchTab, sizeTab)
                rowValue = "\t".join([str(x) for x in values])
                # print(f"values: {values}")
                print(f"rowValue: {rowValue}")
                self.saveContent(date, matchTab, sizeTab, rowValue)

g = Generate()

g.addTypeReading('5 jogos', 'Casa/Visitante')
g.addTypeReading('10 jogos', 'Casa/Visitante')

script = sys.argv[0]
date = sys.argv[1]
g.execute(date)


