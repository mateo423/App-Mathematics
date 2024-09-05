from flask import Flask, render_template,request
from src.Maths.mathematics import summation, subtraction, multiplication

app = Flask(__name__,template_folder='src/templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = request.form.get('num1')
    num2 = request.form.get('num2')
    operation = request.form.get('operation')

    if not num1 or not num2:
        return render_template('index.html', result='Error: Falta el parámetro num1 o num2')

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return render_template('index.html', result='Error: No se puede convertir num1 o num2 a float')

    if operation == 'add':
        result = str(summation(num1, num2))
    elif operation == 'sub':
        result = str(subtraction(num1, num2))
    elif operation == 'mult':
        result = str(multiplication(num1, num2))
    else:
        return render_template('index.html', result='Error: Operación no válida')

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
