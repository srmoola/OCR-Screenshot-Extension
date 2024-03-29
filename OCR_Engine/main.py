from flask import Flask
from flask_cors import CORS
from flask import request, jsonify
from flask_cors import cross_origin
import pytesseract

from base64_img import base64_to_img
from imageprocess import return_processed_image

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def MainLink():
    return "Server is Running!"


@app.route("/get-text", methods=["POST"])
@cross_origin()
def GetTextLink():
    if request.method == "POST":
        try:
            json_data = request.get_json()

            if "text_data" in json_data:
                text_data = json_data["text_data"]
                img = base64_to_img(text_data)
                get_text = pytesseract.image_to_string(img)
                return jsonify({"result": get_text})
            else:
                return jsonify({"error": "Missing 'text_data' key in JSON data"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    return "Invalid request method"


if __name__ == "__main__":
    app.run()
