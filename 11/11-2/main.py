num=list(input())
result=0

for i in range(len(num)):
    a=int(num[i])
    if result<=1 or a<=1:
        result+=a
    else:
        result*=a

print(result)