from flask import Flask, render_template, request, jsonify
from datetime import datetime
from pytz import timezone

app = Flask(__name__)


def readData():
    with open("./data.txt","r") as f:
        [variable,lastping,prod] = f.readline().strip().split("/")
    #print(f"'{variable}' et '{lastping}'")
    return variable,lastping,prod

def writeData(variable,lastping,prod):
    with open("./data.txt","w") as f:
        f.write(f"{variable}/{lastping}/{prod}")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/modifier_variable', methods=['POST'])
def modifier_variable():
    variable = request.form.get('bouton')
    _,lastping,prod = readData()
    writeData(variable,lastping,prod)
    return render_template('index.html')

@app.route('/consulter_variable', methods=['GET'])
def consulter_variable():
    prod = request.args.get('prod')
    now = datetime.now().astimezone(timezone('Europe/Paris'))
    lastping = now.strftime("%H:%M:%S le %d-%m-%Y ")
    variable,_,_ = readData()
    writeData(variable,lastping,prod)
    return jsonify({'variable': variable})

@app.route('/consulter_variable_from_oueb', methods=['GET'])
def consulter_variable_from_oueb():
    variable,_,_ = readData()
    return jsonify({'variable': variable})


@app.route('/lastping', methods=['GET'])
def get_lastping():
    _,lastping,prod = readData()
    return jsonify({'lastping': lastping,'prod':prod})

if __name__ == '__main__':
    app.run(debug=True)
