from Library_v1.Utils.string import (
    slug_name,
    default_space,
)

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