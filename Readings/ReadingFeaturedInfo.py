from Library_v1.Driver.DriverInterface import DriverInterface
from Library_v1.Driver.DriverActions import DriverActions
import re

from Readings.Data.Featured import Featured

BASE_XPATH = "//*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div"
getInfoXpath = lambda relativeXpath: f"{BASE_XPATH}{relativeXpath}"

class ReadingFeaturedInfo():
    def __init__(self, driver: DriverInterface) -> None:
        self.driver = driver
        self.actions = DriverActions(driver)
        self.featured = None;

    def read(self, ):
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

    def print(self, ):
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

    def get(self, ) -> Featured:
        return Featured(self.featured)