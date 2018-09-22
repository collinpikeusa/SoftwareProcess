
def dispatch(parm={}):
    httpResponse = {}
    if(not('op' in parm)):
        httpResponse['status'] = 'error: missing op'
    elif(parm['op'] == 'create'):
        httpResponse['status'] = 'created'
        httpResponse['cube'] = createCube(parm)
    return httpResponse


# ------------------- Inner Functions ---------------------
def createCube(parm):
    cube = []
    colors = ['green', 'yellow', 'blue', 'white', 'red', 'orange']
    if('f' in parm):
        color[0] = parm['f']
    
    cube.extend(createSide(''))
    for face in expectedFaces:
        cube.extend(createSide(face))
    return cube

def createSide(parm):
    side = []
    for i in range(0, 9):
        side.append(parm)
    return side
