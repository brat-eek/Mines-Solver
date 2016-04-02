from PIL import Image
import math, operator
import ImageChops
import os
import time
from PIL import ImageFilter

def rmsdiff3(im1,im2):
    pix1=im1.load()
    pix2=im2.load()
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

def neighbour(i,j):
	hmunop=0
	hmbbs=0
	uo = [[0 for x in range(2)] for x in range(10)]

	if i-1>=0 and j-1>=0:
		if trix[i-1][j-1]==-1:
			hmbbs=hmbbs+1
		
		if trix[i-1][j-1]==0:
			hmunop=hmunop+1
			uo[hmunop-1][0]=i-1
			uo[hmunop-1][1]=j-1
		
	
	if i-1>=0 and j>=0:
		if trix[i-1][j]==-1:
			hmbbs=hmbbs+1
		
		if trix[i-1][j]==0:
			hmunop=hmunop+1
			uo[hmunop-1][0]=i-1
			uo[hmunop-1][1]=j
		
	
	if i-1>=0 and j+1<=7:
		if trix[i-1][j+1]==-1:
			hmbbs=hmbbs+1
		
		if trix[i-1][j+1]==0:
			hmunop=hmunop+1
			uo[hmunop-1][0]=i-1
			uo[hmunop-1][1]=j+1
		
	
	if i>=0 and j-1>=0:
		if trix[i][j-1]==-1:
			hmbbs=hmbbs+1
		
		if trix[i][j-1]==0:
			hmunop=hmunop+1
			uo[hmunop-1][0]=i
			uo[hmunop-1][1]=j-1
		
	
	if i>=0 and j+1<=7:
		if trix[i][j+1]==-1:
			hmbbs=hmbbs+1
		
		if trix[i][j+1]==0:
			hmunop=hmunop+1
			uo[hmunop-1][0]=i
			uo[hmunop-1][1]=j+1
		
	
	if i+1<=7 and j-1>=0:
		if trix[i+1][j-1]==-1:
			hmbbs=hmbbs+1
		
		if trix[i+1][j-1]==0:
			hmunop=hmunop+1
			uo[hmunop-1][0]=i+1
			uo[hmunop-1][1]=j-1
		
	
	if i+1<=7 and j>=0:
		if trix[i+1][j]==-1:
			hmbbs=hmbbs+1
		
		if trix[i+1][j]==0:
			hmunop=hmunop+1
			uo[hmunop-1][0]=i+1
			uo[hmunop-1][1]=j
		
	
	if i+1<=7 and j+1<=7:
		if trix[i+1][j+1]==-1:
			hmbbs=hmbbs+1
		
		if trix[i+1][j+1]==0:
			hmunop=hmunop+1
			uo[hmunop-1][0]=i+1
			uo[hmunop-1][1]=j+1

	#printf("unopened are %d\n and bombs are  %d\n",hmunop,hmbbs);
	newno=trix[i][j]-hmbbs
	if newno==0:
		#set all unopened boxes as click karo lapak ke
		for p in range(0,hmunop):
			xi=uo[p][0]
			yi=uo[p][1]
			trix[uo[p][0]][uo[p][1]]=100
			os.system("xdotool mousemove {0} {1} click 1".format(300+yi*90,xi*90+70))
		
	
	if hmunop-newno==0:
		#set all unopened boxes as bombed
		for p in range(0,hmunop):
			xi=uo[p][0]
			yi=uo[p][1]
			trix[uo[p][0]][uo[p][1]]=-1;
			os.system("xdotool mousemove {0} {1} click 3".format(300+90*yi,70+90*xi))
				


def decide(where):
	if where==0:
		return 1
	elif where==1:
		return 2
	elif where==2:
		return 3
	elif where==3:
		return 4
	elif where==4:
		return 10
	elif where==5: 
		return 0
	elif where==6:
		return -1



trix = [[0 for x in range(8)] for x in range(8)]
'''
trix=[[0,-1,1,10,10,10,2,-1],
		[-1,2,1,10,10,10,2,-1],
		[2,2,1,1,1,1,1,1],
		[1,-1,1,1,-1,1,10,10],
		[1,1,1,2,2,2,10,10],
		[10,10,10,2,-1,2,10,10],
		[1,1,10,3,-1,3,10,10],
		[-1,1,10,2,-1,2,10,10]]
'''
time.sleep(2)
os.system("xdotool mousemove 500 271 click 1")    
os.system("xdotool mousemove 644 527 click 1")
os.system("xdotool mousemove 942 514 click 1")
cnt = 0
while True:		
	#time.sleep(1)   
	cnt = cnt + 1
	os.system("maim -x 250 -y 25 -w 750 -h 735 -d 1 ~/mines/board.png")
 	#time.sleep(1) # maybe remove this
 	#a=input("continue")
	board = Image.open('board.png')

	image_numbers = [1, 2, 3, 4, 10, 50, 99] # 10 -> open, 50 -> closed
	img = {}
	for i in image_numbers:
		img[i] = Image.open('num' + str(i) + '.png')
		img[i] = img[i].convert('L')
		img[i] = img[i].filter(ImageFilter.GaussianBlur(3))
    	#img[i].show()


	ystart = 17
	for i in xrange(0,8):
		xstart = 16
		for j in xrange(0,8):
			c = []
			converted_image = board.crop((xstart, ystart, xstart + 89, ystart + 88))
			converted_image = converted_image.convert('L')
			converted_image = converted_image.filter(ImageFilter.GaussianBlur(3))

			for f in image_numbers:
				c.append(rmsdiff3(img[f],converted_image))

			trix[i][j] = decide(c.index(min(c)))	
			xstart = xstart + 89
		ystart = ystart + 88

	

	for i in range(0,8):      #when removing comments tab this inside while
		for j in range(0,8):
			if trix[i][j]>=1 and trix[i][j]<9:
				neighbour(i,j)

	#print trix
	#a=input("continue")