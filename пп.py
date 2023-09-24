class Car:

    def __init__(self, color, consumption):
        self.__color = color
        self.__consumption = consumption

    def data2(self):
        self.__daata()

    def __daata(self):
        print(self.__color, self.__consumption)

lamb = Car('red', 2)
lamb.data2()
# print(lamb.color)
# print(lamb.consumption)