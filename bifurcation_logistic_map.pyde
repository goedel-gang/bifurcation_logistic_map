# vim: ft=python

from find_stable_points import stable_points, decimal, logi_map

LO = 2.4
HI = 3.9
RES = 1080
PREC = 6
PER_FRAME = 1

def draw_bifurcation(lo, hi, n, prec):
    print("drawing {} points from {} to {}, with precision of {}dp".format(n, lo, hi, prec))
    for i in xrange(n):
        r = lo + (hi - lo) * float(i) / n
        for osc in stable_points(prec, lambda x: logi_map(x, decimal.Decimal(r))):
            point(float(i) * width / n, float(osc) * height)
        yield

def setup():
    global drawfunc
    size(1080, 720)
    background(0)
    stroke(255)
    drawfunc = draw_bifurcation(LO, HI, RES, PREC)

def draw():
    try:
        for _ in xrange(PER_FRAME):
            next(drawfunc)
    except StopIteration:
        pass
