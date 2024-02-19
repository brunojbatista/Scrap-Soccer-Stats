

class Account():
    def __init__(self, user: str, password: str) -> None:
        self.user = user
        self.password = password

    def getUser(self, ):
        return self.user

    def getPassword(self, ):
        return self.password