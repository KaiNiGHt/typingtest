from msvcrt import getch

while True : 
    a = getch()
    if ord(a) == 8 :
        print('bs')
    elif ord(a) == 13 :
        print('return')
    elif ord(a) == 27 :
        print('esc')
    elif ord(a) == 224 :
        print('special key')
        b = getch()

        if (ord(b) == 83) :
            print('delete')
    elif ord(a) == 32 :
        print("space")
    
    else:
        print('else key')
        print(ord(a))
        print(chr(ord(a)))
