'''
Created on Oct 12,2018

@author: Collin Pike
'''
import unittest
import RCube.dispatch as RCube


class IsFullTest(unittest.TestCase):
    def test_cubeSizeCheck(self):
        cube = 'purple,purple,purple,'\
               'purple,purple,purple,'\
               'purple,purple,purple,'\
               'yellow,yellow,yellow,'\
               'yellow,yellow,yellow,'\
               'yellow,yellow,yellow,'\
               'blue,blue,blue,'\
               'blue,blue,blue,'\
               'blue,blue,blue,'\
               'white,white,white,'\
               'white,white,white,'\
               'white,white,white,'\
               'red,red,red,'\
               'red,red,red,'\
               'red,red,red,'\
               'orange,orange,orange,'\
               'orange,orange,orange,'\
               'orange,orange,orange'
        actual = RCube.isFull(cube.split(','))
        expected = True
        self.assertEquals(actual,expected)