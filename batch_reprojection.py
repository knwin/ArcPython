# batch projecting MMR 2000 GCS base UTM 46 and UTM 47 shpfiles into WGS84
# features: folder structure will be copied into target folder
#          all shpfiles inside sub-folders will be reprojected
#          determine zone 46 or 47 by the folder name as the folder has the map sheet names

import arcpy,os

srcDir = r'D:\\OMM_GIS\\Department_RAW_Data\\SD Data\\20180919_TNT_Export_Taungoo\\EET\\'
desDir = r'D:\\TempGIS\\'

# CRS wkts  
wgs84_gcs = "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]"
mmr2000_gcs = "GEOGCS['GCS_MM_2000',DATUM['D_MM_2000',SPHEROID['MM_2000',6377276.345,300.8017]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]"
custom_geot = "GEOGTRAN[METHOD['Molodensky'],PARAMETER['X_Axis_Translation',246.632],PARAMETER['Y_Axis_Translation',784.833],PARAMETER['Z_Axis_Translation',276.923]]"

mmr2000_utm47_crs = "PROJCS['MM_2000_UTM_Zone_47N',GEOGCS['GCS_MM_2000',DATUM['D_MM_2000',SPHEROID['MM_2000',6377276.345,300.8017]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',99.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]"
mmr2000_utm46_crs = "PROJCS['MM_2000_UTM_Zone_46N',GEOGCS['GCS_MM_2000',DATUM['D_MM_2000',SPHEROID['MM_2000',6377276.345,300.8017]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',93.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]"

arcpy.env.overwriteOutput = True

# create custom transformation from Myanmar 2000 to WGS84

customtransformation = "Customtran_MMR2000_to_WGS1984"  #add custom transformation 

def add_customtransformation():
    try:
	#Output_Geographic_Coordinate_System = "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]"
	
	# Process: Create Custom Geographic Transformation
	# arcpy.CreateCustomGeoTransformation_management (geot_name, in_coor_system, out_coor_system, custom_geot)
	arcpy.CreateCustomGeoTransformation_management(customtransformation, mmr2000_gcs , wgs84_gcs, custom_geot) 
	
	print ("custom transformation added")
    except:
        print ("Custom transformation with the name " + customtransformation + " already exisits.")

     
# folder structure copying
def copy_folderstructure (srcDir, desDir):
    for dirpath, dirnames, filenames in os.walk(srcDir):
	structure = os.path.join(desDir, dirpath[len(srcDir):])
	if not os.path.isdir(structure):
	    os.mkdir(structure)
	else:
	    print("Folder does already exits!")

# listing all files in subdirectoires
def list_shp_files(dir): 
    r = [] 
    subdirs = [x[0] for x in os.walk(dir)]
    for subdir in subdirs: 
        files = os.walk(subdir).next()[2] 
        if (len(files) > 0): 
            for file in files:
                if file.endswith(".shp"):
                    r.append(subdir+ '\\' + file)
    return r

# Project myanmar datum base dataset to WGS84
def mmr2wgs84(inShp, outShp):
    # immediate folder name for UTM Zone guessing
    shpfolder = os.path.dirname(inShp)
    shpfolder = os.path.basename(shpfolder)
    # determine utm zone from folder name
    if shpfolder[2:4] > 95:
	in_coor_system = mmr2000_utm47_crs
    else:
	in_coor_system = mmr2000_utm46_crs
    try:
	# redefine the projection to be consistent
	arcpy.DefineProjection_management(inShp, in_coor_system)
	# Project_management (in_dataset, out_dataset, out_coor_system, transform_method, {in_coor_system}, {preserve_shape}, {max_deviation}, {vertical})
    
	print (inShp + " is being reprojected into WGS84")        
        arcpy.Project_management(inShp, outShp, wgs84_gcs, customtransformation, in_coor_system)
    except:
        print ("Cannot reproject " + outShp + "file.")

# # # main process
copy_folderstructure(srcDir, desDir) # folder structure copying

add_customtransformation() # add custom transformation to use in reprojection

myShpFiles =list_shp_files(srcDir) # get all shp files

# reproject all files
for inShp in myShpFiles:
    outShp = inShp.replace(srcDir,desDir)
    mmr2wgs84(inShp, outShp)
    
print("reprojection completed")
