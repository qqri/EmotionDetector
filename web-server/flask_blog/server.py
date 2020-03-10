import pickle
from flask import Flask, request, jsonify
import numpy as np
import json
app = Flask(__name__)


@app.route('/predict',methods=['GET','POST'])
def predict():
    data = request.get_json(silent=True, cache=False,force=True)
    # if data:
    #     thejson = json.dumps(data)
    if data:
        if request.method == 'POST':
            prediction = model.predict_classes( model.getSequences(data))
            # output = prediction[0]
            # return flask.jsonify(output)
            label = str(np.squeeze(prediction))
            return label

        elif request.method == 'GET':
            return "test!"

if __name__ == '__main__':
    model = pickle.load(open('./model/gru_model.pkl', 'rb'))
    print("*"*20)
    app.run()