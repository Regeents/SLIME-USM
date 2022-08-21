import os
import pyfiglet
from colorama import init, Fore, Style
init(convert=True)

#Config the Titles and Authors
print("\033[1;36;40m")
ascii_name = pyfiglet.figlet_format("SLIME USM")
print(ascii_name)
print('Author: Regeents')
print('Twitter: https://twitter.com/Regeents')
print('Discord: Regeents#7971\n')
print('====================')



def usm_video(file : str):
    os.system(f'cmd /c "cd {path}/ & crid_mod -b 0096EE86 -a 46D6F935 -v -x {file[0:-4]}.usm"')
    os.system(f'cmd /c "cd {path}/ & ffmpeg -i {file[0:-4]}.m2v -i {file[0:-4]}.adx {file[0:-4]}.mp4"')
    os.remove(f'{path}/{file[0:-4]}.usm')
    os.remove(f'{path}/{file[0:-4]}.m2v')
    os.remove(f'{path}/{file[0:-4]}.adx')
    
path = input("Enter the folder path:\n")
filenames = os.listdir(path)

for filename in filenames:
    last = filename[-5:]
    if last == "bytes":
        os.rename(path + '/' + filename, path + '/' + filename[:-6])


filenames = os.listdir(path)

for filename in filenames:
    usm_video(filename)

print("\033[1;32;40m")
print('[!] Video(s) extracted! Press enter to exit..')
print("\033[1;33;40m")

input()