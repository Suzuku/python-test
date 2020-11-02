
# mixin 多重继承


class Name():
    def __init__(self, name):
        self.__name = name

    def printName(self):
        print(self.name)


class Age():
    def __init__(self, age):
        self.__age = age

    def printAge(self):
        print(self.age)


class Son(Name, Age):
    def __init__(self, name, age):
        super().__init__()


son = Son('233', 22)
son.printName()
son.printAge()
