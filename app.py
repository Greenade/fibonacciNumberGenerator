import math
from flask import Flask, request
from flask import render_template
import numpy as np

app = Flask(__name__)

sqrtFive = np.sqrt(5) 
alpha = (1 + sqrtFive) / 2
beta = (1 - sqrtFive) / 2

# main page
@app.route("/")
def hello_world():
    return render_template('hello.html')

@app.route("/button-clicked", methods=['POST'])
def button_clicked():
    n = request.form['n']
    result = fib(n)
    return render_template('hello.html', result=result, n=n) 

def fib(n: int):
    intn = int(n)
    f = ((alpha ** intn) - (beta ** intn)) // (sqrtFive)
    if math.isinf(f) or math.isnan(f):
        return "too big to display"
    else:
        return int(f)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)