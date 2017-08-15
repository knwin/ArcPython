#list projection name, extent and field of all shp files under a directory
import arcpy,csv,os  
  
mydir = #drag and drop a folder from ArcCatalogue
file = r'list_all.csv' 
outfile = mydir +'\\'+ file       

# listing all files in subdirectoires 
#   ---below code borrowed from https://goo.gl/g6Mihd
def list_files(dir):                                                                                                  
    r = []                                           
    subdirs = [x[0] for x in os.walk(dir)]
    for subdir in subdirs:              
        files = os.walk(subdir).next()[2]                  
        if (len(files) > 0):                                                        
            for file in files:                                                   
                r.append(subdir+ '\\' + file)                                       
    return r

# #--loop through all files ending in .shp, list projection names etc in a new row and save as csv
with open(outfile,'w+b') as f:
  w = csv.writer(f) 
  for file in list_files(mydir):
        if file.endswith(".shp"):
           fields = arcpy.ListFields(file)  
           field_names = [field.name for field in fields]
           desc = arcpy.Describe(file)
           sr = ([desc.spatialReference.name])
           #ext= ([desc.extent])
           aRow = ([mydir])
           aRow.extend([file])
           aRow.extend(sr)
           #aRow.extend(ext)
           aRow.extend(field_names)
           w.writerow(aRow)		   
f.close
