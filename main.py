from matplotlib import pyplot as plt
import math
import numpy as np
from scipy.integrate import nquad
from math import sin, cos, sqrt


sunrise = 0.5182846413
sunset = 2.623308013

def V(t):
    return np.array([-0.9304175680*math.cos(t),
                     0.2281023137 + 0.7282534563*math.sin(t),
                     0.2868666653 - 0.5790714587*math.sin(t)])

def N(u,v):
    return np.array([-1*math.sin(v)*math.sqrt(600.25 + 4.352279728*(10**(-6))*(u**4) - 0.001504000694*u**3 + 0.1105036829*u**2 + 0.121741986800003*u),
                     -1*math.cos(v)*math.sqrt(600.25 + 4.352279728*(10**(-6))*(u**4) - 0.001504000694*u**3 + 0.1105036829*u**2 + 0.121741986800003*u),
                     8.704559455*(10**(-6))*(u + 0.544778599834209)*(u - 66.4000000544333)*(u - 193.319416005557)])

def gherkin_realistic():
    integrall = lambda u, v, t: np.dot(V(t), N(u, v))
    def u_boundary(v, t):
        return [0, 180]

    def v_boundary(t):
        return (t, math.pi + t)

    def t_boundary():
        return [sunrise, sunset]

    result, error, somehin = (nquad(integrall, [u_boundary, v_boundary, t_boundary], full_output=True))
    print(result)
    loop_step = 0.1

    final_answer = 0
    total_errors = 0


    time = sunrise + loop_step
    old_time = sunrise

    plot_points = [[],[]]
    while time < sunset:


        integrall = lambda u,v,t: np.dot(V(t),N(u,v))

        def u_boundary(v,t):
            return [0, 180]

        def v_boundary(t):
            return (t, math.pi + t)

        def t_boundary():
            return (old_time, time)


        result, error, somehin = (nquad(integrall, [u_boundary, v_boundary, t_boundary], full_output=True))
        print(result)
        total_errors += error
        final_answer += result

        # adding points for the plot
        plot_points[0].append(time)
        plot_points[1].append(result)

        #change
        old_time += loop_step
        time += loop_step

    plot_flux(plot_points)

def plot_flux(points):
    plt.plot(points[0], points[1], 'go-',label="time step 0.1")
    plt.xlabel("time [hrs]")
    plt.ylabel("Energy per area [kWh/m^2]")
    plt.title("Gherkin Tower")
    plt.show()

if __name__ == "__main__":
    gherkin_realistic()