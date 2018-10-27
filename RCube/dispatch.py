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
    elif(parm['op'] == 'rotate'):
        httpResponse['status'] = rotateCube(parm)
    else:
        httpResponse['status'] = 'error: %s is not a valid op' % parm['op']
    return httpResponse


# ------------------- Inner Functions ---------------------

def createCube(parm):
    cube = []
    colors = defineColors(parm)
    if(isinstance(colors,int)):
        return -2
    for face in colors:
        cube.extend(createSide(face))

    if(not isDuplicate(colors)):
        return -1
    return cube

def checkCube(parm):
    color = defineColors(parm)
    if(color == -1):
        return 'error: unsolvable cube configuration'
    if(not isDuplicate(color)):
        return 'error: at least two faces have the same color'
    if('cube' not in parm):
        return 'error: cube must be specified'
    cube = parm['cube'].split(',')
    if(not isValidSize(cube)):
        return 'error: cube is not sized properly'
    if(not checkFacesForCorrectColors(cube, color)):
        return 'error: one of the faces is not a designated color'
    if(not checkNumberOfColors(cube, color)):
        return 'error: one of the colors is not the correct number'
    if(not checkMiddle(cube, color)):
        return 'error: middle does not match designated color'
    if(isFull(cube, color)):
        return 'full'
    if(isCrosses(cube)):
        return 'crosses'
    if(isSpots(cube)):
        return 'spots'
    if(not checkEdges(cube, color)):
        return 'error: unsolvable cube configuration'
    if(not checkCorners(cube, color)):
        return 'error: unsolvable cube configuration'
    return 'unknown'

def rotateCube(parm):
    faces = ['f', 'F', 'r', 'R', 'b', 'B', 'l', 'L', 't', 'T', 'u', 'U']
    if('cube' not in parm):
        return 'error: cube must be specified'
    if('face' not in parm):
        return 'error: face is missing'
    if(parm['face'] not in faces):
        return 'error: face is unknown'
    

# ------ Supporting functions --------------
# -- Check functions ---
def isFull(cube, colors):
    start = 0
    end = 9
    for color in colors:
        for i in range(start, end):
            if(cube[i] != color):
                return False
        start += 9
        end += 9
    return True

def isCrosses(cube):
    start = 0
    end = 9
    for _ in range(0, 6):
        oneSide = cube[start]
        anotherSide = cube[start + 1]
        if(oneSide == anotherSide):
            return False
        side = cube[start:end]
        crossSide = [oneSide, anotherSide, oneSide,
                     anotherSide, anotherSide, anotherSide,
                     oneSide, anotherSide, oneSide]
        if(side != crossSide):
            return False
        start += 9
        end += 9
    return True

def isSpots(cube):
    start = 0
    end = 9
    for _ in range(0, 6):
        oneSide = cube[start]
        anotherSide = cube[start + 4]
        if(oneSide == anotherSide):
            return False
        side = cube[start:end]
        spotSide = [oneSide, oneSide, oneSide,
                     oneSide, anotherSide, oneSide,
                     oneSide, oneSide, oneSide]
        if(side != spotSide):
            return False
        start += 9
        end += 9
    return True

def checkMiddle(cube, colors):
    color = 0
    for middle in range(4, 54, 9):
        if(cube[middle] != colors[color]):
            return False
        color += 1
    return True

def checkEdges(cube, colors):
    cubeEdgeColors = [[colors[0], colors[4]],
                      [colors[0], colors[1]],
                      [colors[0], colors[5]],
                      [colors[0], colors[3]],
                      [colors[1], colors[2]],
                      [colors[4], colors[2]],
                      [colors[3], colors[2]],
                      [colors[2], colors[5]],
                      [colors[1], colors[4]],
                      [colors[1], colors[5]],
                      [colors[4], colors[3]],
                      [colors[5], colors[3]]] 
    
    cubeEdges = [[cube[1], cube[43]],
                 [cube[5], cube[12]],
                 [cube[7], cube[46]],
                 [cube[3], cube[32]],
                 [cube[14], cube[21]],
                 [cube[37], cube[19]],
                 [cube[30], cube[23]],
                 [cube[25], cube[52]],
                 [cube[10], cube[41]],
                 [cube[16], cube[50]],
                 [cube[39], cube[28]],
                 [cube[48], cube[34]]]
    
    numberOfFoundEdges = 0
    foundEdge = []
    for edge in cubeEdges:
        for color in cubeEdgeColors:
            if(len(set(edge) - set(color)) == 0):
                if(color in foundEdge):
                    return False
                foundEdge.append(color)
                numberOfFoundEdges += 1
                
    if(numberOfFoundEdges != 12):
        return False
    return True

def checkCorners(cube, colors):
    cubeCornerColors = [[colors[0], colors[3], colors[4]],
                        [colors[0], colors[4], colors[1]],
                        [colors[0], colors[3], colors[5]],
                        [colors[0], colors[1], colors[5]],
                        [colors[3], colors[4], colors[2]],
                        [colors[2], colors[4], colors[1]],
                        [colors[1], colors[2], colors[5]],
                        [colors[3], colors[5], colors[2]]]
    
    cubeCorners = [[cube[0], cube[29], cube[42]],
                   [cube[2], cube[44], cube[9]],
                   [cube[6], cube[35], cube[45]],
                   [cube[8], cube[15], cube[47]],
                   [cube[27], cube[36], cube[20]],
                   [cube[18], cube[38], cube[11]],
                   [cube[17], cube[24], cube[53]],
                   [cube[33], cube[51], cube[26]]]
    
    numberOfFoundCorners = 0
    foundCorners = []
    for corner in cubeCorners:
        for color in cubeCornerColors:
            if(len(set(corner) - set(color)) == 0):
                if(color in foundCorners):
                    return False
                foundCorners.append(color)
                numberOfFoundCorners += 1

    if(numberOfFoundCorners != 8):
        return False
    return True

def checkNumberOfColors(cube, colors):
    for color in colors:
        numberOfColor = 0
        for i in range(0, 54):
            if(color == cube[i]):
                numberOfColor += 1
        if(numberOfColor != 9):
            return False
    return True

def isValidSize(cube):
    if(len(cube) == 54):
        return True
    return False

def checkFacesForCorrectColors(cube, color):
    for i in range(0, 54):
        if(cube[i] not in color):
            return False
    return True
            
# -- Create Functions ---

def createSide(parm):
    side = []
    for _ in range(0, 9):
        side.append(parm)
    return side

# -- Other Functions

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

def defineColors(parm):
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
