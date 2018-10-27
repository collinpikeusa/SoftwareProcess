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
        rotatedCube = rotateCube(parm)
        if(rotatedCube[0:5] == 'error'):
            httpResponse['status'] = rotatedCube
        else:
            httpResponse['status'] = 'rotated'
            httpResponse['cube'] = rotatedCube 
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
    checkIfValidCube = checkCube(parm)
    if(checkIfValidCube[0:5] == 'error'):
        return checkIfValidCube
    if('face' not in parm):
        return 'error: face is missing'
    if(parm['face'] not in faces):
        return 'error: face is unknown'
    cube = parm['cube'].split(',')
    if(parm['face'] == 'F'):
        return rotateFaceF(cube)
    if(parm['face'] == 'f'):
        return rotateFacef(cube)
    if(parm['face'] == 'R'):
        return rotateFaceR(cube)
    if(parm['face'] == 'r'):
        return rotateFacer(cube)
    return 'error in rotating cube'

# ------ Supporting functions --------------
# -- Rotate functions ---
def rotateFaceF(cube):
    rotatedCube = list(cube)
    # fix front side
    rotatedCube[0] = cube[2]
    rotatedCube[1] = cube[5]
    rotatedCube[2] = cube[8]
    rotatedCube[3] = cube[1]
    rotatedCube[5] = cube[7]
    rotatedCube[6] = cube[0]
    rotatedCube[7] = cube[3]
    rotatedCube[8] = cube[6]
    # fix top side
    rotatedCube[42] = cube[9]
    rotatedCube[43] = cube[12]
    rotatedCube[44] = cube[15]
    # fix right side
    rotatedCube[9] = cube[47]
    rotatedCube[12] = cube[46]
    rotatedCube[15] = cube[45]
    # fix under side
    rotatedCube[45] = cube[29]
    rotatedCube[46] = cube[32]
    rotatedCube[47] = cube[35]
    # fix left side
    rotatedCube[29] = cube[44]
    rotatedCube[32] = cube[43]
    rotatedCube[35] = cube[42]
    return rotatedCube

def rotateFacef(cube):
    rotatedCube = list(cube)
    # fix front side
    rotatedCube[0] = cube[6]
    rotatedCube[1] = cube[3]
    rotatedCube[2] = cube[0]
    rotatedCube[3] = cube[7]
    rotatedCube[5] = cube[1]
    rotatedCube[6] = cube[8]
    rotatedCube[7] = cube[5]
    rotatedCube[8] = cube[2]
    # fix top side
    rotatedCube[42] = cube[35]
    rotatedCube[43] = cube[32]
    rotatedCube[44] = cube[29]
    # fix right side
    rotatedCube[9] = cube[42]
    rotatedCube[12] = cube[43]
    rotatedCube[15] = cube[44]
    # fix under side
    rotatedCube[45] = cube[15]
    rotatedCube[46] = cube[12]
    rotatedCube[47] = cube[9]
    # fix left side
    rotatedCube[29] = cube[45]
    rotatedCube[32] = cube[46]
    rotatedCube[35] = cube[47]
    return rotatedCube

def rotateFaceR(cube):
    rotatedCube = list(cube)
    # fix Right side
    rotatedCube[9] = cube[11]
    rotatedCube[10] = cube[14]
    rotatedCube[11] = cube[17]
    rotatedCube[12] = cube[10]
    rotatedCube[14] = cube[16]
    rotatedCube[15] = cube[9]
    rotatedCube[16] = cube[12]
    rotatedCube[17] = cube[15]
    # fix top side
    rotatedCube[44] = cube[18]
    rotatedCube[41] = cube[21]
    rotatedCube[38] = cube[24]
    # fix back side
    rotatedCube[18] = cube[53]
    rotatedCube[21] = cube[50]
    rotatedCube[24] = cube[47]
    # fix under side
    rotatedCube[47] = cube[2]
    rotatedCube[50] = cube[5]
    rotatedCube[53] = cube[8]
    # fix front side
    rotatedCube[2] = cube[38]
    rotatedCube[5] = cube[41]
    rotatedCube[8] = cube[44]
    return rotatedCube

def rotateFacer(cube):
    rotatedCube = list(cube)
    # fix right side
    rotatedCube[9] = cube[15]
    rotatedCube[10] = cube[12]
    rotatedCube[11] = cube[9]
    rotatedCube[12] = cube[16]
    rotatedCube[14] = cube[10]
    rotatedCube[15] = cube[17]
    rotatedCube[16] = cube[14]
    rotatedCube[17] = cube[11]
    # fix top side
    rotatedCube[44] = cube[8]
    rotatedCube[41] = cube[5]
    rotatedCube[38] = cube[2]
    # fix back side
    rotatedCube[18] = cube[44]
    rotatedCube[21] = cube[41]
    rotatedCube[24] = cube[38]
    # fix under side
    rotatedCube[47] = cube[24]
    rotatedCube[50] = cube[21]
    rotatedCube[53] = cube[18]
    # fix front side
    rotatedCube[2] = cube[47]
    rotatedCube[5] = cube[50]
    rotatedCube[8] = cube[53]
    return rotatedCube

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
