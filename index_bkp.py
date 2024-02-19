from Library_v1.Driver.ChromeDriver import ChromeDriver
from Library_v1.Driver.DriverActions import DriverActions
import re

from Library_v1.Utils.string import (
    slug_name,
    default_space,
)

from Exceptions.StatReadingError import StatReadingError
from Exceptions.StatNotFoundError import StatNotFoundError
from Exceptions.StatWritingError import StatWritingError

STATS_BY_TAB = {
    # ---------------------------------------------------------
    # CASE Médias e Dispersões
    'Médias e Dispersões': {
        'Média Custo do Gol (1.0)': {
            "home": [
                {
                    "column": 'Casa - Média Custo do Gol (1.0)',
                    "value": -1,
                },
                {
                    "column": 'Casa - CV Custo do Gol (1.0)',
                    "value": -1,
                },
            ],
            "away": [
                {
                    "column": 'Fora - Média Custo do Gol (1.0)',
                    "value": -1,
                },
                {
                    "column": 'Fora - CV Custo do Gol (1.0)',
                    "value": -1,
                },
            ]
        },
        'Média Custo do Gol (2.0)': {
            "home": [
                {
                    "column": 'Casa - Média Custo do Gol (2.0)',
                    "value": -1,
                },
                {
                    "column": 'Casa - CV Custo do Gol (2.0)',
                    "value": -1,
                },
            ],
            "away": [
                {
                    "column": 'Fora - Média Custo do Gol (2.0)',
                    "value": -1,
                },
                {
                    "column": 'Fora - CV Custo do Gol (2.0)',
                    "value": -1,
                },
            ]
        },
        'Gols marcados no HT': {
            "home": [
                {
                    "column": 'Casa - Gols marcados no HT',
                    "value": -1,
                },
                {
                    "column": 'Casa - CV Gols marcados no HT',
                    "value": -1,
                },
            ],
            "away": [
                {
                    "column": 'Fora - Gols marcados no HT',
                    "value": -1,
                },
                {
                    "column": 'Fora - CV Gols marcados no HT',
                    "value": -1,
                },
            ]
        },
        'Gols sofridos no HT': {
            "home": [
                {
                    "column": 'Casa - Gols sofridos no HT',
                    "value": -1,
                },
                {
                    "column": 'Casa - CV Gols sofridos no HT',
                    "value": -1,
                },
            ],
            "away": [
                {
                    "column": 'Fora - Gols sofridos no HT',
                    "value": -1,
                },
                {
                    "column": 'Fora - CV Gols sofridos no HT',
                    "value": -1,
                },
            ]
        },
        'Gols marcados no 2T': {
            "home": [
                {
                    "column": 'Casa - Gols marcados no 2T',
                    "value": -1,
                },
                {
                    "column": 'Casa - CV Gols marcados no 2T',
                    "value": -1,
                },
            ],
            "away": [
                {
                    "column": 'Fora - Gols marcados no 2T',
                    "value": -1,
                },
                {
                    "column": 'Fora - CV Gols marcados no 2T',
                    "value": -1,
                },
            ]
        },
        'Gols sofridos no 2T': {
            "home": [
                {
                    "column": 'Casa - Gols sofridos no 2T',
                    "value": -1,
                },
                {
                    "column": 'Casa - CV Gols sofridos no 2T',
                    "value": -1,
                },
            ],
            "away": [
                {
                    "column": 'Fora - Gols sofridos no 2T',
                    "value": -1,
                },
                {
                    "column": 'Fora - CV Gols sofridos no 2T',
                    "value": -1,
                },
            ]
        },
        'Gols marcados no FT': {
            "home": [
                {
                    "column": 'Casa - Gols marcados no FT',
                    "value": -1,
                },
                {
                    "column": 'Casa - CV Gols marcados no FT',
                    "value": -1,
                },
            ],
            "away": [
                {
                    "column": 'Fora - Gols marcados no FT',
                    "value": -1,
                },
                {
                    "column": 'Fora - CV Gols marcados no FT',
                    "value": -1,
                },
            ]
        },
        'Gols sofridos no FT': {
            "home": [
                {
                    "column": 'Casa - Gols sofridos no FT',
                    "value": -1,
                },
                {
                    "column": 'Casa - CV Gols sofridos no FT',
                    "value": -1,
                },
            ],
            "away": [
                {
                    "column": 'Fora - Gols sofridos no FT',
                    "value": -1,
                },
                {
                    "column": 'Fora - CV Gols sofridos no FT',
                    "value": -1,
                },
            ]
        },
    },
    # ---------------------------------------------------------
    # CASE 1º Gol
    '1º Gol': {
        'Jogos marcou o primeiro gol no HT': {
            "home": [
                {
                    "column": 'Casa - Jogos marcou o primeiro gol no HT',
                    "value": -1,
                },
                {
                    "column": 'Casa - Jogos marcou o primeiro gol no HT e Venceu',
                    "value": -1,
                },
                {
                    "column": 'Casa - Jogos marcou o primeiro gol no HT e Empatou',
                    "value": -1,
                },
                {
                    "column": 'Casa - Jogos marcou o primeiro gol no HT e Perdeu',
                    "value": -1,
                },
            ],
            "away": [
                {
                    "column": 'Fora - Jogos marcou o primeiro gol no HT',
                    "value": -1,
                },
                {
                    "column": 'Fora - Jogos marcou o primeiro gol no HT e Venceu',
                    "value": -1,
                },
                {
                    "column": 'Fora - Jogos marcou o primeiro gol no HT e Empatou',
                    "value": -1,
                },
                {
                    "column": 'Fora - Jogos marcou o primeiro gol no HT e Perdeu',
                    "value": -1,
                },
            ]
        },
        'Jogos sofreu o primeiro gol no HT': {
            "home": [
                {
                    "column": 'Casa - Jogos sofreu o primeiro gol no HT',
                    "value": -1,
                },
                {
                    "column": 'Casa - Jogos sofreu o primeiro gol no HT e Venceu',
                    "value": -1,
                },
                {
                    "column": 'Casa - Jogos sofreu o primeiro gol no HT e Empatou',
                    "value": -1,
                },
                {
                    "column": 'Casa - Jogos sofreu o primeiro gol no HT e Perdeu',
                    "value": -1,
                },
            ],
            "away": [
                {
                    "column": 'Fora - Jogos sofreu o primeiro gol no HT',
                    "value": -1,
                },
                {
                    "column": 'Fora - Jogos sofreu o primeiro gol no HT e Venceu',
                    "value": -1,
                },
                {
                    "column": 'Fora - Jogos sofreu o primeiro gol no HT e Empatou',
                    "value": -1,
                },
                {
                    "column": 'Fora - Jogos sofreu o primeiro gol no HT e Perdeu',
                    "value": -1,
                },
            ]
        },
        'Jogos marcou o primeiro gol no 2T': {
            "home": [
                {
                    "column": 'Casa - Jogos marcou o primeiro gol no 2T',
                    "value": -1,
                },
                {
                    "column": 'Casa - Jogos marcou o primeiro gol no 2T e Venceu',
                    "value": -1,
                },
                {
                    "column": 'Casa - Jogos marcou o primeiro gol no 2T e Empatou',
                    "value": -1,
                },
                {
                    "column": 'Casa - Jogos marcou o primeiro gol no 2T e Perdeu',
                    "value": -1,
                },
            ],
            "away": [
                {
                    "column": 'Fora - Jogos marcou o primeiro gol no 2T',
                    "value": -1,
                },
                {
                    "column": 'Fora - Jogos marcou o primeiro gol no 2T e Venceu',
                    "value": -1,
                },
                {
                    "column": 'Fora - Jogos marcou o primeiro gol no 2T e Empatou',
                    "value": -1,
                },
                {
                    "column": 'Fora - Jogos marcou o primeiro gol no 2T e Perdeu',
                    "value": -1,
                },
            ]
        },
        'Jogos sofreu o primeiro gol no 2T': {
            "home": [
                {
                    "column": 'Casa - Jogos sofreu o primeiro gol no 2T',
                    "value": -1,
                },
                {
                    "column": 'Casa - Jogos sofreu o primeiro gol no 2T e Venceu',
                    "value": -1,
                },
                {
                    "column": 'Casa - Jogos sofreu o primeiro gol no 2T e Empatou',
                    "value": -1,
                },
                {
                    "column": 'Casa - Jogos sofreu o primeiro gol no 2T e Perdeu',
                    "value": -1,
                },
            ],
            "away": [
                {
                    "column": 'Fora - Jogos sofreu o primeiro gol no 2T',
                    "value": -1,
                },
                {
                    "column": 'Fora - Jogos sofreu o primeiro gol no 2T e Venceu',
                    "value": -1,
                },
                {
                    "column": 'Fora - Jogos sofreu o primeiro gol no 2T e Empatou',
                    "value": -1,
                },
                {
                    "column": 'Fora - Jogos sofreu o primeiro gol no 2T e Perdeu',
                    "value": -1,
                },
            ]
        },
        'Jogos marcou o primeiro gol no FT': {
            "home": [
                {
                    "column": 'Casa - Jogos marcou o primeiro gol no FT',
                    "value": -1,
                },
                {
                    "column": 'Casa - Jogos marcou o primeiro gol no FT e Venceu',
                    "value": -1,
                },
                {
                    "column": 'Casa - Jogos marcou o primeiro gol no FT e Empatou',
                    "value": -1,
                },
                {
                    "column": 'Casa - Jogos marcou o primeiro gol no FT e Perdeu',
                    "value": -1,
                },
            ],
            "away": [
                {
                    "column": 'Fora - Jogos marcou o primeiro gol no FT',
                    "value": -1,
                },
                {
                    "column": 'Fora - Jogos marcou o primeiro gol no FT e Venceu',
                    "value": -1,
                },
                {
                    "column": 'Fora - Jogos marcou o primeiro gol no FT e Empatou',
                    "value": -1,
                },
                {
                    "column": 'Fora - Jogos marcou o primeiro gol no FT e Perdeu',
                    "value": -1,
                },
            ]
        },
        'Jogos sofreu o primeiro gol no FT': {
            "home": [
                {
                    "column": 'Casa - Jogos sofreu o primeiro gol no FT',
                    "value": -1,
                },
                {
                    "column": 'Casa - Jogos sofreu o primeiro gol no FT e Venceu',
                    "value": -1,
                },
                {
                    "column": 'Casa - Jogos sofreu o primeiro gol no FT e Empatou',
                    "value": -1,
                },
                {
                    "column": 'Casa - Jogos sofreu o primeiro gol no FT e Perdeu',
                    "value": -1,
                },
            ],
            "away": [
                {
                    "column": 'Fora - Jogos sofreu o primeiro gol no FT',
                    "value": -1,
                },
                {
                    "column": 'Fora - Jogos sofreu o primeiro gol no FT e Venceu',
                    "value": -1,
                },
                {
                    "column": 'Fora - Jogos sofreu o primeiro gol no FT e Empatou',
                    "value": -1,
                },
                {
                    "column": 'Fora - Jogos sofreu o primeiro gol no FT e Perdeu',
                    "value": -1,
                },
            ]
        },
    },
}

c = ChromeDriver()
actions = DriverActions(c)


# ---------------------------------------------------------
# Logando na plataforma
actions.navigate_url("https://app.fulltradersports.com/login")
actions.clear_element("//input[@id='username']")
actions.write_element("//input[@id='username']", "brunojbatista@hotmail.com")
actions.clear_element("//input[@id='password']")
actions.write_element("//input[@id='password']", "BjNb88649137")
actions.sleep(1)
actions.click_element("//button[@type='submit']")

actions.sleep(10)

# ---------------------------------------------------------
# Navegar até os jogos
actions.navigate_url("https://app.fulltradersports.com/sherlock/matches")
actions.sleep(5)

# actions.sleep(3600)
# ---------------------------------------------------------
# Criar um laço no qual será lido os dados todos da partida

"""
    //*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div

    //*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div/div/div[@role='grid']/div[5]

    //*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div/div/div[@role='grid']/div[2]/div//p


    //div[./input[contains(@placeholder, 'Buscar por jogos')]]

    //*[./input[contains(@placeholder, 'Buscar por jogos')]]/div[3]//div[@data-selected]


    (//*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div/div)[2]/div[@role='tablist']/button

    (((//*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div/div)[2]/div/div)[1]/div/div/div)[2]/div/div

    (((//*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div/div)[2]/div/div)[1]/div/div/div)[2]/div/div/div[@role='tablist']
"""

BASE_XPATH = "//*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div"
getInfoXpath = lambda relativeXpath: f"{BASE_XPATH}{relativeXpath}"

def changeSideMatch(sideMatch = 'Casa/Visitante'):
    xpath = f"(((//*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div/div)[2]/div/div)[1]/div/div/div)[2]/div/div/div[@role='tablist']/button[text()='{sideMatch}']"
    ariaSelected = actions.get_attr(xpath, 'aria-selected', time=0)
    if ariaSelected == False or ariaSelected == 'false':
        actions.force_click_element(xpath)
        attemps = 60
        while attemps > 0:
            attemps = attemps - 1
            currentAriaSelected = actions.get_attr(xpath, 'aria-selected', time=0)
            if currentAriaSelected != ariaSelected: break;
            actions.sleep(0.5)
        if attemps <= 0: raise TimeoutError(f"O tempo de espera para abrir a aba '{sideMatch}'")
    actions.sleep(3)

def changeTotalMatch(totalMatch = '5 jogos'):
    xpath = f"(//*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div/div)[2]/div[@role='tablist']/button[text()='{totalMatch}']"
    ariaSelected = actions.get_attr(xpath, 'aria-selected', time=0)
    if ariaSelected == False or ariaSelected == 'false':
        actions.force_click_element(xpath)
        attemps = 60
        while attemps > 0:
            attemps = attemps - 1
            currentAriaSelected = actions.get_attr(xpath, 'aria-selected', time=0)
            if currentAriaSelected != ariaSelected: break;
            actions.sleep(0.5)
        if attemps <= 0: raise TimeoutError(f"O tempo de espera para abrir a aba '{totalMatch}'")
    actions.sleep(3)

def changeTabList(tabName = 'Custo do gol'):
    xpath = f"((((//*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div/div)[2]/div)[2]//div[@role='tablist'])[1])/button[text()='{tabName}']"
    ariaSelected = actions.get_attr(xpath, 'aria-selected', time=0)
    if ariaSelected == False or ariaSelected == 'false':
        actions.force_click_element(xpath, time=60)
        attemps = 60
        while attemps > 0:
            attemps = attemps - 1
            currentAriaSelected = actions.get_attr(xpath, 'aria-selected', time=0)
            if currentAriaSelected != ariaSelected: break;
            actions.sleep(0.5)
        if attemps <= 0: raise TimeoutError(f"O tempo de espera para abrir a aba '{tabName}'")
    actions.sleep(3)

def createStats():
    stats = {}
    for tabName in STATS_BY_TAB:
        tab = STATS_BY_TAB[tabName]
        for statName in tab:
            if statName not in stats:
                stats[statName] = tab[statName]
    return stats;

def readStats(statTabName: str = None, measurements: list = []):
    print(f">> readStats:")
    stats = {}

    def checkValue(value):
        if value == '' or value is None: return 0
        return float(value)
    
    # currentStats = STATS_BY_TAB[statTabName]
    ignored_case = [
        'Jogos de referência',
        'Média Match Odds FT',
    ]
    case_1 = [
        'Média Custo do Gol (1.0)',
        'Média Custo do Gol (2.0)',
    ]
    case_2 = [
        'Gols marcados no HT', 
        'Gols sofridos no HT', 
        'Gols marcados no 2T', 
        'Gols sofridos no 2T', 
        'Gols marcados no FT', 
        'Gols sofridos no FT',
    ]
    case_3 = [
        'Jogos marcou o primeiro gol no HT', 
        'Jogos sofreu o primeiro gol no HT', 
        'Jogos marcou o primeiro gol no 2T', 
        'Jogos sofreu o primeiro gol no 2T', 
        'Jogos marcou o primeiro gol no FT', 
        'Jogos sofreu o primeiro gol no FT'
    ]

    if len(measurements) <= 0: 
        return createStats()

    stats = STATS_BY_TAB[statTabName]
    for name in measurements:
        print(f"-"*50)
        xpath = f"((((//*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div/div)[2]/div/div)[1]/div/div/div)[2]/div/div/div[last()]/div/div/div/div[.//p[text()='{name}']])"
        rowsEls = actions.get_elements(f"({xpath}/div)", time=0)
        leftColumn = []
        middleColumn = []
        rightColumn = []
        for rowEl in rowsEls:
            textEls = actions.set_ref(rowEl).get_elements("./div//p")
            texts = [actions.get_text(x) for x in textEls]
            for textIndex, text in enumerate(texts):
                textPosition = textIndex + 1
                if textPosition % 3 == 1:
                    leftColumn.append(text)
                elif textPosition % 3 == 2:
                    middleColumn.append(text)
                elif textPosition % 3 == 0:
                    rightColumn.append(text)
        if len(middleColumn) <= 0: continue;
        group = middleColumn[0];

        print(f"-----------------------------------------")
        # input(f"Esperando para rodar a leitura de '{group}' ...")
        print(f"leftColumn: {leftColumn}")
        print(f"middleColumn: {middleColumn}")
        print(f"rightColumn: {rightColumn}")
        if group in ignored_case:
            continue;
        elif group in case_1:
            for indexColumn, value in enumerate(leftColumn):
                value = checkValue(value)
                print(f"\tvalue: {value}")
                stats[group]["home"][indexColumn]["value"] = value
            for indexColumn, value in enumerate(rightColumn):
                value = checkValue(value)
                print(f"\tvalue: {value}")
                stats[group]["away"][indexColumn]["value"] = value
        elif group in case_2:
            for indexColumn, value in enumerate(leftColumn[1:]):
                value = checkValue(value)
                print(f"\tvalue: {value}")
                stats[group]["home"][indexColumn]["value"] = value
            for indexColumn, value in enumerate(rightColumn[1:]):
                value = checkValue(value)
                print(f"\tvalue: {value}")
                stats[group]["away"][indexColumn]["value"] = value
        elif group in case_3:
            print("leftColumn:")
            for indexColumn, value in enumerate(leftColumn):
                print(f"value: {value}")
                match = re.search(r"(\d+)[^\d]*?\(\s*(\d+\.?\d*)\s*%\s*\)", str(value))
                if match:
                    percentage = match.group(2)
                    percentage = checkValue(percentage)
                    print(f"percentage - before: {percentage}")
                    if percentage > 0: percentage = round(percentage/100, 4)
                    print(f"percentage - after: {percentage}")
                    stats[group]["home"][indexColumn]["value"] = percentage
            print(f"stats[group]['home']: {stats[group]['home']}")

            print("rightColumn:")
            for indexColumn, value in enumerate(rightColumn):
                print(f"value: {value}")
                match = re.search(r"(\d+)[^\d]*?\(\s*(\d+\.?\d*)\s*%\s*\)", str(value))
                if match:
                    percentage = match.group(2)
                    percentage = checkValue(percentage)
                    print(f"percentage - before: {percentage}")
                    if percentage > 0: percentage = round(percentage/100, 4)
                    print(f"percentage - after: {percentage}")
                    stats[group]["away"][indexColumn]["value"] = percentage
        else:
            raise StatNotFoundError(f"Não foi encontrado a estatística '{group}'")

        print(f"stats[group]: {stats[group]}")

    return stats;

def mergeStats(statsRef, statsRelative):
    for statName in statsRelative:
        statsRef[statName] = statsRelative[statName]
    return statsRef

def getStatsName(statsConverted: list):
    return [x[0] for x in statsConverted]

def getStatsValue(statsConverted: list):
    return [x[1] for x in statsConverted]

def convertStats(stats: dict):
    print(f"stats: {stats}")
    print("==========================================================================")
    values = []
    for group in stats:
        for stat in stats[group]['home']:
            values.append((
                stat["column"],
                stat["value"]
            ))
        for stat in stats[group]['away']:
            values.append((
                stat["column"],
                stat["value"]
            ))
    return values;

def mergeData(data: dict, convertedStats: list):
    for stat, value in convertedStats:
        if stat not in data: raise StatWritingError(f"Não foi identificado '{stat}'")
        data[stat] = value
    return data;

def pushHomeAwayFile(content):
    file = open("matches_home_away.txt", "a", encoding="utf-8")
    file.write(content)
    file.close()

def pushGlobalFile(content):
    file = open("matches_global.txt", "a", encoding="utf-8")
    file.write(content)
    file.close()

def createDataStats(baseData: dict):
    return {
        **baseData,
        # --------------------------------------
        # Médias e Dispersões
        'Casa - Média Custo do Gol (1.0)': -1,
        'Casa - CV Custo do Gol (1.0)': -1,
        'Casa - Média Custo do Gol (2.0)': -1,
        'Casa - CV Custo do Gol (2.0)': -1,
        'Casa - Gols marcados no HT': -1,
        'Casa - CV Gols marcados no HT': -1,
        'Casa - Gols sofridos no HT': -1,
        'Casa - CV Gols sofridos no HT': -1,
        'Casa - Gols marcados no 2T': -1,
        'Casa - CV Gols marcados no 2T': -1,
        'Casa - Gols sofridos no 2T': -1,
        'Casa - CV Gols sofridos no 2T': -1,
        'Casa - Gols marcados no FT': -1,
        'Casa - CV Gols marcados no FT': -1,
        'Casa - Gols sofridos no FT': -1,
        'Casa - CV Gols sofridos no FT': -1,
        
        'Fora - Média Custo do Gol (1.0)': -1,
        'Fora - CV Custo do Gol (1.0)': -1,
        'Fora - Média Custo do Gol (2.0)': -1,
        'Fora - CV Custo do Gol (2.0)': -1,
        'Fora - Gols marcados no HT': -1,
        'Fora - CV Gols marcados no HT': -1,
        'Fora - Gols sofridos no HT': -1,
        'Fora - CV Gols sofridos no HT': -1,
        'Fora - Gols marcados no 2T': -1,
        'Fora - CV Gols marcados no 2T': -1,
        'Fora - Gols sofridos no 2T': -1,
        'Fora - CV Gols sofridos no 2T': -1,
        'Fora - Gols marcados no FT': -1,
        'Fora - CV Gols marcados no FT': -1,
        'Fora - Gols sofridos no FT': -1,
        'Fora - CV Gols sofridos no FT': -1,

        # --------------------------------------
        # 1º Gol
        'Casa - Jogos marcou o primeiro gol no HT': -1,
        'Casa - Jogos marcou o primeiro gol no HT e Venceu': -1,
        'Casa - Jogos marcou o primeiro gol no HT e Empatou': -1,
        'Casa - Jogos marcou o primeiro gol no HT e Perdeu': -1,
        'Casa - Jogos sofreu o primeiro gol no HT': -1,
        'Casa - Jogos sofreu o primeiro gol no HT e Venceu': -1,
        'Casa - Jogos sofreu o primeiro gol no HT e Empatou': -1,
        'Casa - Jogos sofreu o primeiro gol no HT e Perdeu': -1,
        'Casa - Jogos marcou o primeiro gol no 2T': -1,
        'Casa - Jogos marcou o primeiro gol no 2T e Venceu': -1,
        'Casa - Jogos marcou o primeiro gol no 2T e Empatou': -1,
        'Casa - Jogos marcou o primeiro gol no 2T e Perdeu': -1,
        'Casa - Jogos sofreu o primeiro gol no 2T': -1,
        'Casa - Jogos sofreu o primeiro gol no 2T e Venceu': -1,
        'Casa - Jogos sofreu o primeiro gol no 2T e Empatou': -1,
        'Casa - Jogos sofreu o primeiro gol no 2T e Perdeu': -1,
        'Casa - Jogos marcou o primeiro gol no FT': -1,
        'Casa - Jogos marcou o primeiro gol no FT e Venceu': -1,
        'Casa - Jogos marcou o primeiro gol no FT e Empatou': -1,
        'Casa - Jogos marcou o primeiro gol no FT e Perdeu': -1,
        'Casa - Jogos sofreu o primeiro gol no FT': -1,
        'Casa - Jogos sofreu o primeiro gol no FT e Venceu': -1,
        'Casa - Jogos sofreu o primeiro gol no FT e Empatou': -1,
        'Casa - Jogos sofreu o primeiro gol no FT e Perdeu': -1,

        'Fora - Jogos marcou o primeiro gol no HT': -1,
        'Fora - Jogos marcou o primeiro gol no HT e Venceu': -1,
        'Fora - Jogos marcou o primeiro gol no HT e Empatou': -1,
        'Fora - Jogos marcou o primeiro gol no HT e Perdeu': -1,
        'Fora - Jogos sofreu o primeiro gol no HT': -1,
        'Fora - Jogos sofreu o primeiro gol no HT e Venceu': -1,
        'Fora - Jogos sofreu o primeiro gol no HT e Empatou': -1,
        'Fora - Jogos sofreu o primeiro gol no HT e Perdeu': -1,
        'Fora - Jogos marcou o primeiro gol no 2T': -1,
        'Fora - Jogos marcou o primeiro gol no 2T e Venceu': -1,
        'Fora - Jogos marcou o primeiro gol no 2T e Empatou': -1,
        'Fora - Jogos marcou o primeiro gol no 2T e Perdeu': -1,
        'Fora - Jogos sofreu o primeiro gol no 2T': -1,
        'Fora - Jogos sofreu o primeiro gol no 2T e Venceu': -1,
        'Fora - Jogos sofreu o primeiro gol no 2T e Empatou': -1,
        'Fora - Jogos sofreu o primeiro gol no 2T e Perdeu': -1,
        'Fora - Jogos marcou o primeiro gol no FT': -1,
        'Fora - Jogos marcou o primeiro gol no FT e Venceu': -1,
        'Fora - Jogos marcou o primeiro gol no FT e Empatou': -1,
        'Fora - Jogos marcou o primeiro gol no FT e Perdeu': -1,
        'Fora - Jogos sofreu o primeiro gol no FT': -1,
        'Fora - Jogos sofreu o primeiro gol no FT e Venceu': -1,
        'Fora - Jogos sofreu o primeiro gol no FT e Empatou': -1,
        'Fora - Jogos sofreu o primeiro gol no FT e Perdeu': -1,
    }

# def mountStuct(data: dict)

def readMatch(): 
    line = None
    data = {
        "Casa": None,
        "Fora": None,
        "Data": None,
        "Hora": None,
        "Liga": None,
        "Pais": None,
        "Casa HT": -1,
        "Casa FT": -1,
        "Fora HT": -1,
        "Fora FT": -1,

        "Odd Casa": -1,
        "Odd Empate": -1,
        "Odd Fora": -1,
        "Odd Under 0.5 HT": -1,
        "Odd Under 0.5 FT": -1,
        "Odd Under 1.5 FT": -1,
        "Odd Under 2.5 FT": -1,
        "Odd Não Ambas": -1,
        "Odd Over 0.5 HT": -1,
        "Odd Over 0.5 FT": -1,
        "Odd Over 1.5 FT": -1,
        "Odd Over 2.5 FT": -1,
        "Odd Ambas": -1,

        "Casa LG Score": -1,
        "H Score": -1,
        "Fora LG Score": -1,
    }
    lineBaseData = []
    lineBaseDataHomeAway = []
    lineBaseDataGlobal = []
    
    input("Aperte qualquer tecla para continuar ler a próxima partida...")

    print(f"-"*80)
    # gridXpath = getInfoXpath("/div/div[@role='grid']")
    # gridEl = actions.get_element(gridXpath)

    # ---------------------------------------------------------------
    # Pegando o nome do time da casa

    hometeamXpath = getInfoXpath("/div/div[@role='grid']/div[1]//p")
    hometeam = actions.get_text(hometeamXpath)
    print(f"hometeam: {hometeam}")
    data['Casa'] = hometeam

    # ---------------------------------------------------------------
    # Pegando o nome do time de fora

    awayteamXpath = getInfoXpath("/div/div[@role='grid']/div[3]//p")
    awayteam = actions.get_text(awayteamXpath)
    print(f"awayteam: {awayteam}")
    data['Fora'] = awayteam

    # ---------------------------------------------------------------
    # Pegando a data

    date = actions.get_text("(//*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div/div/div[@role='grid']/div[2]/div//p)[1]")
    if date is None: date = ''
    print(f"date: {date}")
    data['Data'] = date

    time = actions.get_text("(//*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div/div/div[@role='grid']/div[2]/div//p)[2]")
    if time is None: time = ''
    print(f"time: {time}")
    data['Hora'] = time

    league = actions.get_text("(//*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div/div/div[@role='grid']/div[2]/div//p)[3]")
    country = ''
    if league is None: league = ''
    match = re.search(r"(.*?)\s*\((.*)\)", league)
    if match:
        league = match.group(1)
        country = match.group(2)
    print(f"league: {league}")
    print(f"country: {country}")
    data['Liga'] = league
    data['Pais'] = country

    # ---------------------------------------------------------------
    # Pegando o placar do time da casa

    hometeamScoreFTXpath = getInfoXpath("/div/div[@role='grid']/div[2]/div[2]/div[1]//p[1]")
    if actions.has_element(hometeamScoreFTXpath, time=0):
        hometeamScoreFT = actions.get_text(hometeamScoreFTXpath)
        if not hometeamScoreFT is None: hometeamScoreFT = int(hometeamScoreFT)
        else: hometeamScoreFT = -1
    else:
        hometeamScoreFT = -1
    print(f"hometeamScoreFT: {hometeamScoreFT}")
    data['Casa FT'] = hometeamScoreFT

    hometeamScoreHTXpath = getInfoXpath("/div/div[@role='grid']/div[2]/div[2]/div[1]//p[2]")
    if actions.has_element(hometeamScoreHTXpath, time=0):
        hometeamScoreHT = actions.get_text(hometeamScoreHTXpath)
        if not hometeamScoreHT is None: 
            match = re.search(r"(\d+)", hometeamScoreHT)
            if match:
                hometeamScoreHT = int(match.group(1))
            else:
                hometeamScoreHT = -1
        else: hometeamScoreHT = -1
    else:
        hometeamScoreHT = -1
    print(f"hometeamScoreHT: {hometeamScoreHT}")
    data['Casa HT'] = hometeamScoreHT

    # ---------------------------------------------------------------
    # Pegando o placar do time de fora

    awayteamScoreFTXpath = getInfoXpath("/div/div[@role='grid']/div[2]/div[2]/div[2]//p[2]")
    if actions.has_element(awayteamScoreFTXpath, time=0):
        awayteamScoreFT = actions.get_text(awayteamScoreFTXpath)
        if not awayteamScoreFT is None: awayteamScoreFT = int(awayteamScoreFT)
        else: awayteamScoreFT = -1
    else:
        awayteamScoreFT = -1
    print(f"awayteamScoreFT: {awayteamScoreFT}")
    data['Fora FT'] = awayteamScoreFT

    awayteamScoreHTXpath = getInfoXpath("/div/div[@role='grid']/div[2]/div[2]/div[2]//p[1]")
    if actions.has_element(awayteamScoreHTXpath, time=0):
        awayteamScoreHT = actions.get_text(awayteamScoreHTXpath)
        match = re.search(r"(\d+)", awayteamScoreHT)
        if match:
            awayteamScoreHT = int(match.group(1))
        else:
            awayteamScoreHT = -1
    else:
        awayteamScoreHT = -1
    print(f"awayteamScoreHT: {awayteamScoreHT}")
    data['Fora HT'] = awayteamScoreHT

    # ---------------------------------------------------------------
    # Pegando as odds

    if actions.has_element("//button[text()='Ver mais odds']", time=0):
        actions.click_element("//button[text()='Ver mais odds']")
        actions.sleep(1)

    oddsEl = getInfoXpath("/div/div[@role='grid']/div[4]//span")
    oddsEls = actions.get_elements(oddsEl)
    odds = [actions.get_text(x) for x in oddsEls]
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
        print(f"\t{mapOdd[index]}: {odd}")
        data[mapOdd[index]] = odd

    # ---------------------------------------------------------------
    # Pegando o LG Score da casa
        
    homeLGScore = -1
    HScore = -1
    awayLGScore = -1
    
    try:
        homeLGScoreXpath = "(//*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div/div/div[@role='grid']/div[5]//p)[1]"
        homeLGScore = actions.get_text(homeLGScoreXpath, time=0)
        match = re.search(r"(\d+)", homeLGScore)
        if match:
            homeLGScore = int(match.group(1))
        else:
            homeLGScore = -1
    except ValueError:
        pass
    print(f"homeLGScore: {homeLGScore}")
    data["Casa LG Score"] = homeLGScore

    # ---------------------------------------------------------------
    # Pegando o H-Score

    try:
        HScoreXpath = "(//*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div/div/div[@role='grid']/div[6]//p)[1]"
        HScore = actions.get_text(HScoreXpath, time=0)
        match = re.search(r"(\d+)", HScore)
        if match:
            HScore = int(match.group(1))
        else:
            HScore = -1
    except ValueError:
        pass
    print(f"HScore: {HScore}")
    data["H Score"] = HScore

    # ---------------------------------------------------------------
    # Pegando o LG Score de fora
    
    try:
        awayLGScoreXpath = "(//*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div/div/div[@role='grid']/div[7]//p)[1]"
        awayLGScore = actions.get_text(awayLGScoreXpath, time=0)
        match = re.search(r"(\d+)", awayLGScore)
        if match:
            awayLGScore = int(match.group(1))
        else:
            awayLGScore = -1
    except ValueError:
        pass
    print(f"awayLGScore: {awayLGScore}")
    data["Fora LG Score"] = awayLGScore

    stats_home_away = createStats()
    stats_global = createStats()
    data_home_away = createDataStats(data)
    data_global = createDataStats(data)
    if not actions.has_element("//p[text()='Jogo sem dados de pré live']", time=0):
        changeTotalMatch('5 jogos')
        # ===============================================================================================================
        # ===============================================================================================================
        # ===============================================================================================================
        # Fazendo as leituras Casa/Visitante
        changeSideMatch('Casa/Visitante')
        # ---------------------------------------------------------------
        # Lendo as médias e dispersões
        attempts = 10;
        while attempts > 0:
            attempts = attempts - 1
            tabName = 'Médias e Dispersões'
            changeTabList(tabName)
            print(">> Médias e Dispersões:")

            rowsEl = actions.get_elements("(((((//*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div/div)[2]/div/div)[1]/div/div/div)[2]/div/div/div[last()]/div/div/div)/div/div[1])/div[2]/p", time=0)
            measurements = [default_space(actions.get_text(x)) for x in rowsEl]
            print(f"measurements: {measurements}")
            try:
                stats_home_away = mergeStats(stats_home_away, readStats(tabName, measurements))
                if  stats_home_away['Média Custo do Gol (1.0)']["home"][0]["value"] < 0 or \
                    stats_home_away['Média Custo do Gol (1.0)']["away"][0]["value"] < 0 or \
                    stats_home_away['Média Custo do Gol (2.0)']["home"][0]["value"] < 0 or \
                    stats_home_away['Média Custo do Gol (2.0)']["away"][0]["value"] < 0:
                    raise StatReadingError("Não foi possível ler os dados estatisticos")
            except StatReadingError:
                actions.sleep(2)
                continue
            break;
        if attempts <= 0: StatNotFoundError("Não foi encontrado a estatística")

        # ---------------------------------------------------------------
        # 1º Gol
        attempts = 10;
        while attempts > 0:
            attempts = attempts - 1
            tabName = '1º Gol'
            changeTabList(tabName)
            print(">> 1º Gol':")

            rowsEl = actions.get_elements("(((((//*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div/div)[2]/div/div)[1]/div/div/div)[2]/div/div/div[last()]/div/div/div)/div/div[1])/div[2]/p", time=0)
            measurements = [default_space(actions.get_text(x)) for x in rowsEl]
            print(f"measurements: {measurements}")
            try:
                stats_home_away = mergeStats(stats_home_away, readStats(tabName, measurements))
                if  stats_home_away['Jogos marcou o primeiro gol no HT']["home"][0]["value"] < 0 or \
                    stats_home_away['Jogos marcou o primeiro gol no HT']["away"][0]["value"] < 0 or \
                    stats_home_away['Jogos sofreu o primeiro gol no HT']["home"][0]["value"] < 0 or \
                    stats_home_away['Jogos sofreu o primeiro gol no HT']["away"][0]["value"] < 0:
                    raise StatReadingError("Não foi possível ler os dados estatisticos")
            except StatReadingError:
                actions.sleep(2)
                continue
            break;
        if attempts <= 0: StatNotFoundError("Não foi encontrado a estatística")

        # ===============================================================================================================
        # ===============================================================================================================
        # ===============================================================================================================
        # Fazendo as leituras Global
        changeSideMatch('Global')
        # ---------------------------------------------------------------
        # Lendo as médias e dispersões
        attempts = 10;
        while attempts > 0:
            attempts = attempts - 1
            tabName = 'Médias e Dispersões'
            changeTabList(tabName)
            print(">> Médias e Dispersões:")

            rowsEl = actions.get_elements("(((((//*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div/div)[2]/div/div)[1]/div/div/div)[2]/div/div/div[last()]/div/div/div)/div/div[1])/div[2]/p", time=0)
            measurements = [default_space(actions.get_text(x)) for x in rowsEl]
            print(f"measurements: {measurements}")
            try:
                stats_global = mergeStats(stats_global, readStats(tabName, measurements))
                if  stats_global['Média Custo do Gol (1.0)']["home"][0]["value"] < 0 or \
                    stats_global['Média Custo do Gol (1.0)']["away"][0]["value"] < 0 or \
                    stats_global['Média Custo do Gol (2.0)']["home"][0]["value"] < 0 or \
                    stats_global['Média Custo do Gol (2.0)']["away"][0]["value"] < 0:
                    raise StatReadingError("Não foi possível ler os dados estatisticos")
            except StatReadingError:
                actions.sleep(2)
                continue
            break;
        if attempts <= 0: StatNotFoundError("Não foi encontrado a estatística")

        # ---------------------------------------------------------------
        # 1º Gol
        attempts = 10;
        while attempts > 0:
            attempts = attempts - 1
            tabName = '1º Gol'
            changeTabList(tabName)
            print(">> 1º Gol':")

            rowsEl = actions.get_elements("(((((//*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div/div)[2]/div/div)[1]/div/div/div)[2]/div/div/div[last()]/div/div/div)/div/div[1])/div[2]/p", time=0)
            measurements = [default_space(actions.get_text(x)) for x in rowsEl]
            print(f"measurements: {measurements}")
            try:
                stats_global = mergeStats(stats_global, readStats(tabName, measurements))
                if  stats_global['Jogos marcou o primeiro gol no HT']["home"][0]["value"] < 0 or \
                    stats_global['Jogos marcou o primeiro gol no HT']["away"][0]["value"] < 0 or \
                    stats_global['Jogos sofreu o primeiro gol no HT']["home"][0]["value"] < 0 or \
                    stats_global['Jogos sofreu o primeiro gol no HT']["away"][0]["value"] < 0:
                    raise StatReadingError("Não foi possível ler os dados estatisticos")
            except StatReadingError:
                actions.sleep(2)
                continue
            break;
        if attempts <= 0: StatNotFoundError("Não foi encontrado a estatística")

    # else:
    #     stats_home_away = createStats()
    #     stats_global = createStats()

    statsHomeAwayConverted = convertStats(stats_home_away)
    # print(f"statsHomeAwayConverted: {statsHomeAwayConverted}")
    data_home_away = mergeData(data_home_away, statsHomeAwayConverted)
    print(f"data_home_away: {data_home_away}")

    statsGlobalConverted = convertStats(stats_global)
    # print(f"statsGlobalConverted: {statsGlobalConverted}")
    data_global = mergeData(data_global, statsGlobalConverted)
    print(f"data_global: {data_global}")

    

# Montar a primeira linha
# firstLine = []
# firstLine.append('Data')
# firstLine.append('Hora')
# firstLine.append('Liga')
# firstLine.append('Pais')
# firstLine.append('Casa')
# firstLine.append('Fora')

# firstLine.append('Casa HT')
# firstLine.append('Fora HT')
# firstLine.append('Casa FT')
# firstLine.append('Fora FT')

# firstLine.append('Casa LG Score')
# firstLine.append('HScore')
# firstLine.append('Fora LG Score')

# firstLine.append('Odd Casa')
# firstLine.append('Odd Empate')
# firstLine.append('Odd Fora')

# firstLine.append('Odd Under 0.5 HT')
# firstLine.append('Odd Under 0.5 FT')
# firstLine.append('Odd Under 1.5 FT')
# firstLine.append('Odd Under 2.5 FT')
# firstLine.append('Odd Não Ambas')

# firstLine.append('Odd Over 0.5 HT')
# firstLine.append('Odd Over 0.5 FT')
# firstLine.append('Odd Over 1.5 FT')
# firstLine.append('Odd Over 2.5 FT')
# firstLine.append('Odd Ambas')

# pushHomeAwayFile("\t".join(firstLine))
# pushGlobalFile("\t".join(firstLine))

while True:

    input("Aperte qualquer tecla após selecionar o filtro para ler as partidas")

    try:
        totalMatches = len(actions.get_elements("//*[./input[contains(@placeholder, 'Buscar por jogos')]]/div[3]//div[@data-selected]"))
    except Exception:
        totalMatches = 0

    if totalMatches <= 0: 
        print(f"Não existe partidas disponíveis, tente outro filtro...")
        continue;

    for matchNumber in range(1, totalMatches+1):
        print("-"*50)
        print(f"Abrindo a partida {matchNumber}...")
        xpath = f"(//div[./input[contains(@placeholder, 'Buscar por jogos')]]/div[3]//div[@data-selected])[{matchNumber}]"
        hometeam = actions.get_text(f"({xpath}//p)[2]")
        dataSelected = actions.get_attr(xpath, 'data-selected')
        print(f"dataSelected: {dataSelected}")
        if dataSelected == False or dataSelected == 'false':
            actions.click_element(xpath)
            xpathCompare = f"//*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div/div/div[@role='grid']/div[1]//p"
            attemps = 60
            while attemps > 0:
                attemps = attemps - 1
                if not actions.has_element(xpathCompare, time=0): 
                    actions.sleep(0.5)
                    continue;
                hometeamCompare = actions.get_text(xpathCompare)
                if hometeamCompare == hometeam: break;
            if attemps <= 0: raise TimeoutError("O tempo de espera para abrir a partida esgotou")
        print(f"Aberto com sucesso!")
        actions.sleep(2)

        readMatch()


# actions.sleep(3600)

# -----------------------------------------------------------------------------------------
# Leitura da partida



