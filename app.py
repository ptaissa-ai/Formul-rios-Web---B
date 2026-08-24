from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime, timezone
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get(
    "SECRET_KEY",
    "semana06-taissapieri"
)

@app.route("/", methods=["GET", "POST"])
def index():

    name = session.get("name", "Taissa")
    surname = session.get("surname", "Pieri")
    institution = session.get("institution", "IFSP")
    discipline = session.get("discipline", "DSWA5")

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        surname = request.form.get("surname", "").strip()
        institution = request.form.get("institution", "").strip()
        discipline_value = request.form.get("discipline", "dswa5")

        discipline_map = {
            "dswa5": "DSWA5",
            "dwba4": "DWBA4",
            "GPSA5": "Gestão de projetos"
        }

        discipline = discipline_map.get(
            discipline_value,
            discipline_value
        )

        session["name"] = name
        session["surname"] = surname
        session["institution"] = institution
        session["discipline"] = discipline

        return redirect(url_for("index"))

    ip = request.headers.get(
        "X-Forwarded-For",
        request.remote_addr
    )

    if ip and "," in ip:
        ip = ip.split(",")[0].strip()

    host = request.host
    timestamp = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    return render_template(
        "index.html",
        name=name,
        surname=surname,
        institution=institution,
        discipline=discipline,
        ip=ip,
        host=host,
        timestamp=timestamp
    )


@app.route("/login", methods=["GET", "POST"])
def login():

    timestamp = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip()
        senha = request.form.get("senha", "")

        session["usuario_login"] = usuario

        return redirect(url_for("login_response"))

    return render_template(
        "login.html",
        timestamp=timestamp
    )


@app.route("/loginResponse")
def login_response():

    usuario = session.get("usuario_login", "")

    timestamp = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    return render_template(
        "login_response.html",
        usuario=usuario,
        timestamp=timestamp
    )


if __name__ == "__main__":
    app.run(debug=True)
