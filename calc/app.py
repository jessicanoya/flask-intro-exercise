# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


# The get() method in the context of request.args is used to retrieve the value
# of a query parameter from the URL of an HTTP request
@app.route('/add')
def do_add():
    """Add a and b parameters."""
    # print(request.args)
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a, b)

    return str(result)


@app.route('/sub')
def do_sub():
    """Subtract b from a."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a, b)

    return str(result)


@app.route('/mult')
def do_mult():
    """Multiply a and b."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a, b)

    return str(result)


@app.route('/div')
def do_div():
    """Divide a by b."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a, b)

    return str(result)


calcs = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}


@app.route('/math/<calc>')
def all_calc(calc):
    """Do calculations on a and b."""

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = calcs[calc](a, b)

    return str(result)
