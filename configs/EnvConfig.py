import os 

DATADIR='.DATA/'

if not os.path.isdir(DATADIR):
    os.mkdir(DATADIR)
else:
    print("=> DATADIR already exists")