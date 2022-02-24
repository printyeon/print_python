def  box(n,m):
    for i in range(n):
        for j in range(m):
            print("* ", end=" ")
        print()
        
a=int(input("행 입력 "))
b=int(input("열 입력 "))
print()

box(a,b)