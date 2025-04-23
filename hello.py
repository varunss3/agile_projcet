from flask import Flask

app = Flask(name)

@app.route('/')
def say_hello():
    return "Hello hi, Here!"

if name == "main":
    app.run(host="0.0.0.0", port=5000)
