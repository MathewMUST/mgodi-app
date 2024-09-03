# # # from flask import Flask

# # # app = Flask(__name__)

# # # @app.route('/')
# # # def home():
# # #     return "Hello, Flask!"

# # # if __name__ == "__main__":
# # #     app.run(debug=True)


# from flask import Flask, request, render_template
# import pickle
# import numpy as np
# from datetime import datetime

# app = Flask(__name__)

# # Load the model
# model = pickle.load(open('model.pkl', 'rb'))

# # Define the weather mapping
# weather_mapping = {
#     0: 'dizzle',
#     1: 'fog',
#     2: 'rain',
#     3: 'snow',
#     4: 'sun'
# }

# @app.route('/')
# def mgodi():
#     return render_template('mgodi.html', prediction=None)

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Convert the date input to a datetime object and then to a numeric value if needed
#         date_str = request.form['date']
#         date = datetime.strptime(date_str, "%Y-%m-%d").timestamp()

#         precipitation = float(request.form['precipitation'])
#         temp_max = float(request.form['temp_max'])
#         temp_min = float(request.form['temp_min'])
#         wind = float(request.form['wind'])

#         # Features array
#         input_features = [[date, precipitation, temp_max, temp_min, wind]]
#         prediction_numeric = model.predict(input_features)[0]

#         # Map the numeric prediction to the human-readable label
#         prediction = weather_mapping.get(prediction_numeric, "Unknown")

#         return render_template('mgodi.html', prediction=prediction)
#     except Exception as e:
#         return render_template('mgodi.html', prediction=f"Error: {e}")

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, request, render_template
import pickle
import numpy as np
from datetime import datetime

app = Flask(__name__)

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

# Define the weather mapping
weather_mapping = {
    0: 'drizzle',
    1: 'fog',
    2: 'rain',
    3: 'snow',
    4: 'sun'
}

@app.route('/')
def mgodi():
    return render_template('mgodi.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Convert the date input to a numeric value
        date_str = request.form['date']
        date = datetime.strptime(date_str, "%Y-%m-%d").toordinal()

        precipitation = float(request.form['precipitation'])
        temp_max = float(request.form['temp_max'])
        temp_min = float(request.form['temp_min'])
        wind = float(request.form['wind'])

        # Features array
        input_features = [[date, precipitation, temp_max, temp_min, wind]]

        # Debug: Print input features
        print(f"Input Features: {input_features}")

        prediction_numeric = model.predict(input_features)[0]

        # Debug: Print raw model prediction
        print(f"Raw Model Prediction: {prediction_numeric}")

        # Map the numeric prediction to the human-readable label
        prediction = weather_mapping.get(prediction_numeric, "Unknown")

        # Debug: Print mapped prediction
        print(f"Mapped Prediction: {prediction}")

        return render_template('mgodi.html', prediction=prediction)
    except Exception as e:
        return render_template('mgodi.html', prediction=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)
