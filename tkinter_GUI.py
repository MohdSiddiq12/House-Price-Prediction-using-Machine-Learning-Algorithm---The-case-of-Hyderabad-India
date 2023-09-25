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
root.geometry("1920x1080")
root.configure(bg='#333333')
root.title("Linear Regression Predictor")

# Square to Gaj Conversion
sqft_label = tk.Label(text="Square Feet:")
sqft_entry = tk.Entry()
convert_button = tk.Button(text="Convert", command=square_to_gaj)
label_result = tk.Label(text=" ")

sqft_label.pack()
sqft_entry.pack()
convert_button.pack()
label_result.pack()

# Prediction
input_labels = ["X4:", "X5:", "X6:", "X1:", "X2:", "X3:"]
entry_x_list = []

for label_text in input_labels:
    label = tk.Label(root, text=label_text)
    entry = tk.Entry(root)
    entry_x_list.append(entry)
    label.pack()
    entry.pack()

predict_button = tk.Button(root, text="Predict", command=predict)
predicted_label = tk.Label(root, text="Predicted Output: ")

predict_button.pack()
predicted_label.pack()

root.mainloop()
