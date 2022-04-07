# Import Statements
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import data
asteroidDataRaw=pd.read_csv('AstroStats_Robbins_Moon.csv', sep=',')
# print(asteroidDataRaw.head())

ellipseArea = np.pi * asteroidDataRaw["DIAM_ELLI_MAJOR_IMG"] * asteroidDataRaw["DIAM_ELLI_MINOR_IMG"]

# Goal: Graph of Diameter of the major axis of the crater from an ellipse fit
# (DIAM_ELLI_MAJOR_IMG) vs. Ellipticity (DIAM_ELLI_ELLIP_IMG)
plt.figure()
plt.plot(ellipseArea, asteroidDataRaw["DIAM_ELLI_ELLIP_IMG"], 'o', markersize=0.5)
plt.xscale("log")
plt.xlabel("Diameter of the major axis of the crater from an ellipse fit (km)")
plt.ylabel("Ellipticity (unitless)")

# Goal: Graph of Diameter of the major axis of the crater from an ellipse fit
# (DIAM_ELLI_MAJOR_IMG) vs. Eccentricity (DIAM_ELLI_ECCEN_IMG)
plt.figure()
plt.plot(ellipseArea, asteroidDataRaw["DIAM_ELLI_ECCEN_IMG"], 'o', markersize=0.5)
plt.xscale("log")
plt.xlabel("Diameter of the major axis of the crater from an ellipse fit (km)")
plt.ylabel("Eccentricity (unitless)")
plt.show()
