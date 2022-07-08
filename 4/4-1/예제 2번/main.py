n=int(input())
t=0
for a in range(n+1):
    for b in range(60):
        for c in range(60):
            if "3" in str(a)+str(b)+str(c) :
                t+=1
print(t)

