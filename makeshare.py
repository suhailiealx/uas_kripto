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


img1 = Image.open(infile1) #original file
img2 = Image.open(infile2) #share user

f, e = os.path.splitext("outfile")
out_filename_system = f+"_shareSystem.png"

img1 = img1.convert('1')  # convert image to 1 bit
img2 = img2.convert('1')  # convert image to 1 bit

width = img1.size[0]*2
height = img1.size[1]*2

out_image_system = Image.new('1', (width, height))
draw_system = ImageDraw.Draw(out_image_system)

C0 = ((1, 0, 1, 0), (0, 1, 0, 1))
C1 = ((1, 0, 0, 1), (0, 1, 1, 0))

# Cycle through pixels
for x in xrange(0, int(width/2)):
    for y in xrange(0, int(height/2)):
        pixel1 = img1.getpixel((x, y))
        if pixel1 == 0: #Pixel was black
            draw_system.point((x*2, y*2), not(img2.getpixel((x*2,y*2))))
            draw_system.point((x*2+1, y*2), not(img2.getpixel((x*2+1,y*2))))
            draw_system.point((x*2, y*2+1), not(img2.getpixel((x*2,y*2+1))))
            draw_system.point((x*2+1, y*2+1), not(img2.getpixel((x*2+1,y*2+1))))

        else : #Pixel was white
            draw_system.point((x*2, y*2), img2.getpixel((x*2,y*2)))
            draw_system.point((x*2+1, y*2), img2.getpixel((x*2+1,y*2)))
            draw_system.point((x*2, y*2+1), img2.getpixel((x*2,y*2+1)))
            draw_system.point((x*2+1, y*2+1), img2.getpixel((x*2+1,y*2+1)))


out_image_system.save(out_filename_system, 'PNG')
print("Done.")