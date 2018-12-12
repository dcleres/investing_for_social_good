from os import listdir
from os.path import isfile, join

mypath = './' + day + '/' + hour + '/'

for f in listdir(mypath):
    
    print('READING' , mypath + f)
    df = pd.read_json(mypath + f, lines=True)
    df = df[df.lang=='en']
    df = df.reset_index()
    
    df.to_json(mypath + f, compression='bz2')
