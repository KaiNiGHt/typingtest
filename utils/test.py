from time import time
from msvcrt import getch, kbhit
from os import system
class Test : 
    def __init__(self, l) : 
        self.__list = l
        self.__score = 0
        self.__start = 0
        self.__before = 0
        self.__delta = 0

    def __render(self, ori, ans) : 
        system('cls')
        print(ori)
        print(ans)
        if time() - self.__start > 0 : 
            print(self.__score / (time() - self.__start))
    
    def update(self) : 
        self.__start = time()
        self.__before = time()
        self.__delta = 0

        for i in self.__list :
            answer = ""
            self.__render(i, answer)

            while True : 
                if kbhit() : 
                    key = getch()

                    if ord(key) == 13 : 
                        break

                    elif ord(key) == 8 : 
                        if len(answer) > 0 : 
                            answer = answer[:-1]
                            if self.__score > 1 : 
                                self.__score -= 1

                            self.__render(i, answer)

                    elif len(answer) + 1 >= len(i) : 
                        break
                    else : 
                        answer += chr(ord(key))

                        if answer[-1] == i[len(answer) - 1] : 
                            self.__score += 1
                        
                        self.__render(i, answer)

                self.__delta += time() - self.__before
                
                if self.__delta >= 0.5 :              
                    self.__render(i, answer)
                    self.__delta = 0
                
                self.__before = time()