import timeit

def dot(a, b):
    return a[0]*b[0]+a[1]*b[1]

def getSupport(d, a, b):
    mx = 10**10
    am = (0, 0)
    bm = (0, 0)
    for el in a:
        if dot(d, el) < mx:
            mx = dot(d, el)
            am = el
    mx = 10**10
    
    for el in b:
        if dot((-d[0], -d[1]), el) < mx:
            mx = dot((-d[0], -d[1]), el)
            bm = el
    
    return (am[0]-bm[0], am[1]-bm[1])

def GJK(a, b):
    x = (0.1, 0.1)
    for k in range(10):
        d = (2*x[0], 2*x[1])
        s = getSupport(d, a, b)
        yk = 0.1
        x = (x[0]*yk+(1-yk)*s[0], x[1]*yk+(1-yk)*s[1])
    return x

print(timeit.timeit(lambda:GJK([(0, 0),(1, 2),(2, 0)], [(1, 3), (1, 4), (2, 4), (2, 3)]), number=10000)/10000)