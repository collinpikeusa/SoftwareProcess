'''
    Functions used for dispatch of microservice
    Created on Sep 22, 2018
    
    @author: Collin Pike
'''

from __builtin__ import int

def dispatch(parm={}):
    httpResponse = {}
    if(not('op' in parm)):
        httpResponse['status'] = 'error: missing op'
    elif(parm['op'] == ''):
        httpResponse['status'] = 'error: op code is missing'                 
    elif(parm['op'] == 'create'):
        cube = createCube(parm)
        if(isinstance(cube, int) and cube == -1):
            httpResponse['status'] = 'error: at least two faces have the same color'  
        elif(isinstance(cube, int) and cube == -2):
            httpResponse['status'] = 'error: face color is missing'  
        else:  
            httpResponse['status'] = 'created'
            httpResponse['cube'] = cube
    elif(parm['op'] == 'check'):
        httpResponse['status'] = checkCube(parm)
    else:
        httpResponse['status'] = 'error: %s is not a valid op' % parm['op']
    return httpResponse


# ------------------- Inner Functions ---------------------

def createCube(parm):
    cube = []
    colors = changeColors(parm)
    if(isinstance(colors,int)):
        return -2
    for face in colors:
        cube.extend(createSide(face))

    if(not isDuplicate(colors)):
        return -1
    return cube

def checkCube(parm):
    colors = changeColors(parm)
    if('cube' not in parm):
        return 'error: cube must be specified'
    cube = parm['cube'].split(',')
    print(cube)
    if(isFull(cube)):
        return 'full'
    return 'error: check failed'
    
def isFull(cube):
    sideCount = 0
    for _ in cube:
        sideCount += 1
    if(sideCount == 54):
        return True
    return False

def createSide(parm):
    side = []
    for _ in range(0, 9):
        side.append(parm)
    return side

def isDuplicate(colors):
    duplicate = 0
    for i in colors:
        for j in colors:
            if (i == j):
                duplicate += 1
        
        if (duplicate > 1):
            return False
        else:
            duplicate = 0
    
    return True

def changeColors(parm):
    colors = ['green', 'yellow', 'blue', 'white', 'red', 'orange']
    faces = ['f', 'r', 'b', 'l', 't', 'u']
    for i in range(0, 6):
        side = faces[i]
        if (side in parm):
            if (parm[side] is ''):
                return -1
            else:
                colors[i] = parm[side]
    return colors
