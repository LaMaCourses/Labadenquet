from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)
variable = None
lastping = None


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/modifier_variable', methods=['POST'])
def modifier_variable():
    global variable
    variable = request.form.get('bouton')
    return render_template('index.html')

@app.route('/consulter_variable', methods=['GET'])
def consulter_variable():
    global variable,lastping
    heure = (int(datetime.now().strftime("%H"))+1)%24
    lastping = str(heure)+datetime.now().strftime(":%M:%S le %d-%m-%Y ")
    return jsonify({'variable': variable})

@app.route('/consulter_variable_from_oueb', methods=['GET'])
def consulter_variable_from_oueb():
    global variable
    return jsonify({'variable': variable})


@app.route('/lastping', methods=['GET'])
def get_lastping():
    global lastping
    return jsonify({'lastping': lastping})

if __name__ == '__main__':
    app.run(debug=True)
