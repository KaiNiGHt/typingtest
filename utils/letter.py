from . import read_
from . import test
from random import choice
class Letter : 
    def __init__(self, file) : 
        letters = read_.Read(file)
        self.__list = []

        for i in range(50) : 
            self.__list.append(choice(letters.get()))
        
        test.Test(self.__list).update()
