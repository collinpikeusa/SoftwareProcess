'''
Created on Oct 12, 2018

@author: Collin Pike
'''
import unittest
import RCube.dispatch as RCube


class IsCrossesTest(unittest.TestCase):


    def test_CrossesCheck(self):
        cube = "r,w,r,w,w,w,r,w,r,w,g,w,g,g,"\
               "g,w,g,w,o,y,o,y,y,y,o,y,o,y,b,y,b,b"\
               ",b,y,b,y,g,r,g,r,r,r,g,r,g,b,o,b,o,o,o,b,o,b"
        actual = RCube.isCrosses(cube.split(','))
        expected = True
        self.assertEqual(actual, expected)
