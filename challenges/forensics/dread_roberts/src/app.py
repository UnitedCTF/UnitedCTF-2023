from flask import Flask, render_template, request 
print("Importing flask_tor\n")
from flask_tor.flask_tor import run_with_tor


print("Starting flask app\n")
app = Flask(__name__)
print("Starting Tor network application\n")
tor = run_with_tor()

@app.route("/")
def hello():
    str = site = tor.onion_host.replace(".onion", "")
    print(request.host_url)
    if ".onion" in request.host_url:
        str = "FLAG-T25pb24tTGluay1BcmUtQXdlc29tZQo"
    return render_template('index.html',secret=str)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9802)
