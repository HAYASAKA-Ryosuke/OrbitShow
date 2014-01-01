import math
import ephem
import numpy
import time
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
plt.ion()
# data downloaded from the form at
# http://coastwatch.pfeg.noaa.gov/erddap/tabledap/apdrcArgoAll.html
home = ephem.Observer()
home.lon = '-122.63'   # +E
home.lat = '45.56'      # +N
home.elevation = 80 # meters
 
# Always get the latest ISS TLE data from:
iss = ephem.readtle("ISS (ZARYA)",
	"1 25544U 98067A   14001.61097693  .00008534  00000-0  15682-3 0  3716",
	"2 25544  51.6486 205.2067 0004928 341.4189  88.6312 15.50091814865480")
#
iss.compute(home)
lon=math.degrees(iss.sublong)
lat=math.degrees(iss.sublat)
m = Basemap(projection='cyl',lon_0=180)
x,y=m(360+lon,lat)
m.drawmapboundary(fill_color='#99ffff')
m.fillcontinents(color='#cc9966',lake_color='#99ffff')
m.scatter(x,y,20,marker='o',color='b')
plt.draw()
