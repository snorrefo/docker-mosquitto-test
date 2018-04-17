from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():

    script = 'script'
    div = 'div'
    return render_template("index.html", script=script, div=div)


@app.route('/api/logger/pollingfreq/', methods=['POST', 'GET'])
def pol():

    if request.method == 'POST':

        return 'POST'

    else:

        return 'GET'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
