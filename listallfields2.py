import arcpy,csv,os  
  
#mydir = r'C:\Users\william\Documents\MIMU\Data\Transport\\'
mydir = r'D:\20161212_Basic ArcGIS Training\Day1\Data\commondata\01_admin\\'
outfile = r'C:\temp\test3.txt'        
  
#--loop through all files endin in .shp, list fields in a new row
with open(outfile,'w+') as f:
    w = csv.writer(f) 
    for file in os.listdir(mydir):
        if file.endswith(".shp"):

            fields = arcpy.ListFields(mydir+file)  
            field_names = [field.name for field in fields]  
            #--write all field names to the output file
            all_field_names = ([mydir])
            file_name = ([file])// new lines added by knw
            all_field_names.extend(file_name)// new lines added by knw
            all_field_names.extend(field_names)// new lines added by knw
            w.writerow(all_field_names) 
f.close
