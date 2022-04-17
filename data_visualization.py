# Import Statements
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
asteroidDataRaw=pd.read_csv('AstroStats_Robbins_Moon.csv', sep=',')

# Clean data by only using craters whose diameter and ellipticity are both 0
asteroidData = asteroidDataRaw[(asteroidDataRaw["DIAM_ELLI_ELLIP_IMG"] > 0) & (asteroidDataRaw["DIAM_ELLI_MAJOR_IMG"] > 0)]

# All crater ellipticity over this number are define as an "elliptical crater"
elliptic_cutoff_ellip = 1.16

# All crater diameters (km) greater than this number are "large" craters
large_crater_cutoff = 100

# Define dataframes of craters by shape
circle_craters = asteroidData[asteroidData["DIAM_ELLI_ELLIP_IMG"] < elliptic_cutoff_ellip]
ellipse_craters = asteroidData[asteroidData["DIAM_ELLI_ELLIP_IMG"] > elliptic_cutoff_ellip]

# Define dataframes of craters by size
small_craters = asteroidData[asteroidData["DIAM_ELLI_MAJOR_IMG"] <= large_crater_cutoff]
large_craters = asteroidData[asteroidData["DIAM_ELLI_MAJOR_IMG"] > large_crater_cutoff]

# Define area of crater series using the crater's major axis diameter
# from an ellipse fit (later unused as we use only diameter instead of area)
ellipseArea = np.pi * asteroidData["DIAM_ELLI_MAJOR_IMG"] * asteroidData["DIAM_ELLI_MINOR_IMG"]


def plot_size_ellip():
    # Graph of crater diameter (major ellipse diameter) vs. ellipticity
    plt.figure()
    plt.plot(asteroidData["DIAM_ELLI_MAJOR_IMG"], asteroidData["DIAM_ELLI_ELLIP_IMG"], 'o', markersize=0.3)
    plt.axhline(y=elliptic_cutoff_ellip, color='r', linestyle='--')
    plt.axvline(x=large_crater_cutoff, color='k', linestyle='-.')
    plt.xscale("log")
    plt.xlabel("Lunar Crater Major Axis Diameter (km)")
    plt.ylabel("Lunar Crater Ellipticity (unitless)")
    plt.title("Relationship Between Lunar Crater Ellipticity and Major Axis Diameter")
    plt.legend(["Lunar Craters", "Elliptical Cutoff", "Large Crater Cutoff"])

def plot_small_size_ellip():
    # Graph of only small craters' diameter (major ellipse diameter) vs. ellipticity
    plt.figure()
    plt.plot(small_craters["DIAM_ELLI_MAJOR_IMG"], small_craters["DIAM_ELLI_ELLIP_IMG"], 'o', markersize=0.5)
    plt.axhline(y=elliptic_cutoff_ellip, color='r', linestyle='--')
    plt.xscale("log")
    plt.xlabel("Lunar Crater Major Axis Diameter (km)")
    plt.ylabel("Lunar Crater Ellipticity (unitless)")
    plt.title("Relationship Between Small Lunar Crater Ellipticity and Major Axis Diameter")
    plt.legend(["Lunar Craters", "Elliptical Cutoff"])

def plot_large_size_ellip():
    # Graph of only small craters' diameter (major ellipse diameter) vs. ellipticity
    plt.figure()
    plt.plot(large_craters["DIAM_ELLI_MAJOR_IMG"], large_craters["DIAM_ELLI_ELLIP_IMG"], 'o', markersize=0.5)
    plt.axhline(y=elliptic_cutoff_ellip, color='r', linestyle='--')
    plt.xscale("log")
    plt.xlabel("Lunar Crater Major Axis Diameter (km)")
    plt.ylabel("Lunar Crater Ellipticity (unitless)")
    plt.title("Relationship Between Large Lunar Crater Ellipticity and Major Axis Diameter")
    plt.legend(["Lunar Craters", "Elliptical Cutoff"])

def plot_area_eccent():
    # Graph of crater area (assuming an ellipse fit) vs. Eccentricity
    plt.figure()
    plt.plot(ellipseArea, asteroidData["DIAM_ELLI_ECCEN_IMG"], 'o', markersize=0.5)
    plt.xscale("log")
    plt.xlabel("Area of the crater from an ellipse fit (km)")
    plt.ylabel("Eccentricity (unitless)")
    plt.title("Area vs Eccentricity of Lunar Craters")

def plot_circle_size_freq():
    # Graph of size-frequency of all circular craters (defined having an
    # ellipticity below elliptic_cutoff_ellip)

    plt.figure()
    ax = sns.histplot(circle_craters["DIAM_CIRC_IMG"], bins=50, log_scale=True, linewidth=0.5, stat='density', color='#994F00')
    sns.kdeplot(circle_craters["DIAM_CIRC_IMG"], log_scale=True, ax=ax, color='#006CD1', linewidth=3)
    plt.xlabel("Diameter of the circular craters from an circular fit (km)")
    plt.ylabel("Frequency")
    plt.title("Size-Frequency of Circular Lunar Craters")
    plt.legend(["KDE Plot", "Lunar Craters"])


    # Alternative version of above in case we don't want to use seaborn
    # plt.hist(circleArea, bins=50)
    # plt.xscale("log")

    ## Code left just for reference that eccentricity and ellipticity
    ## cutoffs look to be the same graph
    # circle_craters_ecc = asteroidData[asteroidData["DIAM_ELLI_ECCEN_IMG"] < circle_cutoff_ecc]
    # circleArea_alt = np.pi * (circle_craters_ecc["DIAM_CIRC_IMG"] / 2) ** 2
    # plt.figure()
    # ax2 = sns.histplot(circleArea_alt, bins=50, log_scale=True, linewidth=0.5, stat='density')
    # sns.kdeplot(circleArea_alt, log_scale=True, ax=ax2, color='r')
    # plt.xlabel("Area of the circular craters from an circular fit (km)")
    # plt.ylabel("Frequency")
    # plt.title("Size-Frequency of  Circular Lunar Craters (Eccentricity Cutoff)")

def plot_small_ellip_freq():
    # Graph of only small crater's ellipticity frequency
    plt.figure()
    plt.hist(small_craters["DIAM_ELLI_ELLIP_IMG"], bins=50)
    plt.xlabel("Ellipticity of the small craters (km)")
    plt.ylabel("Frequency")
    plt.title("Ellipticity Frequency of Small Lunar Craters")

def plot_large_ellip_freq():
    # Graph of only large crater's ellipticity frequency
    plt.figure()
    plt.hist(large_craters["DIAM_ELLI_ELLIP_IMG"], bins=50)
    plt.xlabel("Ellipticity of the large craters (km)")
    plt.ylabel("Frequency")
    plt.title("Ellipticity Frequency of Large Lunar Craters")

# Calling plotting functions
# plot_size_ellip()
# plot_small_size_ellip()
# plot_large_size_ellip()

# plot_area_eccent()

# plot_circle_size_freq()

# plot_small_ellip_freq()
# plot_large_ellip_freq()

plt.show()
