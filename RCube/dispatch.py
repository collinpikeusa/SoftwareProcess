
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
        if(duplicate > 1):
            httpResponse['status'] = 'error: at least two faces have the same color'
        else:  
            httpResponse['status'] = 'created'
        httpResponse['cube'] = createCube(parm)
    return httpResponse


# ------------------- Inner Functions ---------------------
def createCube(parm):
    cube = []
    colors = ['green', 'yellow', 'blue', 'white', 'red', 'orange']
    if('f' in parm):
        colors[0] = parm['f']
    if('r' in parm):
        colors[1] = parm['r']
    if('b' in parm):
        colors[2] = parm['b']
    if('l' in parm):
        colors[3] = parm['l']
    if('t' in parm):
        colors[4] = parm['t']
    if('u' in parm):
        colors[5] = parm['u']
    for face in colors:
        cube.extend(createSide(face))
    return cube

def createSide(parm):
    side = []
    for i in range(0, 9):
        side.append(parm)
    return side
