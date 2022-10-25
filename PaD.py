# -*- coding: cp1250 -*-

# Only part of the script is created by Daria Rapoport, 2016/04,
# based on the script created by Bc. Petr Nov�k, 2015/04:
# # Faculty of Environmental Sciences
# Czech University of Life Sciences Prague
#Script creates raster of Peucke and Douglass' weights


# Unchanged part of Novak

# Peucke and Douglass
# Created by Bc. Petr Nov�k, 2015/04
# Faculty of Environmental Sciences
# Czech University of Life Sciences Prague 
 
'''
Skript obsahuje dv� funkce: nPaD a PaD. 
nPaD hled� elevaci a sou�adnice t�� sousedn�ch bun�k. 
PaD na�te vstupn� DEM, p�evede jej na array a n�sledn� 
proch�z� array za pomoc� okna o velikosti 2x2 bu�ky. 
Porovn� tak elevaci ka�dou bu�ky DEM s jej�mi t�emi sousedy. 
Bu�ky, kter� nebyly ani jednou ozna�eny za nejvy��� 
z dan� �tve�ice, jsou s hodnotou 1 zaps�ny do v�sledn�ho rastru.
'''

import os, math, arcpy, sys
import numpy as np
import rta as rt
arcpy.env.overwriteOutput = True

# x,y sou�adnice a elevace t�� sousedn�ch bun�k
def nPaD(array,x,y):
    n0=array[x,y+1] #elevace
    n3=[x,y+1]      #sou�adnice
    n1=array[x+1,y+1]
    n4=[x+1,y+1]
    n2=array[x+1,y]    
    n5=[x+1,y]
    return n0, n1, n2, n3, n4, n5

def PaD(in_dem):
    arcpy.AddMessage("PaD: Na��t�m data...")
    # Na�te rastr DEM do np.array
    inDEM = rt.rta(in_dem)
    XMax = inDEM[1]
    YMax = inDEM[2]
    vCell = inDEM[3]
    LeftX = inDEM[4]
    LextY = inDEM[5]

    arcpy.AddMessage( "PaD: Data na�tena, za��n� v�po�et")
    # Nov� np.array hodnot = 1
    PaD_aray = np.ones([XMax,YMax])

    # Prohled� cel� rastr 
    for x in range (0,XMax-1):
        for y in range (0,YMax-1):
            nb=nPaD(inDEM[0],x,y)
            # Porovn� �tve�ice hodnot a najde nejvy��� elevaci
            if inDEM[0][x][y] > nb[0]:
                if inDEM[0][x][y] > nb[1]:
                    if inDEM[0][x][y] > nb[2]:
                        # V�em nejvy���m elevac�m p�i�ad� = 0
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

    arcpy.AddMessage("PaD: Rastr vah metodou Peucker and Douglas vytvo�en")
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
