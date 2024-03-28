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

class Under25FT(Bet):
    def __init__(self, matchTab: str, sizeTab: str, classification: str, match: Match, featured: Featured, stat: Stats) -> None:
        super().__init__(matchTab, sizeTab, classification, match, featured, stat, 'Under 2.5 FT')
        self.isEnaled = self.hasClassification()
        self.methods = {
            'm': [
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
            # 'a': [
            #     {
            #         'matchTab': '5 jogos',
            #         'sizeTab': 'Casa/Visitante',
            #         'hasStats': stat.hasStats('5 jogos', 'Casa/Visitante'),
            #         'params': stat.getParams(
            #             '5 jogos', 
            #             'Casa/Visitante', 
            #             'Casa - Média CG (1.0)', 
            #             'Fora - Média CG (1.0)',
            #             'Casa - CV CG (1.0)',
            #             'Fora - CV CG (1.0)',
            #             'Casa - Média GM no HT',
            #             'Fora - Média GM no HT',
            #             'Casa - CV GM no HT',
            #             'Fora - CV GM no HT',
            #             'Casa - Over 2.5 FT (%)',
            #             'Fora - Over 2.5 FT (%)',

            #             'Casa - Over 0.5 HT (%)',
            #             'Fora - Over 0.5 HT (%)',
            #             'Casa - Over 1.5 HT (%)',
            #             'Fora - Over 1.5 HT (%)',

            #             'Casa - Média GS no HT',
            #             'Fora - Média GS no HT',
            #             'Casa - CV GS no HT',
            #             'Fora - CV GS no HT',
            #         ),
            #         'featured': {
            #             'Casa LG Score': featured.getCasaLGScore(),
            #             'H Score': featured.getHScore(),
            #             'Fora LG Score': featured.getForaLGScore(),
            #         }
            #     },
            # ],
            # 'b': [
            #     {
            #         'matchTab': '5 jogos',
            #         'sizeTab': 'Casa/Visitante',
            #         'hasStats': stat.hasStats('5 jogos', 'Casa/Visitante'),
            #         'params': stat.getParams(
            #             '5 jogos', 
            #             'Casa/Visitante', 
            #             'Casa - Média CG (1.0)', 
            #             'Fora - Média CG (1.0)',
            #             'Casa - CV CG (1.0)',
            #             'Fora - CV CG (1.0)',
            #             'Casa - Média GM no HT',
            #             'Fora - Média GM no HT',
            #             'Casa - CV GM no HT',
            #             'Fora - CV GM no HT',

            #             'Casa - Média GS no HT',
            #             'Fora - Média GS no HT',
            #             'Casa - CV GS no HT',
            #             'Fora - CV GS no HT',
            #         ),
            #         'featured': {
            #             'Casa LG Score': featured.getCasaLGScore(),
            #             'H Score': featured.getHScore(),
            #             'Fora LG Score': featured.getForaLGScore(),
            #         }
            #     },
            # ],
            'd': [
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

                        'Casa - Média GS no HT',
                        'Fora - Média GS no HT',
                        'Casa - CV GS no HT',
                        'Fora - CV GS no HT',
                    )
                },
            ],
        }

    def mMethods(self, method: str):
        methodsStruct = self.methods['m']
        for struct in methodsStruct:
            if struct['matchTab'] == self.matchTab and struct['sizeTab'] == self.sizeTab:
                # print(f"É um sinal...")
                hasStats = struct['hasStats']
                # print(f"hasStats: {hasStats}")
                if not hasStats: return []
                params = struct['params']

                homeCG1_0 = params['Casa - Média CG (1.0)']
                S = homeCG1_0

                awayCG1_0 = params['Fora - Média CG (1.0)']
                T = awayCG1_0

                homeCVCG1_0 = params['Casa - CV CG (1.0)']
                U = homeCVCG1_0

                awayCVCG1_0 = params['Fora - CV CG (1.0)']
                V = awayCVCG1_0

                homeGMHT = params['Casa - Média GM no HT']
                AA = homeGMHT

                awayGMHT = params['Fora - Média GM no HT']
                AB = awayGMHT

                homeCVGMHT = params['Casa - CV GM no HT']
                AC = homeCVGMHT

                awayCVGMHT = params['Fora - CV GM no HT']
                AD = awayCVGMHT


                homeGSHT = params['Casa - Média GS no HT']
                AE = homeGSHT

                awayGSHT = params['Fora - Média GS no HT']
                AF = awayGSHT

                homeCVGSHT = params['Casa - CV GS no HT']
                AG = homeCVGSHT

                awayCVGSHT = params['Fora - CV GS no HT']
                AH = awayCVGSHT


                homeOver25FT = params['Casa - Over 2.5 FT (%)']
                AI = homeOver25FT

                awayOver25FT = params['Fora - Over 2.5 FT (%)']
                AJ = awayOver25FT


                homeDPCG1_0 = -1
                if homeCG1_0 > 0: homeDPCG1_0 = homeCVCG1_0 / homeCG1_0 # ok
                awayDPCG1_0 = -1
                if awayCG1_0 > 0: awayDPCG1_0 = awayCVCG1_0 / awayCG1_0 # ok
                avgCG1_0    = (homeCG1_0 + awayCG1_0) / 2 # ok
                avgCVCG1_0  = (homeCVCG1_0 + awayCVCG1_0) / 2 # ok
                avgDPCG1_0  = (homeDPCG1_0 + awayDPCG1_0) / 2 # ok

                AV = homeDPCG1_0
                AW = awayDPCG1_0
                AX = avgCG1_0
                AY = avgCVCG1_0
                AZ = avgDPCG1_0
                
                homeDPGMHT = -1
                if homeGMHT > 0: homeDPGMHT  = homeCVGMHT / homeGMHT # ok
                awayDPGMHT = -1
                if awayGMHT > 0: awayDPGMHT  = awayCVGMHT / awayGMHT # ok
                avgGMHT     = (homeGMHT + awayGMHT) / 2 # ok
                avgCVGMHT   = (homeCVGMHT + awayCVGMHT) / 2 # ok
                avgDPGMHT   = (homeDPGMHT + awayDPGMHT) / 2 # ok

                BA = homeDPGMHT
                BB = awayDPGMHT
                BC = avgGMHT
                BD = avgCVGMHT
                BE = avgDPGMHT

                homeDPGSHT = -1
                if homeGSHT > 0: homeDPGSHT  = homeCVGSHT / homeGSHT # ok
                awayDPGSHT = -1
                if awayGSHT > 0: awayDPGSHT  = awayCVGSHT / awayGSHT # ok
                avgGSHT     = (homeGSHT + awayGSHT) / 2 # ok
                avgCVGSHT   = (homeCVGSHT + awayCVGSHT) / 2 # ok
                avgDPGSHT   = (homeDPGSHT + awayDPGSHT) / 2 # ok

                BF = homeDPGSHT
                BG = awayDPGSHT
                BH = avgGSHT
                BI = avgCVGSHT
                BJ = avgDPGSHT

                Cf1 = homeCG1_0     * homeDPCG1_0 # ok
                Cf2 = awayCG1_0     * awayDPCG1_0 # ok
                Cf3 = -1
                if awayCVCG1_0 > 0: Cf3 = homeCVCG1_0   / awayCVCG1_0 # ok
                Cf4 = Cf1           * Cf2 # ok
                Cf5 = homeGMHT      * homeDPGMHT # ok
                Cf6 = awayGMHT      * awayDPGMHT # ok
                Cf7 = Cf5           * Cf6 # ok
                Cf8 = homeOver25FT  * awayOver25FT # ok
                Cf9 = avgGMHT       * avgGSHT # ok

                BK = Cf1
                BL = Cf2
                BM = Cf3
                BN = Cf4
                BO = Cf5
                BP = Cf6
                BQ = Cf7
                BR = Cf8
                BS = Cf9
                
                filtersMethod = {
                    'm1': E(AX<2.5,AY>=1,OU(E(U<0.9,V>=1.5),E(U>=1.5,V>=1.4),E(U>=0.8,U<1.1,V>=1.2,V<1.5))),
                    'm2': E(AX>=3.1,AX<4.3,AY>=1.1),
                    'm3': E(BC>=0.1,BC<1,BD>=0.9,OU(E(AC>=0.7,AC<1.3,AD>=2.1,AD<2.3))),
                    'm4': OU(E(BC>=0.4,BC<0.5,BH>=0.4,BH<0.5),E(BC>=0.7,BC<0.8,BH>=0.7,BH<0.8)),
                    'm5': OU(E(AX>=1.5,AX<2,BS>=0,BS<0.25),E(AX>=2,AX<2.5,BS>=0.375,BS<0.5)),
                    'm6': E(BK>=0.5,BK<0.8,BL>=0.2,BL<0.6),
                    'm7': E(BK>=0,BK<0.8,BL>=1.7),
                    'm8': E(BK>=1.5,BL>=1.4),
                    'm9': E(BK>=0.5,BK<0.8,BL>=0.2,BL<0.6),
                    'm10': E(BM>=0.8,BM<1.2,AY>=1.5),
                    'm11': E(BM>=0.8,BM<1,AY>=1.05,AY<1.15),
                    'm12': E(BM>=0.1,BM<0.4,AY>=1.05,AY<1.6),
                    'm13': E(BM>=1.3,BM<2.6,BN>=0,BN<0.3),
                    'm14': E(BM>=2.6,BM<5.8,BN>=0.3,BN<1),
                    'm15': E(BM>=1.4,BM<2.5,BN>=1.9,BN<3.1),
                    'm16': E(BM>=0.4,BM<2.5,BN>=3.1),
                    'm17': E(BM>=0.8,BM<1,BN>=1.1,BN<1.2),
                    'm18': E(BM>=1.3,BM<1.4,BN>=0.7,BN<0.8),
                    'm19': E(BM>=1.6,BM<2.1,BN>=1.1,BN<1.2),
                    'm20': E(BM>=1.7,BM<2.3,BN>=0.8,BN<0.9),
                }

                groups = {
                    'mg1': ['m6', 'm17', 'm18'],
                    'mg2': ['m1', 'm2', 'm3', 'm4', 'm5'],
                    'mg3': ['m7', 'm8', 'm9'],
                    'mg4': ['m10', 'm11', 'm12'],
                    'mg5': ['m1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9', 'm10', 'm11', 'm12'],
                    'mg6': ['m13', 'm14', 'm15', 'm16', 'm17', 'm18', 'm19', 'm20'],
                }

                availableMethods = []
                if method in filtersMethod: 
                    if filtersMethod[method]: availableMethods = [method]
                elif method in groups:
                    for m in groups[method]:
                        if filtersMethod[m]: availableMethods.append(m)
                return availableMethods;

        return []

    # def aMethod(self, method: str):
    #     methodsStruct = self.methods['a']
    #     for struct in methodsStruct:
    #         if struct['matchTab'] == self.matchTab and struct['sizeTab'] == self.sizeTab:
    #             # print(f"É um sinal...")
    #             hasStats = struct['hasStats']
    #             # print(f"hasStats: {hasStats}")
    #             if not hasStats: return []
    #             params = struct['params']



    #             homeCG1_0 = params['Casa - Média CG (1.0)']
    #             if homeCG1_0 < 0: return []

    #             awayCG1_0 = params['Fora - Média CG (1.0)']
    #             if awayCG1_0 < 0: return []

    #             homeCVCG1_0 = params['Casa - CV CG (1.0)']
    #             if homeCVCG1_0 < 0: return []

    #             awayCVCG1_0 = params['Fora - CV CG (1.0)']
    #             if awayCVCG1_0 < 0: return []



    #             homeGSHT = params['Casa - Média GS no HT']
    #             if homeGSHT < 0: return []

    #             awayGSHT = params['Fora - Média GS no HT']
    #             if awayGSHT < 0: return []

    #             homeCVGSHT = params['Casa - CV GS no HT']
    #             if homeCVGSHT < 0: return []

    #             awayCVGSHT = params['Fora - CV GS no HT']
    #             if awayCVGSHT < 0: return []



    #             homeDPCG1_0 = homeCVCG1_0 / homeCG1_0 # ok
    #             awayDPCG1_0 = awayCVCG1_0 / awayCG1_0 # ok
    #             avgCG1_0    = (homeCG1_0 + awayCG1_0) / 2 # ok
    #             avgCVCG1_0  = (homeCVCG1_0 + awayCVCG1_0) / 2 # ok
    #             avgDPCG1_0  = (homeDPCG1_0 + awayDPCG1_0) / 2 # ok

    #             # homeDPGMHT  = homeCVGMHT / homeGMHT # ok
    #             # awayDPGMHT  = awayCVGMHT / awayGMHT # ok
    #             # avgGMHT     = (homeGMHT + awayGMHT) / 2 # ok
    #             # avgCVGMHT   = (homeCVGMHT + awayCVGMHT) / 2 # ok
    #             # avgDPGMHT   = (homeDPGMHT + awayDPGMHT) / 2 # ok

    #             homeDPGSHT  = homeCVGSHT / homeGSHT # ok
    #             awayDPGSHT  = awayCVGSHT / awayGSHT # ok
    #             avgGSHT     = (homeGSHT + awayGSHT) / 2 # ok
    #             avgCVGSHT   = (homeCVGSHT + awayCVGSHT) / 2 # ok
    #             avgDPGSHT   = (homeDPGSHT + awayDPGSHT) / 2 # ok

    #             Cfa1 = homeCG1_0 * awayGSHT
    #             Cfa2 = awayCG1_0 * homeGSHT

    #             # Cf1 = homeCG1_0     * homeDPCG1_0 # ok
    #             # Cf2 = awayCG1_0     * awayDPCG1_0 # ok
    #             # Cf3 = homeCVCG1_0   / awayCVCG1_0 # ok
    #             # Cf4 = Cf1           * Cf2 # ok
    #             # Cf5 = homeGMHT      * homeDPGMHT # ok
    #             # Cf6 = awayGMHT      * awayDPGMHT # ok
    #             # Cf7 = Cf5           * Cf6 # ok
    #             # Cf8 = homeOver25FT  * awayOver25FT # ok
    #             # Cf9 = avgGMHT       * avgGSHT # ok

    #             if not(Cfa1>=0 and Cfa1<4 and Cfa2>=0 and Cfa2<2):
    #                 return []
                
    #             filtersMethod = {
    #                 'a1': homeCVCG1_0>=1.5 and awayCVGSHT>=0 and awayCVGSHT<1.1,
    #                 'a2': homeCVCG1_0>=1.4 and awayCVGSHT>=2.1,
    #                 'a3': homeCVCG1_0>=0 and homeCVCG1_0<0.7 and awayCVGSHT>=2.1,

    #                 'a4': awayCVCG1_0>=1.6 and homeCVGSHT>=0 and homeCVGSHT<1,
    #                 'a5': awayCVCG1_0>=1.3 and homeCVGSHT>=2.2,

    #                 'a6': homeCVCG1_0>=0 and homeCVCG1_0<0.9 and awayCVCG1_0>=2.2,
    #                 'a7': homeCVCG1_0>=1.3 and awayCVCG1_0>=1.6,

    #                 'a8': homeCVGSHT>=0 and homeCVGSHT<1.5 and awayCVGSHT>=0 and awayCVGSHT<0.9,
    #                 'a9': homeCVGSHT>=0 and homeCVGSHT<0.9 and awayCVGSHT>=1.3,
    #                 'a10': homeCVGSHT>=2.2 and homeCVGSHT<2.3 and awayCVGSHT>=0.9 and awayCVGSHT<1.1,
    #             }

    #             groups = {
    #                 'a-best': ['a4', 'a7'],
    #                 'a-all': ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', ],
    #             }

    #             availableMethods = []
    #             if method in filtersMethod: 
    #                 if filtersMethod[method]: availableMethods = [method]
    #             elif method in groups:
    #                 for m in groups[method]:
    #                     if filtersMethod[m]: availableMethods.append(m)
    #             return availableMethods;

    #     return []
    
    # def bMethod(self, method: str):
    #     methodsStruct = self.methods['b']
    #     for struct in methodsStruct:
    #         if struct['matchTab'] == self.matchTab and struct['sizeTab'] == self.sizeTab:
    #             # print(f"É um sinal...")
    #             hasStats = struct['hasStats']
    #             # print(f"hasStats: {hasStats}")
    #             if not hasStats: return []
    #             params = struct['params']



    #             homeGMHT = params['Casa - Média GM no HT']
    #             if homeGMHT < 0: return []

    #             awayGMHT = params['Fora - Média GM no HT']
    #             if awayGMHT < 0: return []

    #             homeCVGMHT = params['Casa - CV GM no HT']
    #             if homeCVGMHT < 0: return []

    #             awayCVGMHT = params['Fora - CV GM no HT']
    #             if awayCVGMHT < 0: return []



    #             homeGSHT = params['Casa - Média GS no HT']
    #             if homeGSHT < 0: return []

    #             awayGSHT = params['Fora - Média GS no HT']
    #             if awayGSHT < 0: return []

    #             homeCVGSHT = params['Casa - CV GS no HT']
    #             if homeCVGSHT < 0: return []

    #             awayCVGSHT = params['Fora - CV GS no HT']
    #             if awayCVGSHT < 0: return []

    #             try:
    #                 Cfb1 = round(homeGMHT / awayGSHT, 1)
    #             except ZeroDivisionError:
    #                 return []

    #             try:
    #                 Cfb2 = round(awayGMHT / homeGSHT, 1)
    #             except ZeroDivisionError:
    #                 return []

    #             if not(Cfb1>=0.5 and Cfb1<1.5 and Cfb2>=0.5 and Cfb2<1.5):
    #                 return []
                
    #             filtersMethod = {
    #                 'b1': homeCVGMHT>=1 and homeCVGMHT<1.1 and awayCVGMHT>=1 and awayCVGMHT<1.1,
    #                 'b2': homeCVGMHT>=2.2 and homeCVGMHT<2.3 and awayCVGMHT>=1.4 and awayCVGMHT<1.5,
    #                 'b3': homeCVGMHT>=0.9 and homeCVGMHT<1 and awayCVGMHT>=2.2 and awayCVGMHT<2.3,
    #                 'b4': homeCVGMHT>=0.7 and homeCVGMHT<0.8 and awayCVGMHT>=2.2 and awayCVGMHT<2.3,

    #                 'b5': homeCVGSHT>=1.3 and homeCVGSHT<1.4 and awayCVGSHT>=0.9 and awayCVGSHT<1,
    #                 'b6': homeCVGSHT>=1.4 and homeCVGSHT<1.5 and awayCVGSHT>=1 and awayCVGSHT<1.1,
    #                 'b7': homeCVGSHT>=2.2 and homeCVGSHT<2.3 and awayCVGSHT>=1 and awayCVGSHT<1.1,
    #                 'b8': homeCVGSHT>=1 and homeCVGSHT<1.1 and awayCVGSHT>=2.2 and awayCVGSHT<2.3,
    #                 'b9': homeCVGSHT>=2.2 and homeCVGSHT<2.3 and awayCVGSHT>=2.2 and awayCVGSHT<2.3,

    #                 'b10': homeCVGMHT>=0.9 and homeCVGMHT<1 and awayCVGSHT>=1 and awayCVGSHT<1.1,
    #                 'b11': homeCVGMHT>=0.7 and homeCVGMHT<0.8 and awayCVGSHT>=1 and awayCVGSHT<1.1,
    #                 'b12': homeCVGMHT>=2.2 and homeCVGMHT<2.3 and awayCVGSHT>=2.2 and awayCVGSHT<2.3,
                    
    #                 'b13': awayCVGMHT>=1 and awayCVGMHT<1.1 and homeCVGSHT>=1 and homeCVGSHT<1.1,
    #             }

    #             groups = {
    #                 'b-all': ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'b10', 'b11', 'b12', 'b13', ],
    #             }

    #             availableMethods = []
    #             if method in filtersMethod: 
    #                 if filtersMethod[method]: availableMethods = [method]
    #             elif method in groups:
    #                 for m in groups[method]:
    #                     if filtersMethod[m]: availableMethods.append(m)
    #             return availableMethods;

    #     return []

    def dMethod(self, method: str):
        methodsStruct = self.methods['d']
        for struct in methodsStruct:
            if struct['matchTab'] == self.matchTab and struct['sizeTab'] == self.sizeTab:
                # print(f"É um sinal...")
                hasStats = struct['hasStats']
                # print(f"hasStats: {hasStats}")
                if not hasStats: return []
                params = struct['params']

                homeCG1_0 = params['Casa - Média CG (1.0)']

                awayCG1_0 = params['Fora - Média CG (1.0)']

                homeCVCG1_0 = params['Casa - CV CG (1.0)']

                awayCVCG1_0 = params['Fora - CV CG (1.0)']


                homeGMHT = params['Casa - Média GM no HT']

                awayGMHT = params['Fora - Média GM no HT']

                homeCVGMHT = params['Casa - CV GM no HT']

                awayCVGMHT = params['Fora - CV GM no HT']



                homeGSHT = params['Casa - Média GS no HT']

                awayGSHT = params['Fora - Média GS no HT']

                homeCVGSHT = params['Casa - CV GS no HT']

                awayCVGSHT = params['Fora - CV GS no HT']

                homeDPCG1_0 = -1
                if homeCG1_0 > 0: homeDPCG1_0 = homeCVCG1_0 / homeCG1_0 # ok
                awayDPCG1_0 = -1
                if awayCG1_0 > 0: awayDPCG1_0 = awayCVCG1_0 / awayCG1_0 # ok
                # avgCG1_0    = (homeCG1_0 + awayCG1_0) / 2 # ok
                # avgCVCG1_0  = (homeCVCG1_0 + awayCVCG1_0) / 2 # ok
                # avgDPCG1_0  = (homeDPCG1_0 + awayDPCG1_0) / 2 # ok

                homeDPGMHT = -1
                if homeGMHT > 0: homeDPGMHT  = homeCVGMHT / homeGMHT # ok
                awayDPGMHT = -1
                if awayGMHT > 0: awayDPGMHT  = awayCVGMHT / awayGMHT # ok
                # avgGMHT     = (homeGMHT + awayGMHT) / 2 # ok
                # avgCVGMHT   = (homeCVGMHT + awayCVGMHT) / 2 # ok
                # avgDPGMHT   = (homeDPGMHT + awayDPGMHT) / 2 # ok

                homeDPGSHT = -1
                if homeGSHT > 0: homeDPGSHT  = homeCVGSHT / homeGSHT # ok
                awayDPGSHT = -1
                if awayGSHT > 0: awayDPGSHT  = awayCVGSHT / awayGSHT # ok
                # avgGSHT     = (homeGSHT + awayGSHT) / 2 # ok
                # avgCVGSHT   = (homeCVGSHT + awayCVGSHT) / 2 # ok
                # avgDPGSHT   = (homeDPGSHT + awayDPGSHT) / 2 # ok


                Cf1 = homeCG1_0 * homeDPCG1_0
                Cf2 = awayCG1_0 * awayDPCG1_0
                Cf3 = homeGMHT * homeDPGMHT
                Cf4 = awayGMHT * awayDPGMHT
                Cf5 = homeGSHT * homeDPGSHT
                Cf6 = awayGSHT * awayDPGSHT

                BK = Cf1
                BL = Cf2
                BM = Cf3
                BN = Cf4
                BO = Cf5
                BP = Cf6

                try:
                    Cf7 = (BK/BL)*(BM/BN)*(BO/BP)
                except ZeroDivisionError:
                    Cf7 = -1
                BQ = Cf7

                try:
                    Cf8 = (BK/BM)*(BL/BN)
                except ZeroDivisionError:
                    Cf8 = -1
                BR = Cf8

                try:
                    Cf9 = (BM/BO)*(BN/BP)
                except ZeroDivisionError:
                    Cf9 = -1
                BS = Cf9

                try:
                    Cf10 = (BK/BO)*(BL/BP)
                except ZeroDivisionError:
                    Cf10 = -1
                BT = Cf10

                try:
                    Cf11 = (BQ/BR)
                except ZeroDivisionError:
                    Cf11 = -1
                BU = Cf11

                try:
                    Cf12 = (BS/BT)
                except ZeroDivisionError:
                    Cf12 = -1
                BV = Cf12


                filtersMethod = {
                    'd1': BQ>=0 and BQ<0.5 and BR>=0.5 and BR<0.4,
                    'd2': BQ>=6.1 and BR>=0 and BR<0.3,
                    'd3': BQ>=0 and BQ<1.9 and BR>=2.05,
                    'd4': BQ>=0.4 and BQ<0.7 and BT>=0.25 and BT<0.35,
                    'd5': BQ>=0 and BQ<1.8 and BT>=2.5,
                    'd6': BR>=0.15 and BR<0.45 and BS>=0.5 and BS<1,
                    'd7': BR>=0 and BR<1.05 and BS>=7.7,
                    'd8': BR>=0.05 and BR<0.35 and BT>=0.15 and BT<0.2,
                    'd9': BR>=0 and BR<1.55 and BT>=2.5,
                    'd10': BR>=1.5 and BT>=0 and BT<0.45,
                    'd11': BR>=0.25 and BR<0.4 and BU>=0.2 and BU<0.9,
                    'd12': BR>=0.25 and BR<0.5 and BV>=2.2 and BV<4,
                    'd13': BS>=0.5 and BS<0.9 and BT>=0.05 and BT<0.25,
                    'd14': BS>=0 and BS<1.9 and BV>=2.7 and BV<4.1,
                    'd15': BS>=0 and BS<2.4 and BV>=6.3 and BV<8.7,
                    'd16': BT>=0.05 and BT<0.45 and BV>=2.3 and BV<2.9,
                    'd17': BT>=0.05 and BT<0.5 and BV>=3.1 and BV<4,
                    'd18': BU>=0.2 and BU<2.5 and BV>=2.5 and BV<4,
                    'd19': BU>=0 and BU<3.8 and BV>=6,
                }

                groups = {
                    'dg1': ['d2', 'd3', 'd5', 'd7', 'd9', 'd10', 'd15', 'd19'],
                }

                availableMethods = []
                if method in filtersMethod: 
                    if filtersMethod[method]: availableMethods = [method]
                elif method in groups:
                    for m in groups[method]:
                        if filtersMethod[m]: 
                            availableMethods.append(m)
                return availableMethods;

        return []

    def getSignal(self, method: str = 'm1') -> list:
        if not self.isEnaled: return [];
        if re.search(r"^m.*$", method):
            return self.mMethods(method)
        # elif re.search(r"^a.*$", method):
        #     return self.aMethod(method)
        # elif re.search(r"^b.*$", method):
        #     return self.bMethod(method)
        elif re.search(r"^d.*$", method):
            return self.dMethod(method)
        else:
            return []
    
    def print(self, ):
        txt = f"{self.featured.getPais()} | {self.featured.getLiga()}\n{self.match.getTime()} | {self.match.getHometeam()} x {self.match.getAwayteam()} | Odd: {self.featured.getOddUnder25FT()}"
        score = None
        result = None
        if self.featured.isStarted():
            homeScore = self.featured.getHomeFT()
            awayScore = self.featured.getAwayFT()
            totalScore = homeScore + awayScore
            if homeScore < 0 or awayScore < 0: 
                result = "Resultado: Não Informado"
                score = f"Placar Final: Não Informado"
            else:
                score = f"Placar Final: {homeScore} x {awayScore}"
                if totalScore < 3: result = "Resultado: Green"
                else: result = "Resultado: Red"
            txt = f"{txt}\n{score}"
            txt = f"{txt}\n{result}"
        print(txt)
