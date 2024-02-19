from Library_v1.Utils.string import (
    create_regex_latin_str,
    slug_name
)

class Match():
    def __init__(self, hometeam: str, awayteam: str, time: str) -> None:
        self.time = time
        self.hometeam = hometeam
        self.awayteam = awayteam

    def getHometeam(self, ):
        return self.hometeam
    
    def getAwayteam(self, ):
        return self.awayteam
    
    def getTime(self, ):
        return self.time
    
    def getId(self, ):
        return slug_name(f"{self.hometeam}_x_{self.awayteam}")
    
    def get(self, ):
        return {
            "hometeam": self.hometeam,
            "awayteam": self.awayteam,
            "time": self.time,
        }
    
    def print(self, ):
        print(f"{self.getTime()} | {self.getHometeam()} x {self.getAwayteam()}")