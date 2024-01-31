from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
variable_a_modifier = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/modifier_variable', methods=['POST'])
def modifier_variable():
    global variable_a_modifier
    bouton_presse = request.form.get('bouton_presse')
    # Logique pour modifier la variable en fonction du bouton pressé
    variable_a_modifier = bouton_presse
    return jsonify({'success': True})

@app.route('/consulter_variable', methods=['GET'])
def consulter_variable():
    global variable_a_modifier
    # Logique pour consulter la variable
    return jsonify({'variable': variable_a_modifier})

if __name__ == '__main__':
    app.run(debug=True)
