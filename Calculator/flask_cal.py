from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form.get('expression')
    try:
        result = str(eval(expression))
    except:
        result = "Error"
    return result

if __name__ == '__main__':
    app.run(debug=True)