## modified code from
### https://gis.stackexchange.com/questions/130588/python-script-to-add-fields-to-feature-classes
import arcpy,os
mydir = r'C:\Warehouses\tgo_shp\Kwin_bdy\\'

#Start a loop and iterate over the files in the folder

for file in os.listdir(mydir):
  
  if file.endswith(".shp"):

    #Add a text field called "Name" of length 50

    arcpy.AddField_management(file, "Kwin_No", "TEXT", field_length = 25)

    #Within each attribute table, write the name of the #current file

    with arcpy.da.UpdateCursor(file, "Kwin_No") as cursor:
       for row in cursor:
         row[0] = file
         cursor.updateRow(row)
