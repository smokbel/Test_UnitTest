import requests 
import unittest
import os, json, sys, time 
from modules.test_case import TestUnit

## Example test cases for the inspirehep.net api. See more information here: http://old.inspirehep.net/info/hep/api ##

class ApiTest(TestUnit):

    @classmethod 
    def setUpClass(cls):
        super(ApiTest, cls).setUpClass()
        #print('Set Up Class')
        pass

    @classmethod
    def tearDownClass(cls):
        #print('Tear Down Class')
        super(ApiTest, cls).tearDownClass()
        pass 

    def test_001_get(self):
        ## Author 'Laflamme' 50 most cited papers. ##
        response = requests.get("https://inspirehep.net/api/literature?sort=mostcited&size=50&q=a%20R.Laflamme.1")
        self.assertEqual(200, response.status_code)

    def test_002_exceed_limit(self):
        ## The maximum most cited size is 1000. Anything over 1000 should return a 400 error. ##
        response = requests.get("https://inspirehep.net/api/literature?sort=mostcited&size=1005&q=a%20R.Laflamme.1")
        self.assertEqual(400, response.status_code)
        expected_message = "Maximum search page size of `1000` results exceeded."
        actual_message = response_body(response)["message"]
        self.assertEqual(expected_message, actual_message)

    def test_003_fail_on_purpose(self):
        ## I made this test fail on purpose, so you can view the log output of a failed test: 
        ## in log/test_003_fail_on_purpose. ## 
        response = requests.get("https://inspirehep.net/api/literature?sort=mostcited&size=1005&q=a%20R.Laflamme.1")
        response = response_body(response)
        self.assertIn("Not in message", response["message"])

    def test004_upcoming_seminars(self): 
        ## Total number of seminars is 29. Display 5 on each page. ##
        response = requests.get("https://inspirehep.net/api/seminars?size=5&page=1&start_date=upcoming")
        response = response_body(response)
        expected_response = 5
        actual_response = len(response["hits"]["hits"])
        self.assertEqual(expected_response, actual_response)

    def test005_no_seminars(self): 
        ## There are no upcoming seminars 25 pages down. Expect empty results. ##
        response = requests.get("https://inspirehep.net/api/seminars?size=5&page=25&start_date=upcoming")
        response = response_body(response)
        expected_response = 0
        actual_response = len(response["hits"]["hits"])
        self.assertEqual(expected_response, actual_response)
    
    def test_006_invalid_request(self):
        ## Invalid request ##
        response = requests.get("https://inspirehep.net/api/seminars?size=5&page=25&start_date=today")
        self.assertEqual(400, response.status_code)
        expected_message = "Validation error."
        actual_message = response_body(response)["message"]
        self.assertEqual(expected_message, actual_message)
    
## Helper function ##
def response_body(response):
    return response.json()
        
if __name__ == "__main__":
    unittest.main()
