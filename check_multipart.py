# checking multi-part features
arcpy.env.workspace = r"C:\TempGIS\DOP\15010110_Test\150101101_Ba Yint Naung"  
  
fcList = arcpy.ListFeatureClasses("BID_150101718002.shp")  
arcpy.AddField_management("BID_150101718002.shp", "isMulti", "TEXT")  
for fc in fcList:  
  
    with arcpy.da.UpdateCursor(fc, ["SHAPE@","BLD_CODE","isMulti"]) as cursor:  
        for row in cursor:  
  
            geometry = row[0]  
  
            if geometry.isMultipart == True:  
                print "{0} is Multipart".format(row[1])
                row[2] = "yes"
                cusor.updateRow(row)
