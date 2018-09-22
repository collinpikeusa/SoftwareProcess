'''
Created on Sep 22, 2018

@author: Collin Pike
'''
import unittest
import RCube.dispatch as RCube


class CreateSideTest(unittest.TestCase):


    def test100_010_CreateSide(self):
        expectedResult = 'green'
        actualResult = RCube.createSide('green')
        for elementIndex in range(0,9):
            self.assertEqual(expectedResult, actualResult[elementIndex])
