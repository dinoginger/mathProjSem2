import matplotlib
import math
import numpy as np
from scipy.integrate import nquad
from math import sin, cos, sqrt
sunrise = 0.5182846413
sunset = 2.623308013


def main():


    def range_u(v, t):
        return [0, 180]

    def range_v(t):
        return (t, math.pi + t)

    def range_t():
        return [sunrise, sunset]

    #result, error = (nquad(integrand, [range_u, range_v, range_t]))
    #print('Result is ', abs(result), 'with error ', error) # Result is  16661.078130317885 with error  3.596560418372974e-06

    i = sunrise
    old_i = sunrise
    total_result = 0
    print(i)
    while i < sunset-0.1:
        integrand = lambda u, v: np.dot(V(i), N(u, v))
        i += 0.1
        def rangee_u(v):
            return [0,180]
        def rangee_v():
            return [i, math.pi + i]
        print(old_i, i)
        #print(f"{i}, {old_i}")
        old_i = i
        result, error, somehin = (nquad(integrand, [rangee_u, rangee_v], full_output=True))
        total_result += result
    print(total_result)


def N(u,v):
    return np.array([-1*math.sin(v)*math.sqrt(600.25 + 4.352279728*(10**(-6))*(u**4) - 0.001504000694*u**3 + 0.1105036829*u**2 + 0.121741986800003*u),
                     -1*math.cos(v)*math.sqrt(600.25 + 4.352279728*(10**(-6))*(u**4) - 0.001504000694*u**3 + 0.1105036829*u**2 + 0.121741986800003*u),
                     8.704559455*(10**(-6))*(u + 0.544778599834209)*(u - 66.4000000544333)*(u - 193.319416005557)])

def V(t):
    return np.array([-0.9304175680*math.cos(t),
                     0.2281023137 + 0.7282534563*math.sin(t),
                     0.2868666653 - 0.5790714587*math.sin(t)])


def range_u(v,t):
    return [0,180]

def range_v(t):
    return (t, math.pi + t)

def range_t():
    return [sunrise,sunset]

if __name__ == "__main__":
    main()