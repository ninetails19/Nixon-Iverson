# math game
import random

x= random.randint(1, 10)
y= random.randint(1, 10)

while True:
    print("1. Main")
    print("2. Quit")
    cois = int(input("= "))
    if cois == 1:
        print("---Level---")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        print("4. Extreme")
        play= int(input("= "))
        if play == 1:
            print("Level Easy")
            print(x,"+",y)
            ans= int(input("= "))
            if ans == x + y:
                print("the answer is", x + y)
                print("Yes you got it")
                break
            else:
                print("try again!")
        elif play == 2:
            print("Level Medium")
            print(x,"X",y)
            ans= int(input("= "))
            if ans == x * y:
                print("the answer is", x * y)
                print("Yes you got it")
                break
            else:
                print("try again!")
        elif play == 3:
            print("Level Hard")
            print(x,":",y)
            ans= float(input("= "))
            if ans == x / y:
                print("the answer is", x / y)
                print("Yes you got it")
                break
            else:
                print("try again!")
        elif play == 4:
            print("Level Extreme")
            print(x,"X",y,":",y,"x",x,":",x)
            ans= float(input("= "))
            if ans == x * y / y * x / x:
                print("the answer is", x * y / y * x / x)
                print("Yes you got it")
                break
            else:
                print("try again!")
    else:
        print("thx for playing")