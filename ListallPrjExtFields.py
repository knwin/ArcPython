#list projection name, extent and field of all shp files under a directory
import arcpy,csv,os  
  
mydir = r'D:\20161212_Basic ArcGIS Training\Day4\ArcCat_ex\\'
file = r'listallprojectionn.txt' 
outfile = mydir + file        

# #--loop through all files ending in .shp, list projection names etc in a new row and save as csv
with open(outfile,'w+') as f:
  w = csv.writer(f) 
  for file in os.listdir(mydir):
        if file.endswith(".shp"):
           fields = arcpy.ListFields(mydir+file)  
           field_names = [field.name for field in fields]
           desc = arcpy.Describe(mydir+file)
           sr = ([desc.spatialReference.name])
           ext= ([desc.extent])
           aRow = ([mydir])
           aRow.extend([file])
           aRow.extend(sr)
           aRow.extend(ext)
           aRow.extend(field_names)
           w.writerow(aRow)		   
f.close
