# -*- coding: cp1250 -*-
# Raster to Numpy.Array
# Created by Bc. Petr Novák, 2015/04, used by Daria Rapoport for ArcGIS Hydrology Toolbox creation
# Faculty of Environmental Sciences
# Czech University of Life Sciences Prague 

import os, arcpy
import numpy as np

# Funkce pro pøevod rastru do numpy.array
def rta (rast):
    # Naète rastr
    inRas = arcpy.Raster(rast)                                    
    # Zjistí jeho souøadnice
    lowerLeftX = inRas.extent.XMin
    lowerLeftY = inRas.extent.YMin  
    # Zjistí velikost pixelu
    sCell = inRas.meanCellWidth
    vCell = inRas.meanCellHeight
    # Pøevede rastr na numpy.array
    new_ar=arcpy.RasterToNumPyArray(rast,nodata_to_value=-9999)       
    # Poèet hodnout v øádku
    XMax= new_ar.shape[0]   
    # Poèet øádku
    YMax= new_ar.shape[1]   
    return new_ar, XMax, YMax, vCell, lowerLeftX, lowerLeftY






