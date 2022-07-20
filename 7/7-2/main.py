def search(a3,target,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    if a3[mid]==target:
        return mid
    elif a3[mid]>target:
        return search(a3, target, start, mid-1)
    elif a3[mid] < target:
        return search(a3, target, start, mid + 1)


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
    result=search(a1,i,0,n-1)
    print(result)

    if result==None:
        print("NO")
    else:
        print("YES")








