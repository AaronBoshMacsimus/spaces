from flask import Flask, render_template, jsonify
from flask_cors import CORS
app = Flask(__name__, static_folder="./static/static", template_folder="./templates")
CORS(app)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/text/<command>", methods=["GET"])
def display_command(command):
    print(f"Received Command: {command}")
    return jsonify({"message": f"Command '{command}' received successfully!"})
@app.route("/<path:path>")
def static_proxy(path):
    return app.send_static_file(path)
if __name__ == "__main__":
    app.run(debug=True)

