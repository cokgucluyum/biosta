import math

def head(a):
    a = str(a)
    a = a.upper()
    print(f"{a} \n"+"-"*50)

def root(x,y=2):
    return x**(1/y)

def linput(a="",b=""):
    print(b)
    i = 0
    l = []
    while i == 0:
        x = input()
        if x != a:
            l.append(x)
        else:
            i += 1
    return l

def sigma(l):
    s = 0
    try:
        for x in l:
            x = float(x)
            s += x
        return s
    except ValueError:
        return "Numbers Only"

def ssq(l):
    ss = 0
    s = 0
    n = len(l)
    try:
        for x in l:
            x = float(x)
            ss += (x**2)
            s += x
        sq = s**2
        ssq = ss-(sq/n)
        return ssq
    except ValueError:
        return "Numbers Only"

def fact(a):
    try:
        a = int(a)
        if a == int(a) and a>0:
            m = 1
            for x in range(1,a+1):
                m *= x
            return m
        else:
            return "Positive Only"
    except ValueError:
        return "Integers only"

def pifunc(l):
    m = 1
    try:
        for x in l:
            x = float(x)
            m *= x
        return m
    except ValueError:
        return "Numbers only"

def mu(l):
    s = 0
    n = len(l)
    try:
        for x in l:
            x = float(x)
            s += x
        return (s/n)
    except ValueError:
        return "Numbers only"
    except ZeroDivisionError:
        return "-"

def stde(l):
    s = 0
    n = len(l)
    try:
        for x in l:
            x = float(x)
            s += x
        mu = s/n
        ds = 0
        for x in l:
            x = float(x)
            d = (x-mu)**2
            ds += d
        dss = ds/n
        return root(dss)
    except ValueError:
        return "Numbers only"

def var(l):
    s = 0
    n = len(l)
    try:
        for x in l:
            x = float(x)
            s += x
        mu = s/n
        ds = 0
        for x in l:
            x = float(x)
            d = (x-mu)**2
            ds += d
        dss = ds/n
        return dss
    except ValueError:
        return "Numbers only"

