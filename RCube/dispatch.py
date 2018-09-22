
def dispatch(parm={}):
    httpResponse = {}
    if(not('op' in parm)):
        httpResponse['status'] = 'error: missing op'
    elif(parm['op'] == 'create'):
        httpResponse['status'] = 'created'
        httpResponse['cube'] = createCube(parm)
    return httpResponse


# ------------------- Inner Funtions ---------------------
def createCube(parm):
    cube = ['green']
    return cube
