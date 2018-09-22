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
#    output: '{'status': 'created', 'cube': [
#                'f',  'f',  'f',
#                'f',  'f',  'f',
#                'f',  'f',  'f',
#                'r', 'r', 'r',
#                'r', 'r', 'r',
#                'r', 'r', 'r', 
#                'b', 'b', 'b',
#                'b', 'b', 'b',
#                'b', 'b', 'b', 
#                'l', 'l', 'l',
#                'l', 'l', 'l',
#                'l', 'l', 'l', 
#                't', 't', 't',
#                't', 't', 't', 
#                't', 't', 't',
#                'u', 'u', 'u',
#                'u', 'u', 'u',
#                'u', 'u', 'u',]}
#
#    test 040
#    input:    parm: {'op': 'create', 'f': 'f', 'r': 'r', 'b': 'b', 'l': 'l', 't': '1'}
#    output:   {'status': 'created', 'cube': [
#                    'f',  'f',  'f',
#                    'f',  'f',  'f',
#                    'f',  'f',  'f',
#                    'r', 'r', 'r',
#                    'r', 'r', 'r',
#                    'r', 'r', 'r',
#                    'b', 'b', 'b',
#                    'b', 'b', 'b',
#                    'b', 'b', 'b',
#                    'l', 'l', 'l',
#                    'l', 'l', 'l',
#                    'l', 'l', 'l',
#                    '1', '1', '1',
#                    '1', '1', '1',
#                    '1', '1', '1',
#                    'orange', 'orange', 'orange',
#                    'orange', 'orange', 'orange',
#                    'orange', 'orange', 'orange']}
#
#    test 050
#    input:    parm: {'op': 'create', 'f': 'f', 'r': 'r', 'b': 'b', 'l': 'l', 'under': '42'}
#    output:   {'status': 'created', 'cube': [
#                    'f',  'f',  'f',
#                    'f',  'f',  'f',
#                    'f',  'f',  'f',
#                    'r', 'r', 'r',
#                    'r', 'r', 'r',
#                    'r', 'r', 'r',
#                    'b', 'b', 'b',
#                    'b', 'b', 'b',
#                    'b', 'b', 'b',
#                    'l', 'l', 'l',
#                    'l', 'l', 'l',
#                    'l', 'l', 'l',
#                    '1', '1', '1',
#                    '1', '1', '1',
#                    '1', '1', '1',
#                    'orange', 'orange', 'orange',
#                    'orange', 'orange', 'orange',
#                    'orange', 'orange', 'orange']}
#
# Sad Path
#    test 910
#        input: parm: {'op': 'create', 'f': 'red', 'u': 'red'}
#        output: {'status': 'error: at least two faces have the same color'}

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

    def test100_040_ShouldCreateCubeWithAllDifferentSidesButOneAndANumber(self):
        parm = {'op': 'create', 'f': 'f', 'r': 'r', 'b': 'b', 'l': 'l', 't': '1'}
        expectedFaces = ['f', 'r', 'b', 'l', '1', 'orange']
        actualResult = RCube.createCube(parm)
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0,9):
                self.assertEqual(face, actualResult[elementIndex])
                elementIndex += 1
    
    def test100_050_ShouldCreateCubeWithAllDifferentSidesButOneAndANumberAndInvalidSyntax(self):
        parm = {'op': 'create', 'f': 'f', 'r': 'r', 'b': 'b', 'l': 'l', 't': '1','under': '42'}
        expectedFaces = ['f', 'r', 'b', 'l', '1', 'orange']
        actualResult = RCube.createCube(parm)
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0,9):
                self.assertEqual(face, actualResult[elementIndex])
                elementIndex += 1
