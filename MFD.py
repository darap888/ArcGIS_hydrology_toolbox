# -*- coding: cp1250 -*-

# Multiple Flow Direction

# Created by Daria Rapoport, 2016/04,
# based on script created by Bc. Petr Novák, 2015/04:
# module "rta" and functions "slope" and "neighbors_z" are taken unchanged.

# Faculty of Environmental Sciences
# Czech University of Life Sciences Prague 

"""
The script contains 2 functions: neighbors_z and slope.
Neighbors_z is looking for the elevations of the neighboring cells.
Slope calculates slope to each of the neighboring cells.
Input DEM is transfered to an array. Flow directions to all neighbors
with positive slopes for each element of DEM array(i.e. each cell of DEM)
are then determined. Simultaneously, control of sink areas is performed.
"""

import os, math, arcpy
import numpy as np
import rta as rt
arcpy.env.overwriteOutput = True

# Function searches for the elevations of 8 neighbors of a cell
def neighbors_z(array,x,y):
    n1=array[x,y+1]
    n2=array[x+1,y+1]
    n4=array[x+1,y]
    n8=array[x+1,y-1]
    n16=array[x,y-1]
    n32=array[x-1,y-1]
    n64=array[x-1,y]
    n128=array[x-1,y+1]
    return n1, n2, n4, n8, n16, n32, n64, n128

# Function calculates slopes to each of 8 neighbors of a selected cell
def slope (cell, nb, vCell):
    slp=[]
    for k in range(8):
        if k%2==0:
            s=(cell-nb[k])/vCell
        else:
            s=(cell-nb[k])/vCellSqrt
        slp.append(s)
    return slp

arcpy.AddMessage("Reading data from DEM ... ")
# Input:
# Raster DEM
in_dem = sys.argv[1]
# Raster DEM is transfered to np.array
ar_dem = rt.rta(in_dem)
XMax = ar_dem[1]
YMax = ar_dem[2]
vCell = ar_dem[3]
LeftX = ar_dem[4]
LextY = ar_dem[5]
vCellSqrt = vCell*math.sqrt(2)

# Output:
# Raster of flow directions
out_ras = sys.argv[2]

arcpy.AddMessage("Calculations begin...")
# Creation of array of zeros
dir_aray = np.zeros([XMax,YMax])

# Basic 8-neighbor values for determination of flow direction
rastr_dir=[1,2,4,8,16,32,64,128]

# Going through all the raster 
for x in range (1,XMax-1):
    for y in range (1,YMax-1):
        # Calculates slopes to 8 neighbors of a cell
        slp=slope(ar_dem[0][x][y],neighbors_z(ar_dem[0],x,y),vCell)
        #Pits and flat areas error
        if (max(slp)) <= 0:
            arcpy.AddError(str("Raster error(flat area or sink),maximum slope value = ")+str(max(slp)))           
            break
        
        #Flow direction of a given cell is a sum of 8 possible direction values
        #of all positive slopes (maximum 253 unique combinations,
        #e.g. if we have 2 positive slopes from a cell to the North(direction vlue=1)
        #and North-West (direction value=128), direction value of a cell = 1+128=129)
        
        posslp=0
        for i in range(8):
            if slp[i]>0:
                posslp=posslp+rastr_dir[i]
        dir_aray[x,y]=posslp


        
    # Pits and flat areas error
    if (max(slp)) <= 0:
        arcpy.AddError(str("Raster error(flat area or sink),maximum slope value = ")+str(max(slp)))
        break
arcpy.AddMessage("Creating of flow direction raster...")
#Creating of flow direction raster
new_raster = arcpy.NumPyArrayToRaster(dir_aray,arcpy.Point(LeftX,LextY),vCell,value_to_nodata=-9999) 
new_raster.save(out_ras)
