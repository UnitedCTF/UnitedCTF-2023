from flask import Flask, request, render_template, send_from_directory
from timeout_decorator import timeout
import os

app = Flask(__name__)

@timeout(2)
@app.route("/", methods=["GET"])
def root():
    q = request.args.get("q")
    if q is None or not q:
        return render_template("index.html")
    result = eval(q)
    
    return render_template("index.html", result=result)

@app.route('/static/<path:filename>')
def serve_static(filename):
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir, 'static'), filename)

if __name__ == "__main__":
    app.run()
