N = int(input())
X = int(input())
count = 0
c = 0
for i in range(X):
    star = int(input())
    c += star * N
    if(c >= 40000000):
        count += 1
        c = 0
print(count)