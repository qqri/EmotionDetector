import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)
model = pickle.load(open('model/gru_model.pkl','rb'))


@app.route('/api',methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict_classes( model.getSequences(data))
    output = prediction[0]
    return jsonify(output)

if __name__ == '__main__':
    print("*"*20)
    predict()
    #app.run(port=5000, debug=True)
    app.run()