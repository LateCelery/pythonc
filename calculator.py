# Online Python - IDE, Editor, Compiler, Interpreter
print ("""
+ add
- sub 
/ dev
* m
// quotient 
% remander 
^ ext
root sqr
""")



def a(x, y):
    print (x + y)
def s(x, y):
    print (x - y)
def d(x, y):
    print (x / y)
def m(x, y):
    print (x * y) 
def ext(x, y):
    print (x ** y)
def quo(x, y):
    print (x // y)
def mod(x, y):
    print (x % y)
def sqt(x):
    print (ext (x, 0.5))


first = float (input("number 1: " ))

sign = input("sign: " )

sec = float (input("number 2: " ))

if sign == "+":
    a (first, sec)

if sign == "-":
    s (first, sec)

if sign == "/":
    d (first, sec)

if sign == "*":
    m (first, sec)

if sign == "^":
    ext (first, sec)


if sign == "//":
    quo (first, sec)


if sign == "root":
    sqt (first)

if sign == "%":
    mod (first, sec)
