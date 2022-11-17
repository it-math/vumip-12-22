s = 0
x = int(input())
n = 1
while n <= 10:
    s += x ** n / (n + 2)
    n += 1
print(s)