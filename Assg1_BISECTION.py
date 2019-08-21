
import math
xa = 0
xb = 1
xc = 0
eps_max = 5 * math.pow(10, -7)
eps = 1.0
itn = 1
itn_max = 22
while itn<itn_max:
    if eps <= eps_max:
        f = xc*xc*xc + xc -1
        print("solution in %d iterations is: %f and function value = %f" %(itn, xc, f))
        if f == 0:
            print("we found f = 0 in %d iterations" %(itn))
            break
    xp = xc
    itn = itn + 1
    xc = (xa + xb)/2
    eps = xc - xp
    fa = xa*xa*xa + xa - 1
    fc = xc*xc*xc + xc - 1
    if fa*fc < 0:
        xb = xc
    else:
        xa = xc
