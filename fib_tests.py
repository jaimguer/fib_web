
import fib
import unittest
import flask
import json

class FibTestCase(unittest.TestCase):
  def setUp(self):
    self.app = fib.app.test_client()

  def dict_result(self, uri):
    result = self.app.get(uri)
    d = json.loads(result.data)
    return d['result']

  def dict_status(self, uri):
    result = self.app.get(uri)
    return result.status_code

  def test_string(self):
    assert self.dict_status('/fib/hello_world') == 400

  def test_negative(self):
    assert self.dict_status('/fib/-1') == 400

  def test_zero(self):
    assert self.dict_status('/fib/0') == 400

  def test_one(self):
    assert self.dict_result('/fib/1') == [0]

  def test_two(self):
    assert self.dict_result('/fib/2') == [0, 1]

  def test_five(self):
    assert self.dict_result('/fib/5') == [0, 1, 1, 2, 3]

if __name__ == '__main__':
    unittest.main()
