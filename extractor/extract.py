import os, shutil

foundfiles = []

dest = "C:/Games/House Flipper 2/HouseFlipper2_Data/StreamingAssets/bd/CustomPictures/Store"

dir = os.path.dirname(os.path.realpath(__file__))

dirs = next(os.walk(dir))[1]

for x in dirs:
    foundfiles.append(dir + "/" + x + "/" + os.listdir(dir + "/" + x)[0])
    
for z in foundfiles:
    shutil.copy(z, dest)