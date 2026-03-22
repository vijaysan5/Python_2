# ___ 0001___ Iterator :

# one by one latter is show use print(next(__)) 
"""x = "Honey/Bee"
y = iter(x)

print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))"""
# print(next(y))     >>> Extra Print >>> Error >>> inset ("StopIteration") >>><<<"""


# def __iter__ and __next__ >>> fun's
"""class Number:
    def __iter__ (self):
        self.num = 0
        return self
    def __next__ (self):
        x = self.num
        self.num += 5
        return x
Num = Number()
htz = iter(Num)
print(next(htz))
print(next(htz))
print(next(htz))
print(next(htz))
print(next(htz))
print(next(htz))
"""

# If - else Condition >>> raise > StopIteration :
"""class Value_:
    def __iter__ (self):
        self.num = 0
        return self
    def __next__ (self):
        if self.num < 10 :
            x = self.num
            self.num += 2
            return x
        else :
            raise StopIteration    
Nn = Value_()
new = iter(Nn)
for now in new :
    print( now )"""

# (Loop) While True > use >>> try and except 
"""a = [10, 30, 50, 70]
it_b = iter (a)

while True :
    try :
        print(next (it_b))
    except StopIteration :
        print("End the funtion")
        break"""



##______use >> yield >>> insted of return.

# use >>> yield . For Loop :
"""def new_value():
    yield 1
    yield 3
    yield 5
    yield 7
    yield 9
for san in new_value():
    print(san)"""

# use >>> yield . While Loop :
"""def new_(amount):
    now = 1
    while now <= amount:
        yield now
        now += 1
n = new_(5)
for flow in n:
    print(flow)"""

# use >> max values
"""def more_value(x):
    for a in range(x):
        yield a
k = more_value(870311)
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(k)"""



#____ METHODS :
## " Send() Method : "
"""def san():
    while True :
        new = yield 
        print("Name :", new)
n = san()
next(n)
n.send("Yash")
n.send("France")
n.send("Rose")"""

## " close() Method : "
"""def san_():
    try :
        yield 10
        yield 25
        yield 30
        yield 45
        yield 50
    finally :
        print("san_() fun is completed")
x = san_()
print(next(x))
print(next(x))
x.close()"""

## " Closure Method : "
"""def funA(san_name):
    san_name = san_name  # san_name >>> output my_san = funA("name") or "any name" >>> show this name in output
    def funB():
        print(san_name)
    return funB
my_san = funA("yashVijay")
my_san()

def Outer_():
    print("New_outer function.")
    def Inner_():
        print("New_inner function.")
    Inner_()
Outer_()"""

"""def outer_fun(a):
    b = 23

    def inner_fun(c):
        return a + b + c
    
    return inner_fun

name = outer_fun(21)
new = name (11)
print(new)"""

# _____Decoraters :
 
"""def casechange(function_name):
    def myself():
        return function_name().title()
    return myself
@casechange
def new_self():
    return "HaPpY BiRthDaY>!"
print(new_self())"""

"""def casechange(function_name):
    def myself():
        return function_name()
    return myself

def wish_(function_name):
    def myself():
        return f'Happy {function_name()} to my Family.>>>!'
    return myself

@casechange
@wish_
def Whishing():
    return "Birthday"
print(Whishing())"""






