from flask import Flask, jsonify, abort, make_response

app = Flask(__name__)

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

def abort_message():
  abort(make_response(jsonify(result="Please provide an integer greater than 0"), 400))

@app.route('/fib/<n>')
def fib(n):
  try:
    n = int(n)
    if n < 1:
      abort_message()
    else:
      return jsonify({'result': fibCalc(n)})
  except ValueError:
      abort_message()

if __name__ == "__main__":
  app.run()

