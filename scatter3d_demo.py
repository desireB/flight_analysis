'''
==============
3D scatterplot
==============

Demonstration of a basic scatterplot in 3D.
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt
import pandas as pd

import csv


CSV_COLUMNS = ["Id","Latitude","Longitude","FlightMode","Altitude_meters","VpsAltitude_meters"]


def read_csv_file(filename_in):

    # my_data = genfromtxt(filename_in, delimiter=',')
    # with open(filename_in, 'r') as csvin:
    #     readfile = csv.reader(csvin, delimiter=',')
    # df_data = pd.read_csv(
    #     filename_in,
    #     names=CSV_COLUMNS,
    #     # skipinitialspace=True,
    #     engine="python"
    #     # skiprows=1
    #     )
    df_data=pd.read_csv(filename_in, sep=',')
    return df_data

def randrange(n, vmin, vmax):
    '''
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    '''
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

n = 4000

geo_data = read_csv_file('dji.csv')
geo_info = geo_data[["Id","Latitude","Longitude","Altitude_meters","VpsAltitude_meters"]]
print(geo_info[:5])
short_geo_info = geo_info[:n]

# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
# for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
    # xs = randrange(n, 23, 32)
    # ys = randrange(n, 0, 100)
    # zs = randrange(n, zlow, zhigh)
    # xs = geo_data['Latitude'][:5]
    # ys = geo_data['Longitude'][:5]
    # zs = geo_data['Altitude_meters'][:5]
    # ax.scatter(xs, ys, zs, c=c, marker=m)

# for index in range(0,n-1):
#     # print(short_geo_info["Id"][index])
#     xs = short_geo_info["Latitude"][index]
#     ys = short_geo_info["Longitude"][index]
#     zs = short_geo_info["Altitude_meters"][index]
#     ax.scatter(xs, ys, zs)
#     # print("\n")

ax.plot(short_geo_info["Latitude"], short_geo_info["Longitude"], short_geo_info["Altitude_meters"])

ax.set_xlabel('Latitude')
ax.set_ylabel('Longitude')
ax.set_zlabel('Altitude')

ax.text2D(0.05, 0.95, "Desire Banse DJI Flight investigation", transform=ax.transAxes)
#
plt.show()
