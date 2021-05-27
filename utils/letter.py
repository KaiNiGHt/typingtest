from . import read
from . import test
from random import choice
class Letter : 
    def __init__(self, file) : 
        letters = read.Read(file)
        self.__list = []

        for i in range(100) : 
            self.__list.append(choice(letters.get()))
        
        test.Test(self.__list).update()
