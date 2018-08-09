class Student :

    def __init__(self,name, address, email, mobile):

        self.name = name
        self.address = address
        self.email = email
        self.mobile = mobile
        self.__password = 'pass'

    def displayName(self):
         print(self.name)

    def setName(self, name):
        self.name =name

    def getName(self):
        return self.name

    def setPassword(self,password):
        self.__password = password

    def getPassword(self):
        return self.__password