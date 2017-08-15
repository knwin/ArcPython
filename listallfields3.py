##list field name of all shp files in subdirectories
import arcpy,csv,os  
  
#mydir = r'C:\Users\william\Documents\MIMU\Data\Transport\\'
mydir = r'D:\20161212_Basic ArcGIS Training\Day1\Data'
outfile = r'C:\temp\test3.txt'        
#below code borrowed from https://goo.gl/g6Mihd
# listing all files in subdirectoires
def list_files(dir):                                                                                                  
    r = []                                           
    subdirs = [x[0] for x in os.walk(dir)]
    for subdir in subdirs:              
        files = os.walk(subdir).next()[2]                  
        if (len(files) > 0):                                                        
            for file in files:                                                   
                r.append(subdir+ '\\' + file)                                       
    return r
	
# codes from Will, modifed to suit above code blocks	
# #--loop through subdirectories and all files endin in .shp, list fields in a new row
with open(outfile,'w+') as f:
    w = csv.writer(f)	
    for file in list_files(mydir):
        if file.endswith(".shp"):

            fields = arcpy.ListFields(file)  
            field_names = [field.name for field in fields]  
            #--write file names and all field names to the output file
            all_field_names = ([file])// new lines added by knw
            all_field_names.extend(field_names) // new lines added by knw
            w.writerow(all_field_names) 
f.close
