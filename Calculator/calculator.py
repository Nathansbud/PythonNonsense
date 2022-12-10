from math import (
    log as logarithm,
    cos, sin, tan, pi, acos, asin, atan, e, 
)

r2d = lambda r: r * (180 / pi)
d2r = lambda d: (d) * (pi/180)

def cosd(deg):  return cos(d2r(deg))
def sind(deg):  return sin(d2r(deg))
def tand(deg): return tan(d2r(deg))

def acosd(deg): return acos(d2r(deg))
def asind(deg): return asin(d2r(deg))
def atand(deg): return atan(d2r(deg))

def log(v, base=10): return logarithm(v, base)
def ln(v): return logarithm(v, e)
def lg(v): return logarithm(v, 2)
