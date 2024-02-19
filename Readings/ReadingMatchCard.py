from Library_v1.Driver.DriverInterface import DriverInterface
from Library_v1.Driver.DriverActions import DriverActions

from Library_v1.Utils.string import (
    slug_name,
)

from Exceptions.MatchNotFoundError import MatchNotFoundError

from Readings.Data.Match import Match

BASE_XPATH = "//*[@id='__next']/section/div[2]/div[2]/div/div/div[1]/div[2]/div/div[3]/div[2]"
getXPath = lambda relativeXpath: f"{BASE_XPATH}{relativeXpath}"

"""
    //*[@id='__next']/section/div[2]/div[2]/div/div/div[1]/div[2]/div/div[3]/div[2]

    card:
    //*[@id='__next']/section/div[2]/div[2]/div/div/div[1]/div[2]/div/div[3]/div[2]/div/div[2]/div

    (//*[@id='__next']/section/div[2]/div[2]/div/div/div[1]/div[2]/div/div[3]/div[2]/div/div[2]/div)[1]/div//p
"""

class ReadingMatchCard():
    def __init__(self, driver: DriverInterface, position: int) -> None:
        self.driver = driver
        self.actions = DriverActions(self.driver)
        self.position = position
        self.cardXPath = f"(//div[./input[contains(@placeholder, 'Buscar por jogos')]]/div[3]//div[@data-selected])[{self.position}]"
        self.info = None;
        self.match: Match = None

    def openMatch(self, ):
        self.read();
        slugHometeam = slug_name(self.match.getHometeam())
        dataSelected = self.actions.get_attr(self.cardXPath, 'data-selected')
        if dataSelected == False or dataSelected == 'false':
            self.actions.click_element(self.cardXPath)
            xpathCompare = f"//*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div/div/div[@role='grid']/div[1]//p"
            attemps = 60
            while attemps > 0:
                attemps = attemps - 1
                if self.actions.has_element("//*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div//button[contains(text(), 'Tentar novamente')]", time=0):
                    self.actions.click_element("//*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div//button[contains(text(), 'Tentar novamente')]")
                    attemps = 60
                    continue;
                if not self.actions.has_element(xpathCompare, time=0): 
                    self.actions.sleep(0.5)
                    continue;
                hometeamCompare = slug_name(self.actions.get_text(xpathCompare))
                if hometeamCompare == slugHometeam: break;
                if attemps <= 0: 
                    # raise TimeoutError("O tempo de espera para abrir a partida esgotou")
                    input("Partida demorou para abrir, resolva o problema e aperte qualquer botão para prosseguir...")
        print(f"Aberto com sucesso!")
        self.actions.sleep(1)
                    
    def read(self, ):
        if self.info: return;
        if not self.actions.has_element(self.cardXPath, time=0):
            raise MatchNotFoundError(f"A partida na posição '{self.position}' não encontrada")
        time = self.actions.get_text(f"{self.cardXPath}/div/p")
        hometeam = self.actions.get_text(f"({self.cardXPath}/div/div[not(contains(@class, 'divider'))]/div/div/div[1]/p)[1]")
        awayteam = self.actions.get_text(f"({self.cardXPath}/div/div[not(contains(@class, 'divider'))]/div/div/div[1]/p)[2]")
        # print(f"hometeam: {hometeam}")
        # print(f"awayteam: {awayteam}")
        # print(f"time: {time}")
        self.match = Match(hometeam, awayteam, time)

    def get(self, ) -> Match:
        return self.match