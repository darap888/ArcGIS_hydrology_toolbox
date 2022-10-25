# -*- coding: cp1250 -*-
# Multiple Flow Simulation surface drainage
# Created by Daria Rapoport, 2016/04,
# based on script created by Bc. Petr Novák, 2015/04:
# modules "rta" and "Heap"; functions "slope","neighbors_xy" and "neighbors_z" are taken unchanged.
# Faculty of Environmental Sciences
# Czech University of Life Sciences Prague 

"""
The script contains 3 functions: neighbors_z, neighbors_xy and slope.
Neighbors_z is looking for the elevations of the neighboring cells.
Neighbors_xy searches for the coordinates [x,y] of the neighoring cells.
Slope calculates slope to each of the neighboring cells.
Input DEM is transfered to an array. Initial array of flow accumulation is created (array of ones + weights if provided).
Heap of vectors(x,y,z) sorted by the value of elevation "z" is created.
Starting with a cell with maximum elevation flow directions to all neighbors with positive slopes are determined.
Accumulation value of a cell in the direction of a flow is increased
by an accumulation value of the currently processed cell according to the weight of its slope value in all positive neighboring slopes.
"""

import os, math, arcpy
import numpy as np
import rta as rt
import Heap as h
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


# Function searches for the coordinates [x,y] of the neighoring cells
def neighbors_xy(x,y):
    n1=[x,y+1]
    n2=[x+1,y+1]
    n4=[x+1,y]
    n8=[x+1,y-1]
    n16=[x,y-1]
    n32=[x-1,y-1]
    n64=[x-1,y]
    n128=[x-1,y+1]
    return n1,n2,n4,n8,n16,n32,n64,n128

arcpy.AddMessage("Reading data from DEM ... ")
# Input:
# Raster DEM
in_dem = sys.argv[1]
# Raster DEM is transfered to np.array
aar_dem = rt.rta(in_dem)
ar_dem = aar_dem[0]
XMax = aar_dem[1]
YMax = aar_dem[2]
vCell = aar_dem[3]
LeftX = aar_dem[4]
LextY = aar_dem[5]
vCellSqrt=vCell*math.sqrt(2)
del aar_dem

# Output:
# Raster of flow accumulation
out_aku = sys.argv[2]
#user-specified parameter p controlling flow divergency (Default p=1,1) (Freeman, 1991)
p = float(sys.argv[3])


# Raster of weights
if sys.argv[4] == "true":
    self_scale = sys.argv[5]
    # Transfer of weights raster to np.array
    ar_scale=rt.rta(self_scale)
    
   
arcpy.AddMessage( "Data is loaded, the calculation begins ...")
ha=[] 
# Creating of heap of vectors(x,y,z) sorted by the value of elevation "z"
for xi in range (1,XMax-1):
    for yi in range (1,YMax-1):
        h.inz_el (ha, (xi, yi, ar_dem[xi,yi]), index=2)

# Initial np.array for accumulation values
if sys.argv[4]== "false":
    ar_aku=np.ones([XMax,YMax])
else:
    ar_aku=np.ones([XMax,YMax])+ar_scale[0]


arcpy.AddMessage( "Calculation of flow accumulation begins...")
# Accumulation value of a cell in the direction of a flow (neighbor cell with positive slope)
#will be increased by an accumulation value of an inflow cell (current "central" cell)
#Calculation starts from the cells with the highest elevations (using binary heap)

while len(ha)>0:
    x= ha[0][0]
    y= ha[0][1]
    if x in range (1,XMax-1):
        if y in range (1,YMax-1):
            slp=slope(ha[0][2],neighbors_z(ar_dem,x,y),vCell)
            slsum=0
            posslop=[]
            posnb=[]
            #Determination of the neighbors with positive slopes
            for i in range(8):
                if slp[i]>0:
                    slsum=slsum+slp[i]**p
                    posslop.append(slp[i])
                    posnb.append(i)
            for el in posnb:
                # Neighboring cell in the direction of flow 
                nxy=neighbors_xy(x,y)[el]
                #Its flow accumulation value=its current flow accumulation + flow accum.from "central" cell
                ar_aku[nxy[0],nxy[1]]=ar_aku[nxy[0],nxy[1]]+ar_aku[x,y]*(posslop[posnb.index(el)]**p/slsum)
            
    # Deleting of maximum from the heap and putting there next maximum
    h.ret_max(ha,2)

arcpy.AddMessage( "Creating of flow accumulation raster...")
# Creating of flow accumulation raster
new_raster = arcpy.NumPyArrayToRaster(ar_aku,arcpy.Point(LeftX,LextY),vCell,value_to_nodata=-9999) 
new_raster.save(out_aku)
