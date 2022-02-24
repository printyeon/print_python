#동전던지기

from random import randint
mon=50; #맨처음 돈

print("현재 돈 : ",mon ,"\n60원을 벌자!!\n")

while(True) :
    Num = randint(1,2)
    a = int(input("두구두구두구 1일까 2일까 "))
    if(a==1 or a==2) :
        if(Num==a) :
            mon=mon+9
            print("맞았다! 지금", mon, "원 있다!\n")
        else :
            mon=mon-10
            print("틀렸다.. 지금", mon, "있다!\n")
            
        #이겼을때    
        if(mon>=60) :
            print("이여어어어어어어얼 이겼네 끝이다!!")
            break;
        #졌을때
        if(mon<=0) :
            print("이이이이이이이잉 졌네 끝이다ㅠ")
            break;
    else :
        print("잘못입력했다요\n")