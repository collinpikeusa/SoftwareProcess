
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
    if(parm['f']):
        
    expectedFaces = ['green', 'yellow', 'blue', 'white', 'red', 'orange']
    for face in expectedFaces:
        cube.extend(createSide(face))
    return cube

def createSide(parm):
    side = []
    for i in range(0, 9):
        side.append(parm)
    return side
