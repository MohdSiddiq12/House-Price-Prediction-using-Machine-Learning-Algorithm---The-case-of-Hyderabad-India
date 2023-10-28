import tkinter as tk
from tkinter import messagebox
from joblib import load
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pickle

def preprocess_input(locality_encoder, input_data):
    # Convert locality to numerical using the encoder
    if 'locality' in input_data:
        input_data['locality'] = locality_encoder.transform([input_data['locality']])[0]
    
    # Convert type_bhk to numerical format
    if 'type_bhk' in input_data:
        input_data['type_bhk'] = int(input_data['type_bhk'])
    
    # Add other preprocessing steps if needed
    return input_data

def predict():
    try:
        # Load the saved model
        model = load('House_price_prediction.joblib')
        
        # Load the fitted label encoders
        with open('label_encoders.pkl', 'rb') as file:
            encoders = pickle.load(file)
            locality_encoder = encoders['locality']
            # Load other encoders if available
        
        # Get user input values from Entry widgets
        input_values = {
            'bathroom': float(entry_list[0].get()),
            'floor': float(entry_list[1].get()),
            'locality': entry_list[2].get(),
            'property_age': float(entry_list[3].get()),
            'property_size': float(entry_list[4].get()),
            'totalFloor': float(entry_list[5].get()),
            'type_bhk': entry_list[6].get()
        }

        # Preprocess the input data
        input_values = preprocess_input(locality_encoder, input_values)

        # Use the model to make a prediction
        predicted_output = model.predict(np.array(list(input_values.values())).reshape(1, -1))

        # Display the predicted output
        predicted_label.config(text=f'Predicted Output: {predicted_output[0]}')
    except Exception as e:
        predicted_label.config(text=f'Error: {str(e)}')

root = tk.Tk()
root.geometry("800x600")
root.title("Linear Regression Predictor")

# Labels and Entry widgets for features
input_labels = ["bathroom:", "floor:", "locality:", "property_age:", "property_size:", "totalFloor:", "type_bhk:"]
entry_list = []

for i, label_text in enumerate(input_labels):
    label = tk.Label(root, text=label_text)
    entry = tk.Entry(root, highlightthickness=1, width=20)
    entry_list.append(entry)

    label.grid(row=i, column=0, padx=10, pady=5)
    entry.grid(row=i, column=1, padx=10, pady=5)

# Predict button and label for the output
predict_button = tk.Button(root, text="Predict", command=predict)
predicted_label = tk.Label(root, text="Predicted Output: ")

predict_button.grid(row=len(input_labels), column=0, columnspan=2, padx=10, pady=5)
predicted_label.grid(row=len(input_labels), column=2, padx=10, pady=5)

root.mainloop()
