import sys
import re
#class ubot

class ubot:
    def __init__(self):
        self.coordinate_x = 0
        self.coordinate_y = 0
        self.direction = 'North'
    def setLocation(self,x,y):
        self.coordinate_x = x
        self.coordinate_y = y
    def getX(self):
        return self.coordinate_x
    def getY(self):
        return self.coordinate_y
    def getDirection(self):
        return self.direction
    def setDirection(self,direction):
        self.direction = direction
    def setX(self,x):
        self.coordinate_x = x
    def setY(self,y):
        self.coordinate_y = y
    def displayLocation(self):
        print "X: ",self.coordinate_x, " Y: ",self.coordinate_y, " Direction: ",self.direction

#extract command of ubot to list
def extract_cmd(cmds):
    cmd_list = []
    for cmd in cmds:
        walk_cmd = {}
        if cmd.isdigit():
            continue
        else:
            cmd_list.append(cmd)
    return cmd_list

def extract_number(string):
    number_list = re.findall(r"W(\d+)",string)
    return number_list

#action follow command
def action(object,cmds):
    number_list = extract_number(cmds)
    cmd_list = extract_cmd(cmds)
    for cmd in cmd_list:
        if cmd=='L':
            turnLeft(object)
        elif cmd == 'R':
            turnRight(object)
        elif cmd == 'W':
            step = int(number_list.pop(0))
            walk(object,step)
    return object
#ubot move
def turnLeft(object):
    if object.getDirection() == 'North':
        object.setDirection('West')
    elif object.getDirection() == 'West':
        object.setDirection('South')
    elif object.getDirection() == 'South':
        object.setDirection('East')
    elif object.getDirection() == 'East':
        object.setDirection('North')

def turnRight(object):
    if object.getDirection() == 'North':
        object.setDirection('East')
    elif object.getDirection() == 'East':
        object.setDirection('South')
    elif object.getDirection() == 'South':
        object.setDirection('West')
    elif object.getDirection() == 'West':
        object.setDirection('North')

def walk(object,step):
    if object.getDirection() == 'North':
        y = object.getY()
        y+= step
        object.setY(y)
    elif object.getDirection() == 'East':
        x = object.getX()
        x+= step
        object.setX(x)
    elif object.getDirection() == 'South':
        y = object.getY()
        y-= step
        object.setY(y)
    elif object.getDirection() == 'West':
        x = object.getX()
        x-= step
        object.setX(x)

#main
def main(cmds):
    global ubot
    ubot = ubot()
    ubot = action(ubot,cmds)
    ubot.displayLocation()
    

if __name__ == "__main__":
     main(sys.argv[1])
