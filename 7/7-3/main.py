n,m=map(int,input().split())

array=list(map(int,input().split()))

start=0
end=max(array)


while(start<=end):
    result = 0
    mid = (start + end) // 2
    for i in array:
        if i > mid:
            result = result + i - mid

    if result==m:
        print(mid)
        break
    elif result>m:
        start=mid+1

    else:
        end=mid-1




