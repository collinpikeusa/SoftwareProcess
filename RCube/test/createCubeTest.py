'''
Created on Sep 22, 2018

@author: Collin Pike
'''
import unittest
import RCube.dispatch as RCube


class CreateCubeTest(unittest.TestCase):

# Happy path:
#    input:    parm: {'op': 'create'}    no options
#    output:    default model cube, which is a JSON string:
#        {'status': 'created', 'cube': [
#            'green', 'green', 'green',
#            'green', 'green', 'green',
#            'green', 'green', 'green', 
#            'yellow', 'yellow', 'yellow',
#            'yellow', 'yellow', 'yellow',
#            'yellow', 'yellow', 'yellow',
#            'blue', 'blue', 'blue',
#            'blue', 'blue', 'blue',
#            'blue', 'blue', 'blue',
#            'white', 'white', 'white',
#            'white', 'white', 'white',
#            'white', 'white', 'white',
#            'red', 'red', 'red',
#            'red','red', 'red',
#            'red', 'red', 'red',
#            'orange', 'orange', 'orange',
#            'orange', 'orange', 'orange', 'orange', 'orange', 'orange']} 

    def test100_010_ShouldCreateOneElementCube(self):
        parm = {'op': 'create'}
        expectedResult = ['green']
        actualResult = RCube.createCube(parm)
        self.assertListEqual(expectedResult, actualResult)
        

