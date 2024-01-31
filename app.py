from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
variable = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/modifier_variable', methods=['POST'])
def modifier_variable():
    global variable
    variable = request.form.get('bouton')
    return jsonify({'success': True})

@app.route('/consulter_variable', methods=['GET'])
def consulter_variable():
    global variable
    # Logique pour consulter la variable
    return jsonify({'variable': variable})

if __name__ == '__main__':
    app.run(debug=True)
