from __builtin__ import int

def dispatch(parm={}):
    httpResponse = {}
    if(not('op' in parm)):
        httpResponse['status'] = 'error: missing op'                
    elif(parm['op'] == 'create'):
        duplicate = 0
        for i in parm.values():
            for j in parm.values():
                if(i == j):
                    duplicate += 1
            if(duplicate > 1):
                break
            else:
                duplicate = 0
        if(duplicate > 1):
            httpResponse['status'] = 'error: at least two faces have the same color'
        cube = createCube(parm)
        if(isinstance(cube, int)):
            httpResponse['status'] = 'error: at least two faces have the same color'
        else:  
            httpResponse['status'] = 'created'
            httpResponse['cube'] = cube
    return httpResponse


# ------------------- Inner Functions ---------------------
def createCube(parm):
    cube = []
    colors = ['green', 'yellow', 'blue', 'white', 'red', 'orange']
    if('f' in parm):
        if(parm['f'] is not ''):
            colors[0] = parm['f']
    if('r' in parm):
        if(parm['f'] is not ''):
            colors[1] = parm['r']
    if('b' in parm):
        if(parm['f'] is not ''):
            colors[2] = parm['b']
    if('l' in parm):
        if(parm['f'] is not ''):
            colors[3] = parm['l']
    if('t' in parm):
        if(parm['f'] is not ''):
            colors[4] = parm['t']
    if('u' in parm):
        if(parm['f'] is not ''):
            colors[5] = parm['u']
    for face in colors:
        cube.extend(createSide(face))

    duplicate = 0
    for i in colors:
        for j in colors:
            if(i == j):
                duplicate += 1
        if(duplicate > 1):
            cube = -1
            break
        else:
            duplicate = 0
    return cube

def createSide(parm):
    side = []
    for _ in range(0, 9):
        side.append(parm)
    return side
