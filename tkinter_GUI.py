# Import necessary libraries
import tkinter as tk
from tkinter import messagebox
import joblib

# Function to convert square feet to gaj
#If someone does not understands square feet's 
#using this function they can understand gaj in square terms
def square_to_gaj():
    try:
        # Get the input value from the Entry widget
        square_feet = float(sqft_entry.get())
        
        # Calculate gaj (1 gaj = 9 square feet)
        gaj = square_feet * 9 
        
        # Display the result in the label
        label_result.config(text="{} Square feet is equal to {} gaj".format(square_feet, gaj))
    except ValueError:
        # Display an error message if the input is not a valid number
        messagebox.showerror("Error", "Please enter a valid number")

# Function to make a prediction using a saved machine learning model
def predict():
    try:
        # Load the saved machine learning model
        model = joblib.load('linear_regression_model_real_estate.pkl')

        # Get user input values from Entry widgets
        input_values = [float(entry_x.get()) for entry_x in entry_x_list]

        # Use the model to make a prediction
        predicted_output = model.predict([input_values])

        # Display the predicted output
        predicted_label.config(text=f'Predicted Output: {predicted_output[0]}')
    except Exception as e:
        # Display an error message if an exception occurs during prediction
        predicted_label.config(text=f'Error: {str(e)}')

# Create the main application window
root = tk.Tk()
root.title("Linear Regression Predictor")

# Square to Gaj Conversion Section
sqft_label = tk.Label(text="Square Feet:")
sqft_entry = tk.Entry()
convert_button = tk.Button(text="Convert", command=square_to_gaj)
label_result = tk.Label(text=" ")

sqft_label.pack()
sqft_entry.pack()
convert_button.pack()
label_result.pack()

# Prediction Section
input_labels = ["X1:", "X2:", "X3:", "X4:", "X5:", "X6:"]
entry_x_list = []

# Create Entry widgets for user input and labels for description
for label_text in input_labels:
    label = tk.Label(root, text=label_text)
    entry = tk.Entry(root)
    entry_x_list.append(entry)
    label.pack()
    entry.pack()

# Create a button to trigger prediction and a label to display the result
predict_button = tk.Button(root, text="Predict", command=predict)
predicted_label = tk.Label(root, text="Predicted Output: ")

predict_button.pack()
predicted_label.pack()

# Start the main application loop
root.mainloop()
