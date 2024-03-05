from Readings.Data.Stats import Stats
from Cache import Cache
from CacheStats import CacheStats

from Readings.Data.Match import Match
from Readings.Data.Featured import Featured
from Readings.Data.Stats import Stats
from Betting.Bet import Bet

from Library_v1.Utils.time import (
    date_now,
    format_date,
    add_day,
    get_date
)

import sys
import datetime
import re

from Exceptions.MarketNotFoundError import MarketNotFoundError

from Betting.Under25FT import Under25FT

class Betting():
    def __init__(self, matchTab: str, sizeTab: str, market: str, classification: str) -> None:
        self.matches = []
        self.matchTab = matchTab
        self.sizeTab = sizeTab
        self.market = market
        self.classification = classification
        self.bets = {
            'Under 2.5 FT': {
                'Super Favorito': [],
                'Favorito': [],
                'Equilibrado': [],
                'Zebra': [],
            },
        }
        if self.matchTab not in ['5 jogos', '10 jogos', '20 jogos']: raise MarketNotFoundError('Quantidade de partidas não identificado')
        if self.sizeTab not in ['Casa/Visitante', 'Global']: raise MarketNotFoundError('Lado da partida não identificado')
        if self.market not in ['Under 2.5 FT']: raise MarketNotFoundError('Mercado não identificado')
        if self.classification not in ['Super Favorito', 'Favorito', 'Equilibrado', 'Zebra']: raise MarketNotFoundError('Classificação das partidas não identificado')

    def setBets(self, ):
        for match, featured, stats in self.matches:
            if self.classification == 'Equilibrado':
                if self.market == 'Under 2.5 FT':
                    bet = Under25FT(self.matchTab, self.sizeTab, self.classification, match, featured, stats)
                    if bet.hasClassification(): self.bets[self.market][self.classification].append(bet)
        # print(f"self.bets: {self.bets}")

    def getBets(self, ):
        return self.bets[self.market][self.classification]

    def execute(self, date: datetime, *methods):
        formatDate = format_date(date, '<YYYY>-<MM>-<DD>')
        cache = Cache(formatDate)
        if not cache.hasData():
            print(f"A data '{formatDate}' informada não tem registro")
            return
        matches = cache.getMathes()
        for match in matches:
            # print(f"="*30)
            # match.print()
            cache.setMatchRef(match)
            featured = cache.getFeatured()
            cacheStats = CacheStats(formatDate, match.getHometeam(), match.getAwayteam())
            stats = cacheStats.getStats()
            self.matches.append((match, featured, stats))
        
        self.setBets()
        
        print('='*50)
        print(f"Partidas do dia {format_date(date, '<DD>/<MM>/<YYYY>')}:")
        for method in methods:
            hasSignalBet = [bet for bet in self.getBets() if bet.isSignal(method)]
            # print(f"hasSignalBet: {hasSignalBet}")
            print('-'*30)
            print(f">> Método de {self.market}: {method}")
            for bet in hasSignalBet:
                bet.print()

# script = sys.argv[0]
date = sys.argv[1]
# methods = sys.argv[2:]
# date = 'today'
# date = 'tomorrow'
# date = '2024-02-27'
# date = '2024-02-29'
# date = '2024-03-01'
# date = '2024-03-01'
# date = 'today'
if date == 'today' or date == 'now': date = date_now()
elif date == 'tomorrow': date = add_day(date_now())
elif date == 'yesterday': date = add_day(date_now(), -1)
else:
    match = re.search(r"(\d{4})\-(\d{2})\-(\d{2})", date)
    year = int(match.group(1))
    month = int(match.group(2))
    day = int(match.group(3))
    date = get_date(year, month, day)
# print(f"date: {date}")


Betting(
    '5 jogos', 
    'Casa/Visitante', 
    'Under 2.5 FT', 
    'Equilibrado')\
.execute(
    date, 
    'default', 
    'm2', 
    'm3', 
    'm4', 
    'm5', 
    'm6', 
    'm7', 
    'm8', 
    'm9'
)


