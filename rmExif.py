# Exif Remover
# By Kalawela Lo
# 01/19/2022
#
# This program removes extra data stored in pictures.
# Often cameras record location/time/etc
# This improves privacy of photos

from logging import exception
import sys
from PIL import Image

#this removes Exif from image
def stripExif(file):
    try:
        image = Image.open(file)
        data = list(image.getdata())
        image_without_exif = Image.new(image.mode, image.size)
        image_without_exif.putdata(data)
        image_without_exif.save("stripped_"+file)
        print(f'{file} processed and saved as stripped_{file}')
    except exception as e:
        print(e)
        print("Attempting to continue...")

def stripExifs(files):
    for file in files:
        stripExif(file)

def main():
    #get arguments on command line
    arguments = sys.argv[1:] 
    if len(arguments) == 0:
        print(f'Usage: python {sys.argv[0]} image [image2 [image3] ...]')
    else:
        stripExifs(arguments)
    print("Done")

if __name__ == "__main__":
    main()