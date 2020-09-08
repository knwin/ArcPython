# Collections of "how to.." in arcpy

## how to find geometry type of a feature class
__arcpy.Describe(lyr).shapeType__
 - Point
 - Polyline
 - Polygon

## how to find if there is(are) selected feature(s) in a layer
__arcpy.Describe(lyr).FIDset__ this will return the FID(s) of the selected feature(s)

**len(arcpy.Describe(lyr).FIDset)** will return number of feature selected. if Zero, nothing is selected

## how to check if a geodatabase exist
__arcpy.Exists(gdb_path)__ return __true__ or __false__


## how to delet feature classes in a geodatabase
```
arcpy.env.workspace = gdb_path
fcs = arcpy.ListFeatureClasses()
for fc in fcs:
    try:
        arcpy.Delete_management(fc)
    except:
        pass
```
        

## how to copy feature(s) from as new feature class
```
arcpy.CopyFeatures_management(source_fc, new_fc, "", "0", "0", "0")
```


## how to copy feature(s) from one feature class to another
```
searchCur = arcpy.SearchCursor(source_fc)
inCur = arcpy.InsertCursor(target_fc)

for Row in searchCur:
    inCur.insertRow(Row)
```

## How to add a new field into attribute table
```
NEW_FIELD = "geo_len_km"
DATA_TYPE = "DOUBLE"
arcpy.AddField_management(fc, NEW_FIELD, DATA_TYPE, "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
```