from flask import *
import json

app = Flask(__name__)

class Manager:
    def __init__(self):
        self.data_name = []
        self.data_age = []

    def store(self, name, age):
        self.data_name.append(name)
        self.data_age.append(age)
        self._dump()

    def _dump(self):
        d = {"name": self.data_name, "age": self.data_age}
        f = open("tmp.json", 'w')
        json.dump(d, f, indent=4)
        f.close()

m = Manager()

@app.route("/", methods = ["GET", "POST"])
def main():
    message = "enter your name here:"
    return render_template('index.html', message = message)

@app.route("/fuck", methods = ["GET", "POST"])
def fuck():
    name = request.form["name"]
    age = request.form["age"]
    global m
    m.store(name, age)
    message = "name: " + name + " age: " + age + "\n"
    message += "enter your name here:"
    if request.method == "POST":
        return render_template('index.html', message = message)

if __name__ == "__main__":  
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)


