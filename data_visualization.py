# Import Statements
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import data
asteroidDataRaw=pd.read_csv('AstroStats_Robbins_Moon.csv', sep=',')

# Define area of crater dataframe using diameter of the major
# axis of the crater from an ellipse fit
ellipseArea = np.pi * asteroidDataRaw["DIAM_ELLI_MAJOR_IMG"] * asteroidDataRaw["DIAM_ELLI_MINOR_IMG"]

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

# Calling plotting functions
plot_size_ellip()
plot_size_eccent()
plt.show()
