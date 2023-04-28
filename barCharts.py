import matplotlib.pyplot as plt
import numpy as np


# Notation: [equinox, spring, summer, fall, winter]
giza_flux = np.array([1.70,1.94,2.16,1.43,1.15])
gherkin_flux = np.array([0.93,1.01,1.09,0.81,0.62])
pisa_flux = np.array([0.82,0.83,0.82,0.77,0.68])


def plot_bar():
    width = 0.60  # the width of the bars: can also be len(x) sequence
    names = ["Equinox", "Spring (-11.75°)", "Summer", "Autumn (11.75°)", "Winter"]

    p1 = plt.bar(names, giza_flux, width)
    p2 = plt.bar(names, gherkin_flux, width,
                 bottom=giza_flux)
    p3 = plt.bar(names, pisa_flux, width,
                 bottom=gherkin_flux + giza_flux)

    plt.ylabel('Energy per area [kWh/m^2]')
    plt.xlabel('Season of the year')
    plt.title('Comparison of energy per area for structures throughout the year')
    plt.legend((p1[0], p2[0], p3[0]), ('Great Pyramid of Giza', 'Gherkin', 'Leaning Tower of Pisa'))

if __name__ == "__main__":
    plot_bar()
    plt.show()