def check_pwd(pwd):
    b=1
    while True :
        a=input("비밀번호 4자리를 입력하세요 : ")
        if a!=pwd :
            print("땡!!!!", 5-b ,"번의 기회가 남았습니다 다시입력하세요\n")
            b=b+1
            if b>5 :
                break
        else :
            print("정확한 비번이다!!")
            break
        
pwd=input("비밀번호를 설정하세요 : ")

check_pwd(pwd)

    
    
#pwd="1234"
#check_pwd()
#print("틀")

# def check_pwd(pwd) :
#     return pwd == "1234" #트루 펄스 반환
# 
# while check_pwd(input("비밀번호 4자리를 입력하세요 : ")) == False:
#     print("땡!!!! 다시입력하세요\n")
#     
#     
# print("정확한 비번이다!")