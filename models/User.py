from datetime import datetime

class User:

    def __init__(self, ced, username, password, state, rol):
        self.ced = ced
        self.username = username
        self.password = password
        self.state = state
        self.rol = rol
    
    def getUser(self):
        return self.__dict__
    
    def createUser(self):
        self.fecha_creacion = datetime.now()
    
    def updateUser(self):
        self.fecha_modificacion = datetime.now()
    