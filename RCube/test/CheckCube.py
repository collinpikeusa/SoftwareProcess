'''
Created on Oct 12, 2018

@author: Collin Pike
'''
import unittest
import RCube.dispatch as RCube

class CheckCubeTest(unittest.TestCase):

    def test_CheckFullCube(self):
        cube = 'f,f,f,f,f,f,f,f,f,r,r,r,r,r,r,r,r,r,b,b,b,'\
               'b,b,b,b,b,b,l,l,l,l,l,l,l,l,l,t,t,t,t,t,t,t,t,t,u'\
               ',u,u,u,u,u,u,u,u'
        cubeDefinition = {'op': 'check', 'f': 'f', 'r': 'r', 'b': 'b', 'l': 'l', 't': 't', 'u': 'u', 'cube': cube}
        actual = RCube.checkCube(cubeDefinition)
        expected = 'full'
        self.assertEqual(actual, expected)

    def test_CheckCrossesCube(self):
        cube = "r,w,r,w,w,w,r,w,r,w,g,w,g,g,"\
               "g,w,g,w,o,y,o,y,y,y,o,y,o,y,b,y,b,b"\
               ",b,y,b,y,g,r,g,r,r,r,g,r,g,b,o,b,o,o,o,b,o,b"
        cubeDefinition = {'op': 'check', 'f': 'w', 'r': 'g', 'b': 'y', 'l': 'b', 't': 'r', 'u': 'o', 'cube': cube}
        actual = RCube.checkCube(cubeDefinition)
        expected = 'crosses'
        self.assertEqual(actual, expected)
   
    def test_CheckCubeSadPath(self):
        cube = 'f,f,f,f,f,f,f,f,f,r,r,r,r,r,r,r,r,r,b,b,b,'\
               'b,b,b,b,b,b,l,l,l,l,l,l,l,l,l,t,t,t,t,t,t,t,t,t,u'\
               ',u,u,u,u,u,u,u'
        cubeDefinition = {'op': 'check', 'f': 'f', 'r': 'r', 'b': 'b', 'l': 'l', 't': 't', 'u': 'u', 'cube': cube}
        actual = RCube.checkCube(cubeDefinition)
        expected = 'error:'
        self.assertEqual(actual[0:6], expected)
