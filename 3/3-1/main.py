while True:
    n, m, k = map(int, input().split())
    if (k <= m):
        break
    print("m보다 작은 k의 값을 입력해주세요.")

while True:

    a = list(map(int, input().split()))
    if (len(a) == n):
        break
    print(n, "개의 정수를 입력해주세요", )

a.sort()
print(a)

x = a[n - 1]
y = a[n - 2]
z = 0
r = 0

for i in range(m):
    if (r == k):
        z += y
        r = 0
    else:

        z += x
        r += 1

print(z)
