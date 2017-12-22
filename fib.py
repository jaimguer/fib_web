from flask import Flask, jsonify, abort, make_response

app = Flask(__name__)

# Fibonacci sequence calculation
# Does not use recursive solution to prevent stack overflow
def fibCalc(n):
  listOfFibs = []
  if n == 1:
    listOfFibs = [0]
  elif n == 2:
    listOfFibs = [0,1]
  else:
    listOfFibs = [0, 1]
    first      = 0
    second     = 1
    for _ in xrange(2, n):
      nextNum = first + second
      first   = second
      second  = nextNum
      listOfFibs.append(nextNum)
  return listOfFibs

# Custom abort message for integers < 1 and non-integer values
def abort_message():
  abort(make_response(jsonify(result="Please provide an integer greater than 0"), 400))

# Exposed endpoint to users
@app.route('/fib/<n>')
def fib(n):
  try:
    # input is a string, cast to integer
    n = int(n) 
    if n < 1:
      abort_message()
    else:
      return jsonify({'result': fibCalc(n)})
  # cast to integer was unsuccessful
  except ValueError:
      abort_message()

if __name__ == "__main__":
  app.run()

