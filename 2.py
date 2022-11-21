s123=input()
sbstr123=input()
co12=0
le12=0
for i in sbstr123:
    le12+=1
for i in range(le12):
    if i==le12-1:
        la_cha=sbstr123[i]
for i in s123:
    if i==la_cha:
        co12+=1
print(co12)