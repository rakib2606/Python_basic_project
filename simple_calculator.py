def result(a,b,c):
    a = float(a)
    c= float(c)

    if b == "+":
        res = a+c
    elif b == "-":
        res = a-c
    elif b == "*":
        res = a*c
    elif b == "/":
        res = a/c
    else:
        return a

    print(f"{a} {b} {c} = {res}")
    return res

a,b,c = input().split()
a = result(a,b,c)
while True:
    b,c = input().split()
    a = result(a,b,c)
