import tkinter as tk
from tkinter import messagebox
import joblib

def square_to_gaj():
    try:
        square_feet = float(sqft_entry.get())
        gaj = square_feet * 9
        label_result.config(text="{} Square feet is equal to {} gaj".format(square_feet, gaj))
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

def predict():
    try:
        # Load the saved model
        model = joblib.load('linear_regression_model_real_estate.pkl')

        # Get user input values from Entry widgets
        input_values = [float(entry_x.get()) for entry_x in entry_x_list]

        # Use the model to make a prediction
        predicted_output = model.predict([input_values])

        # Display the predicted output
        predicted_label.config(text=f'Predicted Output: {predicted_output[0]}')
    except Exception as e:
        predicted_label.config(text=f'Error: {str(e)}')

root = tk.Tk()
root.geometry("500x500")
root.configure(bg='#333333')
root.title("Linear Regression Predictor")

# Square to Gaj Conversion
sqft_label = tk.Label(root, text="Square Feet:")
sqft_entry = tk.Entry(root)
convert_button = tk.Button(root, text="Convert", command=square_to_gaj)
label_result = tk.Label(root, text=" ")

sqft_label.grid(row=0, column=0, padx=10, pady=5)
sqft_entry.grid(row=0, column=1, padx=10, pady=5)
convert_button.grid(row=0, column=2, padx=10, pady=5)
label_result.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

# Prediction
input_labels = ["X1:", "X2:", "X3:", "X4:", "X5:", "X6:"]
entry_x_list = []

for i, label_text in enumerate(input_labels):
    label = tk.Label(root, text=label_text)
    entry = tk.Entry(root)
    entry_x_list.append(entry)

    label.grid(row=i + 2, column=0, padx=10, pady=5)
    entry.grid(row=i + 2, column=1, padx=10, pady=5)

predict_button = tk.Button(root, text="Predict", command=predict)
predicted_label = tk.Label(root, text="Predicted Output: ")

predict_button.grid(row=len(input_labels) + 2, column=0, columnspan=2, padx=10, pady=5)
predicted_label.grid(row=len(input_labels) + 2, column=2, padx=10, pady=5)

root.mainloop()
