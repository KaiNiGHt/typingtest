from utils import letter
import time
import os
def init() :
    title = ""

    for c in "T Y P I N G T E S T" : 
        title += c
        print(title)
        time.sleep(0.05)
        os.system('cls')
    print("T Y P I N G T E S T")
    time.sleep(0.5)
    print("쉬운 오픈 소스 영어 타자연습 프로그램")
    print("Easy Open Source English Typing Practice Program")
    time.sleep(0.5)
    print("version 0.1.1 Ahlpa")
    time.sleep(0.5)
    print("GitHub 리포지토리에 기여하여 프로그램을 발전시켜주세요!")
    print("Github : https://github.com/KaiNiGHt/typingtest")
    os.system("pause")
    while True:
        os.system("cls")
        n = input("단계 입력 (1 : 자리연습, 2 : 낱말연습, 3, 4 : 짧은글 연습. 나가려면 -1 혹은 exit를 입력하세요.) : ")
        if n >= "1" and n <= "4" :
            letter.Letter('./utils/database/english/resource/letter_' + n + '.txt')
        elif n == "exit" or n == "-1":
            print("종료합니다.")
            time.sleep(1)
            break
        elif n == "d" or n == "devmode" or n =="developer" or n == "dev" :
            letter.Letter('./utils/database/english/resource/developer.txt')
        else:
            print("오류 : 입력이 올바르지 않습니다.")
            time.sleep(1)
            os.system("cls")




