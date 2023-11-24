from os import *

for x,y,z in walk("."):
    for file in listdir(x):
        system(f'git add {file}')
        print(0)