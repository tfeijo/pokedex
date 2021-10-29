from flask import Flask
import os

template_dir = os.path.abspath('src/view')

app = Flask(__name__, template_folder=template_dir)

from src.routes import *

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='3001')
