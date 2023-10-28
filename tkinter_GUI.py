import tkinter as tk
from tkinter import messagebox
from joblib import load
import numpy as np

def predict():
    try:
        # Load the saved model
        model = load('House_price_prediction.joblib')

        # Get user input values from Entry widgets
        input_values = [float(entry.get()) for entry in entry_list]

        # Use the model to make a prediction
        predicted_output = model.predict(np.array(input_values).reshape(1, -1))

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
