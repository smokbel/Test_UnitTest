## Test_UnitTest

### Overview 

This is a basic testing framework, used to demonstrate testing with Pythons unittest. 

### Install requirements 

After cloning the repository, please install all requirements by running:

```
pip install -r requirements.txt
```

### Run a test 
There are 6 different tests in the tests/api_test.py file. To run a specific test, follow the format: ./tests/api_test.py ApiTest.test_name

For example: 

```
 python ./tests/api_test.py ApiTest.test_006_invalid_request
 python ./tests/api_test.py ApiTest.test_002_exceed_limit
```
There is one purposely failing test, test_003_fail_on_purpose, just to showcase how the logger would log a failure. See the log folder after running this test for more details. 

### Run all tests 

Alternatively, you can just run all the tests at once using the following command:

```
python ./tests/api_test.py 
```
