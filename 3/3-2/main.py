n, m = map(int, input().split())
c = 0
for i in range(n):
    while True:
        a = list(map(int, input().split()))
        if (len(a) == m):
            break
        print(m, "개의 숫자를 입력하세요.")
    b = min(a)
    c = max(b, c)

print(c)

