from flask import Flask, render_template, request, jsonify

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
    global variable
    lastping = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({'variable': variable,'lastping':lastping})

if __name__ == '__main__':
    app.run(debug=True)
