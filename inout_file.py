#파일만들어서 안에 내용 넣기

outfile = None
instr = ""
outfile = open("test03.txt","w", encoding="utf-8") #file write
while True:
    instr = input("내용입력 : ")
    if instr !="":
        outfile.write(instr+"\n")
    else:
        break
outfile.close()

#파일출력
infile,outfile = None,None
instr=""
infile= open("test03.txt","r",encoding="utf-8") #file read
outfile = open("test003.txt","w",encoding="utf-8")#file write

while True :
    instr = infile.read()
    if instr!="":
        print(instr+"\n")
    else:
        break
 
# #파일카피
# infile,outfile = None,None
# instr=""
# infile= open("test03.txt","r",encoding="utf-8") #file read
# outfile = open("test003.txt","w",encoding="utf-8")#file write
# 
# while True :
#     instr = infile.read()
#     if instr!="":
#         outfile.write(instr+"\n")
#     else:
#         break
# infile.close() 
# outfile.close()

#for파일카피
infile,outfile = None,None
instr=""
infile= open("test03.txt","r",encoding="utf-8") #file read
outfile = open("test003.txt","w",encoding="utf-8")#file write

instr = infile.read()
for i in instr :
    if instr!="":
        outfile.write(i)
infile.close() 
outfile.close()


