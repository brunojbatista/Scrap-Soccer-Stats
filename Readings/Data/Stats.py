from Library_v1.Utils.string import (
    slug_name,
    default_space,
)

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

class Stats():
    def __init__(self, stats: list = None) -> None:
        """
            stats:
                id,
                values: [
                    ...
                ]
        """
        self.stats = []
        if not stats is None: self.setAll(stats)

    def getStatDict():
        return {**STATS}
    
    def getHeaders():
        _STATS = Stats.getStatDict()
        headers = []
        for stat in _STATS:
            fields = _STATS[stat]["fields"]
            for field in fields:
                headers.append(f"Casa - {field}")
                headers.append(f"Fora - {field}")
        return headers

    def getAll(self, ):
        return self.stats
    
    def setAll(self, stats: list):
        self.stats = stats

    def getId(self, matchTab: str, sizeTab: str):
        return slug_name(f"{matchTab}_{sizeTab}")

    def get(self, matchTab: str, sizeTab: str):
        id = self.getId(matchTab, sizeTab)
        return self.getById(id)

    def getById(self, id: str):
        stat = None
        for s in self.stats:
            if s["id"] == id:
                stat = s
                break;
        return stat
    
    def getParams(self, matchTab: str, sizeTab: str, *params) -> dict:
        _params = {}
        stat = self.get(matchTab, sizeTab)
        if stat is None: return None
        # print(f"stat: {stat}")
        # print(f"stat['values']: {stat['values']}")
        values = {}
        for measurement in stat['values']:
            # print(f"measurement: {measurement}")
            for team in stat['values'][measurement]:
                # print(f"team: {team}")
                # print(f"stat['values'][measurement][team]: {stat['values'][measurement][team]}")
                for statName, value in stat['values'][measurement][team]:
                    values[statName] = value
        for param in params:
            if param not in values: raise ValueError(f"Não existe o parametro '{param}' nas estatistica da partida")
            _params[param] = values[param]
        return _params;

    def set(self, matchTab: str, sizeTab: str, values: list):
        id = self.getId(matchTab, sizeTab)
        return self.setById(id, values)

    def setById(self, id: str, values: list):
        if not self.hasStatsById(id):
            self.stats.append({
                "id": id,
                "values": values
            })
        else:
            for index, stat in enumerate(self.stats):
                if stat["id"] == id:
                    self.stats[index]["values"] = values
                    break;
        return True;

    def hasStats(self, matchTab: str, sizeTab: str):
        return not self.get(matchTab, sizeTab) is None

    def hasStatsById(self, id: str):
        return not self.getById(id) is None
    
    def getMap(self, matchTab: str, sizeTab: str) -> list:
        data = {}
        values = self.get(matchTab, sizeTab)["values"]
        for statName in values:
            for header, value in values[statName]['home']:
                data[header] = value
            for header, value in values[statName]['away']:
                data[header] = value
        return data