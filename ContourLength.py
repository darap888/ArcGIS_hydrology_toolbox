# -*- coding: utf-8 -*-

# Countour Length

# Created by Daria Rapoport, 2016/04,
#
# Faculty of Environmental Sciences
# Czech University of Life Sciences Prague 

"""
The script calculates contour lengths - sum of orthogonals to flow directions 
(towards downslope neighbors), which equals to: 1) grid size for cardinal neighbors
and grid size*√2 for diagonal neighbors (Freeman, 1991); 2)grid size*0,5 for cardinal neighbors
and grid size*0,354 for diagonal neighbors (Quinn et al., 1991); 3)grid size*0,6 for cardinal neighbors
and grid size*0,4 for diagonal neighbors (Wlock&McCabe, 1995) or 4) grid size multiplied by user-specified factors different for cardinal and diagonal directions.
Input Flow Direction raster is transfered to an array, for each cell of which
number of flow directions towards diagonal and cardinal neighboring cells is determined.
Accordingly, sum of contour length is calculated and converted to output raster. 
"""

import os, arcpy, math
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
# Raster of Contour Lengths (as defined by Freeman, 1991)
out_ras = sys.argv[2]

#Freeman's (1991) contour length definition
if sys.argv[3] == "true":
    wc=vCell
    wd=math.sqrt(2)*wc

    #Quinn's (1991) contour length definition
elif sys.argv[4] == "true":
    wc=vCell*0.5
    wd=vCell*0.354

#Wolock&McCabe's (1994) contour length definition
elif sys.argv[5] == "true":
    wc=vCell*0.6
    wd=vCell*0.4
    
#User-specified contour length definition
elif sys.argv[5] == "true":
    wc=vCell*(sys.argv[6])
    wd=vCell*(sys.argv[7])
else:
    arcpy.AddMessage("Choose one method for the calculation of contou lengths...")
arcpy.AddMessage("Calculations begin...")
# Creation of array of zeros - basis for the output creation
contours = np.zeros([XMax,YMax])


    # Going through all the input raster 
for x in range (1,XMax-1):
    for y in range (1,YMax-1):
        contour=0
        for i in range(4):
        #reading of directions and calculation of contour lengths for diagonal and cardinal neighbors
            try:
                if bin(int(ar_dem[0][x][y]))[-2*i-1]=='1':
                    contour+=wc
                
            except:
                pass
                    
        
            try:
                if bin(int(ar_dem[0][x][y]))[-2*i-2]=='1':
                    contour+=wd
            except:
                pass

        contours[x,y]=contour
        

     
arcpy.AddMessage("Creating of contour lengths raster...")
#Creating of output raster
new_raster = arcpy.NumPyArrayToRaster(contours,arcpy.Point(LeftX,LextY),vCell,value_to_nodata=-9999) 
new_raster.save(out_ras)
