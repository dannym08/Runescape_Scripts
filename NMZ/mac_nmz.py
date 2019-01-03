''' Use general nmz_script now! This is left for reference for now'''
from Quartz.CoreGraphics import CGEventCreateMouseEvent
from Quartz.CoreGraphics import CGEventPost
from Quartz.CoreGraphics import kCGEventMouseMoved
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseUp
from Quartz.CoreGraphics import kCGMouseButtonLeft
from Quartz.CoreGraphics import kCGHIDEventTap
import Quartz

import random, time

def mouseEvent(type, posx, posy):
        theEvent = CGEventCreateMouseEvent(
                    None, 
                    type, 
                    (posx,posy), 
                    kCGMouseButtonLeft)
        CGEventPost(kCGHIDEventTap, theEvent)

def mousemove(posx,posy):
        mouseEvent(kCGEventMouseMoved, posx,posy);

def position():
        point = Quartz.CGEventGetLocation( Quartz.CGEventCreate(None) )
        return point.x, point.y

def click(posx,posy):
        # uncomment this line if you want to force the mouse 
        # to MOVE to the click location first (I found it was not necessary).
        #mouseEvent(kCGEventMouseMoved, posx,posy);
        curX, curY = position()
        mouseEvent(kCGEventLeftMouseDown, curX, curY);
        sleep_time = random.randint(5, 35)
        sleep_time = sleep_time / 1000 #conver to milliseconds
        time.sleep(sleep_time)
        mouseEvent(kCGEventLeftMouseUp, curX, curY);


if __name__ ==  '__main__':
    while True:
        sleep_time = random.randint(25, 55) #25-55 seconds
        time.sleep(sleep_time)
        click(0,0)
        print("Click")
        sleep_time = random.randint(350, 600)
        sleep_time = sleep_time / 1000 #conver to milliseconds
        time.sleep(sleep_time)
        click(0,0)
