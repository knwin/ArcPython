#Extract unique values of a field in attribute tableshp
# code ref: https://gis.stackexchange.com/questions/208430/trying-to-extract-a-list-of-unique-values-from-a-field-using-python
def unique_values(table , field):
    with arcpy.da.SearchCursor(table, [field]) as cursor:
        return sorted({row[0] for row in cursor})

table = r'Y:\BernDiskstation\RSGIS\GIS\FD\2017-07-05_13-28-42\D\Data\All GIS Data_collection\02_ActivityDatasets\02_Concession\Plantaion\Ayeyarwady\Ayeyarwady_plantation.shp'
field = 'Dist'
myValues = unique_values(table, field)

print (myValues)