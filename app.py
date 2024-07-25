from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import numpy as np
app = Flask(__name__)
CORS(app) 

def model_output(data):
    with open('my_model.pkl', 'rb') as file:
      loaded_model = pickle.load(file)
      print(loaded_model)
      new_data = [np.array([data])]
      return loaded_model.predict(new_data)

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/api/stress', methods=['POST'])
def stress():
    print("in")
    print(request.json)
    data = request.json
    print(data)
    result = model_output(int(data['stressLevel']))
    print(result)
    print("haaaaaa noooooo")
    return jsonify({'result': result[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0')


#  const response = await fetch("http://127.0.0.1:5000/api/stress", {
#           method: "POST",
#           headers: {
#             "Content-Type": "application/json",
#           },
#           athulMindTitle.textContent = stressNumber.value;
#           body: JSON.stringify({ stressLevel: stressLevel }),
#         });

# iam getting error