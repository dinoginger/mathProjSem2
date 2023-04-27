from matplotlib import pyplot as plt
import math
import numpy as np
from scipy.integrate import nquad
from math import sin, cos, sqrt

# At given latitude of Great pyramid of Giza
sunrise = 0.5182846413
sunset = 2.623308013

height = 138
base = 230

# Vector field for the real latitude of Great pyramid of Giza
def V(t):
    return np.array([-cos(t),
                     -0.9910260996*sin(t),
                     -0.1336685075*sin(t)])
# finish later.

def giza():
    # Vector field:
    def V(t):
        return np.array([-cos(t), 0, -sin(t)])

    base = 230
    height = 138

    # East panel normal vector.
    def N(u):
        return np.array([-3/10 + (3*u)/1150,0, u/460 - 1/4])
    # Calculating flux for east panel:
    integrand = lambda u, v, t: np.dot(V(t),N(u))

    def rangee_u(v,t):
        return [-base/2, base/2]

    def rangee_v(t):
        return [-base/2 , base/2]
    def rangee_t():
        return [0 , math.pi - (51.5*math.pi)/180]

    result, error, somehin = (nquad(integrand, [rangee_u, rangee_v, rangee_t()], full_output=True))
    print(result)
    plot_points = [[],[]] # will be list of tuples where each tuple is a coord

    print(i)
    while i < sunset-0.1:
        integrand = lambda u, v: np.dot(V_gherkin(i), N_gherkin(u, v))
        i += 0.1
        def rangee_u(v):
            return [0,180]
        def rangee_v():
            return [i, math.pi + i]
        print(old_i, i)
        #print(f"{i}, {old_i}")
        old_i = i
        result, error, somehin = (nquad(integrand, [rangee_u, rangee_v], full_output=True))
        plot_points[0].append(i)
        plot_points[1].append(result)

        total_result += result
    print(total_result)
    print(plot_points)
    plot_flux(plot_points)


def range_u(v,t):
    return [0,180]

def range_v(t):
    return (t, math.pi + t)

def range_t():
    return [sunrise,sunset]

def plot_flux(points):
    plt.plot(points[0], points[1], 'go-',label="time step 0.1")
    plt.show()

if __name__ == "__main__":
    giza()