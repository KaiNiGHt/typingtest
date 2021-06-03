from random import *

class Read :
    def __init__(self, file) :
        f = open(file, 'r')
        self.__list = f.readlines()
        f.close()
        
    def get(self) :
        return self.__list