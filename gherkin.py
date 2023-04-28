from matplotlib import pyplot as plt
import math
import numpy as np
from scipy.integrate import nquad
from math import sin, cos, sqrt
from pisaTower import get_sunrise_and_sunset, sunVectorField, plot_flux


# constants
summer = -23.5 * (math.pi/180)
winter = 23.5 * (math.pi/180)
fall = 11.75 * (math.pi/180)
spring = -11.75 * (math.pi/180)
equinox = 0 * (math.pi/180)
area = 25202
loop_step = 'define'
AMOUNT_OF_NODES = 15


def N(u,v):
    return np.array([-1*math.sin(v)*math.sqrt(600.25 + 4.352279728*(10**(-6))*(u**4) - 0.001504000694*u**3 + 0.1105036829*u**2 + 0.121741986800003*u),
                     -1*math.cos(v)*math.sqrt(600.25 + 4.352279728*(10**(-6))*(u**4) - 0.001504000694*u**3 + 0.1105036829*u**2 + 0.121741986800003*u),
                     8.704559455*(10**(-6))*(u + 0.544778599834209)*(u - 66.4000000544333)*(u - 193.319416005557)])

def gherkin(lat, season):
    plot_points = [[],[]]

    integrall = lambda u, v, t: np.dot(sunVectorField(season, t,latitude=lat), N(u, v))
    sunrise, sunset = get_sunrise_and_sunset(lat, season)


    def u_boundary(v, t):
        return [0, 180]

    def v_boundary(t):
        return (t, math.pi + t)

    def t_boundary():
        return [sunrise, sunset]

    result, error, somehin = (nquad(integrall, [u_boundary, v_boundary, t_boundary], full_output=True))
    print(result)


    final_answer = 0
    total_errors = 0

    time = sunrise + loop_step
    old_time = sunrise

    while time < sunset:


        integrall = lambda u,v,t: np.dot(sunVectorField(season,t,latitude=lat),N(u,v))

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
        plot_points[0].append(6 + (time*12/math.pi) )
        plot_points[1].append(result / area)

        #change
        old_time += loop_step
        time += loop_step
    print(final_answer)

    return plot_points



if __name__ == "__main__":
    latitude = 51.51 * math.pi / 180
    # as our loop step we need to take something in the middle, so the integrated values wouldnt be relative
    winter_sunrise, winter_sunset = get_sunrise_and_sunset(latitude, winter)
    loop_step = (winter_sunset - winter_sunrise) / AMOUNT_OF_NODES
    print("loop_step", loop_step)
    # list of full fluxes for bar chart

    # --

    points = gherkin(latitude, fall)
    plot_flux(points, "Fall", color="orange")

    points = gherkin(latitude, summer)
    plot_flux(points, "summer", color="red")

    points = gherkin(latitude, equinox)
    plot_flux(points, "equinox", color="black")

    points = gherkin(latitude, winter)
    plot_flux(points, "winter", color="blue")

    points = gherkin(latitude, spring)
    plot_flux(points, "spring", color="green")
    plt.legend(['Autumn (11.75°)', 'Summer', 'Equinox', 'Winter', 'Spring (-11.75°)'])
    plt.title("The Gherkin energy yield per day throughout seasons")
    # init grid
    plt.xticks(list(range(4,20)))
    plt.grid()
    plt.ylim(0.0235,0.043)
    plt.xlim(4,21)

    plt.show()

    #plt.bar(data=[])