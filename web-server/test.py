from flask import Flask, request
import json
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    maybe_json = request.get_json(silent=True, cache=False, force=True)
    if maybe_json:
        thejson = json.dumps(maybe_json)
    else:
        thejson = "no json"
    print(thejson)
    return "good job"

if __name__ == '__main__':
    print("*"*20)
    #app.run(port=5000, debug=True)
    app.run()