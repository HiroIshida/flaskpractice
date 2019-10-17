from flask import *
import json
import numpy as np

app = Flask(__name__)

class Othero:
    def __init__(self, N_):
        self.N = N_
        self.board = [[None for i in range(N_)] for j in range(N_)]

    def put(self, i, j, stone):
        self.board[i, j] = stone

    def encord_html(self):
        str_html = "<body>"
        str_html += "<table class=\"table\">"
        for i in range(self.N):
            str_html += "<tr>"
            for j in range(self.N):
                if self.board[i][j] is not None:
                    str_html += ("<td>" + self.board[i][j] + "</td>")
                else:
                    str_html += ("<td>" + "</td>")
            str_html += "</tr>"
        str_html += "</table>"
        str_html += "</body>"
        return str_html

global str_header 
f = open('index.html', 'r')
str_header = f.read()
f.close()

global ot
ot = Othero(10)

@app.route("/", methods = ["GET", "POST"])
def main():
    global ot
    global str_header
    str_body = ot.encord_html()
    print str_body
    str_html = "<html>" + str_header + str_body + "</html>"
    return str_html


if __name__ == "__main__":  
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)


