import os, glob, time, re, sys
from subprocess import call


#History: SBS 2015 
#Purpose: for a supplied vector layer (e.g. shapefile) and greyscale raster tile, 
#         fix classification using gdal 
#inputs: 
#   rasterGreyCp = raster tif tile
#   shpPrefix = input shapefile prefix (part without extension)
#   shpFix +input shapefile name
#   suffix = appended to grey raster input
#   colorfile =  text based colorfile to assign pixel classes should have structure: classID
#                red-decimalValue green-decimalValue blue-decimalValue, e.g. 1   255 255 255 (one class per row)
#                in this case, '1' is the classID and the rgb decimal color is 255, 255, 255 or white
#   classID = string name of class attribute in shapefile (e.g. 'ID')


def fixPixels(rasterGreyCp,shpFix,shpPrefix,suffix,colorfile,classID):   #rasterGreyCp is the LC greyscale raster to correct.
   filename_split = os.path.splitext(rasterGreyCp)
   filename_zero, fileext = filename_split
   basename = os.path.basename(filename_zero)
   rasterColorOut=filename_zero+suffix+'.tif'
   call(["gdal_rasterize", "-a", classID, "-l",shpPrefix ,shpFix, rasterGreyCp])  #eg. gdal_rasterize -a MC_ID -l  fixPix fixPix.shp grey.tif
   call(["gdaldem", "color-relief", rasterGreyCp, colorFile, rasterColorOut])    #create colored tiff
   return