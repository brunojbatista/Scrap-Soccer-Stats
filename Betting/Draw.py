from Betting.Bet import Bet
from Readings.Data.Featured import Featured
from Readings.Data.Match import Match
from Readings.Data.Stats import Stats
import re

def E(*params):
    for p in params: 
        if not p: return False
    return True

def OU(*params):
    for p in params: 
        if p: return True
    return False

class Draw(Bet):
    def __init__(self, matchTab: str, sizeTab: str, classification: str, match: Match, featured: Featured, stat: Stats) -> None:
        super().__init__(matchTab, sizeTab, classification, match, featured, stat, 'Under 2.5 FT')
        self.isEnaled = self.hasClassification()
        self.methods = {
            'a': [
                {
                    'matchTab': '5 jogos',
                    'sizeTab': 'Casa/Visitante',
                    'hasStats': stat.hasStats('5 jogos', 'Casa/Visitante'),
                    'params': stat.getParams(
                        '5 jogos', 
                        'Casa/Visitante', 
                        'Casa - Média CG (1.0)', 
                        'Fora - Média CG (1.0)',
                        'Casa - CV CG (1.0)',
                        'Fora - CV CG (1.0)',
                        'Casa - Média GM no HT',
                        'Fora - Média GM no HT',
                        'Casa - CV GM no HT',
                        'Fora - CV GM no HT',
                        'Casa - Over 2.5 FT (%)',
                        'Fora - Over 2.5 FT (%)',

                        'Casa - Over 0.5 HT (%)',
                        'Fora - Over 0.5 HT (%)',
                        'Casa - Over 1.5 HT (%)',
                        'Fora - Over 1.5 HT (%)',

                        'Casa - Média GS no HT',
                        'Fora - Média GS no HT',
                        'Casa - CV GS no HT',
                        'Fora - CV GS no HT',
                    ),
                    'featured': {
                        'Casa LG Score': featured.getCasaLGScore(),
                        'H Score': featured.getHScore(),
                        'Fora LG Score': featured.getForaLGScore(),
                    }
                },
            ],
        }

    def aMethods(self, method: str):
        methodsStruct = self.methods['a']
        for struct in methodsStruct:
            if struct['matchTab'] == self.matchTab and struct['sizeTab'] == self.sizeTab:
                # print(f"É um sinal...")
                hasStats = struct['hasStats']
                # print(f"hasStats: {hasStats}")
                if not hasStats: return []
                params = struct['params']

                # print(f"Entrou.......")

                homeCG1_0 = params['Casa - Média CG (1.0)']
                Q = homeCG1_0

                awayCG1_0 = params['Fora - Média CG (1.0)']
                R = awayCG1_0

                homeCVCG1_0 = params['Casa - CV CG (1.0)']
                S = homeCVCG1_0

                awayCVCG1_0 = params['Fora - CV CG (1.0)']
                T = awayCVCG1_0

                homeGMHT = params['Casa - Média GM no HT']
                Y = homeGMHT

                awayGMHT = params['Fora - Média GM no HT']
                Z = awayGMHT

                homeCVGMHT = params['Casa - CV GM no HT']
                AA = homeCVGMHT

                awayCVGMHT = params['Fora - CV GM no HT']
                AB = awayCVGMHT


                homeGSHT = params['Casa - Média GS no HT']
                AC = homeGSHT

                awayGSHT = params['Fora - Média GS no HT']
                AD = awayGSHT

                homeCVGSHT = params['Casa - CV GS no HT']
                AE = homeCVGSHT

                awayCVGSHT = params['Fora - CV GS no HT']
                AF = awayCVGSHT


                homeOver25FT = params['Casa - Over 2.5 FT (%)']
                AG = homeOver25FT

                awayOver25FT = params['Fora - Over 2.5 FT (%)']
                AH = awayOver25FT


                homeDPCG1_0 = -1
                if homeCG1_0 > 0: homeDPCG1_0 = homeCVCG1_0 / homeCG1_0 # ok
                awayDPCG1_0 = -1
                if awayCG1_0 > 0: awayDPCG1_0 = awayCVCG1_0 / awayCG1_0 # ok
                avgCG1_0    = (homeCG1_0 + awayCG1_0) / 2 # ok
                avgCVCG1_0  = (homeCVCG1_0 + awayCVCG1_0) / 2 # ok
                avgDPCG1_0  = (homeDPCG1_0 + awayDPCG1_0) / 2 # ok

                AT = homeDPCG1_0
                AU = awayDPCG1_0
                AV = avgCG1_0
                AW = avgCVCG1_0
                AX = avgDPCG1_0
                
                homeDPGMHT = -1
                if homeGMHT > 0: homeDPGMHT  = homeCVGMHT / homeGMHT # ok
                awayDPGMHT = -1
                if awayGMHT > 0: awayDPGMHT  = awayCVGMHT / awayGMHT # ok
                avgGMHT     = (homeGMHT + awayGMHT) / 2 # ok
                avgCVGMHT   = (homeCVGMHT + awayCVGMHT) / 2 # ok
                avgDPGMHT   = (homeDPGMHT + awayDPGMHT) / 2 # ok

                AY = homeDPGMHT
                AZ = awayDPGMHT
                BA = avgGMHT
                BB = avgCVGMHT
                BC = avgDPGMHT

                homeDPGSHT = -1
                if homeGSHT > 0: homeDPGSHT  = homeCVGSHT / homeGSHT # ok
                awayDPGSHT = -1
                if awayGSHT > 0: awayDPGSHT  = awayCVGSHT / awayGSHT # ok
                avgGSHT     = (homeGSHT + awayGSHT) / 2 # ok
                avgCVGSHT   = (homeCVGSHT + awayCVGSHT) / 2 # ok
                avgDPGSHT   = (homeDPGSHT + awayDPGSHT) / 2 # ok

                BD = homeDPGSHT
                BE = awayDPGSHT
                BF = avgGSHT
                BG = avgCVGSHT
                BH = avgDPGSHT

                Cf1 = Q*AT
                Cf2 = R*AU
                Cf3 = Y*AY
                Cf4 = Z*AZ
                Cf5 = AC*BD
                Cf6 = AD*BE

                BI = Cf1
                BJ = Cf2
                BK = Cf3
                BL = Cf4
                BM = Cf5
                BN = Cf6

                try:
                    Cf7 = (BI/BJ)*(BK/BL)*(BM/BN)
                except ZeroDivisionError:
                    Cf7 = -1
                BO = Cf7

                try:
                    Cf8 = (BI/BK)*(BJ/BL)
                except ZeroDivisionError:
                    Cf8 = -1
                BP = Cf8

                try:
                    Cf9 = (BK/BM)*(BL/BN)
                except ZeroDivisionError:
                    Cf9 = -1
                BQ = Cf9

                try:
                    Cf10 = (BI/BM)*(BJ/BN)
                except ZeroDivisionError:
                    Cf10 = -1
                BR = Cf10

                try:
                    Cf11 = (BO/BP)
                except ZeroDivisionError:
                    Cf11 = -1
                BS = Cf11

                try:
                    Cf12 = (BQ/BR)
                except ZeroDivisionError:
                    Cf12 = -1
                BT = Cf12

                
                
                
                filtersMethod = {
                    'a1': E(BO>=1.7,BO<2.6,BP>=0.8,BP<1),
                    'a2': E(BO>=5.8,BO<8.3,BQ>=0.1,BQ<1.7),
                    'a3': E(BO>=1.3,BO<2.9,BQ>=1.2,BQ<2.2),
                    'a4': E(BO>=0,BO<0.6,BS>=1,BS<1.3),
                    'a5': E(BO>=1.2,BO<2.6,BT>=1,BT<1.2),
                    'a6': E(BO>=0,BO<1.3,BT>=2.4,BT<2.6),
                    'a7': E(BP>=0,BP<0.6,BQ>=0,BQ<0.2),
                    'a8': E(BP>=0,BP<0.8,BQ>=1.3,BQ<1.5),
                    'a9': E(BP>=0,BP<0.3,BR>=0.1,BR<0.3),
                    'a10': E(BP>=0.5,BP<0.9,BR>=0.6,BR<0.9),
                    'a11': E(BP>=0.1,BP<0.5,BS>=1,BS<1.3),
                    'a12': E(BP>=0.9,BP<1,BT>=1,BT<1.1),
                    'a13': E(BP>=0.3,BP<0.5,BT>=2.4,BT<2.6),
                    'a14': E(BQ>=1,BQ<2.1,BS>=1.1,BS<1.4),
                    'a15': E(BQ>=0.1,BQ<0.5,BT>=1,BT<1.1),
                    'a16': E(BR>=0,BR<0.5,BS>=5.9,BS<6.5),
                    'a17': E(BR>=0,BR<0.6,BS>=7.4,BS<7.9),
                    'a18': E(BR>=0.2,BR<1.1,BT>=2.3,BT<2.6),
                    'a19': E(BR>=0,BR<1,BT>=7.2,BT<12.9),
                    'a20': E(BS>=1.9,BS<3.1,BT>=1,BT<1.3),
                }

                groups = {
                    'ag1': ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'a11', 'a12', 'a13', 'a14', 'a15', 'a16', 'a17', 'a18', 'a19', 'a10', ]
                    # 'mg1': ['m6', 'm17', 'm18'],
                    # 'mg2': ['m1', 'm2', 'm3', 'm4', 'm5'],
                    # 'mg3': ['m7', 'm8', 'm9'],
                    # 'mg4': ['m10', 'm11', 'm12'],
                    # 'mg5': ['m1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9', 'm10', 'm11', 'm12'],
                    # 'mg6': ['m13', 'm14', 'm15', 'm16', 'm17', 'm18', 'm19', 'm20'],
                }

                availableMethods = []
                if method in filtersMethod: 
                    if filtersMethod[method]: availableMethods = [method]
                elif method in groups:
                    for m in groups[method]:
                        if filtersMethod[m]: availableMethods.append(m)
                return availableMethods;

        return []

    def getSignal(self, method) -> list:
        if not self.isEnaled: return [];
        if re.search(r"^a.*$", method):
            return self.aMethods(method)
        else:
            return []
    
    def print(self, ):
        txt = f"{self.featured.getPais()} | {self.featured.getLiga()}\n{self.match.getTime()} | {self.match.getHometeam()} x {self.match.getAwayteam()} | Odd: {self.featured.getOddDraw()}"
        score = None
        result = None
        if self.featured.isStarted():
            homeScore = self.featured.getHomeFT()
            awayScore = self.featured.getAwayFT()
            if homeScore < 0 or awayScore < 0: 
                result = "Resultado: Não Informado"
                score = f"Placar Final: Não Informado"
            else:
                score = f"Placar Final: {homeScore} x {awayScore}"
                if homeScore == awayScore: result = "Resultado: Green"
                else: result = "Resultado: Red"
            txt = f"{txt}\n{score}"
            txt = f"{txt}\n{result}"
        print(txt)
