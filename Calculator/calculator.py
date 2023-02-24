from math import (
    log as logarithm,
    cos, sin, tan, pi, acos, asin, atan, e, sqrt
)

r2d = lambda r: r * (180 / pi)
d2r = lambda d: (d) * (pi/180)

def cosd(deg, rt=6): return round(cos(d2r(deg)), rt)
def sind(deg, rt=6): return round(sin(d2r(deg)), rt)
def tand(deg, rt=6): return round(tan(d2r(deg)), rt)

def acosd(deg, rt=6): return round(acos(d2r(deg)), rt)
def asind(deg, rt=6): return round(asin(d2r(deg)), rt)
def atand(deg, rt=6): return round(atan(d2r(deg)), rt)

def log(v, base=10): return logarithm(v, base)
def ln(v): return logarithm(v, e)
def lg(v): return logarithm(v, 2)
