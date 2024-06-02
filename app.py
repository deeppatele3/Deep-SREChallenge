from flask import Flask, render_template
import socket

phyapplication = Flask(__name__)

host = socket.gethostname()

ver = "1.0.3"

@phyapplication.route('/')
def index():
    return render_template('hostname&version.html', hostname=host, version=ver)

if __name__ == '__main__':
    phyapplication.run(debug=True)
