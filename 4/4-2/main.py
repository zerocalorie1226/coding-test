column=['a','b','c','d','e','f','g','h']
row=['1','2','3','4','5','6','7','8']

location=list(input())
print(location)

o=0
#나이트가 갈 수 있는 방법
method=[(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)]

for step in method:
    n = column.index(location[0])
    m = row.index(location[1])

    n1=n+step[0]
    m1=m+step[1]

    if n1>=1 and n1<=8 and m1>=1 and m1<=8:
        o+=1

print(o)
