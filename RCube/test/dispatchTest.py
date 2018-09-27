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
#    test 010
#      input:   parm having at least one element with a key of "op"        
#      output:  JSON string containing a key of "status"
#      
# Sad path 
#    test 910
#      input:   no string       
#      output:  dictionary consisting of an element with a key of "status" and value of "error: missing op"
#
#    test 920
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
    
# Acceptance Test
# 200 Dispatch -op=create
# Confidence Level: BVA
# Analysis
#      inputs:     http://url/rcube?op=create<options>
#                        where options can be zero or one of the following:
#                            f=<string>    String of length GT 0. Optional. Default to "green". Unvalidated
#                            r=<string>    String of length GT 0. Optional. Default to "yellow". Unvalidated        
#                            b=<string>    String of length GT 0. Optional. Default to "blue". Unvalidated        
#                            l=<string>    String of length GT 0. Optional. Default to "white". Unvalidated        
#                            t=<string>    String of length GT 0. Optional. Default to "red". Unvalidated        
#                            u=<string>    String of length GT 0. Optional. Default to "orange". Unvalidated   
#      outputs:     A JSON string containing, at a minimum, a key of "status"
#
# Happy path:
#    input:     zero options
#        http://url/rcube?op=create
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
#            'orange', 'orange', 'orange',
#            'orange', 'orange', 'orange']}  
#
#    input:     empty option value
#        http://url/rcube?op=create&f=
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
#            'orange', 'orange', 'orange',
#            'orange', 'orange', 'orange']} 
#
# Sad Path
#    test 910
#        input: http://url/rcube?op=create&f=red&u=red
#        output: {'status': 'error: at least two faces have the same color'}
#    test 920
#        input: http:// ... /rcube?op=create&f=f&r=r&b=b&l=l&t=1&u=0
#        output {'status': 'error: at least one face had a negative value'}
       

    def test200_010_ShouldCreateDefaultCubeStatus(self):
        queryString="op=create"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('created', resultDict['status'][0:7])
    
    def test200_020_ShouldCreateDefaultCubeKey(self):
        queryString="op=create"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('cube', resultDict)
    
    def test200_030_ShouldCreateDefaultCube(self):
        queryString="op=create&f="
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('status', resultDict)
        self.assertEquals('created', resultDict['status'][0:7])
        
    def test200_910_ShouldReturnErrorDuplicateColors(self):
        queryString="op=create&f=red&u=red"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('error', resultDict['status'][0:5])  
    
    def test200_920_ShouldReturnErrorDuplicateColorsOneGiven(self):
        queryString="op=create&f=yellow"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('error', resultDict['status'][0:5]) 
    
    def test200_930_ShouldReturnErrorDuplicateColorsOneGivenUpperCase(self):
        queryString="op=create&f=Yellow"
        resultString = self.httpGetAndResponse(queryString)
        resultDict = self.string2dict(resultString)
        self.assertIn('error', resultDict['status'][0:5])  
    