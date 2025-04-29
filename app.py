from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Collect all 30 fields (Time, V1-V28, Amount)
        features = []
        features.append(float(request.form['Time']))  # Time
        for i in range(1, 29):
            features.append(float(request.form[f'V{i}']))  # V1 to V28
        features.append(float(request.form['Amount']))  # Amount

        final_features = np.array([features])  # 2D array
        prediction = model.predict(final_features)
        output = "Fraud" if prediction[0] == 1 else "Valid"
        return render_template('index.html', prediction_text=f'Prediction: {output}')
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
