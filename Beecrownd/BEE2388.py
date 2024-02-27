x = int(input())
sum = 0
for i in range(x):
    n, m = input().split()
    sum += int(n) * int(m)
print(sum)