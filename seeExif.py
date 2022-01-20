import sys
from PIL import Image

def seeExif(file):
    image = Image.open(file)
    EXIF_data = image._getexif()
    print(EXIF_data)

def seeExifs(files):
    for file in files:
        seeExif(file)

def main():
    arguments = sys.argv[1:] 
    if len(arguments) == 0:
        print(f'Usage: python {sys.argv[0]} image [image2 [image3] ...]')
    else:
        seeExifs(arguments)
    print("Done")

if __name__ == "__main__":
    main()