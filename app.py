from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)


def readData():
    with open("./data.txt","r") as f:
        [variable,lastping] = f.readline().strip().split("/")
    print(f"'{variable}' et '{lastping}'")
    return variable,lastping

def writeData(variable,lastping):
    with open("./data.txt","w") as f:
        f.write(f"{variable}/{lastping}")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/modifier_variable', methods=['POST'])
def modifier_variable():
    variable = request.form.get('bouton')
    _,lastping = readData()
    writeData(variable,lastping)
    return render_template('index.html')

@app.route('/consulter_variable', methods=['GET'])
def consulter_variable():
    heure = (int(datetime.now().strftime("%H"))+1)%24
    lastping = str(heure)+datetime.now().strftime(":%M:%S le %d-%m-%Y ")
    variable,_ = readData()
    writeData(variable,lastping)
    return jsonify({'variable': variable})

@app.route('/consulter_variable_from_oueb', methods=['GET'])
def consulter_variable_from_oueb():
    variable,_ = readData()
    return jsonify({'variable': variable})


@app.route('/lastping', methods=['GET'])
def get_lastping():
    _,lastping = readData()
    return jsonify({'lastping': lastping})

if __name__ == '__main__':
    app.run(debug=True)
