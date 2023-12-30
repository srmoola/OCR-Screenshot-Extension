from __main__ import app
from base64_img import base64_to_img, show_image
from flask import request, jsonify
from flask_cors import cross_origin


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
                return jsonify({"result": f"Received text data: {text_data}"})
            else:
                return jsonify({"error": "Missing 'text_data' key in JSON data"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    return "Invalid request method"
