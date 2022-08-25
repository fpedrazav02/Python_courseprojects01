'''
This is a programm that receives 2 args, a folder name...with all the
JPG photos and a name for a new folder in which it will store all
PNG copies
'''

from genericpath import isdir
from queue import Empty
import sys
import os
import re
from PIL import Image

path_to_jpg_folder = os.path.abspath(sys.argv[1])
path_to_dest_folder = os.getcwd() + '/' + sys.argv[2]
l_jpg_folder = os.listdir(sys.argv[1])
split_jpg_folder = list(map(lambda string: string.split('.', 1), l_jpg_folder))


def c_jpg_folder():
    jpg_folder = sys.argv[1]
    l_jpg_folder = os.listdir(sys.argv[1])

    if not os.path.isdir(jpg_folder):
        print('no encontrado')
        return False
    if os.listdir(jpg_folder) == []:
        print("Empty directory...not JPG's found...")
        return False

    for item in l_jpg_folder:
        pattern = re.search(r"\.jpg$", item)
        if not pattern:
            return False
    return True


def c_dest_folder():
    dest_folder = sys.argv[2]
    path = os.getcwd() + '/' + dest_folder
    if not os.path.isdir(dest_folder):
        os.mkdir(path)
    else:
        return False
    return True


def check_params():
    try:
        if len(sys.argv) != 3:
            raise ValueError
        if not c_jpg_folder():
            raise AttributeError
        if not c_dest_folder():
            raise Empty

    except ValueError:
        print('Not enough arguments')
    except AttributeError:
        print('oops something went wrong')
    except Empty:
        print('')
    else:
        print(
            f'[*] Images saved successfully to --> {path_to_dest_folder} [*]')


def convert_images():
    counter = 0
    for item in l_jpg_folder:
        dest = path_to_dest_folder + '/' + \
            str(split_jpg_folder[counter][0]) + '.png'
        img = Image.open(path_to_jpg_folder + '/' + item)
        img.save(dest, 'png')
        counter += 1


'''
# PROGAMA
 '''
check_params()
convert_images()
