import pandas as pd
import cv2
import pytesseract
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# circular import from routes.py
import routes

if __name__ == "__main__":
    app.run()
