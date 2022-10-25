# -*- coding: cp1250 -*-
# Raster to Numpy.Array
# Created by Bc. Petr Nov�k, 2015/04
# Faculty of Environmental Sciences
# Czech University of Life Sciences Prague 

import os, arcpy
import numpy as np

# Funkce pro p�evod rastru do numpy.array
def rta (rast):
    # Na�te rastr
    inRas = arcpy.Raster(rast)                                    
    # Zjist� jeho sou�adnice
    lowerLeftX = inRas.extent.XMin
    lowerLeftY = inRas.extent.YMin  
    # Zjist� velikost pixelu
    sCell = inRas.meanCellWidth
    vCell = inRas.meanCellHeight
    # P�evede rastr na numpy.array
    new_ar=arcpy.RasterToNumPyArray(rast,nodata_to_value=-9999)       
    # Po�et hodnout v ��dku
    XMax= new_ar.shape[0]   
    # Po�et ��dku
    YMax= new_ar.shape[1]   
    return new_ar, XMax, YMax, vCell, lowerLeftX, lowerLeftY






