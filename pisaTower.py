from matplotlib import pyplot as plt
import math
import numpy as np
from scipy.integrate import nquad
from math import sin, cos, sqrt

# constants
summer = -23.5 * (math.pi/180)
winter = 23.5 * (math.pi/180)
fall = 11.75 * (math.pi/180)
spring = -11.75 * (math.pi/180)
equinox = 0 * (math.pi/180)
latitude = 43.7230136 * math.pi/180
area = 3456.471540


def N(u):
    return np.array([9.884306153*cos(u),
                     -9.837153075*sin(u),
                     -0.6794325803*sin(u)])

# Vector field. Dependent on Latitude (L), and season of the year (s).
# Summer s = -23.5, Winter = 23.5, equinox s = 0, Spring = -11.25, Fall s = 11.25
def V(s,t):
    return np.array([-cos(t)*cos(s),
                     cos(latitude)*sin(s) + sin(latitude)*sin(t)*cos(s),
                     sin(latitude)*sin(s) - cos(latitude)*sin(t)*cos(s)])

# Returns the value of the sunrise and the sunset at specific latitude and part of the year.
def get_sunrise_and_sunset(s):
    sunrise = math.asin((sin(latitude)*sin(s)/(cos(latitude)*cos(s))))
    return sunrise, math.pi - sunrise

def pisa(s):
    sunrise, sunset = get_sunrise_and_sunset(s)
    integrall = lambda u, t: 56.67*np.dot(V(s,t), N(u)) - (-0.6761758113*sin(-u) + 0.9478158778)*np.dot(V(s,t), N(u))

    def u_boundary(t):
        return [(5*math.pi)/2 + t,(3*math.pi)/2 + t]

    def t_boundary():
        return [sunrise, sunset]

    result, error, somehin = (nquad(integrall, [u_boundary, t_boundary], full_output=True))
    print(result)

    number_of_iterations = int((6 + (sunset*12/math.pi)) - (6 + (sunrise*12/math.pi)))
    print("numL ",number_of_iterations)
    loop_step = (sunset - sunrise) / 15

    final_answer = 0
    total_errors = 0


    time = sunrise + loop_step
    old_time = sunrise

    plot_points = [[],[]]
    while time < sunset:


        integrall = lambda u,t: 56.67*np.dot(V(s,t), N(u)) - (-0.6761758113*sin(-u) + 0.9478158778)*np.dot(V(s,t), N(u))

        def u_boundary(t):
            return [(5 * math.pi) / 2 + t, (3 * math.pi) / 2 + t]

        def t_boundary():
            return [old_time, time]

        result, error, somehin = (nquad(integrall, [u_boundary, t_boundary], full_output=True))
        print(result)
        total_errors += error
        final_answer += result

        # adding points for the plot. We want our flux to be per area and time to be converted to 24. hour thing.
        plot_points[0].append(6 + (time*12/math.pi) ) # Converting to normal hours.
        plot_points[1].append(result / area)

        #change
        old_time += loop_step
        time += loop_step
    else:
        pass


    print(final_answer)


    return plot_points

def plot_flux(points, season_name, color):
    plt.plot(points[0], points[1],label="time step 0.1", color=color)
    plt.xlabel("time of the day [hrs]")
    plt.ylabel("Energy per area [kWh/m^2]")
    plt.xticks([round(value,2) for value in points[0][::2]])
    plt.yticks([round(value, 3) for value in points[1]])
    return

if __name__ == "__main__":
    points = pisa(fall)
    plot_flux(points, "Fall", color="orange")

    points = pisa(summer)
    plot_flux(points, "summer", color="red")

    points = pisa(equinox)
    plot_flux(points, "equinox + equator", color="black")

    points = pisa(winter)
    plot_flux(points, "winter", color="blue")

    points = pisa(spring)
    plot_flux(points, "spring", color="green")
    plt.legend(['Fall', 'Summer', 'Equator', 'Winter', 'Spring'])
    plt.title("Pisa Tower's energy yield per day throughout seasons")
    plt.show()