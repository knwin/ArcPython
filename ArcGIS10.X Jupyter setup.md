# How to setup Jupyter for Arcgis 10.x
(here ArcGIS 10.7 as example, change to actural version)

+ open cmd.exe as adminstrator
 + cd python27\arcgis10.7
 + python -m pip install virtualenv
 + python -m virtualenv venv\jupyter
 + cd venv\jupyter
 + python -m pip install jupyter
 + python -m pip install jupyterlab
 + install any module you want to install here

## link to Arcpy and numpy modules

Although you have installed jupyter, you cannot import arcpy module yet. Do following steps

(ref: https:\\notesfromthelifeboat.com\post\arcpy-virtualenv\)

open cmd.exe as adminstrator
+ cd c:\Python27\ArcGIS10.7
+ mkdir arcpy_includes
+ cd arcpy_includes
+ copy c:\Python27\ArcGIS10.7\Lib\site-packages\Desktop10.7.pth from windows explorer into_
  - into c:\Python27\ArcGIS10.7\arcpy_includes 
  - into c:\Python27\ArcGIS10.7\venv\jupyter\Lib\site-packages 
+ mklink/D numpy c:\Python27\ArcGIS10.7\Lib\site-packages\numpy 

## Prepare for Jupyter lab
+ install jupyter lab: _C:\Python27\ArcGIS10.7\venv\jupyter\Scripts\python -m pip install jupyterlab_ 
+ copy C:\Python27\ArcGIS10.7\venv\jupyter\Scripts\activate.bat as jupyterlab_activate.bat in the same folder
+ edit jupyterlab_activate.bat with notepad
  + add _set "PYTHONPATH=C:\Python27\ArcGIS10.7\Lib\site-packages"_ at second line
  + add _jupyter-lab.exe_ at the end of file

## Create a widnows short cut for Jupyter lab
+ create a shortcut by right click over jupyterlab_activate.bat file and select shortcut to desktop
+ open properties of the _short cut_
  + add path for home folder for jupyter notebooks in _"Start in"_ e.g _C:\jupyter_notebooks\ArcGIS_
  
  Now you double click the short cut and juputer lab will open

type __import arcpy__

if no error, you are ready for ArcGIS on Jupyter environment
