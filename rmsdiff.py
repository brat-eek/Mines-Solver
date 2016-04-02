from __future__ import division
from PIL import Image
import ImageChops
import math, operator
from PIL import ImageFilter

def rmsdiff2(im1,im2):
    pix1=im1.load()
    pix2=im2.load()
    hoja=[[0 for x in range(85)]for x in range(85)]
    for i in range(85):
        for j in range(85):
            hoja[i][j]=(pix1[i,j]-pix2[i,j])**2
    return sum(map(sum,hoja))

def rmsdiff3(im1,im2):
    pix1=im1.load()
    pix2=im2.load()
    #print im1.getpixel((0,0))
    #print pix1[0,0]
    #a=input()
    temp1=0
    temp2=0
    cmon=[[0 for x in range(20)]for x in range(20)]
    for p in range(0,20):
        for q in range(0,20):
            for i in range(4*p,4+4*p):
                for j in range(4*q,4+4*q):
                    temp1 = temp1 + pix1[i,j]
                    temp2 = temp2 + pix2[i,j] 
                    #temp =temp+(pix1[i,j]-pix2[i,j])**2
            temp1 = temp1/16
            temp2 = temp2/16
            cmon[p][q]=(temp1-temp2)**2
            temp1=0
            temp2=0
    return sum(map(sum,cmon))

def rmsdiff(im1, im2):
    h1 = im1.histogram()
    h2 = im2.histogram()

    rms = math.sqrt(reduce(operator.add,
        map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
    return rms

board = Image.open('board2.png')

image_numbers = [1, 2, 3, 4, 10, 50] # 10 -> open, 50 -> closed
img = {}
for i in image_numbers:
    img[i] = Image.open('num' + str(i) + '.png')
    img[i] = img[i].convert('L')
    img[i] = img[i].filter(ImageFilter.GaussianBlur(3))
    img[i].show()

tr = [[0 for x in range(8)] for x in range(8)]

c = []
ystart = 17

for i in xrange(0,8):
    xstart = 18
    for j in xrange(0,8):
        c = []
        converted_image = board.crop((xstart, ystart, xstart + 89, ystart + 88))
        converted_image = converted_image.convert('L')
        converted_image = converted_image.filter(ImageFilter.GaussianBlur(3))
        for f in image_numbers:
            c.append(rmsdiff2(img[f],converted_image))
        #if (i==0 and j==7):
            #print c
            #converted_image.show()        
        tr[i][j] = c.index(min(c))	
        xstart = xstart + 89
    ystart = ystart + 88
print tr