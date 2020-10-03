# Collections of "how to's" in arcpy

## how to find geometry type of a feature class
```arcpy.Describe(lyr).shapeType```
 - Point
 - Polyline
 - Polygon

## how to find if there is(are) selected feature(s) in a layer
```arcpy.Describe(lyr).FIDset``` this will return the FID(s) of the selected feature(s)

```len(arcpy.Describe(lyr).FIDset)``` will return number of feature selected. if Zero, nothing is selected

```
if(len(arcpy.Describe(fc).FIDset)):
  do_something()
```

## how to check if a geodatabase exist
```arcpy.Exists(gdb)``` return __true__ or __false__

```
if not(arcpy.Exists(gdb)):
        arcpy.CreatePersonalGDB_management(path, gdb)
```

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

## how to copy/save feature(s) as new feature class
if selection is applied, only selected features will be copied/saved
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
or use append - filed name matching may need to apply if needed
```
arcpy.Append_management([soure_lyaer], target_layer, "", "", "")
```
## how to copy selected feature(s) from one feature class to another
??

## How to add a new field into attribute table
```
NEW_FIELD = "geo_len_km"
DATA_TYPE = "DOUBLE"
arcpy.AddField_management(fc, NEW_FIELD, DATA_TYPE, "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
```

## How to calculate Area and Length of features

Area and length calculations in Field calculator (python)  
```
!shape.area@acres!
!shape.length@kilometers!
```

Geodesic Area and Length calculations in Field calculator (python)
```
!shape.geodesicArea@acres!
!shape.geodesicLength@kilometers!
```

Python script
```
# Calculate length in KM
arcpy.CalculateField_management(fc, "geo_len_km_", "!shape.length@kilometers!", "PYTHON", "")

# Calculate geodesic length in KM
arcpy.CalculateField_management(fc, "geo_len_km_", "!shape.geodesicLength@kilometers!", "PYTHON", "")
```
```
    Areal unit of measure keywords:
        ACRES | ARES | HECTARES | SQUARECENTIMETERS | SQUAREDECIMETERS | SQUAREINCHES | SQUAREFEET | SQUAREKILOMETERS | SQUAREMETERS | SQUAREMILES | SQUAREMILLIMETERS | SQUAREYARDS | SQUAREMAPUNITS | UNKNOWN
    Linear unit of measure keywords:
        CENTIMETERS | DECIMALDEGREES | DECIMETERS | FEET | INCHES | KILOMETERS | METERS | MILES | MILLIMETERS | NAUTICALMILES | POINTS | UNKNOWN | YARDS
```
[for more details:](https://desktop.arcgis.com/en/arcmap/10.3/manage-data/tables/calculate-field-examples.htm#ESRI_SECTION1_11EAB368A53B4D1C9618A58A1B09F9D0)

## How to find if feature class has M vale, Z value
```arcpy.Describe(lyr).hasM``` return *true* or *false*

```arcpy.Describe(lyr).hasZ``` return *true* or *false*

## How to get full path of a layer selected from dropdownn list
```
layer = arcpy.GetParameterAsText(0)
desc = arcpy.Describe(layer)
path = desc.path
layersource = str(path) + "/" + layer
```
## How to get X,Y,Z,M values of start/end of a line in Field calculator
Choose Python for language option
```
!shape!.firstPoint.X, !shape!.firstPoint.Y,  !shape!.firstPoint.Z, !shape!.firstPoint.M
!shape!.lastPoint.X, !shape!.lastPoint.Y, !shape!.lastPoint.Z, !shape!.lastPoint.M
```

## How to get X,Y,Z,M values of start/end of a line with arcpy
```
with arcpy.da.SearchCursor(infc, ["SHAPE@"]) as rows:
    # Step through each row
    for row in rows:
        f = row[0]
        # Step through each vertex in the feature
        for v in f:
           # get attribute of vertex
           x = v.X
           y = v.Y
           z = v.Z
           m = v.M 
```

### get the folder path of running script
```
path = os.path.dirname(__file__)
```

### returning a field calculation formula base on user selection from drop downlist on a tool
```
len_unit = arcpy.GetParameterAsText(#)
geodesic_formula = {"Kilometers": "!shape.geodesicLength@kilometers!", "Miles":"!shape.geodesicLength@miles!"}
expression = geodesic_formula[len_unit]
field_name = "geo"+ len_unit
arcpy.AddField_management(tmp_layer, field_name, "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(tmp_layer, field_name, expression , "PYTHON", "")
```
