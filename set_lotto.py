import random
pick=set()
while len(pick)<6 :
    n=random.randint(1,45) #랜덤번호 생성
    #if n not in pick : #중복배제
        #pick.append(n) #집합에 요소 추가
    pick.add(n)
print(pick)