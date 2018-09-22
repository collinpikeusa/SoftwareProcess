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
#
#    test 020
#    input:    parm: {'op': 'create', 'f': 'purple'}    one option
#    output:    default model cube, which is a JSON string with one change:
#        {'status': 'created', 'cube': [
#            'purple', 'purple', 'purple',
#            'purple', 'purple', 'purple',
#            'purple', 'purple', 'purple', 
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
#    test 030
#    input:  parm: {'op': 'create', 'r': 'r', 'l': 'l', 't': 't', 'u': 'u', 'f': 'f', 'b': 'b'}
#    output

    def test100_010_ShouldCreateEntireDefaultCube(self):
        parm = {'op': 'create'}
        expectedFaces = ['green', 'yellow', 'blue', 'white', 'red', 'orange']
        actualResult = RCube.createCube(parm)
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0,9):
                self.assertEqual(face, actualResult[elementIndex])
                elementIndex += 1
    
    def test100_020_ShouldCreateCubeWithOneDifferentSide(self):
        parm = {'op': 'create', 'f': 'purple'}
        expectedFaces = ['purple', 'yellow', 'blue', 'white', 'red', 'orange']
        actualResult = RCube.createCube(parm)
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0,9):
                self.assertEqual(face, actualResult[elementIndex])
                elementIndex += 1
        
    def test100_030_ShouldCreateCubeWithAllDifferentSides(self):
        parm = {'op': 'create', 'r': 'r', 'l': 'l', 't': 't', 'u': 'u', 'f': 'f', 'b': 'b'}
        expectedFaces = ['f', 'r', 'b', 'l', 't', 'u']
        actualResult = RCube.createCube(parm)
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0,9):
                self.assertEqual(face, actualResult[elementIndex])
                elementIndex += 1
