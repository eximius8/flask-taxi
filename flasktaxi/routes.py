from flasktaxi import app


@app.route("/")
@app.route("/home")
def client():
    return "asdsa"