import math


def s(x):
    di = math.pow(math.e, (- 1.0 * x))
    return 1.0 / (1.0 + 1.0 * di)

############################################################
# w0a = 0.1
# wx1a = -0.8
# wx2a = 0.3
#
# w0b = 0.3
# wx1b = 0.2
# wx2b = -0.4
#
# w0c = -0.6
# wac = 0.4
# wbc = 0.7
#
# w0d = -0.5
# wad = -0.7
# wbd = 0.6
#
# x1 = 1
# x2 = 1
#
# y1 = 0
# y2 = 1
#
###################################################################

w0a = -1.0
wx1a = 0.5
wx2a = 0.5

w0b = -1.0
wx1b = 2.0
wx2b = -0.5

w0c = -2.0
wac = 2.0
wbc = 2.0

w0d = 0.0
wad = 1.0
wbd = 0.5

x1 = 1.0
x2 = 0.0

y1 = 0
y2 = 1

##############################################################

a = s(w0a + wx1a * x1 + wx2a * x2)
b = s(w0b + wx1b * x1 + wx2b * x2)
c = s(w0c + wac * a + wbc * b)
d = s(w0d + wad * a + wbd * b)

print(a, b, c, d)

rc = - (y1 - c) * c * (1 - c)
rd = - (y2 - d) * d * (1 - d)

ra = (wac * rc) * a * (1 - a) + (wad * rd) * a * (1 - a)
rb = (wbc * rc) * b * (1 - b) + (wbd * rd) * b * (1 - b)

print(rc, rd, ra, rb)

w0a -= 0.1 * ra
wx1a -= 0.1 * ra * x1
wx2a -= 0.1 * ra * x2

w0b -= 0.1 * rb
wx1b -= 0.1 * rb * x1
wx2b -= 0.1 * rb * x2

w0c -= 0.1 * rc
wac -= 0.1 * rc * a
wbc -= 0.1 * rc * b

w0d -= 0.1 * rd
wad -= 0.1 * rd * a
wbd -= 0.1 * rd * b

print(w0a, wx1a, wx2a)
print(w0b, wx1b, wx2b)
print(w0c, wac, wbc)
print(w0d, wad, wbd)

