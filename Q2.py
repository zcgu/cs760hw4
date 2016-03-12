import math

def s(x):
    di = math.pow(math.e, (- 1.0 * x))
    return 1.0 / (1.0 + 1.0 * di)

for x1 in range(0, 2):
    for x2 in range(0, 2):
        for x3 in range(0, 2):
            for x4 in range(0, 2):
                o1 = s(x1 + x2 - 1.5)
                o2 = s(x3 + x4 - 1.5)
                o = s(o1 + o2 - 0.78)

                truth = (x1 == 1 and x2 == 1) or (x3 == 1 and x4 == 1)

                print(x1, x2, x3, x4, truth, o)
