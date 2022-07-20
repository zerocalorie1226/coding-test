n=int(input())

a=[]

for i in range(n):
    a.append(int(input()))

a.sort()
a.reverse()

for i in a:
    print(i,end=" ")
