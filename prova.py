from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/dog', methods=['GET'])
def get_dog():
    # Dati fittizi di un cane
    dog = {
        "nome": "Good",
        "cognome": "Boy",
        "indirizzo": "Via Roma 1, Prato, Italia",
        "numero_di_telefono": "+39 055 1234567",
    }
    return jsonify(dog)

if __name__ == '__main__':
    app.run(debug=True)
