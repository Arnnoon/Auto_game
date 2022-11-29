from re import X
from pyautogui import *
import pyautogui
import time
import keyboard #{'alt', 'alt gr', 'ctrl', 'left alt', 'left ctrl', 'left shift', 'left windows', 'right alt', 'right ctrl', 'right shift', 'right windows', 'shift', 'windows'}
import random
import win32api, win32con

# click :)
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# continuous click
def continuousclick():
    while keyboard.is_pressed('left alt') == False:
        if(keyboard.is_pressed('s') == True):
            x, y = pyautogui.position()
            click(x, y)

# return color value(r, g, b) of pixel
def checkcolor(x, y):
    pic = pyautogui.screenshot(region = (0,0,1919,1079))
    r, g, b = pic.getpixel((x, y))
    return r, g, b

# print position and color value(r, g, b) of given position
def checkPosition(x, y):
    while keyboard.is_pressed('left alt') == False:
        if keyboard.is_pressed('s') == True:
            r, g ,b = checkcolor(x, y)
            print("# x,y (" + str(x) + ", " + str(y) + ")   r,g,b (" + str(r) + ", " + str(g) + ", " + str(b) + ")\t\tif checkcolor("+ str(x) + ", " + str(y) + ")  == (" + str(r) + ", " + str(g) + ", " + str(b) + "):")
    return 1

# print position and color value(r, g, b) of mouse position
def checkClick():
    x1 = y1 = x2 = y2 = -1
    while keyboard.is_pressed('left alt') == False:
        if(keyboard.is_pressed('s') == True):
            x, y = pyautogui.position()
            r, g, b = checkcolor(x, y)
            print("# x,y (" + str(x) + ", " + str(y) + ")   r,g,b (" + str(r) + ", " + str(g) + ", " + str(b) + ")\tif checkcolor("+ str(x) + ", " + str(y) + ")  == (" + str(r) + ", " + str(g) + ", " + str(b) + "):")
            time.sleep(0.1)
        elif(keyboard.is_pressed('a') == True):
            x1, y1 = pyautogui.position()
        elif(keyboard.is_pressed('d') == True):
            x2, y2 = pyautogui.position()

        if x1 != -1 and y1 != -1 and x2 != -1 and y2 != -1:
            print("# x1,y1 (" + str(x1) + ", " + str(y1) + ")  x2,y2 (" + str(x2) + ", " + str(y2) + ")\trandclick(" + str(x1) + ", " + str(y1) + ", " + str(x2) + ", " + str(y2) + ")")
            x1 = y1 = x2 = y2 = -1
            time.sleep(0.1)
    return 1

# return a random pixel position from given area
def randomarea(x1, y1, x2, y2):
    diffx = x2 - x1
    diffy = y2 - y1
    xx = x1 + int(random.random() * diffx)
    yy = y1 + int(random.random() * diffy)
    return xx, yy

# random click from given area
def randclick(x1, y1, x2, y2):
    x, y = randomarea(x1, y1, x2, y2)
    click(x, y)
    return x, y

# random click radius 0-25 pixels around first position
def randclick2(x, y):
    x = x + int(random.random() * 25)
    y = y + int(random.random() * 25)
    click(x, y)
    return x, y

# timesleep for input time + 0-1 sec
def randtimesleep(inputtime):
    pm5 = random.random() * random.random()
    randtime = pm5 + inputtime
    time.sleep(randtime)

def autoRTA(times):
    x = 0
    y = 0
    round = 0
    print("autoRTA will start in 3 sec")
    time.sleep(3)
    print("autoRTA is starting")
    if times == 0:
        times = 999999
    start_time = time.strftime("%H:%M:%S", time.localtime())
    while keyboard.is_pressed('left alt') == False:
        if times < round:
            break
        # x,y (1776, 563)   r,g,b (82, 55, 51)
        if checkcolor(1776, 563) == (82, 55, 51):
            round += 1
            print("round " + str(round))
            randtimesleep(1)
            # x1,y1 = (1418, 440)   x2,y2 = (1747, 539)
            x, y = randclick(1418, 440, 1747, 539)
            print('\tfindmatch\tclick(' + str(x) + ', ' + str(y) + ')')	
            randtimesleep(1)
            # x,y (901, 614)   r,g,b (248, 233, 173)
            if checkcolor(901, 614) == (248, 233, 173):
                round -= 1
                print("\tout of RTA ticket")
                print("finished auto rta")
                # x1,y1 = (861, 594)   x2,y2 = (1017, 674)
                x, y = randclick(861, 594, 1017, 674)
                break
            time.sleep(60)
            while keyboard.is_pressed('left alt') == False:
                # x,y (254, 961)   r,g,b (255, 255, 255)
                if checkcolor(254, 961) == (255, 255, 255):
                    print("\tgive up \tFALSE")
                    randtimesleep(1)
                    # x1,y1 = (209, 925)   x2,y2 = (297, 1003)
                    x, y = randclick(209, 925, 297, 1003)
                    print('\tautoplay\tclick(' + str(x) + ', ' + str(y) + ')')
                    while True:
                        # x,y (367, 771)   r,g,b (204, 103, 20)
                        if checkcolor(367, 771) == (204, 103, 20):
                            randtimesleep(1)
                            # x1,y1 = (1068, 589)   x2,y2 = (1604, 851) 
                            x, y = randclick(1068, 589, 1604, 851)
                            print('\tmatchfinish\tclick(' + str(x) + ', ' + str(y) + ')')
                            break
                        else:
                            time.sleep(5)
                    break
                else:
                    # x,y (946, 604)   r,g,b (215, 179, 87)
                    if checkcolor(946, 604) == (215, 179, 87):
                        print("\tgive up \tTRUE")
                        randtimesleep(1)
                        # x1,y1 = (880, 595)   x2,y2 = (1004, 671)
                        x, y = randclick(880, 595, 1004, 671)
                        break
        randtimesleep(1)    
        
    finish_time = time.strftime("%H:%M:%S", time.localtime())
    print("\n" + str(round) + " rounds")
    print("start time:\t", start_time)
    print("finish time:\t", finish_time)
    return 1

def autoRTAsl(times):
    x = 0
    y = 0
    round = 0
    print("auto Special League RTA will start in 3 sec")
    time.sleep(3)
    print("auto Special League RTA is starting")
    if times == 0:
        times = 999999
    start_time = time.strftime("%H:%M:%S", time.localtime())
    while keyboard.is_pressed('left alt') == False:
        if times < round:
            break
        # x,y (1269, 842)   r,g,b (245, 147, 16)
        if checkcolor(1269, 842) == (245, 147, 16):
            round += 1
            print("round " + str(round))
            randtimesleep(1)
            # x1,y1 (1262, 834)  x2,y2 (1604, 937)
            x, y = randclick(1262, 834, 1604, 937)
            print('\tfindmatch\tclick(' + str(x) + ', ' + str(y) + ')')	
            randtimesleep(1)
            # x,y (901, 614)   r,g,b (248, 233, 173)
            if checkcolor(901, 614) == (248, 233, 173):
                round -= 1
                print("\tout of RTA ticket")
                print("finished auto rta")
                # x1,y1 = (861, 594)   x2,y2 = (1017, 674)
                x, y = randclick(861, 594, 1017, 674)
                break
            randtimesleep(1)
            while keyboard.is_pressed('left alt') == False:
                # Ban Oliver!!!
                # x,y (297, 172)   r,g,b (202, 76, 55)
                if checkcolor(297, 172) == (202, 76, 55):
                    print("\tBan Oliver")
                    randtimesleep(1)
                    # x1,y1 (1576, 550)  x2,y2 (1622, 586)
                    x, y = randclick(1576, 550, 1622, 586)
                    randtimesleep(1)
                    # x1,y1 (758, 609)  x2,y2 (886, 737)
                    x, y = randclick(758, 609, 886, 737)
                    randtimesleep(1)
                    # x1,y1 (828, 935)  x2,y2 (1059, 1000)
                    x, y = randclick(828, 935, 1059, 1000)
                    time.sleep(60)
                # End ban Oliver section
                # x,y (254, 961)   r,g,b (255, 255, 255)
                if checkcolor(254, 961) == (255, 255, 255):
                    print("\tgive up \tFALSE")
                    randtimesleep(1)
                    # x1,y1 = (209, 925)   x2,y2 = (297, 1003)
                    x, y = randclick(209, 925, 297, 1003)
                    print('\tautoplay\tclick(' + str(x) + ', ' + str(y) + ')')
                    while True:
                        # x,y (368, 770)   r,g,b (230, 181, 83)
                        if checkcolor(368, 770) == (230, 181, 83):
                            randtimesleep(1)
                            # x1,y1 = (1068, 589)   x2,y2 = (1604, 851) 
                            x, y = randclick(1068, 589, 1604, 851)
                            print('\tmatchfinish\tclick(' + str(x) + ', ' + str(y) + ')')
                            break
                        else:
                            time.sleep(5)
                    break
                else:
                    # x,y (946, 604)   r,g,b (215, 179, 87)
                    if checkcolor(946, 604) == (215, 179, 87):
                        print("\tgive up \tTRUE")
                        randtimesleep(1)
                        # x1,y1 = (880, 595)   x2,y2 = (1004, 671)
                        x, y = randclick(880, 595, 1004, 671)
                        break
        randtimesleep(1)    
        
    finish_time = time.strftime("%H:%M:%S", time.localtime())
    print("\n" + str(round) + " rounds")
    print("start time:\t", start_time)
    print("finish time:\t", finish_time)
    return 1

def autoTOA():
    x = 0
    y = 0
    boss = 0
    print("autoTOA will start in 3 sec")
    time.sleep(3)
    print("autoTOA is starting")
    while keyboard.is_pressed('left alt') == False:
        boss = 0
        # x,y (1554, 764)   r,g,b (241, 226, 167)
        if checkcolor(1554, 764) == (241, 226, 167):
            # x1,y1 = (1433, 682)   x2,y2 = (1675, 793)
            x, y = randclick(1433, 682, 1675, 793)
            print('start state\t\tclick(' + str(x) + ', ' + str(y) + ')')
            print("\tloading...")
            randtimesleep(6)
            # x,y (383, 962)    r,g,b (255, 255, 255)
            if checkcolor(383, 962) == (255, 255, 255):
                randtimesleep(1)
                # x1,y1 = (345, 925)   x2,y2 = (424, 998)
                x, y = randclick(345, 925, 424, 998)
                print('\tauto FALSE\tclick(' + str(x) + ', ' + str(y) + ')')
            else:
                print("\tauto TRUE")
            randtimesleep(0.5)
            while True:
                # x,y (947, 56)    r,g,b (253, 253, 68)
                r,g,b = checkcolor(947, 56)
                if r > 230 and g > 230 and b < 75 and boss == 0:
                    randtimesleep(1)
                    # x1,y1 = (909, 292)   x2,y2 = (973, 519)
                    x, y = randclick(909, 292, 973, 519)
                    print("\tboss battle")
                    boss = 1
                # x,y (1432, 535)   r,g,b (234, 42, 94)
                if checkcolor(1432, 535) == (234, 42, 94):
                    randtimesleep(0.5)
                    # x1,y1 = (1352, 473)   x2,y2 = (1536, 596)
                    x, y = randclick(1352, 473, 1536, 596)
                    print('finished state\t\tclick(' + str(x) + ', ' + str(y) + ')')
                    # x,y (990, 169)   r,g,b (255, 253, 58)
                    if checkcolor(990, 169) == (255, 253, 58):
                        randtimesleep(0.5)
                        # x1,y1 (1017, 529)  x2,y2 (1522, 623)
                        x, y = randclick(1017, 529, 1522, 623)
                        print('\tdefeated\tclick(' + str(x) + ', ' + str(y) + ')') 
                        return 1
                    # x,y (914, 164)   r,g,b (255, 255, 49)
                    if checkcolor(914, 164) == (255, 255, 49):
                        randtimesleep(0.5)
                        # x1,y1 = (1352, 473)   x2,y2 = (1536, 596)
                        x, y = randclick(1352, 473, 1536, 596)
                        print('\topen reward\tclick(' + str(x) + ', ' + str(y) + ')')
                        randtimesleep(1.5)
                        # x1,y1 = (871, 757)   x2,y2 = (1004, 832)
                        x, y = randclick(871, 757, 1004, 832)
                        print('\tclaim reward\tclick(' + str(x) + ', ' + str(y) + ')')
                    randtimesleep(0.5)
                    # x1,y1 = (473, 533)   x2,y2 = (782, 621)
                    x, y = randclick(473, 533, 782, 621)
                    print('\tnext state\tclick(' + str(x) + ', ' + str(y) + ')')
                    break
                time.sleep(3)
        randtimesleep(0.5)
    return 1

def oneStupgrade():
    round = 1
    print("oneSupgrade will start in 3 sec")
    time.sleep(3)
    print("oneSupgrade is starting")
    while keyboard.is_pressed('left alt') == False:  
        randtimesleep(0.5)
        # x,y (1162, 907)   r,g,b (248, 198, 104)
        if checkcolor(1162, 907) == (248, 198, 104):
            print("round " + str(round))
            randtimesleep(0.25)
            # x1,y1 = (1129, 877)   x2,y2 = (1200, 948)
            randclick(1129, 877, 1200, 948)
            print('\t1st open storage')
            randtimesleep(0.25)
            if round == 1:
                # x,y (510, 218)   r,g,b (248, 233, 173)
                if checkcolor(510, 218) != (248, 233, 173):
                    randtimesleep(0.25)
                    # x1,y1 = (376, 208)   x2,y2 = (643, 264)
                    randclick(376, 208, 643, 264)
                    randtimesleep(0.25)
                    # x1,y1 = (388, 439)   x2,y2 = (599, 500)
                    randclick(388, 439, 599, 500)
                    randtimesleep(0.25)
                    print('\tchoose category')
            # x1,y1 = (392, 310)   x2,y2 = (495, 410)
            randclick(392, 310, 495, 410)
            randtimesleep(0.25)
            print('\tpick 1st monster')
            while True:
                # x,y (940, 908)   r,g,b (248, 233, 173)
                if checkcolor(940, 908) == (248, 233, 173):
                    # x1,y1 = (828, 874)   x2,y2 = (1044, 932)
                    randclick(828, 874, 1044, 932)
                    randtimesleep(0.25)
                    print('\tconfirm 1st monster')
                    while True:
                        # x,y (1162, 907)   r,g,b (248, 198, 104)
                        if checkcolor(1162, 907) == (248, 198, 104):
                            # x1,y1 = (1129, 877)   x2,y2 = (1200, 948)
                            randclick(1129, 877, 1200, 948)
                            randtimesleep(0.25)
                            print('\t2nd open storage')
                            # x1,y1 (179, 455)  x2,y2 (343, 509)
                            randclick(179, 455, 343, 509)
                            randtimesleep(0.25)
                            # x1,y1 (383, 301)  x2,y2 (489, 405)
                            randclick(383, 301, 489, 405)
                            randtimesleep(0.25)
                            print('\tpick 2nd monster')
                            while True:
                                # x,y (940, 908)   r,g,b (248, 233, 173)
                                if checkcolor(940, 908) == (248, 233, 173):
                                    # x1,y1 = (828, 874)   x2,y2 = (1044, 932)
                                    randclick(828, 874, 1044, 932)
                                    randtimesleep(0.25)  
                                    print('\tconfirm 2nd monster')
                                    while True:
                                        # x,y (685, 950)   r,g,b (81, 180, 248)
                                        if checkcolor(685, 950) == (78, 177, 248):
                                            # x1,y1 (607, 866)  x2,y2 (870, 971)
                                            randclick(607, 866, 870, 971)
                                            randtimesleep(0.5)  
                                            print('\tconfirm upgrade')
                                            while True:
                                                # x,y (794, 640)   r,g,b (248, 233, 173)
                                                if checkcolor(794, 640) == (248, 233, 173):
                                                    # x1,y1 (679, 592)  x2,y2 (892, 673)
                                                    randclick(679, 592, 892, 673)
                                                    randtimesleep(1)
                                                    # x1,y1 (1626, 950)  x2,y2 (1713, 987)
                                                    randclick(1626, 950, 1713, 987)     
                                                    randtimesleep(1.5)  
                                                    print('\tskip')  
                                                    # x1,y1 (1449, 861)  x2,y2 (1600, 870)
                                                    randclick(1449, 861, 1600, 870)
                                                    randtimesleep(0.5)
                                                    # x,y (1548, 869)   r,g,b (208, 171, 101)
                                                    if checkcolor(1548, 869) != (208, 171, 101):
                                                        # x1,y1 (1449, 861)  x2,y2 (1600, 870)
                                                        randclick(1449, 861, 1600, 870)
                                                        randtimesleep(0.1)
                                                        randclick(1449, 861, 1600, 870)
                                                        print('\tskill up\tTRUE')
                                                        time.sleep(0.1)
                                                    print('\tend')
                                                    round += 1
                                                    break
                                            break
                                    break
                            break
                    break
    return 1

def breakEssence(max):
    round = 1
    print("breakEssence will start begin when you press 's'")
    while keyboard.is_pressed('left alt') == False:
        if(keyboard.is_pressed('s') == True):
            start_time = time.strftime("%H:%M:%S", time.localtime())
            x, y = pyautogui.position()
            randtimesleep(1)
            randclick2(x, y)
            while keyboard.is_pressed('left alt') == False and round <= max:
                print("\tround " + str(round))
                randtimesleep(0.35)
                # x,y (730, 946)   r,g,b (93, 193, 247)
                if checkcolor(730, 946) == (93, 193, 247):
                    # x1,y1 (659, 863)  x2,y2 (930, 972)
                    randclick(659, 863, 930, 972)
                    randtimesleep(0.65)
                    # x1,y1 (677, 591)  x2,y2 (897, 674)
                    randclick(677, 591, 897, 674)
                    randtimesleep(3.5)
                    # x1,y1 (833, 595)  x2,y2 (1050, 671)
                    randclick(833, 595, 1050, 671)
                    round += 1
            finish_time = time.strftime("%H:%M:%S", time.localtime())
            print("start time:\t", start_time)
            print("finish time:\t", finish_time)
            break
    return 1

def summon10x(amount):
    currentamount = 0
    print("summon 10 times will start when press 's'")
    while keyboard.is_pressed('left alt') == False:
        if(keyboard.is_pressed('s') == True):
            start_time = time.strftime("%H:%M:%S", time.localtime())
            while keyboard.is_pressed('left alt') == False and amount > currentamount:
                # x,y (764, 901)   r,g,b (248, 237, 192)
                if checkcolor(764, 901)  == (248, 237, 192):
                    # x1,y1 (604, 868)  x2,y2 (869, 968)
                    randclick(604, 868, 869, 968)
                    randtimesleep(0.5)
                    # x,y (1490, 839)   r,g,b (248, 233, 173)
                    while checkcolor(1490, 839)  != (248, 233, 173):\
                        # x1,y1 (1629, 951)  x2,y2 (1728, 981)
                        randclick(1629, 951, 1728, 981)
                        randtimesleep(0.25)
                        randtimesleep(0.5)
                    randclick(1377, 803, 1590, 870)
                    currentamount += 10
                    print("\tsummoned " + str(currentamount) + " monster")
            return 1

stop = 0
while keyboard.is_pressed('left alt') == False:
    #win32api.SetCursorPos((352, 546))          move cursor function
    #stop = continuousclick()
    #stop = checkPosition(352, 546)
    #stop = checkClick()
    #stop = autoRTA(0)
    #stop = autoRTAsl(0)
    #stop = autoTOA()
    #stop = oneStupgrade()
    #stop = breakEssence(20)
    stop = summon10x(2000)

    if stop == 1:
        break