import os
import time

time.sleep(3)
x=6
y=6
os.system("xdotool mousemove 500 271 click 3")    
os.system("xdotool mousemove 644 527 click 3")
os.system("xdotool mousemove 942 514 click 3")
a=input()
os.system("xdotool getmouselocation")
time.sleep(2)
x=2
y=2
os.system("xdotool mousemove 300+{0}*90 70+{1}*90 click 1".format(y,x))
x=6
y=6
os.system("xdotool getmouselocation")
time.sleep(2)
os.system("xdotool mousemove 300+{0}*90 70+{1}*90 click 1".format(y,x))
x=0
y=7
os.system("xdotool getmouselocation")
time.sleep(2)
os.system("xdotool mousemove 300+{0}*90 70+{1}*90 click 3".format(y,x))
os.system("xdotool getmouselocation")