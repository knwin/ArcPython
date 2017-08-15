import arcpy,csv,os  
  
mydir = r'C:\Users\william\Documents\MIMU\Data\Transport\\'
outfile = r'C:\temp\test3.txt'        
  
#--loop through all files endin in .shp, list fields in a new row
with open(outfile,'w+') as f:
    w = csv.writer(f) 
    for file in os.listdir(mydir):
        if file.endswith(".shp"):

            fields = arcpy.ListFields(mydir+file)  
            field_names = [field.name for field in fields]  
            #--write all field names to the output file  
            w.writerow(field_names)
f.close
