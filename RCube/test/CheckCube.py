'''
Created on Oct 12, 2018

@author: Collin Pike
'''
import unittest
import RCube.dispatch as RCube

class CheckCubeTest(unittest.TestCase):

    def test_CheckCube(self):
        cube = 'f,f,f,f,f,f,f,f,f,r,r,r,r,r,r,r,r,r,b,b,b,'\
               'b,b,b,b,b,b,l,l,l,l,l,l,l,l,l,t,t,t,t,t,t,t,t,t,u'\
               ',u,u,u,u,u,u,u,u'
        cubeDefinition = {'op': 'check', 'f': 'f', 'r': 'r', 'b': 'b', 'l': 'l', 't': 't', 'u': 'u', 'cube': cube}
        actual = RCube.checkCube(cubeDefinition)
        expected = 'full'
        self.assertEqual(actual, expected)
        
    def test_CheckCubeSadPath(self):
        cube = 'f,f,f,f,f,f,f,f,f,r,r,r,r,r,r,r,r,r,b,b,b,'\
               'b,b,b,b,b,b,l,l,l,l,l,l,l,l,l,t,t,t,t,t,t,t,t,t,u'\
               ',u,u,u,u,u,u,u'
        cubeDefinition = {'op': 'check', 'f': 'f', 'r': 'r', 'b': 'b', 'l': 'l', 't': 't', 'u': 'u', 'cube': cube}
        actual = RCube.checkCube(cubeDefinition)
        expected = 'error:'
        self.assertEqual(actual[0:6], expected)
