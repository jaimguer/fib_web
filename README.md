
# Fib_Web
Provides a web service to calculate the first n Fibonacci numbers, using Python and Flask.

# Prerequisites
Ensure your system has at least Python 2.7 installed.  This was developed on a machine running 2.7.10.  Assuming you have pip installed,
```pip install -r requirements.txt```
will install Flask 0.12.2.  If you don't want your currently installed Python packages touched, consider setting up a virtualenv.

# Running and Using
From the directory containing fib.py, run
```python fib.py &```.
This will start the service on your local machine, running on port 5000 in the background.  To hit the endpoint, run
```curl -i localhost:5000/fib/5```

This will return
```
$ curl -i localhost:5000/fib/5
127.0.0.1 - - [21/Dec/2017 21:54:07] "GET /fib/5 HTTP/1.1" 200 -
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 60
Server: Werkzeug/0.13 Python/2.7.10
Date: Fri, 22 Dec 2017 05:54:07 GMT

{
  "result": [
    0,
    1,
    1,
    2,
    3
  ]
}
```
Remember, the process is running in your background, so make sure to bring it foward and kill it when you're finished.

# Tests
To run the tests, run
```
python fib_tests.py
```

Note that fib_test.py must be in the same directory as fib.py
