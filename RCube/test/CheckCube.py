'''
Created on Oct 12, 2018

@author: Collin Pike
'''
import unittest
import RCube.dispatch as RCube

class CheckCubeTest(unittest.TestCase):

    def test_CheckCube(self):
        cube = ['purple', 'purple', 'purple',
                'purple', 'purple', 'purple',
                'purple', 'purple', 'purple', 
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
        cubeDefinition = {'op': 'check', 'cube': cube}
        actual = RCube.checkCube(cubeDefinition)
        expected = 'full'
        self.assertEqual(actual, expected)
        
    def test_CheckCubeSadPath(self):
        cube = ['purple', 'purple', 'purple',
                'purple', 'purple', 'purple',
                'purple', 'purple', 'purple', 
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
                'orange', 'orange']
        cubeDefinition = {'op': 'check', 'cube': cube}
        actual = RCube.checkCube(cubeDefinition)
        expected = 'error:'
        self.assertEqual(actual[0:6], expected)