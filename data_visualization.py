# Import Statements
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
asteroidDataRaw=pd.read_csv('AstroStats_Robbins_Moon.csv', sep=',')

# TODO: Add data cleaning by checking for values of diameter and ellipticity > 0

# Define area of crater series using diameter of the major
# axis of the crater from an ellipse fit
ellipseArea = np.pi * asteroidDataRaw["DIAM_ELLI_MAJOR_IMG"] * asteroidDataRaw["DIAM_ELLI_MINOR_IMG"]

# Calculate cutoffs for a crater to be defined as a "circular crater"
circle_cutoff_ellip = 1.16 # Ellipticity less than this number is a circle

# All craters' diameters less than or equal to this number are "small"
small_cutoff_diam = 100

# Define circle craters by ellipticity
circle_craters_ellip = asteroidDataRaw[asteroidDataRaw["DIAM_ELLI_ELLIP_IMG"] < circle_cutoff_ellip]

# Seperate craters by diameter
small_craters = asteroidDataRaw[asteroidDataRaw["DIAM_ELLI_MAJOR_IMG"] <= small_cutoff_diam]
large_craters = asteroidDataRaw[asteroidDataRaw["DIAM_ELLI_MAJOR_IMG"] > small_cutoff_diam]


def plot_size_ellip():
    # Graph of crater diameter (major ellipse diameter) vs. ellipticity
    plt.figure()
    plt.plot(asteroidDataRaw["DIAM_ELLI_MAJOR_IMG"], asteroidDataRaw["DIAM_ELLI_ELLIP_IMG"], 'o', markersize=0.3)
    plt.axhline(y=circle_cutoff_ellip, color='r', linestyle='--')
    plt.axvline(x=small_cutoff_diam, color='k', linestyle='-.')
    plt.xscale("log")
    plt.xlabel("Lunar Crater Major Axis Diameter (km)")
    plt.ylabel("Lunar Crater Ellipticity (unitless)")
    plt.title("Relationship Between Lunar Crater Ellipticity and Major Axis Diameter")
    plt.legend(["Lunar Craters", "Elliptical Cutoff", "Large Crater Cutoff"])

    # Same graph, only small craters
    # plt.figure()
    # plt.plot(small_craters["DIAM_ELLI_MAJOR_IMG"], small_craters["DIAM_ELLI_ELLIP_IMG"], 'o', markersize=0.5)
    # plt.xscale("log")
    # plt.xlabel("Diameter of the crater from an ellipse fit (km)")
    # plt.ylabel("Ellipticity (unitless)")
    # plt.title("Diameter vs Ellipticity of Lunar Craters")
    #
    # # Same graph, only large craters
    # plt.figure()
    # plt.plot(large_craters["DIAM_ELLI_MAJOR_IMG"], large_craters["DIAM_ELLI_ELLIP_IMG"], 'o', markersize=0.5)
    # plt.xscale("log")
    # plt.xlabel("Diameter of the crater from an ellipse fit (km)")
    # plt.ylabel("Ellipticity (unitless)")
    # plt.title("Diameter vs Ellipticity of Lunar Craters")

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
    # (defined having an ellipticity below circle_cutoff_ellip)
    # circleArea = np.pi * (circle_craters_ellip["DIAM_CIRC_IMG"] / 2) ** 2
    plt.figure()
    ax = sns.histplot(circle_craters_ellip["DIAM_CIRC_IMG"], bins=50, log_scale=True, linewidth=0.5, stat='density', color='#994F00')
    sns.kdeplot(circle_craters_ellip["DIAM_CIRC_IMG"], log_scale=True, ax=ax, color='#006CD1', linewidth=3)
    plt.xlabel("Diameter of the circular craters from an circular fit (km)")
    plt.ylabel("Frequency")
    plt.title("Size-Frequency of Circular Lunar Craters")

    # Alternative version of above in case we don't want to use seaborn
    # plt.hist(circleArea, bins=50)
    # plt.xscale("log")

    ## Code left just for reference that eccentricity and ellipticity
    ## cutoffs look to be the same graph
    # circle_craters_ecc = asteroidDataRaw[asteroidDataRaw["DIAM_ELLI_ECCEN_IMG"] < circle_cutoff_ecc]
    # circleArea_alt = np.pi * (circle_craters_ecc["DIAM_CIRC_IMG"] / 2) ** 2
    # plt.figure()
    # ax2 = sns.histplot(circleArea_alt, bins=50, log_scale=True, linewidth=0.5, stat='density')
    # sns.kdeplot(circleArea_alt, log_scale=True, ax=ax2, color='r')
    # plt.xlabel("Area of the circular craters from an circular fit (km)")
    # plt.ylabel("Frequency")
    # plt.title("Size-Frequency of  Circular Lunar Craters (Eccentricity Cutoff)")

def plot_small_ellip_freq():
    plt.figure()
    plt.hist(small_craters["DIAM_ELLI_ELLIP_IMG"], bins=50)
    plt.xlabel("Ellipticity of the small craters (km)")
    plt.ylabel("Frequency")
    plt.title("Ellipticity Frequency of Small Lunar Craters")

def plot_large_ellip_freq():
    plt.figure()
    plt.hist(large_craters["DIAM_ELLI_ELLIP_IMG"], bins=50)
    plt.xlabel("Ellipticity of the large craters (km)")
    plt.ylabel("Frequency")
    plt.title("Ellipticity Frequency of Large Lunar Craters")

# Calling plotting functions
plot_size_ellip()
# plot_size_eccent()
# plot_circle_size_freq()
# plot_small_ellip_freq()
# plot_large_ellip_freq()

plt.show()
