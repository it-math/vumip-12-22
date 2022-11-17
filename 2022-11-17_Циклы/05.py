s = 0
x = int(input())
for i in range(1, 10+1):
    s += x ** i / (i + 2)
print(s)