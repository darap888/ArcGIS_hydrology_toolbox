# -*- coding: cp1250 -*-

# Flow Dispersion

# Created by Daria Rapoport, 2016/04,
#
# Faculty of Environmental Sciences
# Czech University of Life Sciences Prague 

"""
The script calculates flow dispersion - number of cells to which flow is routed
from the current cell.
Input Flow Direction raster is transfered to an array, for each cell of which
number of non-zero bits (equivalent to the number of directions towards neighboring cells)
is calculated and converted to output ‘flow dispersion’ raster. 
"""

import os, arcpy
import numpy as np
import rta as rt
arcpy.env.overwriteOutput = True

arcpy.AddMessage("Reading data from DEM ... ")
# Input:
# Raster of flow directions with single flow direction codes used in ArcGIS
#and their summation for multiple flow directions
in_dem = sys.argv[1]
# Raster of flow directions is transfered to np.array
ar_dem = rt.rta(in_dem)
XMax = ar_dem[1]
YMax = ar_dem[2]
vCell = ar_dem[3]
LeftX = ar_dem[4]
LextY = ar_dem[5]

# Output:
# Raster of flow dispersion (raster of numbers of directions form one cell)
out_ras = sys.argv[2]

arcpy.AddMessage("Calculations begin...")
# Creation of array of zeros - basis for the output creation
dir_num = np.zeros([XMax,YMax])


    # Going through all the input raster 
for x in range (1,XMax-1):
    for y in range (1,YMax-1):
        dirn=0
        for i in range(8):
            
                try:
                    if bin(int(ar_dem[0][x][y]))[-i-1]=='1':
                        dirn+=1
                    
                except:
                    pass    
        
        dir_num[x,y]=dirn
        

     
arcpy.AddMessage("Creating of flow dispersion raster...")
#Creating of flow dispersion raster
new_raster = arcpy.NumPyArrayToRaster(dir_num,arcpy.Point(LeftX,LextY),vCell,value_to_nodata=-9999) 
new_raster.save(out_ras)
