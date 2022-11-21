def chec12(input1):
    while(input1>0):
        c123=input1%10
        if(c123==3 or c123==4 or c123==7):
            return False
        input1//=10
    return True
    
input1=int(input())
c12,cou=1,1
while(cou<input1):
    c12+=1
    if(chec12(c12)):
        cou+=1
print(c12)