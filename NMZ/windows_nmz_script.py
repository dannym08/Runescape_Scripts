import win32api, win32con, time, random   


def click(x, y):
    ''' '''
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    

if __name__ == '__main__':
    while True:
        sleep_time = random.randint(25, 55) #22-55 seconds
        time.sleep(sleep_time) #sleep in seconds
        click(0, 0)
        
        sleep_time = random.randint(500, 950)
        sleep_time = sleep_time / 1000  #convert to miliseconds
        time.sleep(sleep_time)
        click(0, 0)
    
    
