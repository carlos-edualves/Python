import os
import re
import shutil

folder = 'C:\\Users\\Administrator\\Downloads'
fotos = 0
extension = '.*(\w{3})'

files = os.listdir(folder)

def listfolder():
    global fotos
    global folder
    global extension
    file = ''
    filezao = []
    path = os.path.join(folder,extension)
    #os.mkdir(path)
    for i in files:
        ext = re.match(extension,i)
        if ext is not None:
            filezao.append(ext.group(1))
            file = list(set(filezao))
            #pathfile = os.path.join(folder,ext.group(0))
            #shutil.move(pathfile,path)
    print(file)

listfolder()
