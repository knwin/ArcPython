#add all shp in subdirectory into current project in arcmap
import arcpy,csv,os  
  
mydir = #drag and drop a folder from ArcCatalogue here
# better copy mydir = part into script window first and add path with drag and drop from catalogue

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

# #--access current project and data frame
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd, "*")[0]

# #--loop through all files ending in .shp, add to current frame
for file in list_files(mydir):
  if file.endswith(".shp"):
    lyr = arcpy.mapping.Layer(file)
    arcpy.mapping.AddLayer(df, lyr, "AUTO_ARRANGE")
