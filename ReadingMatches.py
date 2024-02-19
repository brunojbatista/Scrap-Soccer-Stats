from Library_v1.Driver.DriverInterface import DriverInterface
# from Library_v1.Driver.ChromeDriver import ChromeDriver
from Library_v1.Driver.DriverActions import DriverActions
import re

from Reading import Reading

from Library_v1.Utils.string import (
    slug_name,
    default_space,
)

from Exceptions.ActionError import ActionError

from Readings.ReadingFeaturedInfo import ReadingFeaturedInfo
from Readings.ReadingMatchCard import ReadingMatchCard
from Cache import Cache
from CacheStats import CacheStats
from FulltraderAccount import FulltraderAccount

class ReadingMatches():
    def __init__(self, driver: DriverInterface) -> None:
        self.driver = driver
        self.actions = DriverActions(driver)
        # self.sizeMatch = None
        # self.sizeMatchView = None
        # self.totalMatches = -1
        self.totalAvailableMatches = 0
        self.typeReadings = []
        self.matchReadings = []
        self.sizeReadings = []
        self.statReadings = []
        self.filename = ""
        # self.haSettingTypeReadings = False
        self.account = FulltraderAccount()

    def login(self, ):
        # ---------------------------------------------------------
        # Logando na plataforma
        self.actions.navigate_url("https://app.fulltradersports.com/login")
        self.actions.clear_element("//input[@id='username']")
        self.actions.write_element("//input[@id='username']", self.account.getUser())
        self.actions.sleep(3)
        self.actions.clear_element("//input[@id='password']")
        self.actions.write_element("//input[@id='password']", self.account.getPassword())
        self.actions.sleep(3)
        self.actions.click_element("//button[@type='submit']")
        self.actions.sleep(5)

    def navigateMatchesPage(self, ):
        self.actions.navigate_url("https://app.fulltradersports.com/sherlock/matches")
        self.actions.sleep(5)
        
    # def openMatch(self, matchNumber: int, isOpenHiddenData: bool = True):
    #     xpath = f"(//div[./input[contains(@placeholder, 'Buscar por jogos')]]/div[3]//div[@data-selected])[{matchNumber}]"
    #     hometeam = self.actions.get_text(f"({xpath}//p)[2]")
    #     dataSelected = self.actions.get_attr(xpath, 'data-selected')
    #     print(f"dataSelected: {dataSelected}")
    #     if dataSelected == False or dataSelected == 'false':
    #         self.actions.click_element(xpath)
    #         xpathCompare = f"//*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div/div/div[@role='grid']/div[1]//p"
    #         attemps = 60
    #         while attemps > 0:
    #             attemps = attemps - 1
    #             if self.actions.has_element("//*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div//button[contains(text(), 'Tentar novamente')]", time=0):
    #                 self.actions.click_element("//*[@id='__next']/section/div[2]/div[2]/div/div/div/div[3]/div//button[contains(text(), 'Tentar novamente')]")
    #                 attemps = 60
    #                 continue;
    #             if not self.actions.has_element(xpathCompare, time=0): 
    #                 self.actions.sleep(0.5)
    #                 continue;
    #             hometeamCompare = self.actions.get_text(xpathCompare)
    #             if hometeamCompare == hometeam: break;
    #             if attemps <= 0: 
    #                 # raise TimeoutError("O tempo de espera para abrir a partida esgotou")
    #                 input("Partida demorou para abrir, resolva o problema e aperte qualquer botão para prosseguir...")
    #             self.setTotalMatches()

        # # Abrindo os dados ocultos das odds
        # if isOpenHiddenData:
        #     if self.actions.has_element("//button[text()='Ver mais odds']", time=0):
        #         self.actions.click_element("//button[text()='Ver mais odds']")
        #         self.actions.sleep(1)

        # print(f"Aberto com sucesso!")
        # self.actions.sleep(1)

    def addTypeReading(self, matchTab: str, sizeTab = 'Casa/Visitante'):
        self.typeReadings.append((matchTab, sizeTab))

    def addMatchReading(self, *matchTab):
        self.matchReadings = matchTab

    def addSizeReading(self, *sizeTab):
        self.sizeReadings = sizeTab

    def addStatReading(self, *statTab):
        self.statReadings = statTab

    # def setTypeReadingMatches(self, matchTab = '5 jogos', statTab = 'Custo do gol', sizeTab = 'Casa/Visitante'):
    #     # if self.haSettingTypeReadings: return False
    #     for i in range(1, self.totalAvailableMatches+1):
    #         self.openMatch(i, False)
    #         try:
    #             self.changeTabConfig(matchTab, statTab, sizeTab)
    #             # self.haSettingTypeReadings = True
    #         except ActionError:
    #             continue;
    #         return True
    #     raise ActionError("Erro na configuração de leitura das partidas")

    # def setMainTab(self, matchTab = '5 jogos', sizeTab = 'Casa/Visitante'):
    #     for i in range(1, self.totalAvailableMatches+1):
    #         self.openMatch(i, False)
    #         try:
    #             self.selectSizeTab(sizeTab)
    #             self.selectMatchesTab(matchTab)
    #         except ActionError:
    #             continue;
    #         return True
    #     raise ActionError("Erro na configuração de leitura das partidas")

    def setFilename(self, matchTab: str, sizeTab: str):
        self.filename = slug_name(f"matches_{matchTab}_{sizeTab}")

    def saveContent(self, content: str):
        file = open(f"{self.filename}.txt", "a", encoding="utf-8")
        file.write(f"{content}\n")
        file.close()
        file = None

    def setTotalMatches(self, ):
        try:
            self.totalAvailableMatches = len(self.actions.get_elements("//*[./input[contains(@placeholder, 'Buscar por jogos')]]/div[3]//div[@data-selected]"))
        except Exception:
            self.totalAvailableMatches = 0

    def getSelectedDate(self, ):
        inputSelected = self.actions.get_element("//*[@id='__next']/section/div[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[.//p[contains(text(), 'Selecione a data')]]//label[./div[@data-checked]]/input")
        return self.actions.get_attr(inputSelected, 'value')

    def execute(self, ):
        # from threading import Thread
        # from DelayedKeyboardInterrupt import DelayedKeyboardInterrupt
        # import signal

        self.login()
        self.navigateMatchesPage()
        
        while True:
            input("Aperte qualquer tecla após selecionar o filtro para ler as partidas")

            self.setTotalMatches()
            selectedDate = self.getSelectedDate()
            print(f"selectedDate: {selectedDate}")

            # Abrir a cache do dia da leitura
            cache = Cache(selectedDate)

            if self.totalAvailableMatches <= 0: 
                print("Não foi encontrado nenhuma partida, tente outro filtro...")
                continue

            def process(position: int):
                print("\n")
                print("="*50)
                # input("Esperando para ler a proxima partida...")

                readingMatchCard    = ReadingMatchCard(self.driver, position)
                readingFeatured     = ReadingFeaturedInfo(self.driver)

                # -----------------------------------------------------------------
                # Ler os dados do card da partida
                readingMatchCard.read()
                match = readingMatchCard.get()
                match.print()
                cache.setMatch(match)
                cacheStats = CacheStats(selectedDate, match.getHometeam(), match.getAwayteam())
                # readingMatchCard.openMatch()

                # -----------------------------------------------------------------
                # Leitura das informações gerais da partida
                featuredCache = cache.getFeatured()
                # readingFeatured.read()
                if not featuredCache.hasScore():
                    readingMatchCard.openMatch()
                    readingFeatured.read()
                    featured = readingFeatured.get()
                    cache.setFeatured(featured)

                # -----------------------------------------------------------------
                # Ler os stats caso não exista
                statsCache = cacheStats.getStats()

                for matchTab, sizeTab in self.typeReadings:
                    print("*"*50)
                    print(f"matchTab: {matchTab}")
                    print(f"sizeTab: {sizeTab}")
                    # input("Esperando para ler os stats...")

                    if not statsCache.hasStats(matchTab, sizeTab):
                        print("Não tem o stats setado....")
                        # self.actions.sleep(2)
                        readingMatchCard.openMatch()
                        reading = Reading(self.driver, matchTab, sizeTab, self.statReadings)
                        reading.read()
                        stats = reading.get()
                        print(f"stats: {stats.getAll()}")
                        cacheStats.setStats(stats)
                        cache.setStatsFilename(cacheStats.getFilename())
                    else:
                        print("Ja tem stats setado...")

            for position in range(1, self.totalAvailableMatches+1):
                process(position)

            # TODO: Gerar o arquivo txt com os dados

                # a = Thread(target=process, args=(position))
                # a.start()
                # a.join()

                # if step == 'read_stats' or step == 'read_matches':
                    
                #     # -----------------------------------------------------------------
                #     # Abrir a partida
                #     print(f"matchData: {matchData}")
                #     readingMatchCard.openMatch()

                #     # -----------------------------------------------------------------
                #     # Verificar se há alguma cache salva com o dado da partida



                #     # self.openMatch(position)

                #     # featured = ReadingFeaturedInfo(self.driver)

                #     # featured.execute();

                #     # featured.print();

                #     # reading = Reading(self.driver, self.typeReadings, self.statReadings)

                #     # reading.execute()

                # elif step == 'read_results':
                #     print("Lendo os placares das partidas...")
