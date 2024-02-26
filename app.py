from flask import Flask, render_template, request, jsonify
from datetime import datetim

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
    lastping = datetime.now().strftime("%H:%M:%S le %d-%m-%Y ")
    return jsonify({'variable': variable,'lastping':lastping})

if __name__ == '__main__':
    app.run(debug=True)
