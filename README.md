# ArcGIS_hydrology_toolbox
The hydrological toolbox implementing Multiple Flow Direction Concept  for ArcGIS (written in Python 2.7)
Original Hydrology tools implemented in ArcGIS are based on only Single Flow Direction, therefore have their limits e.g. when tracking the way of contaminants from the source.

Toolbox contains 10 tools (scripts):

1	MFD.py
Input: DEM (Digital Elevation Model) raster
Output: raster of flow directions

2	Fdisp.py
Input: raster of flow directions
Output: raster of flow dispersion

3	FSmfd.py
Input: DEM raster
Output: flow accumulation raster 

4	PaD.py
Input: DEM raster
Returned value: array – local terrain curvature or raster of Peucker&Douglas weights

5	Influence_map.py
The script maps where flow goes from the input pixels (coordinates in column, row terms) and how it is dispersed. User can choose MFD8 (Freemn, 1991) or SFD8 (O'Callaghan&Mark, 1984) algorithm for flow routing. 
Input: DEM raster
Output: map of influence raster

6	nColRow.py
Input: raster of interest
Output: 2 rasters – column and row grids

7	ContourLength.py
Input: flow direction raster
Output: raster of contour widths

8	rta.py
The script contains one function rta (Raster To Array), which converts input raster to ndarray

9	Heap.py
Input: heap
Returned value: sorted array

10	 MFD_code_calculator.py
Input: array of flow direction codes
Output: lists of flow directions for every element of the input

