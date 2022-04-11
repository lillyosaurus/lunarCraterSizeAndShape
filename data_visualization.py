# Import Statements
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
asteroidDataRaw=pd.read_csv('AstroStats_Robbins_Moon.csv', sep=',')

# Define area of crater series using diameter of the major
# axis of the crater from an ellipse fit
ellipseArea = np.pi * asteroidDataRaw["DIAM_ELLI_MAJOR_IMG"] * asteroidDataRaw["DIAM_ELLI_MINOR_IMG"]


## Create a series
circle_cutoff_ecc = 0.4 # Eccentricity less than this number is a circle
circle_cutoff_ellip = 1.16 # Ellipticity less than this number is a circle

# Define circle craters by ellipticity
circle_craters_ellip = asteroidDataRaw[asteroidDataRaw["DIAM_ELLI_ECCEN_IMG"] < circle_cutoff_ellip]
# Define circle craters by eccentricity
circle_craters_ecc = asteroidDataRaw[asteroidDataRaw["DIAM_ELLI_ECCEN_IMG"] < circle_cutoff_ecc]

def plot_size_ellip():
    # Goal: Graph of Crater area (assuming an ellipse fit) vs.
    # Ellipticity (DIAM_ELLI_ELLIP_IMG)
    plt.figure()
    plt.plot(ellipseArea, asteroidDataRaw["DIAM_ELLI_ELLIP_IMG"], 'o', markersize=0.5)
    plt.xscale("log")
    plt.xlabel("Area of the crater from an ellipse fit (km)")
    plt.ylabel("Ellipticity (unitless)")
    plt.title("Area vs Ellipticity of Lunar Craters")

def plot_size_eccent():
    # Goal: Graph of Crater area (assuming an ellipse fit) vs.
    # Eccentricity (DIAM_ELLI_ECCEN_IMG)
    plt.figure()
    plt.plot(ellipseArea, asteroidDataRaw["DIAM_ELLI_ECCEN_IMG"], 'o', markersize=0.5)
    plt.xscale("log")
    plt.xlabel("Area of the crater from an ellipse fit (km)")
    plt.ylabel("Eccentricity (unitless)")
    plt.title("Area vs Eccentricity of Lunar Craters")

def plot_circle_size_freq():
    # Goal: Graph of size-frequency of all circular craters
    # (defined having an eccentricity as below circle_cutoff_ecc)

    circleArea = np.pi * (circle_craters_ecc["DIAM_CIRC_IMG"] / 2) ** 2
    plt.figure()
    ax = sns.histplot(circleArea, bins=50, log_scale=True, linewidth=0.5, stat='density', color='#994F00')
    sns.kdeplot(circleArea, log_scale=True, ax=ax, color='#006CD1', linewidth=3)
    plt.xlabel("Area of the circular craters from an circular fit (km)")
    plt.ylabel("Frequency")
    plt.title("Size-Frequency of Circular Lunar Craters")

    # Alternative version of above in case we don't want to use seaborn
    # plt.hist(circleArea, bins=1000)
    # plt.xscale("log")

    # Code left just for reference that eccentricity and ellipticity cutoffs are the same graph
    # circleArea_alt = np.pi * (circle_craters_ellip["DIAM_CIRC_IMG"] / 2) ** 2
    # plt.figure()
    # ax2 = sns.histplot(circleArea_alt, bins=50, log_scale=True, linewidth=0.5, stat='density')
    # sns.kdeplot(circleArea_alt, log_scale=True, ax=ax2, color='r')
    # plt.xlabel("Area of the circular craters from an ellipse fit (km)")
    # plt.ylabel("Frequency")
    # plt.title("Size-Frequency of  Circular Lunar Craters (Ellipticity Cutoff)")



# Calling plotting functions
plot_size_ellip()
plot_size_eccent()
plot_circle_size_freq()

plt.show()
