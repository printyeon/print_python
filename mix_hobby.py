count=int(input("입력하는 학생수가 총 몇명인가요? : "))

man=list()
num=1
while num <=count:
    print(num,"번째 학생")
    name = input("* 이름 : ")
    hobby = input("* 취미 : ")
    pair = (name, hobby)
    man.append(pair)
    num += 1
    
man_dict = dict(man)
man_set = set(man)
hobbylist=set(man_dict.values())

print(man)
print(hobbylist)

print("전체 학생 목록",list(man_dict.keys()))
print("전체 취미 목록",hobbylist)
print("전체 학생 취미 생활",man_set)
print("전체 학생 취미 생활",man_dict)