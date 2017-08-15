#list projection name of all shp files under a directory
import arcpy,csv,os  
  
mydir = r'D:\20161212_Basic ArcGIS Training\Day4\ArcCat_ex\\'
file = r'listallprojectionn.txt' 
outfile = mydir + file        

# #--loop through all files ending in .shp, list projection names in a new row
with open(outfile,'w+') as f:
  w = csv.writer(f) 
  for file in os.listdir(mydir):
        if file.endswith(".shp"):
           desc = arcpy.Describe(mydir+file)
           sr = ([desc.spatialReference.name])
           aRow = ([mydir])
           aRow.extend([file])
           aRow.extend(sr)
           w.writerow(aRow)		   
f.close
