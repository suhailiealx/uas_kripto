from PIL import Image, ImageDraw
import os
import sys
from random import SystemRandom
random = SystemRandom()
xrange = range

if len(sys.argv) != 3:
    print("This takes two argument; the image to be split.")
    exit()
infile1 = str(sys.argv[1])
infile2 = str(sys.argv[2])

if not os.path.isfile(infile1):
    print("That file 1 does not exist.")
    exit()
if not os.path.isfile(infile2):
    print("That file 2 does not exist.")
    exit()


img1 = Image.open(infile1) #share1
img2 = Image.open(infile2) #share2

f, e = os.path.splitext("outfile")
out_filename_decrypt = f+"_decrypt.png"

img1 = img1.convert('1')  # convert image to 1 bit
img2 = img2.convert('1')  # convert image to 1 bit

width = img1.size[0]
height = img1.size[1]

out_image_decrypt = Image.new('1', (width, height))
draw_decrypt = ImageDraw.Draw(out_image_decrypt)

#Cycle through pixels
for x in xrange(0, int(width)):
    for y in xrange(0, int(height)):
        pixel1 = img1.getpixel((x, y))
        pixel2 = img2.getpixel((x, y))

        draw_decrypt.point((x,y), (pixel1 or pixel2)) #using OR operator

out_image_decrypt.save(out_filename_decrypt, 'PNG')
print("Done.")