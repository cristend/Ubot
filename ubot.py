import sys
import re
#class ubot

class ubot:
    def __init__(self):
        self.coordinate_x = 0
        self.coordinate_y = 0
        self.direction = 0
        self.drctn = {0:'North',1:'East',2:'South',3:'West'}
    def displayLocation(self):
        print "X: ",self.coordinate_x, " Y: ",self.coordinate_y, " Direction: ",self.drctn[self.direction]

#extract command of ubot to list
def extract_cmd(cmds):
    return [cmd for cmd in cmds if not cmd.isdigit()]

def extract_number(string):
    number_list = re.findall(r"W(\d+)",string)
    return number_list

#action follow command
def action(ubot,cmds):
    number_list = extract_number(cmds)
    cmd_list = extract_cmd(cmds)
    for cmd in cmd_list:
        if cmd=='L':
            turnLeft(ubot)
        elif cmd == 'R':
            turnRight(ubot)
        elif cmd == 'W':
            step = int(number_list.pop(0))
            walk(ubot,step)
    return ubot
#ubot move
def turnLeft(ubot):
    ubot.direction = (ubot.direction - 1) % 4

def turnRight(ubot):
    ubot.direction = (ubot.direction + 1) % 4

def walk(ubot,step):
    if ubot.direction == 0:
        y = ubot.coordinate_y
        y+= step
        ubot.coordinate_y = y
    elif ubot.direction == 1:
        x = ubot.coordinate_x
        x+= step
        ubot.coordinate_x = x
    elif ubot.direction == 2:
        y = ubot.coordinate_y
        y-= step
        ubot.coordinate_y = y
    elif ubot.direction == 3:
        x = ubot.coordinate_x
        x-= step
        ubot.coordinate_x = x

#main
def main(cmds):
    bot = ubot()
    bot = action(bot,cmds)
    bot.displayLocation()
    

if __name__ == "__main__":
     main(sys.argv[1])
