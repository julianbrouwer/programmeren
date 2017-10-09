#ik zet onder elk antwoord of ik deze goed of fout had

a = 3
def f(y):
    global a
    a = 9
    return 2*y + a
print(a)
#goed

x = 1
y = 4
def fun():
    x = 2
    global y
    y = 3
    print(y, end = ' ')
fun()
print(y, end = ' ')
#goed



x = 2
y = 5
def fun():
    y = 3
    global x
    x = 1
    print(x*y, end = ' ')
    return x*y
x = fun()
print(x*y, end = ' ')
#deze had ik niet goed


a = 3
def fun1():
    global a
    print("a:", a, end = ' ')
    b = 7
    a = 0
    return b
def fun2(y):
    a = y + fun1()
    b = 7
    a += 1
    return a
a = 9
fun2(5)
print("a:", a)
#goed


x = 1
y = 4
def doe1():
    global x
    y = 7
    x = 0
    return y
def doe2():
    x = doe1()
    x += 1
    return x
x = doe1()
print(x)
#goed


a = 5
def fun1():
    global a
    b = 2
    a = 4
    return a+b
def fun2(y):
    global a
    a = y + fun1()
    a += 1
    return a
print("a:", a, end = ' ')
a = fun2(3)
print("a:", a)
#goed


x = 1
y = 3
def doe1():
    global x
    y = 4
    x = 0
    return x+y
def doe2():
    x = doe1()
    x += 2
    return x
doe2()
print(x)
#deze had ik niet goed


def doe1():
    y = 7
    x = 0
    return y
def doe2():
    global x
    x = doe1()
    x += 1
doe2()
print(x)
#goed
