from flask import *
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    name = request.args.get('name', '?')
    age = int(request.args.get('age', '?'))
    return render_template('home.html', name = name, age = age)
     
@app.route("/calc")
def calc():
    number1 = int(request.args.get('number'))
    number2 = int(request.args.get('numbers'))
    operator = request.args.get('operator')
    result = None
    if operator == "+":
        result = number1+number2
    elif operator == "-":
        result = number1-number2
    elif operator == "/":
        result = number1/number2
    elif operator == "*":
        result = number1/number2
    elif operator == "%":
        result = number1%number2
    elif operator == "//":
        result = number1//number2
    elif operator == "**":
        result = number1**number2
    
    return render_template('calc.html', result=result)
     

if __name__ == '__main__':
    app.run(debug=True)
    