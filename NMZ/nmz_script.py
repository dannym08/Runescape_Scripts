'''General NMZ script used for both windows and Mac.
    Flicks your prayer at 1hp so you can train in NMZ with Dharoks and stay at 1 hp.
    Leave courser over prayer with rapid heal selected on quick prayer'''

import os, time, random
os = os.name

#import libraries needed depending on OS
if os == 'nt': #windows
    import win32api, win32con
elif os == 'poxix': #mac
    from Quartz.CoreGraphics import CGEventCreateMouseEvent
    from Quartz.CoreGraphics import CGEventPost
    from Quartz.CoreGraphics import kCGEventMouseMoved
    from Quartz.CoreGraphics import kCGEventLeftMouseDown
    from Quartz.CoreGraphics import kCGEventLeftMouseDown
    from Quartz.CoreGraphics import kCGEventLeftMouseUp
    from Quartz.CoreGraphics import kCGMouseButtonLeft
    from Quartz.CoreGraphics import kCGHIDEventTap
    import Quartz


def click(x, y):
    '''Generates a mouse click at the current mouse location.'''
    if os == 'nt':
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,  0, 0, 0)
        sleep_time = random.randint(5, 35) #randomized to avoid detection
        sleep_time = sleep_time / 1000  # convert to milliseconds
        time.sleep(sleep_time)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,  0, 0, 0)
    elif os == 'posix':
        curX, curY = Quartz.CGEventGetLocation(Quartz.CGEventCreate(None))
        theEvent = CGEventCreateMouseEvent(None, kCGEventLeftMouseDown,(curX, curY),kCGMouseButtonLeft)
        CGEventPost(kCGHIDEventTap, theEvent)
        sleep_time = random.randint(5, 35) #randomized to avoid detection
        sleep_time = sleep_time / 1000  # convert to milliseconds
        time.sleep(sleep_time)
        theEvent = CGEventCreateMouseEvent(None, kCGEventLeftMouseUp, (curX, curY), kCGMouseButtonLeft)
        CGEventPost(kCGHIDEventTap, theEvent)


#Normal hp regen is every minute so you must flick prayer every minute.
#Click time randomized to avoid auto detection.
if __name__ == '__main__':
    while True:
        i = 1

        sleep_time = random.randint(25, 55)  # 22-55 seconds
        time.sleep(sleep_time)  # sleep in seconds
        click(0, 0)

        print("Click ", i)

        sleep_time = random.randint(350, 600)
        sleep_time = sleep_time / 1000  # conver to milliseconds
        time.sleep(sleep_time)
        click(0, 0)
        i+= 1