#--------------------------Function Library Imports---------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#--------------------------Data Imports and cleaning---------------------------
# Import data
asteroidDataRaw=pd.read_csv('AstroStats_Robbins_Moon.csv', sep=',')

# Clean data by only using craters whose ellipticity and diameter are both > 0
asteroidData = asteroidDataRaw[(asteroidDataRaw["DIAM_ELLI_ELLIP_IMG"] >= 0) & \
    (asteroidDataRaw["DIAM_ELLI_MAJOR_IMG"] > 0)]
#use drop na to remove remaining invalid values
asteroidData = asteroidDataRaw.dropna(0, subset=["DIAM_ELLI_ELLIP_IMG", "DIAM_ELLI_MAJOR_IMG"])
print(asteroidData)

#--------------------------Define Cutoff Values---------------------------
# Crater ellipticity greater than this number are "elliptical" craters
ELLIPTIC_CUTOFF_ELLIP = 1.16
# Crater diameters (km) greater than this number are "large" craters
LARGE_CRATER_CUTOFF = 100

#--------------------------Functions kept to show process---------------------------
def plot_circle_size_freq(df, bins):
    # Graph of size-frequency of all circular craters (defined having an
    # ellipticity below ELLIPTIC_CUTOFF_ELLIP)
    plt.figure()
    sns.histplot(df["DIAM_CIRC_IMG"], bins=bins, log_scale=True, linewidth=0.5, stat='density', color='#994F00')
    plt.xlabel("Diameter of the circular craters from an circular fit (km)")
    plt.ylabel("Frequency")
    plt.title("Size-Frequency of Circular Lunar Craters")

    # Alternative version of above in case we don't want to use seaborn
    # plt.hist(df["DIAM_CIRC_IMG"], bins=50)
    # plt.xscale("log")

def plot_small_ellip_freq(df, bins):
    # Graph of only the small craters' ellipticity frequency
    plt.figure()
    plt.hist(df["DIAM_ELLI_ELLIP_IMG"], bins=bins)
    plt.xlabel("Ellipticity of the small craters (km)")
    plt.ylabel("Frequency")
    plt.title("Ellipticity Frequency of Small Lunar Craters")

def plot_large_ellip_freq(df, bins):
    # Graph of only large craters' ellipticity frequency
    plt.figure()
    plt.hist(df["DIAM_ELLI_ELLIP_IMG"], bins=bins)
    plt.xlabel("Ellipticity of the large craters (km)")
    plt.ylabel("Frequency")
    plt.title("Ellipticity Frequency of Large Lunar Craters")

def plot_small_size_ellip(df, markersize):
    # Graph of only small craters' diameter (major ellipse diameter) vs. ellipticity
    plt.figure()
    plt.plot(df["DIAM_ELLI_MAJOR_IMG"], df["DIAM_ELLI_ELLIP_IMG"], 'o', markersize=markersize)
    plt.axhline(y=ELLIPTIC_CUTOFF_ELLIP, color='r', linestyle='--')
    plt.xscale("log")
    plt.xlabel("Lunar Crater Major Axis Diameter (km)")
    plt.ylabel("Lunar Crater Ellipticity (unitless)")
    plt.title("Relationship Between Small Lunar Crater Ellipticity and Major Axis Diameter")
    plt.legend(["Lunar Craters", "Elliptical Cutoff"])

def plot_large_size_ellip(df, markersize):
    # Graph of only small craters' diameter (major ellipse diameter) vs. ellipticity
    plt.figure()
    plt.plot(df["DIAM_ELLI_MAJOR_IMG"], df["DIAM_ELLI_ELLIP_IMG"], 'o', markersize=markersize)
    plt.axhline(y=ELLIPTIC_CUTOFF_ELLIP, color='r', linestyle='--')
    plt.xscale("log")
    plt.xlabel("Lunar Crater Major Axis Diameter (km)")
    plt.ylabel("Lunar Crater Ellipticity (unitless)")
    plt.title("Relationship Between Large Lunar Crater Ellipticity and Major Axis Diameter")
    plt.legend(["Lunar Craters", "Elliptical Cutoff"])

def random_asteroid_sample(frac_samples):
    # Create dataframe with random sampling of the original Robbins' database
    randomAsteroidData = asteroidData.sample(frac=frac_samples, axis='index')
    return randomAsteroidData

#--------------------------Functions used in current analysis---------------------------
def define_subset_dataframes(df):
    # Define dataframes of craters by shape
    circleCraters = df[df["DIAM_ELLI_ELLIP_IMG"] <= ELLIPTIC_CUTOFF_ELLIP]
    ellipseCraters = df[df["DIAM_ELLI_ELLIP_IMG"] > ELLIPTIC_CUTOFF_ELLIP]

    # Define dataframes of craters by size
    smallCraters = df[df["DIAM_ELLI_MAJOR_IMG"] <= LARGE_CRATER_CUTOFF]
    largeCraters = df[df["DIAM_ELLI_MAJOR_IMG"] > LARGE_CRATER_CUTOFF]
    return [circleCraters, ellipseCraters, smallCraters, largeCraters]

def plot_size_ellip(df, markersize):
    # Graph of crater diameter (major ellipse diameter) vs. ellipticity
    plt.figure()
    plt.plot(df["DIAM_ELLI_MAJOR_IMG"], df["DIAM_ELLI_ELLIP_IMG"], 'o', markersize=markersize, alpha=0.1)
    plt.axhline(y=ELLIPTIC_CUTOFF_ELLIP, color='r', linestyle='--')
    plt.axvline(x=LARGE_CRATER_CUTOFF, color='k', linestyle='-.')
    plt.xscale("log")
    plt.xlabel("Lunar Crater Major Axis Diameter (km)")
    plt.ylabel("Lunar Crater Ellipticity (unitless)")
    plt.title("Relationship Between Lunar Crater Ellipticity and Major Axis Diameter")
    plt.legend(["Lunar Craters", "Elliptical Cutoff", "Large Crater Cutoff"])

def plot_prop_ellip(df, binwidth):
    # Plot dicratized diameter bins, for each bin, get mean and std dev of the ellipticity
    diamBins = bins=np.arange(min(df["DIAM_ELLI_MAJOR_IMG"]), max(df["DIAM_ELLI_MAJOR_IMG"]) + binwidth, binwidth)
    print("Bin Values", diamBins)
    xVals =[]
    yVals = []
    yStdDevs = []
    for index in range(1, len(diamBins)):
        # Greater than smaller than the larger value of the bin, less than the higer value of the bin
        diamsInBin = df[(df["DIAM_ELLI_MAJOR_IMG"] >= diamBins[index-1]) & (df["DIAM_ELLI_MAJOR_IMG"] < diamBins[index])]
        # print("Diams in Bins", diamsInBin)
        xVals.append((diamBins[index] + diamBins[index-1]) / 2)
        yVals.append(np.mean(diamsInBin["DIAM_ELLI_ELLIP_IMG"]))
        yStdDevs.append(np.std(diamsInBin["DIAM_ELLI_ELLIP_IMG"]))

    print("X Values: ", xVals, "\nY Values: ", yVals, "\nY Standard Deviations: ", yStdDevs)
    # plt.bar(xVals, yVals)
    
#--------------------------Past annalysis---------------------------

## Calling plotting functions
# plot_circle_size_freq(df=circleCraters, bins=50)

# plot_small_ellip_freq(df=smallCraters, bins=50)
# plot_large_ellip_freq(df=largeCraters, bins=50)

# plot_size_ellip(df=randomAsteroidData, markersize=4)
# plot_small_size_ellip(df=smallCraters, markersize=0.5)
# plot_large_size_ellip(df=largeCraters, markersize=0.5)

#--------------------------Current annalysis---------------------------
    
# Call dataframe functions (random sampling and subset dataframes)
randomAsteroidData = random_asteroid_sample(frac_samples=0.1)
[circleCraters, ellipseCraters, smallCraters, largeCraters] = define_subset_dataframes(df=randomAsteroidData)

#call plotting function
plot_prop_ellip(asteroidData, 2)

plt.show()
