from time import time
from msvcrt import getch, kbhit
from os import system
class Test : 
    def __init__(self, l) : 
        self.__list = l

    def update(self) : 
        for i in self.__list :
            answer = ""
            
            while True : 
                print(i)
                print(answer)

                if kbhit() : 
                    key = getch()

                    if ord(key) == 13 : 
                        break
                    elif len(answer) >= len(i) : 
                        break
                    else : 
                        if ord(key) == 8:
                            if len(answer) > 0 : 
                                answer = answer[:-1]
                        else : 
                            answer += chr(key)
                system("clear")