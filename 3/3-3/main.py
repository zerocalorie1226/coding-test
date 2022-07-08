while True:
    n, k = map(int, input("n값과 k의 값을 입력해주세요:").split())

    if n>=k:
        break

    print("k값보다 큰 n의 값을 입력해주세요.")

a=0

while n>=k:

    while n%k!=0:
        n-=1
        a+=1

    n=n//k
    a+=1

while True:
    if n == 1:
        break
    n -= 1
    a += 1


print(a)

