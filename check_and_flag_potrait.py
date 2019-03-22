# check and flag portrait polygons for Data driven page generation
arcpy.env.workspace = r"C:\TempGIS\DOP\15010110_Test\150101101_Ba Yint Naung"  
  
fcList = arcpy.ListFeatureClasses("BID_150101718002.shp")  
arcpy.AddField_management("BID_150101718002.shp", "isPortrait", "TEXT")  
for fc in fcList:  
  
    with arcpy.da.UpdateCursor(fc, ["SHAPE@","BLD_CODE","isPortrait"]) as cursor:  
        for row in cursor:  
  
            geometry = row[0] 
            xMax = geometry.extent.XMax
            xMin = geometry.extent.XMin
            yMax = geometry.extent.YMax
            yMin = geometry.extent.YMin
  
            if (xMax - xMin) < (yMax - yMin):  
                print "{0} is Portrait".format(row[1])
                row[2] = "yes"
                cursor.updateRow(row)
