from Library_v1.Utils.time import (
    get_date,
    date_now,
    add_hour,
)
import re

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

class Featured():
    def __init__(self, data: dict = None) -> None:
        self.data = {
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
        self.date = None
        self.keys = list(self.data.keys())
        if data: self.setAll(data)

    def getHeaders():
        return [*FEATURED]

    def setAll(self, data: dict):
        temp = {**self.data}
        for k in data:
            if k not in self.data:
                raise KeyError(f"Chave '{k}' não encontrada")
            temp[k] = data[k]
        self.data = temp

    def set(self, key: str, value):
        if key not in self.data: raise KeyError(f"Chave '{key}' não encontrada")
        self.data[key] = value
        return self;

    def getDate(self, ):
        if not self.date is None: return self.date
        if self.data["Data"] is None or self.data["Hora"] is None: return None
        match = re.search(r"(\d{2})\/(\d{2})\/(\d{4})", self.data["Data"])
        day = int(match.group(1))
        month = int(match.group(2))
        year = int(match.group(3))
        match = re.search(r"(\d{2}):(\d{2})", self.data["Hora"])
        hour = int(match.group(1))
        minute = int(match.group(2))
        matchDate = get_date(year, month, day, hour, minute)
        self.date = matchDate
        return self.date

    def isStarted(self, shifttedHour: int = -2):
        print(f">> isStarted:")
        # if self.data["Data"] is None or self.data["Hora"] is None: return True
        # match = re.search(r"(\d{2})\/(\d{2})\/(\d{4})", self.data["Data"])
        # day = int(match.group(1))
        # month = int(match.group(2))
        # year = int(match.group(3))
        # match = re.search(r"(\d{2}):(\d{2})", self.data["Hora"])
        # hour = int(match.group(1))
        # minute = int(match.group(2))
        # matchDate = get_date(year, month, day, hour, minute)
        matchDate = self.getDate()
        if matchDate is None: return True
        dateNowShiftted = add_hour(date_now(), shifttedHour)
        print(f"dateNowShiftted: {dateNowShiftted}")
        print(f"matchDate: {matchDate}")
        print(f"test: {dateNowShiftted > matchDate}")
        return dateNowShiftted > matchDate

    def hasScore(self, ):
        return self.data["Casa HT"] >= 0 and self.data["Fora HT"] >= 0 and self.data["Casa FT"] >= 0 and self.data["Fora FT"] >= 0
    
    def hasMatchOdds(self, ):
        return self.data["Odd Casa"] > 1 and self.data["Odd Empate"] > 1 and self.data["Odd Fora"] > 1
    
    def has05HT(self, ):
        return self.data["Odd Under 0.5 HT"] > 1 and self.data["Odd Over 0.5 HT"] > 1
    
    def has05FT(self, ):
        return self.data["Odd Under 0.5 FT"] > 1 and self.data["Odd Over 0.5 FT"] > 1

    def has15FT(self, ):
        return self.data["Odd Under 1.5 FT"] > 1 and self.data["Odd Over 1.5 FT"] > 1
    
    def has25FT(self, ):
        return self.data["Odd Under 2.5 FT"] > 1 and self.data["Odd Over 2.5 FT"] > 1
    
    def hasBTTS(self, ):
        return self.data["Odd Não Ambas"] > 1 and self.data["Odd Ambas"] > 1

    def getAll(self, ):
        return self.data;

    def getOddHome(self, ):
        return self.data["Odd Casa"]
    
    def getOddDraw(self, ):
        return self.data["Odd Empate"]
    
    def getOddAway(self, ):
        return self.data["Odd Fora"]
    
    def getOddUnder25FT(self, ):
        return self.data["Odd Under 2.5 FT"]

    def getMap(self, ):
        return self.getAll()