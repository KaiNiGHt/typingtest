from time import time, sleep
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
            print("타수 / SCORE \t",self.__score / (time() - self.__start) * 60)
    
    def update(self) : 
        self.__start = 0
        self.__before = time()
        self.__delta = 0

        for i in self.__list :
            answer = ""
            self.__render(i, answer)

            while True : 
                if kbhit() : 
                    if self.__start == 0 : 
                        self.__start = time()

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
        score = self.__score / (time() - self.__start) * 60
        system("cls")
        print("축하드립니다! 당신은 이 지옥같은 타자연습을 끝냈어요.")
        print("Congratulations! You're done with this hellish typing practice.")
        sleep(0.5)
        print("이걸 끝냈다는것도 놀랍네요.")
        print("It's amazing that you've finished this.")
        sleep(0.5)
        system("cls")
        print("----------------------------------------------------------------")
        print("리더보드 / leader board")
        print("타수     / SCORE  |", score)
        print("시간     / TIME   |", int(time() - self.__start),'s')
        print("----------------------------------------------------------------")
        system("pause")