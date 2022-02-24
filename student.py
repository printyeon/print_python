count = int(input("입력하는 학생수가 총 몇명인가요? : "))

scores = list() #전체학생
num=1

#이름 및 점수 입력
while num<=count :
    print(num,"번째 학생 ")
    name = input("* 이름 : ")
    score = int(input("* 점수 : "))
    pair = (name,score) #이름과 성적 저장
    scores.append(pair)
    num+=1
    

scores_dict = dict(scores)
flag = True
while flag:
    wanted = input("어떤 학생의 성적을 볼까요? ")
    if wanted in scores_dict:
        print(wanted, "학생의 점수 : ", scores_dict[wanted])
        flag = False
        print("프로그램을 종료합니다.")
    else :
        print("찾는 학생(", wanted ,")의 점수가 존재하지 않습니다.")