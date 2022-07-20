#키 값 설정 x[0]=이름, x[1]= 점수
def setting(x):
    return x[1]



n=int(input())

a=[]

for i in range(n):
    data=input().split()
    a.append((data[0],int(data[1])))

a=sorted(a,key=setting)

for i in range(n):
    s=a[i]
    for j in range(1):
        print(s[0],end=" ")