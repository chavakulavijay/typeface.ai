def ternery(input123):
    st23=''
    while(input123!=0):
        st23=str(input123%3)+st23
        input123=input123//3
    return st23
input123=int(input())
print(ternery(input123))