n=int(input())

go=input("L,R,U,D 중 입력해주세요: ").split()


print(go)

x,y=1,1

for i in go:
    if i=="R":
        if x==n:
            continue
        else :
            x+=1
    elif i=="L":
        if x==1:
            continue
        else :
            x-=1
    elif i=="U":
        if y==1:
            continue
        else :
            y-=1
    elif i=="D":
        if y==n:
            continue
        else :
            y+=1
print(x,y)



