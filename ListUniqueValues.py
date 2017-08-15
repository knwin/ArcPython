#Extract unique values of a field in attribute table into csv
# code ref: 
#https://gis.stackexchange.com/questions/208430/trying-to-extract-a-list-of-unique-values-from-a-field-using-python
# modified by Kyaw Naing Win

import arcpy,csv,os  

#---ref codes -----
def unique_values(table , field_name):
    with arcpy.da.SearchCursor(table, [field_name]) as cursor:
        return sorted({row[0] for row in cursor})

#---end of ref codes ----
		
mydir = r'Y:\BernDiskstation\RSGIS\GIS\FD\2017-07-05_13-28-42\D\Data\All GIS Data_collection\02_ActivityDatasets\02_Concession\Plantaion\Ayeyarwady\\'

outfile = mydir + r'listFieldValue.csv'

with open(outfile,'w+b') as f:
  w = csv.writer(f)
  aRow = (['FILE_NAME'])
  aRow.extend(['FIELDS'])
  aRow.extend(['UNIQUE_VALUES'])
  w.writerow(aRow)  
  for file in os.listdir(mydir):
        if file.endswith(".shp"):
           aRow = ([file])
           rowCount = str(arcpy.GetCount_management(mydir+file).getOutput(0)) 
           aRow.extend(['number of record ' + rowCount])
           w.writerow(aRow)
           fields = arcpy.ListFields(mydir+file)  
           field_names = [field.name for field in fields]
           #print (field_names)
           for field_name in field_names:
             #print (field_name)
             if field_name == 'FID':
               continue
               #aRow = ([' '])
               #aRow.extend([field_name])
               #w.writerow(aRow)			   
             elif field_name == 'Shape':
               continue
               #aRow = ([' '])
               #aRow.extend([field_name])
               #w.writerow(aRow)
             else:
               #print (field_name)
               aRow = ([' '])
               aRow.extend([field_name])
               myValues = (unique_values(mydir+file, field_name))			   
               aRow.extend([[str(myValues[x]) for x in range(len(myValues))]])#remove u'String'
               #print (unique_values(mydir+file, field_name))
               w.writerow(aRow)
f.close