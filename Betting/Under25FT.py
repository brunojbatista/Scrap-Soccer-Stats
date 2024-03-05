from Betting.Bet import Bet
from Readings.Data.Featured import Featured
from Readings.Data.Match import Match
from Readings.Data.Stats import Stats
import re

class Under25FT(Bet):
    def __init__(self, matchTab: str, sizeTab: str, classification: str, match: Match, featured: Featured, stat: Stats) -> None:
        super().__init__(matchTab, sizeTab, classification, match, featured, stat, 'Under 2.5 FT')
        self.isEnaled = self.hasClassification()
        self.methods = {
            'default': [
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
                        'Fora - CV CG (1.0)'
                    ),
                    # 'isSignal': False,
                },
            ],
            'm2': [
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
                        'Fora - CV CG (1.0)'
                    ),
                    # 'isSignal': False,
                },
            ],
            'm3': [
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
                        'Fora - CV CG (1.0)'
                    ),
                    # 'isSignal': False,
                },
            ],
            'm4': [
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
                        'Fora - CV CG (1.0)'
                    ),
                    # 'isSignal': False,
                },
            ],
            'm5': [
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
                        'Fora - CV CG (1.0)'
                    ),
                    # 'isSignal': False,
                },
            ],
            'm6': [
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
                        'Fora - CV CG (1.0)'
                    ),
                    # 'isSignal': False,
                },
            ],
            'm7': [
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
                        'Fora - CV CG (1.0)'
                    ),
                    # 'isSignal': False,
                },
            ],
            'm8': [
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
                        'Fora - CV CG (1.0)'
                    ),
                    # 'isSignal': False,
                },
            ],
            'm9': [
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
                        'Fora - CV CG (1.0)'
                    ),
                    # 'isSignal': False,
                },
            ]
        }

    def defaultMethod(self, ):
        method = 'default'
        methodsStruct = self.methods[method]
        for struct in methodsStruct:
            # print(f"struct: {struct}")
            if struct['matchTab'] == self.matchTab and struct['sizeTab'] == self.sizeTab:
                # print(f"É um sinal...")
                hasStats = struct['hasStats']
                # print(f"hasStats: {hasStats}")
                if not hasStats: return False
                params = struct['params']
                # print(f"params: {params}")
                averageCG_1 = (params['Casa - Média CG (1.0)'] + params['Fora - Média CG (1.0)']) / 2
                averageCVCG_1 = (params['Casa - CV CG (1.0)'] + params['Fora - CV CG (1.0)']) / 2
                # print(f"averageCG_1: {averageCG_1}")
                # print(f"averageCVCG_1: {averageCVCG_1}")
                if averageCG_1 < 2.5 and averageCVCG_1 >= 1:
                    if (params['Casa - CV CG (1.0)'] < 0.9 and params['Fora - CV CG (1.0)'] >= 1.5) \
                        or (params['Casa - CV CG (1.0)'] >= 1.6 and params['Fora - CV CG (1.0)'] >= 1.4):
                        return True
        return False
    
    def m2Method(self, ):
        method = 'm2'
        methodsStruct = self.methods[method]
        for struct in methodsStruct:
            # print(f"struct: {struct}")
            if struct['matchTab'] == self.matchTab and struct['sizeTab'] == self.sizeTab:
                # print(f"É um sinal...")
                hasStats = struct['hasStats']
                # print(f"hasStats: {hasStats}")
                if not hasStats: return False
                params = struct['params']
                # print(f"params: {params}")
                averageCG_1 = (params['Casa - Média CG (1.0)'] + params['Fora - Média CG (1.0)']) / 2
                averageCVCG_1 = (params['Casa - CV CG (1.0)'] + params['Fora - CV CG (1.0)']) / 2
                # print(f"averageCG_1: {averageCG_1}")
                # print(f"averageCVCG_1: {averageCVCG_1}")
                if averageCG_1 >= 3.1 and averageCG_1 < 4.3 and averageCVCG_1 >= 1.1:
                    # if (params['Casa - CV CG (1.0)'] < 0.9 and params['Fora - CV CG (1.0)'] >= 1.5) \
                    #     or (params['Casa - CV CG (1.0)'] >= 1.6 and params['Fora - CV CG (1.0)'] >= 1.4):
                    return True
        return False

    def mMethods(self, method: str):
        methodsStruct = self.methods[method]
        for struct in methodsStruct:
            if struct['matchTab'] == self.matchTab and struct['sizeTab'] == self.sizeTab:
                # print(f"É um sinal...")
                hasStats = struct['hasStats']
                # print(f"hasStats: {hasStats}")
                if not hasStats: return False
                params = struct['params']
                homeCVCG1_0 = params['Casa - Média CG (1.0)']
                if homeCVCG1_0 <= 0: return False
                awayCVCG1_0 = params['Fora - Média CG (1.0)']
                if awayCVCG1_0 <= 0: return False
                homeDPCG1_0 = params['Casa - CV CG (1.0)'] / homeCVCG1_0
                awayDPCG1_0 = params['Fora - CV CG (1.0)'] / awayCVCG1_0
                Cf1 = params['Casa - Média CG (1.0)'] * homeDPCG1_0
                Cf2 = params['Fora - Média CG (1.0)'] * awayDPCG1_0
                Cf3 = Cf1 * Cf2
                if method == 'm3':
                    if (Cf1>=1.5 and Cf2>=1.4):
                        return True
                elif method == 'm4':
                    if (Cf1<0.8 and Cf1>=0 and Cf2>=1.7):
                        return True
                elif method == 'm5':
                    if (Cf1>=0.8 and Cf1<1.5 and Cf2>=1.2 and Cf2<1.4):
                        return True
                elif method == 'm6':
                    if (Cf3>=1.1 and Cf3<1.3):
                        return True
                elif method == 'm7':
                    if (Cf3>=2.7):
                        return True
                elif method == 'm8':
                    if (Cf3>=1.1 and Cf3<1.2):
                        return True
                elif method == 'm9':
                    if (Cf3>=1.1):
                        return True
                # elif method == 'm10':
                #     if ((Cf1>=1.5 and Cf2>=1.4)) or \
                #         ((Cf1<0.8 and Cf1>=0 and Cf2>=1.7)) or \
                #         ((Cf3>=1.1 and Cf3<1.3)) or \
                #         ((Cf3>=1.1 and Cf3<1.2)):
                #         return True
        return False
    
    def getSignal(self, method: str) -> bool:
        if method == 'default':
            return self.defaultMethod()
        elif method == 'm2':
            return self.m2Method()
        elif re.search(r"^m\d{1,}", method):
            return self.mMethods(method)
        else:
            return False

    def isSignal(self, method: str = 'default') -> bool:
        if not self.isEnaled: return False;
        return self.getSignal(method)
    
    def print(self, ):
        txt = f"{self.match.getTime()} | {self.match.getHometeam()} x {self.match.getAwayteam()} | Odd: {self.featured.getOddUnder25FT()}"
        print(txt)
