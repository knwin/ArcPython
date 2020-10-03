# Generic Arcpy scripts

### get the folder path of running script
```
path = os.path.dirname(__file__)
```

### check if a feature is selected or not
```
if(len(arcpy.Describe(fc).FIDset)):
  do_something()
```

### check if a temporary database exit
if not(arcpy.Exists(tmp_gdb)):
        arcpy.CreatePersonalGDB_management(path, tmp_gdb)
        
### deleting features in a temporary database
```
fcs = arcpy.ListFeatureClasses()
for fc in fcs:
    try:
        arcpy.Delete_management(fc)
    except:
        pass
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
