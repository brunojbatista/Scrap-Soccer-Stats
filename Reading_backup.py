from Library_v1.Driver.DriverInterface import DriverInterface
from Library_v1.Driver.DriverActions import DriverActions
import re

from Exceptions.StatReadingError import StatReadingError

from Library_v1.Utils.string import (
    slug_name,
    default_space,
)

from Exceptions.ActionError import ActionError

BASE_XPATH = "//*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div"
getInfoXpath = lambda relativeXpath: f"{BASE_XPATH}{relativeXpath}"

MEASUREMENTS_GROUP_A_XPATH = "(//*[@id='__next']/section/div[2]/div[2]/div/div/div/div)[3]/div/div[.//button[text()='5 jogos']]/div[not(@role) and contains(@class, 'tab-panels')]/div[not(@hidden)]/div/div/div[not(@role) and contains(@class, 'tab-panels')]/div[not(@hidden)]/div/div[not(@role) and contains(@class, 'tab-panels')]/div[not(@hidden)]/div/div/div"
MEASUREMENTS_GROUP_B_XPATH = "(//*[@id='__next']/section/div[2]/div[2]/div/div/div/div)[3]/div/div[.//button[text()='5 jogos']]/div[not(@role) and contains(@class, 'tab-panels')]/div[not(@hidden)]/div/div/div[not(@role) and contains(@class, 'tab-panels')]/div[not(@hidden)]/div/div[not(@role) and contains(@class, 'tab-panels')]/div[not(@hidden)]/div/div/div/div"

FEATURED = [
    "Data",
    "Hora",
    "Pais",
    "Liga",
    "Casa",
    "Fora",
    "Casa HT",
    "Fora HT",
    "Casa FT",
    "Fora FT",
    "Odd Casa",
    "Odd Empate",
    "Odd Fora",
    "Odd Under 0.5 HT",
    "Odd Under 0.5 FT",
    "Odd Under 1.5 FT",
    "Odd Under 2.5 FT",
    "Odd Não Ambas",
    "Odd Over 0.5 HT",
    "Odd Over 0.5 FT",
    "Odd Over 1.5 FT",
    "Odd Over 2.5 FT",
    "Odd Ambas",
    "Casa LG Score",
    "H Score",
    "Fora LG Score",
]

STATS = {
    # ----------------------------------------------------
    # Médias e Dispersões
    'Média Custo do Gol (1.0)': {
        'fields': [
            'Média CG (1.0)',
            'CV CG (1.0)',
        ],
        "startIndex": 0,
    },
    'Média Custo do Gol (2.0)': {
        'fields': [
            'Média CG (2.0)',
            'CV CG (2.0)',
        ],
        "startIndex": 0,
    },
    'Gols marcados no HT': {
        'fields': [
            'GM no HT',
            'Média GM no HT',
            'CV GM no HT',
        ],
        "startIndex": 0,
    },
    'Gols sofridos no HT': {
        'fields': [
            'GS no HT',
            'Média GS no HT',
            'CV GS no HT',
        ],
        "startIndex": 0,
    },
    'Gols marcados no 2T': {
        'fields': [
            'GM no 2T',
            'Média GM no 2T',
            'CV GM no 2T',
        ],
        "startIndex": 0,
    },
    'Gols sofridos no 2T': {
        'fields': [
            'GS no 2T',
            'Média GS no 2T',
            'CV GS no 2T',
        ],
        "startIndex": 0,
    },
    'Gols marcados no FT': {
        'fields': [
            'GM no FT',
            'Média GM no FT',
            'CV GM no FT',
        ],
        "startIndex": 0,
    },
    'Gols sofridos no FT': {
        'fields': [
            'GS no FT',
            'Média GS no FT',
            'CV GS no FT',
        ],
        "startIndex": 0,
    },
    # ----------------------------------------------------
    # Over
    "Jogos Over 0.5 no HT": {
        'fields': [
            'Over 0.5 HT (%)',
        ],
        "startIndex": 0,
    },
    "Jogos Over 1.5 no HT": {
        'fields': [
            'Over 1.5 HT (%)',
        ],
        "startIndex": 0,
    },
    "Jogos Over 0.5 no 2T": {
        'fields': [
            'Over 0.5 2T (%)',
        ],
        "startIndex": 0,
    },
    "Jogos Over 1.5 no 2T": {
        'fields': [
            'Over 1.5 2T (%)',
        ],
        "startIndex": 0,
    },
    "Jogos Over 0.5 no FT": {
        'fields': [
            'Over 0.5 FT (%)',
        ],
        "startIndex": 0,
    },
    "Jogos Over 1.5 no FT": {
        'fields': [
            'Over 1.5 FT (%)',
        ],
        "startIndex": 0,
    },
    "Jogos Over 2.5 no FT": {
        'fields': [
            'Over 2.5 FT (%)',
        ],
        "startIndex": 0,
    },
    "Jogos Over 3.5 no FT": {
        'fields': [
            'Over 3.5 FT (%)',
        ],
        "startIndex": 0,
    },
    # ----------------------------------------------------
    # 1º Gol
    'Jogos marcou o primeiro gol no HT': {
        'fields': [
            'Marcou o PG no HT (%)',
            'Marcou o PG no HT e Venceu (%)',
            'Marcou o PG no HT e Empatou (%)',
            'Marcou o PG no HT e Perdeu (%)',
        ],
        "startIndex": 0,
    },
    'Jogos sofreu o primeiro gol no HT': {
        'fields': [
            'Sofreu o PG no HT (%)',
            'Sofreu o PG no HT e Venceu (%)',
            'Sofreu o PG no HT e Empatou (%)',
            'Sofreu o PG no HT e Perdeu (%)',
        ],
        "startIndex": 0,
    },
    'Jogos marcou o primeiro gol no 2T': {
        'fields': [
            'Marcou o PG no 2T (%)',
            'Marcou o PG no 2T e Venceu (%)',
            'Marcou o PG no 2T e Empatou (%)',
            'Marcou o PG no 2T e Perdeu (%)',
        ],
        "startIndex": 0,
    },
    'Jogos sofreu o primeiro gol no 2T': {
        'fields': [
            'Sofreu o PG no 2T (%)',
            'Sofreu o PG no 2T e Venceu (%)',
            'Sofreu o PG no 2T e Empatou (%)',
            'Sofreu o PG no 2T e Perdeu (%)',
        ],
        "startIndex": 0,
    },
    'Jogos marcou o primeiro gol no FT': {
        'fields': [
            'Marcou o PG no FT (%)',
            'Marcou o PG no FT e Venceu (%)',
            'Marcou o PG no FT e Empatou (%)',
            'Marcou o PG no FT e Perdeu (%)',
        ],
        "startIndex": 0,
    },
    'Jogos sofreu o primeiro gol no FT': {
        'fields': [
            'Sofreu o PG no FT (%)',
            'Sofreu o PG no FT e Venceu (%)',
            'Sofreu o PG no FT e Empatou (%)',
            'Sofreu o PG no FT e Perdeu (%)',
        ],
        "startIndex": 0,
    },
    # ----------------------------------------------------
    # + 2 Gols
    "Jogos vencendo 2 gols diferença": {
        'fields': [
            'Vencendo por 2 Gols de diferença (%)',
            'Vencendo por 2 Gols de diferença e Marcou Gol (%)',
            'Vencendo por 2 Gols de diferença e Sofreu Gol (%)',
        ],
        "startIndex": 0,
    },
    "Jogos perdendo 2 gols diferença": {
        'fields': [
            'Perdendo por 2 Gols de diferença (%)',
            'Perdendo por 2 Gols de diferença e Marcou Gol (%)',
            'Perdendo por 2 Gols de diferença e Sofreu Gol (%)',
        ],
        "startIndex": 0,
    },
    "Jogos marcou o primeiro e o segundo gol no HT": {
        'fields': [
            'Marcou o PG e SG no HT (%)',
            'Marcou o PG e SG no HT e Venceu (%)',
            'Marcou o PG e SG no HT e Empatou (%)',
            'Marcou o PG e SG no HT e Perdeu (%)',
        ],
        "startIndex": 0,
    },
    "Jogos sofreu o primeiro e o segundo gol no HT": {
        'fields': [
            'Sofreu o PG e SG no HT (%)',
            'Sofreu o PG e SG no HT e Venceu (%)',
            'Sofreu o PG e SG no HT e Empatou (%)',
            'Sofreu o PG e SG no HT e Perdeu (%)',
        ],
        "startIndex": 0,
    },
    "Jogos marcou o primeiro e o segundo gol no 2T": {
        'fields': [
            'Marcou o PG e SG no 2T (%)',
            'Marcou o PG e SG no 2T e Venceu (%)',
            'Marcou o PG e SG no 2T e Empatou (%)',
            'Marcou o PG e SG no 2T e Perdeu (%)',
        ],
        "startIndex": 0,
    },
    "Jogos sofreu o primeiro e o segundo gol no 2T": {
        'fields': [
            'Sofreu o PG e SG no 2T (%)',
            'Sofreu o PG e SG no 2T e Venceu (%)',
            'Sofreu o PG e SG no 2T e Empatou (%)',
            'Sofreu o PG e SG no 2T e Perdeu (%)',
        ],
        "startIndex": 0,
    },
    "Jogos marcou o primeiro e o segundo gol no FT": {
        'fields': [
            'Marcou o PG e SG no FT (%)',
            'Marcou o PG e SG no FT e Venceu (%)',
            'Marcou o PG e SG no FT e Empatou (%)',
            'Marcou o PG e SG no FT e Perdeu (%)',
        ],
        "startIndex": 0,
    },
    "Jogos sofreu o primeiro e o segundo gol no FT": {
        'fields': [
            'Sofreu o PG e SG no FT (%)',
            'Sofreu o PG e SG no FT e Venceu (%)',
            'Sofreu o PG e SG no FT e Empatou (%)',
            'Sofreu o PG e SG no FT e Perdeu (%)',
        ],
        "startIndex": 0,
    },

}

class Reading():
    printHeader = False

    def __init__(self, driver: DriverInterface, typeReadings: list, statReadings: list) -> None:
        self.driver = driver
        self.actions = DriverActions(self.driver)
        self.typeReadings = typeReadings
        self.statReadings = statReadings

        self.filename = ""

        self.featured = None;
        self.measurements = []
        self.stats = {}

    def getReadingIdentifier(self, match: str, size: str):
        return slug_name(f"{match}_{size}")

    def saveContent(self, filename: str, content: str):
        file = open(f"{filename}.txt", "a", encoding="utf-8")
        file.write(f"{content}\n")
        file.close()
        file = None

    def readFeaturedInfo(self, ):
        if self.featured: return;
        self.featured = {
            "Data": None,
            "Hora": None,
            "Pais": None,
            "Liga": None,
            "Casa": None,
            "Fora": None,
            "Casa HT": -1,
            "Fora HT": -1,
            "Casa FT": -1,
            "Fora FT": -1,
            "Odd Casa": 1,
            "Odd Empate": 1,
            "Odd Fora": 1,
            "Odd Under 0.5 HT": 1,
            "Odd Under 0.5 FT": 1,
            "Odd Under 1.5 FT": 1,
            "Odd Under 2.5 FT": 1,
            "Odd Não Ambas": 1,
            "Odd Over 0.5 HT": 1,
            "Odd Over 0.5 FT": 1,
            "Odd Over 1.5 FT": 1,
            "Odd Over 2.5 FT": 1,
            "Odd Ambas": 1,
            "Casa LG Score": -1,
            "H Score": -1,
            "Fora LG Score": -1,
        }

        # ---------------------------------------------------------------
        # Pegando o nome do time da casa

        hometeamXpath = getInfoXpath("/div/div[@role='grid']/div[1]//p")
        hometeam = self.actions.get_text(hometeamXpath)
        # print(f"hometeam: {hometeam}")
        self.featured['Casa'] = hometeam

        # ---------------------------------------------------------------
        # Pegando o nome do time de fora

        awayteamXpath = getInfoXpath("/div/div[@role='grid']/div[3]//p")
        awayteam = self.actions.get_text(awayteamXpath)
        # print(f"awayteam: {awayteam}")
        self.featured['Fora'] = awayteam

        # ---------------------------------------------------------------
        # Pegando a data

        date = self.actions.get_text("(//*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div/div/div[@role='grid']/div[2]/div//p)[1]")
        if date:
            # print(f"date: {date}")
            self.featured['Data'] = date

        time = self.actions.get_text("(//*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div/div/div[@role='grid']/div[2]/div//p)[2]")
        if time:
            # print(f"time: {time}")
            self.featured['Hora'] = time

        league = self.actions.get_text("(//*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div/div/div[@role='grid']/div[2]/div//p)[3]")
        country = None
        match = re.search(r"(.*?)\s*\((.*)\)", str(league))
        if match:
            league = match.group(1)
            country = match.group(2)
            # print(f"league: {league}")
            self.featured['Liga'] = league
            # print(f"country: {country}")
            self.featured['Pais'] = country
        

        # ---------------------------------------------------------------
        # Pegando o placar do time da casa

        hometeamScoreFTXpath = getInfoXpath("/div/div[@role='grid']/div[2]/div[2]/div[1]//p[1]")
        if self.actions.has_element(hometeamScoreFTXpath, time=0):
            hometeamScoreFT = self.actions.get_text(hometeamScoreFTXpath)
            if not hometeamScoreFT is None: 
                hometeamScoreFT = int(hometeamScoreFT)
                # print(f"hometeamScoreFT: {hometeamScoreFT}")
                self.featured['Casa FT'] = hometeamScoreFT

        hometeamScoreHTXpath = getInfoXpath("/div/div[@role='grid']/div[2]/div[2]/div[1]//p[2]")
        if self.actions.has_element(hometeamScoreHTXpath, time=0):
            hometeamScoreHT = self.actions.get_text(hometeamScoreHTXpath)
            match = re.search(r"(\d+)", hometeamScoreHT)
            if match:
                hometeamScoreHT = int(match.group(1))
                # print(f"hometeamScoreHT: {hometeamScoreHT}")
                self.featured['Casa HT'] = hometeamScoreHT

        # ---------------------------------------------------------------
        # Pegando o placar do time de fora

        awayteamScoreFTXpath = getInfoXpath("/div/div[@role='grid']/div[2]/div[2]/div[2]//p[2]")
        if self.actions.has_element(awayteamScoreFTXpath, time=0):
            awayteamScoreFT = self.actions.get_text(awayteamScoreFTXpath)
            if not awayteamScoreFT is None: 
                awayteamScoreFT = int(awayteamScoreFT)
                # print(f"awayteamScoreFT: {awayteamScoreFT}")
                self.featured['Fora FT'] = awayteamScoreFT

        awayteamScoreHTXpath = getInfoXpath("/div/div[@role='grid']/div[2]/div[2]/div[2]//p[1]")
        if self.actions.has_element(awayteamScoreHTXpath, time=0):
            awayteamScoreHT = self.actions.get_text(awayteamScoreHTXpath)
            match = re.search(r"(\d+)", awayteamScoreHT)
            if match:
                awayteamScoreHT = int(match.group(1))
                self.featured['Fora HT'] = awayteamScoreHT
                # print(f"awayteamScoreHT: {awayteamScoreHT}")

        # ---------------------------------------------------------------
        # Pegando as odds

        if self.actions.has_element("//button[text()='Ver mais odds']", time=0):
            self.actions.click_element("//button[text()='Ver mais odds']")
            self.actions.sleep(1)

        oddsEl = getInfoXpath("/div/div[@role='grid']/div[4]//span")
        oddsEls = self.actions.get_elements(oddsEl)
        odds = [self.actions.get_text(x) for x in oddsEls]
        mapOdd = [
            "Odd Casa",
            "Odd Empate",
            "Odd Fora",
            "Odd Under 0.5 HT",
            "Odd Under 0.5 FT",
            "Odd Under 1.5 FT",
            "Odd Under 2.5 FT",
            "Odd Não Ambas",
            "Odd Over 0.5 HT",
            "Odd Over 0.5 FT",
            "Odd Over 1.5 FT",
            "Odd Over 2.5 FT",
            "Odd Ambas",
        ]
        for index, odd in enumerate(odds):
            if odd == '' or odd is None: odd = 1
            odd = float(odd)
            if odd <= 1: odd = 1
            # print(f"\t{mapOdd[index]}: {odd}")
            self.featured[mapOdd[index]] = odd

        # ---------------------------------------------------------------
        # Pegando o LG Score da casa
            
        homeLGScore = -1
        HScore = -1
        awayLGScore = -1
        
        try:
            homeLGScoreXpath = "(//*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div/div/div[@role='grid']/div[5]//p)[1]"
            homeLGScore = self.actions.get_text(homeLGScoreXpath, time=0)
            match = re.search(r"(\d+)", homeLGScore)
            if match:
                homeLGScore = int(match.group(1))
            else:
                homeLGScore = -1
        except ValueError:
            pass
        # print(f"homeLGScore: {homeLGScore}")
        self.featured["Casa LG Score"] = homeLGScore

        # ---------------------------------------------------------------
        # Pegando o H-Score

        try:
            HScoreXpath = "(//*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div/div/div[@role='grid']/div[6]//p)[1]"
            HScore = self.actions.get_text(HScoreXpath, time=0)
            match = re.search(r"(\d+)", HScore)
            if match:
                HScore = int(match.group(1))
            else:
                HScore = -1
        except ValueError:
            pass
        # print(f"HScore: {HScore}")
        self.featured["H Score"] = HScore

        # ---------------------------------------------------------------
        # Pegando o LG Score de fora
        
        try:
            awayLGScoreXpath = "(//*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div/div/div[@role='grid']/div[7]//p)[1]"
            awayLGScore = self.actions.get_text(awayLGScoreXpath, time=0)
            match = re.search(r"(\d+)", awayLGScore)
            if match:
                awayLGScore = int(match.group(1))
            else:
                awayLGScore = -1
        except ValueError:
            pass
        self.featured["Fora LG Score"] = awayLGScore

    def printFeaturedInfo(self, ):
        print("-"*50)
        print("\tDados principais da partida:")
        print(f"\tData: {self.featured['Data']} às {self.featured['Hora']}")
        print(f"\tPais: {self.featured['Pais']} / Liga: {self.featured['Liga']}")
        print(f"\tPartida: {self.featured['Casa']} x {self.featured['Fora']}")
        print(f"\tPlacar HT: {self.featured['Casa HT']} x {self.featured['Fora HT']}")
        print(f"\tPlacar FT: {self.featured['Casa FT']} x {self.featured['Fora FT']}")
        print(f"\tLG-Score Casa: {self.featured['Casa LG Score']} / H-Score: {self.featured['H Score']} / LG-Score Fora: {self.featured['Fora LG Score']}")
        print(f"\tMatch Odds: {self.featured['Odd Casa']} / {self.featured['Odd Empate']} / {self.featured['Odd Fora']}")
        print(f"\tOdds 0.5 HT: {self.featured['Odd Under 0.5 HT']} / {self.featured['Odd Over 0.5 HT']}")
        print(f"\tOdds 0.5 FT: {self.featured['Odd Under 0.5 FT']} / {self.featured['Odd Over 0.5 FT']}")
        print(f"\tOdds 1.5 FT: {self.featured['Odd Under 1.5 FT']} / {self.featured['Odd Over 1.5 FT']}")
        print(f"\tOdds 2.5 FT: {self.featured['Odd Under 2.5 FT']} / {self.featured['Odd Over 2.5 FT']}")
        print(f"\tOdds Ambas: {self.featured['Odd Não Ambas']} / {self.featured['Odd Ambas']}")

    def selectTabButton(self, tabButtonsXPath: str, tabName: str):
        print(f">> selectTabButton:")
        print(f"tabButtonsXPath: {tabButtonsXPath}")
        print(f"tabName: {tabName}")
        elements = []
        try:
            elements = self.actions.get_elements(tabButtonsXPath, time=5)
        except ValueError:
            input(f"Ocorreu um erro na leitura dos botões da aba de '{tabName}', verifique o que pode ter causado...")
        if len(elements) <= 0: return False
        tabSlug = slug_name(tabName)
        tabNames = [slug_name(self.actions.get_text(x)) for x in elements]
        tabIndex = [int(self.actions.get_attr(x, 'tabindex')) for x in elements]
        for index, tab in enumerate(tabNames):
            if tabSlug == tab:
                if tabIndex[index] < 0:
                    xpath = f"({tabButtonsXPath})[{index+1}]"
                    def run(): 
                        self.actions.click_element(xpath, time=0)
                    if not self.actions.changes_attribute_element(
                        xpath,
                        run,
                        'tabindex'
                    ):
                        raise ActionError(f"Não foi selecionado corretamente a aba '{tabName}'")
                    return True
        return False

    def selectMatchesTab(self, tabName = '5 jogos'):
        tabButtonsXPath = "(((//*[@id='__next']/section/div[2]/div[2]/div/div/div/div)[3]/div/div)[2]//div[@role='tablist'])[1]/button"
        self.selectTabButton(tabButtonsXPath, tabName)

    def selectStatTab(self, tabName = 'Custo do gol'):
        tabButtonsXPath = "(((//*[@id='__next']/section/div[2]/div[2]/div/div/div/div)[3]/div/div)[2]//div[@role='tablist'])[2]/button"
        self.selectTabButton(tabButtonsXPath, tabName)

    def selectSizeTab(self, tabName = 'Casa/Visitante'):
        tabButtonsXPath = "(((//*[@id='__next']/section/div[2]/div[2]/div/div/div/div)[3]/div/div)[2]//div[@role='tablist'])[3]/button"
        self.selectTabButton(tabButtonsXPath, tabName)

    def changeTabConfig(self, matchTab = '5 jogos', statTab = 'Custo do gol', sizeTab = 'Casa/Visitante'):
        self.selectSizeTab(sizeTab)
        self.selectStatTab(statTab)
        self.selectMatchesTab(matchTab)

    def changeReading(self, matchTab = '5 jogos', sizeTab = 'Casa/Visitante'):
        self.selectSizeTab(sizeTab)
        self.selectMatchesTab(matchTab)

    def setMeasurementsA(self, statTab: str):
        attempts = 60
        while attempts > 0:
            attempts = attempts - 1
            if attempts <= 0: raise ActionError(f"Ocorreu um erro de abertura da estatistica '{statTab}'")
            self.actions.sleep(0.5)
            rowsEl = []
            try:
                rowsEl = self.actions.get_elements(f"{MEASUREMENTS_GROUP_A_XPATH}/div[1]/div[2]/p", time=0)
            except Exception:
                # raise ActionError("Não foram encontrados as medições")
                input("Não foram encontrados as medições...")
                # continue;
            self.measurements = [default_space(self.actions.get_text(x)) for x in rowsEl]
            print(f"self.measurements: {self.measurements}")
            break;
    
    def setMeasurementsB(self, statTab: str):
        attempts = 60
        while attempts > 0:
            attempts = attempts - 1
            if attempts <= 0: raise ActionError(f"Ocorreu um erro de abertura da estatistica '{statTab}'")
            self.actions.sleep(0.5)
            rowsEl = []
            try:
                rowsEl = self.actions.get_elements(f"{MEASUREMENTS_GROUP_B_XPATH}/div[2]/p", time=0)
            except Exception:
                # raise ActionError("Não foram encontrados as medições")
                input("Não foram encontrados as medições...")
                # continue;
            self.measurements = [default_space(self.actions.get_text(x)) for x in rowsEl]
            print(f"self.measurements: {self.measurements}")
            break;

    def setStat(self, match: str, size: str):
        readingId = self.getReadingIdentifier(match, size)
        if readingId not in self.stats:
            self.stats[readingId] = {
                # ----------------------------------------------------
                # Médias e Dispersões
                'Média Custo do Gol (1.0)': None,
                'Média Custo do Gol (2.0)': None,
                'Gols marcados no HT': None,
                'Gols sofridos no HT': None,
                'Gols marcados no 2T': None,
                'Gols sofridos no 2T': None,
                'Gols marcados no FT': None,
                'Gols sofridos no FT': None,
                # ----------------------------------------------------
                # 1º Gol
                "Jogos marcou o primeiro gol no HT": None,
                "Jogos sofreu o primeiro gol no HT": None,
                "Jogos marcou o primeiro gol no 2T": None,
                "Jogos sofreu o primeiro gol no 2T": None,
                "Jogos marcou o primeiro gol no FT": None,
                "Jogos sofreu o primeiro gol no FT": None,
                # ----------------------------------------------------
                # + 2 Gols
                "Jogos vencendo 2 gols diferença": None,
                "Jogos perdendo 2 gols diferença": None,
                "Jogos marcou o primeiro e o segundo gol no HT": None,
                "Jogos sofreu o primeiro e o segundo gol no HT": None,
                "Jogos marcou o primeiro e o segundo gol no 2T": None,
                "Jogos sofreu o primeiro e o segundo gol no 2T": None,
                "Jogos marcou o primeiro e o segundo gol no FT": None,
                "Jogos sofreu o primeiro e o segundo gol no FT": None,
                # ----------------------------------------------------
                # Over
                "Jogos Over 0.5 no HT": None,
                "Jogos Over 1.5 no HT": None,
                "Jogos Over 0.5 no 2T": None,
                "Jogos Over 1.5 no 2T": None,
                "Jogos Over 0.5 no FT": None,
                "Jogos Over 1.5 no FT": None,
                "Jogos Over 2.5 no FT": None,
                "Jogos Over 3.5 no FT": None,
            }
   
    def readStats(self, match: str, size: str, stat: str):
        readingId = self.getReadingIdentifier(match, size)
        if stat in [
            'Custo do gol',
            'Médias e Dispersões',
            '1º Gol',
            '+ 2 Gols',
        ]:
            self.setMeasurementsA(stat)
        elif stat in [
            'Over',
        ]:
            self.setMeasurementsB(stat)
        self.readStatsGroupA(readingId, self.measurements, stat)

    def readStatsData(self, measument_xpath: str, position: int):
        print(f">> readStatsData:")
        measurementXPath = f"({measument_xpath})[{position}]"
        dataMeasurementXPath = f"{measurementXPath}//p"
        print(f"dataMeasurementXPath: {dataMeasurementXPath}")
        rowsEl = self.actions.get_elements(dataMeasurementXPath, time=0)
        return [default_space(self.actions.get_text(x)) for x in rowsEl]
            
    def readStatsGroupA(self, readingId: str, measurements: list, stat: str):
        # input("Esperando para começar a ler as estatisticas do grupo...")
        # print(f">> readStatsGroupA:")
        # print(f"readingId: {readingId}")
        # print(f"measurements: {measurements}")
        # print(f"self.stats: {self.stats}")
        stats = self.stats[readingId]
        
        if stat in [
            'Custo do gol',
            'Médias e Dispersões',
            '1º Gol',
            '+ 2 Gols',
        ]:
            searchData = lambda position: self. readStatsData(MEASUREMENTS_GROUP_A_XPATH, position)
        elif stat in [
            'Over',
        ]:
            searchData = lambda position: self. readStatsData(MEASUREMENTS_GROUP_B_XPATH, position)

        for index, measurement in enumerate(measurements):
            print("***"*50)
            if measurement not in STATS: 
                print(f"A estatística '{measurement}' foi ignorada...")
                continue;
            if measurement not in stats:
                print(f"A estatística '{measurement}' não configurada, foi ignorada...")
                continue;
            if stats[measurement]: return;
        
            allData = searchData(index + 1)
            print(f"allData: {allData}")

            homeData = [x for i, x in enumerate(allData) if (i+1) % 3 == 1]
            awayData = [x for i, x in enumerate(allData) if (i+1) % 3 == 0]
            print(f"homeData: {homeData}")
            print(f"awayData: {awayData}")

            statFields = STATS[measurement]["fields"]
            statHome = [f"Casa - {x}" for x in statFields]
            statAway = [f"Fora - {x}" for x in statFields]
            print(f"statHome: {statHome}")
            print(f"statAway: {statAway}")

            home = []
            away = []

            for data in homeData:
                # print(f"\thomeData: {data}")
                match = re.search(r"^\s*(\d+|\d+\.\d+)\s*$", data)
                if match: 
                    home.append(float(match.group(1)))
                    continue;

                match = re.search(r"^\s*\d+\s*\(\s*(\d+|\d+\.\d+)\s*%\s*\)\s*$", data)
                if match: 
                    home.append(round(float(match.group(1))/100, 4))
                    continue;
                
                if data == '':
                    home.append(-1)
                    continue

                raise StatReadingError(f"A leitura não identificou a estatística '{measurement}' no lado da casa")

            for data in awayData:
                # print(f"\tawayData: {data}")
                match = re.search(r"^\s*(\d+|\d+\.\d+)\s*$", data)
                if match: 
                    away.append(float(match.group(1)))
                    continue;

                match = re.search(r"^\s*\d+\s*\(\s*(\d+|\d+\.\d+)\s*%\s*\)\s*$", data)
                if match: 
                    away.append(round(float(match.group(1))/100, 4))
                    continue;
                
                if data == '':
                    away.append(-1)
                    continue

                raise StatReadingError(f"A leitura não identificou a estatística '{measurement}' no lado do visitante")

            print(f"home: {home}")
            print(f"away: {away}")

            statInfoHome = []
            for i, stat in enumerate(statHome):
                statInfoHome.append((stat, home[i]))

            statInfoAway = []
            for i, stat in enumerate(statAway):
                statInfoAway.append((stat, away[i]))

            stats[measurement] = {
                "home": statInfoHome,
                "away": statInfoAway,
            }

        self.stats[readingId] = stats

    def getHeader(self, ):
        headers = [*FEATURED]
        for stat in STATS:
            fields = STATS[stat]["fields"]
            for field in fields:
                headers.append(f"Casa - {field}")
                headers.append(f"Fora - {field}")
        return headers

    def getData(self, ):
        if not self.featured: raise ValueError("Não foi lido os dados de destaque da partida");
        values = []
        readingId = self.getReadingIdentifier(self.match, self.size)
        data = {}
        for feat in FEATURED:
            data[feat] = self.featured[feat]

        if readingId not in self.stats: raise ValueError(f"As estatísticas para '{self.match}' e '{self.size}' não foram lidas");
        
        statsRead = self.stats[readingId]

        homeStats = {}
        awayStats = {}

        for stat in STATS:
            if statsRead[stat]:
                for statHome, valueHome in statsRead[stat]["home"]:
                    homeStats[statHome] = valueHome
                for statAway, valueAway in statsRead[stat]["away"]:
                    awayStats[statAway] = valueAway
            else:
                fields = STATS[stat]["fields"]
                for field in fields:
                    homeStats[f"Casa - {field}"] = -1
                    awayStats[f"Fora - {field}"] = -1

        for stat in homeStats:
            data[stat] = homeStats[stat]

        for stat in awayStats:
            data[stat] = awayStats[stat]

        headers = self.getHeader()
        values = []
        for header in headers:
            if header not in data: raise ValueError(f"Não foi encontrado a estatística '{header}' para compor a lista de valores")
            values.append(data[header])

        return values;

    def getContentHeader(self, ):
        return "\t".join(self.getHeader())
    
    def getContentData(self, ):
        return "\t".join([str(x) for x in self.getData()])

    def saveHeader(self, ):
        self.saveContent(self.filename_header, self.getContentHeader())

    def saveData(self, ):
        self.saveContent(self.filename, self.getContentData())

    def execute(self, ):
        # Reading.hasHeaderSaved = False
        # print("---------------------------------")
        # input("Esperando para ler a proxima partida...")
        self.readFeaturedInfo()
        for match, size in self.typeReadings:
            self.match = match
            self.size = size
            print("---------------------------------")
            self.printFeaturedInfo()
            print("\n")
            print(f"\tmatch: {match} / size: {size}")
            readingId = self.getReadingIdentifier(match, size)
            print(f"\treadingId: {readingId}")
            self.filename = f"{readingId}_statistics"
            self.filename_header = f"headers"
            print(f"\tself.filename: {self.filename}")
            self.setStat(match, size)
            self.changeReading(match, size)
            for stat in self.statReadings:
                print(f"\tstat: {stat}")
                self.selectStatTab(stat)
                self.readStats(match, size, stat)

            # TODO: Salvar toda a lista de estatistica lida

            if not Reading.printHeader:
                self.saveHeader()
                Reading.printHeader = True

            print("="*80)
            data = self.getData()
            print(f"data: {data}")

            self.saveData()


