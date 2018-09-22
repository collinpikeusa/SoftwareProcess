
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
    cube = ['green', 'green', 'green',
            'green', 'green', 'green',
            'green', 'green', 'green', 
            'yellow', 'yellow', 'yellow',
            'yellow', 'yellow', 'yellow',
            'yellow', 'yellow', 'yellow',
            'blue', 'blue', 'blue',
            'blue', 'blue', 'blue',
            'blue', 'blue', 'blue',
            'white', 'white', 'white',
            'white', 'white', 'white',
            'white', 'white', 'white',
            'red', 'red', 'red',
            'red','red', 'red',
            'red', 'red', 'red',
            'orange', 'orange', 'orange',
            'orange', 'orange', 'orange',
            'orange', 'orange', 'orange']
    return cube

def createSide(parm):
    side = []
    for i in range(0, 9):
        side.append(parm)
    return side
