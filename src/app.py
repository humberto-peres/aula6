from flask import Flask, render_template, request
from calculator import Calculator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    input_hour = request.form['inputHour']
    end_hour = request.form['endHour']
    interval = request.form['interval'] if request.form['interval'] else '00:00'

    calculator = Calculator()

    try:
        result = calculator.calculate_hours(input_hour, end_hour, interval)
    except ValueError as e:
        return f"Erro: {e}"

    return f"Horas trabalhadas: {result}"

if __name__ == '__main__':
    app.run(debug=True)
