a = x = 2
b = 5
h = 0.3
for i in range(int((b-a)/h)+1):
    #x = a + i * h
    y = x ** 2
    print(x, y)
    #x += h