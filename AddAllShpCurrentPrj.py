#add all shp in subdirectory into current project in arcmap
#Kyaw Naing Win, OneMap GIS Program Manager
# #---instruction----
# (1)type mydir = in python windows
# (2)from ArcCatalogue windows, drag main folder in to python windows after mydir =
# copy and paste below codes into python windows
# press enter twice

import arcpy,csv,os  
  
#mydir = #drag and drop a folder from ArcCatalogue

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

#clean up
arcpy.RefreshActiveView()
arcpy.RefreshTOC()
del mxd, df, lyr, mydir, file, list_files
