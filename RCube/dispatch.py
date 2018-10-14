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
    if(not isDuplicate(colors)):
        return 'error: colors are defined as duplicates'
    elif(not isValidCubeSize(cube)):
        return 'error: cube is not sized properly'
    elif(not checkNumberOfColors(cube, colors)):
        return 'error: incorrect number of colors'
    elif(not checkCorners(cube, colors)):
        return 'illegal cube'
    elif(not checkEdges(cube, colors)):
        return 'illegal cube'
    elif(not checkMiddle(cube, colors)):
        return 'illegal cube'
    elif(not checkSwaps(cube, colors)):
        return 'illegal cube'
    elif(isFull(cube, colors)):
        return 'full'
    elif(isCrosses(cube)):
        return 'crosses'
    elif(isSpots(cube)):
        return 'spots'
    return 'unknown'

# ------ Supporting functions --------------
# -- Check functions ---
def isFull(cube, colors):
    start = 0
    end = 9
    for color in colors:
        for i in range(start, end):
            if(color != cube[i]):
                return False
        start += 9
        end += 9
    return True

def isCrosses(cube):
    start = 0
    end = 9
    for _ in range(0, 6):
        cornerColor = cube[start]
        anotherColor = cube[start + 1]
        side = [cornerColor, anotherColor, cornerColor,
                anotherColor, anotherColor, anotherColor,
                cornerColor, anotherColor, cornerColor]
        face = cube[start:end]
        if(side != face):
            return False
        start += 9
        end += 9
    return True

def isSpots(cube):
    start = 0
    end = 9
    for _ in range(0, 6):
        spotColor = cube[start + 4]
        anotherColor = cube[start]
        side = [anotherColor, anotherColor, anotherColor,
                anotherColor, spotColor, anotherColor,
                anotherColor, anotherColor, anotherColor]
        face = cube[start:end]
        if(side != face):
            return False
        start += 9
        end += 9
    return True

def isValidCubeSize(cube):
    sideCount = 0
    for _ in cube:
        sideCount += 1
    if(sideCount == 54):
        return True
    return False

def isValidCube(cube, colors):
    if(not checkEdges(cube, colors)):
        return False
    
def checkEdges(cube, colors):
    if(not (checkTopFaceEdges(cube, colors) or checkBackFaceEdges(cube, colors) or checkLeftFaceEdges(cube, colors)
       or checkRightFaceEdges(cube, colors))):
        return False
    return True
        

def checkCorners(cube, colors):
    front_top_left = set([colors[0], colors[4], colors[3]])
    front_top_right = set([colors[0], colors[4], colors[1]])
    front_under_left = set([colors[0], colors[5], colors[3]])
    front_under_right = set([colors[0], colors[5], colors[1]])
    back_top_left = set([colors[2], colors[4], colors[3]])
    back_top_right = set([colors[2], colors[4], colors[1]])
    back_under_left = set([colors[2], colors[5], colors[3]])
    back_under_right = set([colors[2], colors[5], colors[1]])
    
    # ------- Top Left Corner Check -------
    cube_front_left_top = set([cube[0], cube[42], cube[29]])
    cube_front_right_top = set([cube[2], cube[44], cube[9]])
    cube_front_left_under = set([cube[6], cube[45], cube[35]])
    cube_front_right_under = set([cube[8], cube[47], cube[15]])
    cube_back_left_top = set([cube[20], cube[36], cube[27]])
    cube_back_right_top = set([cube[18], cube[38], cube[11]])
    cube_back_left_under = set([cube[24], cube[17], cube[53]])
    cube_back_right_under = set([cube[26], cube[51], cube[33]])
    
    cube_corners_original = [front_top_left, front_top_right, front_under_left, front_under_right,
                             back_top_left, back_top_right, back_under_left, back_under_right]
    cube_corners_mixed = [cube_front_left_top, cube_front_left_under, cube_front_right_top, cube_front_right_under,
                          cube_back_left_top, cube_back_left_under, cube_back_right_top, cube_back_right_under]
    
    match = 0
    for original_corner in cube_corners_original:
        for mixed_corner in cube_corners_mixed:
            if(len(list(mixed_corner - original_corner)) == 0):
                match += 1
    if(match != 8):
        return False
    return True

def checkTopFaceEdges(cube, colors):
    front_back = [colors[0], colors[2]]
    top_under = [colors[4], colors[5]]
    left_right = [colors[1], colors[3]]
    if(cube[1] in front_back):
        if(cube[43] in front_back):
            return False
    elif(cube[1] in left_right):
        if(cube[43] in left_right):
            return False
    elif(cube[1] in top_under):
        if(cube[43] in top_under):
            return False
    if(cube[3] in front_back):
        if(cube[32] in front_back):
            return False
    elif(cube[3] in left_right):
        if(cube[32] in left_right):
            return False
    elif(cube[3] in top_under):
        if(cube[32] in top_under):
            return False
    if(cube[5] in front_back):
        if(cube[12] in front_back):
            return False
    elif(cube[5] in left_right):
        if(cube[12] in left_right):
            return False
    elif(cube[5] in top_under):
        if(cube[12] in top_under):
            return False
    if(cube[7] in front_back):
        if(cube[46] in front_back):
            return False
    elif(cube[7] in left_right):
        if(cube[46] in left_right):
            return False
    elif(cube[7] in top_under):
        if(cube[46] in top_under):
            return False

def checkBackFaceEdges(cube, colors):
    front_back = [colors[0], colors[2]]
    top_under = [colors[4], colors[5]]
    left_right = [colors[1], colors[3]]
    if(cube[19] in front_back):
        if(cube[37] in front_back):
            return False
    elif(cube[19] in left_right):
        if(cube[37] in left_right):
            return False
    elif(cube[19] in top_under):
        if(cube[37] in top_under):
            return False
    if(cube[21] in front_back):
        if(cube[14] in front_back):
            return False
    elif(cube[21] in left_right):
        if(cube[14] in left_right):
            return False
    elif(cube[21] in top_under):
        if(cube[14] in top_under):
            return False
    if(cube[23] in front_back):
        if(cube[30] in front_back):
            return False
    elif(cube[23] in left_right):
        if(cube[30] in left_right):
            return False
    elif(cube[23] in top_under):
        if(cube[30] in top_under):
            return False
    if(cube[25] in front_back):
        if(cube[52] in front_back):
            return False
    elif(cube[25] in left_right):
        if(cube[52] in left_right):
            return False
    elif(cube[25] in top_under):
        if(cube[52] in top_under):
            return False

def checkRightFaceEdges(cube, colors):
    front_back = [colors[0], colors[2]]
    top_under = [colors[4], colors[5]]
    left_right = [colors[1], colors[3]]

    if(cube[10] in front_back):
        if(cube[41] in front_back):
            return False
    elif(cube[10] in left_right):
        if(cube[41] in left_right):
            return False
    elif(cube[10] in top_under):
        if(cube[41] in top_under):
            return False
    if(cube[16] in front_back):
        if(cube[50] in front_back):
            return False
    elif(cube[16] in left_right):
        if(cube[50] in left_right):
            return False
    elif(cube[16] in top_under):
        if(cube[50] in top_under):
            return False

def checkLeftFaceEdges(cube, colors):
    front_back = [colors[0], colors[2]]
    top_under = [colors[4], colors[5]]
    left_right = [colors[1], colors[3]]
    
    if(cube[39] in front_back):
        if(cube[28] in front_back):
            return False
    elif(cube[39] in left_right):
        if(cube[28] in left_right):
            return False
    elif(cube[39] in top_under):
        if(cube[28] in top_under):
            return False
    if(cube[48] in front_back):
        if(cube[34] in front_back):
            return False
    elif(cube[48] in left_right):
        if(cube[34] in left_right):
            return False
    elif(cube[48] in top_under):
        if(cube[34] in top_under):
            return False
    return True

def checkMiddle(cube, colors):
    middle = 4
    for color in colors:
        if(color != cube[middle]):
            return False
        middle += 9
    return True

def checkSwaps(cube, colors):
    swaps = 0
    start = 0
    end = 9
    for color in colors:
        for i in range(start, end):
            if(color != cube[i]):
                swaps += 1
        if(swaps == 1):
            return False
        start += 9
        end += 9
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
