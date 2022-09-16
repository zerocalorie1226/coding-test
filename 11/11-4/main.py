n=map(int,input().split())
won=list(map(int,input().split()))
won.sort()
result=1

for i in won:
    if result<i:
        break
    result+=i

print(result)
