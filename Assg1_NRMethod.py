import math
x0 = 0
x1 = x0
eps_max = 5 * math.pow(10, -7)
eps = 1.0
itn = 0
itn_max = 10

while itn<itn_max:
    if eps <= eps_max:
        f = x1**3 + x1 -1
        print("solution in %d iterations is: %f and function value = %f" %(itn, x1, f))
        if f == 0:
            print("we found f = 0 in %d iterations" %(itn))
            break
    x0 = x1
    itn = itn + 1
    f0 = x0**3 + x0 - 1
    f_dev0 = 3*x0**2 + 1
    x1 = x0 - (f0/f_dev0)
    eps = x1 - x0
