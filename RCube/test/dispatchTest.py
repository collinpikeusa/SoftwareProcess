import unittest
import httplib
import json

class DispatchTest(unittest.TestCase):
        
    def setUp(self):
        self.key = "status"
        self.errorValue = "error:"
        self.operation ="op"
        self.scramble ="create"

    @classmethod
    def setUpClass(cls):
        cls.ERROR = "error:"
        cls.DEFAULT_SIZE = 3
        cls.MICROSERVICE_PATH = "/rcube?"
        cls.MICROSERVICE_URL="127.0.0.1"
        cls.MICROSERVICE_PORT = 5000
#         cls.MICFROSERVICE_URL="umphrda-rcube.mybluemix.net"
#         cls.MICROSERVICE_PORT = 80
        
    def httpGetAndResponse(self, queryString):
        '''Make HTTP request to URL:PORT for /rcube?querystring; result is a JSON string'''
        try:
            theConnection = httplib.HTTPConnection(self.MICROSERVICE_URL, self.MICROSERVICE_PORT)
            theConnection.request("GET", self.MICROSERVICE_PATH + queryString)
            theStringResponse = theConnection.getresponse().read()
            return theStringResponse 
        except Exception as e:
            theStringResponse = "{'diagnostic': 'error: " + str(e) + "'}"
            return theStringResponse
        
    def string2dict(self, httpResponse):
        '''Convert JSON string to dictionary'''
        result = {}
        try:
            jsonString = httpResponse.replace("'", "\"")
            unicodeDictionary = json.loads(jsonString)
            for element in unicodeDictionary:
                if(isinstance(unicodeDictionary[element],unicode)):
                    result[str(element)] = str(unicodeDictionary[element])
                else:
                    result[str(element)] = unicodeDictionary[element]
        except Exception as e:
            result['diagnostic'] = str(e)
        return result
        
#Acceptance Tests
#
# 100 dispatch - basic functionality
# Desired level of confidence: boundary value analysis
# Analysis 
# inputs:     http:// ...myURL... /httpGetAndResponse?parm
#            parm is a string consisting of key-value pairs
#            At a minimum, parm must contain one key of "op"
#
# outputs:    A JSON string containing, at a minimum, a key of "status"
#
# Happy path 
#      input:   parm having at least one element with a key of "op"        
#      output:  JSON string containing a key of "status" 
#
# Sad path 
#      input:   no string       
#      output:  dictionary consisting of an element with a key of "status" and value of "error: missing op"
#
#      input:   valid parm string with at least one key-value pair, no key of "op"
#      output:  dictionary consisting of an element with a key of "status" and value of "error: missing op"
#
#
#
# Note:  These tests require an active web service
#
#
# Happy path
    def test100_010_ShouldReturnSuccessKey(self):
        queryString="op=create"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)

    def test100_020_ShouldReturnSuccessKey(self):
        queryString="op=check&op=create"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
    
# Sad path
    def test100_900_ShouldReturnErrorOnEmptyParm(self):
        queryString=""
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:',resultDict['status'][0:6])
    
    def test100_910_ShouldReturnErrorOnMissingOp(self):
        queryString="f=red"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:',resultDict['status'][0:6])
    
    def test100_920_ShouldReturnErrorOnUnknownOp(self):
        queryString="op=cre"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:',resultDict['status'][0:6])

#         
#Acceptance Tests
#
# 200 dispatch -- op=create
# Desired level of confidence: boundary value analysis
# Analysis 
# inputs:    http:// ...myURL... /rcube?op=create<options>
#            where <options> can be zero or one of:
#                    "f"    Specifies the color of the front side of the cube.  It is a string of length .GT. 0.  Optional.  Defaults to "green" if missing.  Arrives unvalidated.        
#                    "r"    Specifies the color of the right side of the cube.  It is a string of length .GT. 0.  Optional.  Defaults to "yellow" if missing.  Arrives unvalidated.        
#                    "b"    Specifies the color of the back side of the cube.  It is a string of length .GT. 0.  Optional.  Defaults to "blue" if missing.  Arrives unvalidated.        
#                    "l"    Specifies the color of the left side of the cube.  It is a string of length .GT. 0.  Optional.  Defaults to "white" if missing.  Arrives unvalidated.        
#                    "t"    Specifies the color of the top side of the cube.  It is a string of length .GT. 0.  Optional.  Defaults to "red" if missing.  Arrives unvalidated.        
#                    "u"    Specifies the color of the under side of the cube.  It is a string of length .GT. 0.  Optional.  Defaults to "orange" if missing.  Arrives unvalidated.        
#
# outputs:    A JSON string containing, at a minimum, a key of "status"
#
# Happy path 
#      input:   zero options
#               http:// ... myURL ... /rcube?op=create
#      output:  default model cube, which is JSON string: 
#                {'status': 'created', 'cube': [
#                  'green',  'green', 'green', 
#                  'green', 'green', 'green',
#                  'green', 'green', 'green',
#                  'yellow', 'yellow', 'yellow', 
#                  'yellow', 'yellow', 'yellow',
#                  'yellow', 'yellow', 'yellow',  
#                  'blue', 'blue', 'blue',
#                  'blue', 'blue', 'blue', 
#                  'blue', 'blue', 'blue', 
#                  'white', 'white', 'white', 
#                  'white', 'white', 'white',
#                  'white', 'white', 'white',
#                  'red', 'red', 'red',
#                  'red', 'red', 'red', 
#                  'red', 'red', 'red',
#                  'orange', 'orange', 'orange',
#                  'orange', 'orange', 'orange', 
#                  'orange', 'orange', 'orange']}        

# Happy path
    def test200_010_ShouldCreateDefaultCubeStatus(self):
        queryString="op=create"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('created', resultDict['status'][0:7])
     
    
    def test200_020ShouldCreateDefaultCubeKey(self):
        queryString="op=create"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('cube', resultDict)

    def test200_030ShouldCreateDefaultCubeList(self):
        queryString="op=create"
        expectedFaces = ['green', 'yellow', 'blue', 'white', 'red', 'orange']
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)     
        actualResult = resultDict['cube']   
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0,9):
                self.assertEqual(face, actualResult[elementIndex])
                elementIndex += 1
    
    def test200_040_ShouldCreateMultipleFaceCubeWithOneFaceOnInputKey(self):
        queryString="op=create&f=f"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('cube', resultDict)


    def test200_050_ShouldCreateMultipleFaceCubeWithOneFaceOnInputStatus(self):
        queryString="op=create&f=f"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('created', resultDict['status'][0:7])
        
    def test200_060_ShouldCreateMultipleFaceCubeWithOneFaceOnInput(self):
        queryString="op=create&f=f"
        expectedFaces = ['f', 'yellow', 'blue', 'white', 'red', 'orange']
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)     
        actualResult = resultDict['cube'] 
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0,9):
                self.assertEqual(face, actualResult[elementIndex])
                elementIndex += 1
    
    def test200_070_ShouldCreateMultipleFaceCubeWithTwoFacesOnInputKey(self):
        queryString="op=create&f=f&r=2"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('cube', resultDict)

    def test200_080_ShouldCreateMultipleFaceCubeWithTwoFacesOnInputStatus(self):
        queryString="op=create&f=f&r=2"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('created', resultDict['status'][0:7])   
    
    def test200_090_ShouldCreateMultipleFaceCubeWithTwoFacesOnInput(self):
        queryString="op=create&f=f&r=2"
        expectedFaces = ['f', '2', 'blue', 'white', 'red', 'orange']
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)     
        actualResult = resultDict['cube'] 
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0,9):
                self.assertEqual(face, actualResult[elementIndex])
                elementIndex += 1
    
    def test200_100_ShouldCreateMultipleFaceCubeWithThreeFacesOnInputKey(self):
        queryString="op=create&b=b&f=f&r=2"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('cube', resultDict)
        
    def test200_110_ShouldCreateMultipleFaceCubeWithThreeFacesOnInputStatus(self):
        queryString="op=create&b=b&f=f&r=2"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('created', resultDict['status'][0:7])   
           
    def test200_120_ShouldCreateMultipleFaceCubeWithThreeFacesOnInput(self):
        queryString="op=create&b=b&f=f&r=2"
        expectedFaces = ['f', '2', 'b', 'white', 'red', 'orange']
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)     
        actualResult = resultDict['cube'] 
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0,9):
                self.assertEqual(face, actualResult[elementIndex])
                elementIndex += 1
    
    def test200_130_ShouldCreateMultipleFaceCubeWithFourFacesOnInputKey(self):
        queryString="op=create&b=b&f=f&l=4&r=2"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('cube', resultDict)          
    
    def test200_140_ShouldCreateMultipleFaceCubeWithFourFacesOnInputStatus(self):
        queryString="op=create&b=b&f=f&l=4&r=2"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('created', resultDict['status'][0:7])   
                     
    def test200_150_ShouldCreateMultipleFaceCubeWithFourFacesOnInput(self):
        queryString="op=create&b=b&f=f&l=4&r=2"
        expectedFaces = ['f', '2', 'b', '4', 'red', 'orange']
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)     
        actualResult = resultDict['cube'] 
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0,9):
                self.assertEqual(face, actualResult[elementIndex])
                elementIndex += 1
    
    def test200_160_ShouldCreateMultipleFaceCubeWithFiveFacesOnInputKey(self):
        queryString="op=create&t=t&b=b&f=f&l=4&r=2"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('cube', resultDict) 
        
    def test200_170_ShouldCreateMultipleFaceCubeWithFiveFacesOnInputStatus(self):
        queryString="op=create&t=t&b=b&f=f&l=4&r=2"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('created', resultDict['status'][0:7])   
        
    def test200_180_ShouldCreateMultipleFaceCubeWithFourFacesOnInput(self):
        queryString="op=create&t=t&b=b&f=f&l=4&r=2"
        expectedFaces = ['f', '2', 'b', '4', 't', 'orange']
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)     
        actualResult = resultDict['cube'] 
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0,9):
                self.assertEqual(face, actualResult[elementIndex])
                elementIndex += 1
    
    def test200_190_ShouldCreateMultipleFaceCubeWithSixFacesOnInputKey(self):
        queryString="op=create&u=1&t=t&b=b&f=f&l=4&r=2"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('cube', resultDict) 
    
    def test200_200_ShouldCreateMultipleFaceCubeWithSixFacesOnInputKey(self):
        queryString="op=create&u=1&t=t&b=b&f=f&l=4&r=2"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('created', resultDict['status'][0:7])   
    
    def test200_210_ShouldCreateMultipleFaceCubeWithSixFacesOnInput(self):
        queryString="op=create&u=1&t=t&b=b&f=f&l=45&r=200"
        expectedFaces = ['f', '200', 'b', '45', 't', '1']
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)     
        actualResult = resultDict['cube'] 
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0,9):
                self.assertEqual(face, actualResult[elementIndex])
                elementIndex += 1
                
    def test200_220_ShouldCreateMultipleFaceCubeWithSixFacesOnInput(self):
        queryString="op=create&u=u&t=t&b=b&f=f&l=l&r=r"
        expectedFaces = ['f', 'r', 'b', 'l', 't', 'u']
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)     
        actualResult = resultDict['cube'] 
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0,9):
                self.assertEqual(face, actualResult[elementIndex])
                elementIndex += 1
                
    def test200_230_ShouldCreateMultipleFaceCubeWithInvalidFacesOnInput(self):
        queryString="op=create&u=u&t=t&b=b&f=f&l=l&right=r"
        expectedFaces = ['f', 'yellow', 'b', 'l', 't', 'u']
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)     
        actualResult = resultDict['cube'] 
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0,9):
                self.assertEqual(face, actualResult[elementIndex])
                elementIndex += 1
                
    def test200_240_ShouldCreateMultipleFaceCubeWithInvalidFacesOnInput(self):
        queryString="op=create&u=u&top=t&b=b&f=f&l=l&right=r"
        expectedFaces = ['f', 'yellow', 'b', 'l', 'red', 'u']
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)     
        actualResult = resultDict['cube'] 
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0,9):
                self.assertEqual(face, actualResult[elementIndex])
                elementIndex += 1
            
    def test200_250_ShouldCreateMultipleFaceCubeWithMulitpleFacesWithCaseSensitiveColors(self):
        queryString="op=create&u=red&t=Red&b=blue&f=Blue&l=white&r=White"
        expectedFaces = ['Blue', 'White', 'blue', 'white', 'Red', 'red']
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)     
        actualResult = resultDict['cube'] 
        elementIndex = 0
        for face in expectedFaces:
            for _ in range(0,9):
                self.assertEqual(face, actualResult[elementIndex])
                elementIndex += 1
# Sad path
    def test200_900_ShouldReturnErrorOnSameColorInInput(self):
        queryString="op=create&f=purple&l=purple"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:',resultDict['status'][0:6])
     
    def test200_910_ShouldReturnErrorOnSameOnOutput(self):
        queryString ="op=create&f=1&b=yellow"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:',resultDict['status'][0:6])
    
    def test200_920_ShouldReturnErrorOnMissingColor(self):
        queryString ="op=create&f=&r=r"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error:',resultDict['status'][0:6])

#Acceptance Tests
#
# 300 dispatch -- op=check
# Desired level of confidence: boundary value analysis
# Analysis 
# inputs:    http:// ...myURL... /rcube?op=check<options>
#            where <options> can be zero or one of:
#                    "f"    Specifies the color of the front side of the cube.  It is a string of length .GT. 0.  Optional.  Defaults to "green" if missing.  Arrives unvalidated.        
#                    "r"    Specifies the color of the right side of the cube.  It is a string of length .GT. 0.  Optional.  Defaults to "yellow" if missing.  Arrives unvalidated.        
#                    "b"    Specifies the color of the back side of the cube.  It is a string of length .GT. 0.  Optional.  Defaults to "blue" if missing.  Arrives unvalidated.        
#                    "l"    Specifies the color of the left side of the cube.  It is a string of length .GT. 0.  Optional.  Defaults to "white" if missing.  Arrives unvalidated.        
#                    "t"    Specifies the color of the top side of the cube.  It is a string of length .GT. 0.  Optional.  Defaults to "red" if missing.  Arrives unvalidated.        
#                    "u"    Specifies the color of the under side of the cube.  It is a string of length .GT. 0.  Optional.  Defaults to "orange" if missing.  Arrives unvalidated.        
#            and must contain:
#                    "cube" model of the Rubik's cube
# outputs:    A JSON string containing, at a minimum, a key of "status"
#
# Happy Path
# input: Finished cube supplied
#        http:// ...myURL... /rcube?op=check&f=f&r=r&b=b&l=l&t=t&u=u&
#        cube=f,f,f,f,f,f,f,f,f,
#             r,r,r,r,r,r,r,r,r,
#             b,b,b,b,b,b,b,b,b,
#             l,l,l,l,l,l,l,l,l,
#             t,t,t,t,t,t,t,t,t,
#             u,u,u,u,u,u,u,u,u
# output:
#
# Sad path 
#      input:   zero options
#               http:// ... myURL ... /rcube?op=check
#      output:  {'status': 'error: cube must be specified'}

# Happy Path
    def test300_010_ShouldReturnFull(self):
        queryString="op=check&f=f&r=r&b=b&l=l&t=t&u=u&"\
                    "cube=f,f,f,f,f,f,f,f,f,r,r,r,r,r,r,r,r,r,b,b,b,"\
                    "b,b,b,b,b,b,l,l,l,l,l,l,l,l,l,t,t,t,t,t,t,t,t,t,u"\
                    ",u,u,u,u,u,u,u,u"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('full', resultDict['status'])
    
    def test300_010_ShouldReturnCrosses(self):
        queryString="op=check&f=w&r=g&b=y&l=b&t=r&u=o&"\
                    "cube=r,w,r,w,w,w,r,w,r,w,g,w,g,g,"\
                    "g,w,g,w,o,y,o,y,y,y,o,y,o,y,b,y,b,b"\
                    ",b,y,b,y,g,r,g,r,r,r,g,r,g,b,o,b,o,o,o,b,o,b"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('crosses', resultDict['status'])
    
    def test300_010_ShouldReturnSpots(self):
        queryString="op=check&f=r&r=b&b=o&l=g&t=w&u=y&cube="\
                    "y,y,y,y,r,y,y,y,y,o,o,o,o,b,o,o,o,o,w,"\
                    "w,w,w,o,w,w,w,w,r,r,r,r,g,r,r,r,r,b,b,b,"\
                    "b,w,b,b,b,b,g,g,g,g,y,g,g,g,g"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('spots', resultDict['status'])

    def test300_010_ShouldReturnIllegal(self):
        queryString="op=check&f=f&r=r&b=b&l=l&t=t&u=u&cube="\
                    "f,f,f,f,f,b,f,f,f,r,r,r,r,r,r,r,r,r,f,"\
                    "b,b,b,b,b,b,b,b,l,l,l,l,l,l,l,l,l,t,t,"\
                    "t,t,t,t,t,t,t,u,u,u,u,u,u,u,u,u"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('illegal cube', resultDict['status'])

    def test300_010_ShouldReturnUnknown(self):
        queryString="op=check&f=o&r=b&b=r&l=g&t=y&u=w&cube="\
                    "y,y,b,b,o,g,o,b,w,r,b,b,r,b,w,b,w,r,o"\
                    ",g,g,o,r,g,g,b,b,y,y,o,y,g,o,o,o,g,r,w"\
                    ",w,r,y,r,g,o,y,w,y,r,g,w,r,y,w,w"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('unknown', resultDict['status'])

# Sad Path
    def test300_900_ShouldErrorOnNoCubeDefined(self):
        queryString="op=check"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error: cube must be specified', resultDict['status'])
    
    def test300_910_ShouldErrorOnIncorrectSize(self):
        queryString="op=check&f=2&r=o&b=g&l=r&t=b&u=y&cube=y,y,b,b,o,g,o,b,w,r"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('error: cube is not sized properly', resultDict['status'])
    