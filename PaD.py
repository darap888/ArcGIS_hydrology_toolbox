# -*- coding: cp1250 -*-

# created by Daria Rapoport, 2016/04,
# # # Faculty of Environmental Sciences
# Czech University of Life Sciences Prague
#Script creates raster of Peucke and Douglass' weights


# Unchanged part of Novak

# Peucke and Douglass
# Created by Bc. Petr Novák, 2015/04
# Faculty of Environmental Sciences
# Czech University of Life Sciences Prague 
 
'''
Skript obsahuje dvì funkce: nPaD a PaD. 
nPaD hledá elevaci a souøadnice tøí sousedních bunìk. 
PaD naète vstupní DEM, pøevede jej na array a následnì 
prochází array za pomocí okna o velikosti 2x2 buòky. 
Porovná tak elevaci každou buòky DEM s jejími tøemi sousedy. 
Buòky, které nebyly ani jednou oznaèeny za nejvyšší 
z dané ètveøice, jsou s hodnotou 1 zapsány do výsledného rastru.
'''

import os, math, arcpy, sys
import numpy as np
import rta as rt
arcpy.env.overwriteOutput = True

# x,y souøadnice a elevace tøí sousedních bunìk
def nPaD(array,x,y):
    n0=array[x,y+1] #elevace
    n3=[x,y+1]      #souøadnice
    n1=array[x+1,y+1]
    n4=[x+1,y+1]
    n2=array[x+1,y]    
    n5=[x+1,y]
    return n0, n1, n2, n3, n4, n5

def PaD(in_dem):
    arcpy.AddMessage("PaD: Naèítám data...")
    # Naète rastr DEM do np.array
    inDEM = rt.rta(in_dem)
    XMax = inDEM[1]
    YMax = inDEM[2]
    vCell = inDEM[3]
    LeftX = inDEM[4]
    LextY = inDEM[5]

    arcpy.AddMessage( "PaD: Data naètena, zaèíná výpoèet")
    # Nový np.array hodnot = 1
    PaD_aray = np.ones([XMax,YMax])

    # Prohledá celý rastr 
    for x in range (0,XMax-1):
        for y in range (0,YMax-1):
            nb=nPaD(inDEM[0],x,y)
            # Porovná ètveøice hodnot a najde nejvyšší elevaci
            if inDEM[0][x][y] > nb[0]:
                if inDEM[0][x][y] > nb[1]:
                    if inDEM[0][x][y] > nb[2]:
                        # Všem nejvyšším elevacím pøiøadí = 0
                        PaD_aray[x,y] = 0
                    else:
                        PaD_aray[nb[5][0],nb[5][1]] = 0
                elif nb[1] > nb[2]:
                    PaD_aray[nb[4][0],nb[4][1]] = 0
                else:
                    PaD_aray[nb[5][0],nb[5][1]] = 0
            elif nb[0] > nb[1]:
                if nb[0] > nb [2]:
                    PaD_aray[nb[3][0],nb[3][1]] = 0
                else:
                    PaD_aray[nb[5][0],nb[5][1]] = 0
            elif nb[1] > nb[2]:
                PaD_aray[nb[4][0],nb[4][1]] = 0
            else:
                PaD_aray[nb[5][0],nb[5][1]] = 0

    arcpy.AddMessage("PaD: Rastr vah metodou Peucker and Douglas vytvoøen")
    return PaD_aray

#Small part created by Daria Rapoport, which creates raster of Peucker and Douglas weights of input DEM raster
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


out_weights = sys.argv[2]
in_raster=PaD(in_dem)
new_raster = arcpy.NumPyArrayToRaster(in_raster,arcpy.Point(LeftX,LextY),vCell,value_to_nodata=-9999) 
new_raster.save(out_weights)
