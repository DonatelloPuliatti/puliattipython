from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calcolatrice():
    risultato_somma = None
    risultato_moltiplicazione = None

    if request.method == "POST":
        # Gestione della somma
        if "somma" in request.form:
            try:
                numero1 = float(request.form["numero1_somma"])
                numero2 = float(request.form["numero2_somma"])
                risultato_somma = numero1 + numero2
                if risultato_somma == int(risultato_somma):
                    risultato_somma = int(risultato_somma)
            except ValueError:
                risultato_somma = "Errore: inserisci solo numeri!"

        # Gestione della moltiplicazione
        elif "moltiplicazione" in request.form:
            try:
                numero1 = float(request.form["numero1_moltiplicazione"])
                numero2 = float(request.form["numero2_moltiplicazione"])
                risultato_moltiplicazione = numero1 * numero2
                if risultato_moltiplicazione == int(risultato_moltiplicazione):
                    risultato_moltiplicazione = int(risultato_moltiplicazione)
            except ValueError:
                risultato_moltiplicazione = "Errore: inserisci solo numeri!"

    return render_template("calcolatrice.html",
                           risultato_somma=risultato_somma,
                           risultato_moltiplicazione=risultato_moltiplicazione)

if __name__ == "__main__":
    app.run(debug=True)