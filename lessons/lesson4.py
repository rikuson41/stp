def f():
    x = input("type a number")
    #y = input("type a number")
    x = int(x)
    #y = int(y)
    return x ** 2

def words(string):
    print(string)

def plus(a, b, c, d=2, e=3):
    f = a + b + c + d + e
    print(f)

def divided_2(x):
    return x // 2

def times_4(x):
    return x * 4

x = divided_2(6)
y = times_4(x)
print(y)
