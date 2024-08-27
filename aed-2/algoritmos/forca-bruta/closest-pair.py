'''
Closest Pair of Points Problem by brute force
input: list P of n(n>= 2) points p1(x1,y1),...,pn(xn,yn)
output: the distance between the closest pair of points
'''

def ClosestPair(p1, p2):
    d = float('inf')
    for i in range(n):
        for j in range(i+1, n):
            d = min(d, ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5)
    return d

P = [(1, 2), (3, 4), (5, 6), (7, 8)]
n = len(P)
print(ClosestPair(P[0], P[1]))