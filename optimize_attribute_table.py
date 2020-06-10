# Optimizing geospatial data with appropriate field lengths
'''
    Some attributes tables are created without considering appropriated field leghth espicially for string data type. Instead the field leght is set
    with large values like 254. This large field lengths in multiple fileds with many rows cause heavy file size not suitable for attched or upload to
    internet.
    By calculating max lenght of text in the fields and create the field with this max string lenght value greatly reduce the file size. In some cases 1:10 
    ratio.
'''
# credit - Kyaw Naing Win, Ye Htet Aung, OneMap.- 2020 June 10

import os

source_fc ="your_dir_path\\your_shapefile.shp"

out_folder = r"your_\dir_path\_to_store_new_file" #e.g "C:\temp"

buffer_length = 0 # add a few extra length to max length of the string, to define in new field.


# create a new file with same name but empty

out_name = os.path.basename(source_fc)
geometry_type = arcpy.Describe(source_fc).shapeType.upper()
arcpy.CreateFeatureclass_management (out_folder, out_name, geometry_type)
arcpy.DeleteField_management (target_fc, "Id") #Id filed is created by default and need to delete


# extract schema from source

fields = arcpy.ListFields(source_fc)

schema = []

for field in fields:
    mylen =0
    if field.type == "Double" or field.type=="Float":
        schema.append([field.name,field.type,field.length, field.precision, field.scale])
    elif field.type=='String':
        for row in arcpy.da.SearchCursor(source_fc,field.name):
            len0 =len(row[0])
            if len0>mylen:
                mylen=len0
        
        schema.append([field.name,field.type,field.length,mylen])
    else:
        schema.append([field.name,field.type,field.length])
        

# create attribute table in target with same schema as source file

target_fc = out_folder+"\\"+out_name

for index,item in enumerate(schema):
    if index>1:
        
        NAME = item[0]
        TYPE = item[1]
        LENGTH = int(item[2])
        if TYPE == "Double" or TYPE=="Float":
            PRECISION = int(item[3])
            SCALE = int(item[4])
            arcpy.AddField_management(target_fc,NAME,TYPE,field_precision=PRECISION,field_scale=SCALE,field_length=LENGTH,)
        if TYPE =='String':
            LENGTH =int(item[3])+buffer_length
            arcpy.AddField_management(target_fc,NAME,TYPE,field_length=LENGTH)
        else:
            
            arcpy.AddField_management(target_fc,NAME,TYPE,field_length=LENGTH)

 			
# copy features and attributes from source to target

arcpy.Append_management(source_fc,target_fc)     
