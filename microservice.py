'''
    Functions used for starting Flask
    Created on Sep 22, 2018
    
    @author: Collin Pike
'''

import os
from flask import Flask, request
import RCube.dispatch as RCube

app = Flask(__name__)

#-----------------------------------
#  The following code is invoked when the path portion of the URL matches 
#         /rcube
#
#  Parameters are passed as a URL query:
#        /rcube?parm1=value1&parm2=value2
#
@app.route('/rcube')
def server():
    try:
        parm = {}
        operations = request.args.to_dict(flat=False)
        for key in operations:
            parm[key] = str(operations[key][-1])
        result = RCube.dispatch(parm)
        return str(result)
    except Exception as e:
        return e
    
    
#-----------------------------------
port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))

