

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
        self.keys = list(self.data.keys())
        if data: self.setAll(data)

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