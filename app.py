from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/somma", methods=["GET", "POST"])
def somma():
    risultato_somma = None
    if request.method == "POST":
        try:
            numero1 = float(request.form["numero1"])
            numero2 = float(request.form["numero2"])
            risultato_somma = numero1 + numero2
            if risultato_somma == int(risultato_somma):
                risultato_somma = int(risultato_somma)
        except ValueError:
            risultato_somma = "Errore: inserisci solo numeri!"
    return render_template("somma.html", risultato=risultato_somma)

@app.route("/moltiplicazione", methods=["GET", "POST"])
def moltiplicazione():
    risultato_moltiplicazione = None
    if request.method == "POST":
        try:
            numero1 = float(request.form["numero1"])
            numero2 = float(request.form["numero2"])
            risultato_moltiplicazione = numero1 * numero2
            if risultato_moltiplicazione == int(risultato_moltiplicazione):
                risultato_moltiplicazione = int(risultato_moltiplicazione)
        except ValueError:
            risultato_moltiplicazione = "Errore: inserisci solo numeri!"
    return render_template("moltiplicazione.html", risultato=risultato_moltiplicazione)

if __name__ == "__main__":
    app.run(debug=True)
