#가게 물건 개수
n=int(input())

#가게 물건 번호
a1=list(map(int,input().split()))
a1.sort()

#손님 요청 개수
m=int(input())

#손님 요청 물건 번호
a2=list(map(int,input().split()))
a2.sort()

for i in a2:
    if i in a1:
        print("yes",end=" ")
    else:
        print("no",end=" ")







