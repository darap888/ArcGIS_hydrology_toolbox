# -*- coding: cp1250 -*-
# 
# Created by Daria Rapoport, 2016/04
# Script module "rta" is credited to Bc. Petr Novák, 2015/04:
# 
# Faculty of Environmental Sciences
# Czech University of Life Sciences Prague

"""
The script calculates the number of column and row of pixels of the input raster,
producing 2 rasters of column and row numbers of each pixel.
Input raster is coverted to ndarray.
Ndarray of columns and rows numbers of the input raster is created using numpy.indices method.
Arrays of columns and rows are extracted from ndarray by indexing and converted to rasters.
 """

import os, arcpy
import numpy as np
import rta as rt

arcpy.env.overwriteOutput = True
arcpy.AddMessage("Reading data from the input raster ... ")
# Input:
# Raster for which columns and rows will be defined
in_raster = sys.argv[1]
# Raster DEM is transfered to np.array
raster = rt.rta(in_raster)
XMax = raster[1]
YMax = raster[2]
vCell = raster[3]
LeftX = raster[4]
LextY = raster[5]

# Outputs:
# Raster of row numbers
out_rows = sys.argv[3]
# Raster of column numbers
out_cols = sys.argv[2]

arcpy.AddMessage("Calculation begins...")
#Creation of numpy array of indices
grid=np.indices((XMax,YMax))
nrows=grid[0]
ncols=grid[1]

#Writing the outputs 
row_raster = arcpy.NumPyArrayToRaster(nrows,arcpy.Point(LeftX,LextY),vCell,value_to_nodata=-9999) 
row_raster.save(out_rows)

col_raster = arcpy.NumPyArrayToRaster(ncols,arcpy.Point(LeftX,LextY),vCell,value_to_nodata=-9999) 
col_raster.save(out_cols)
