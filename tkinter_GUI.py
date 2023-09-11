import tkinter as tk
from tkinter import messagebox
import joblib

class SquareToGajConverter:
    def __init__(self, root):
        self.root = root
        root.title("Linear Regression Predictor")
        
        # Square to Gaj Conversion Section
        self.create_square_to_gaj_section()

        # Prediction Section
        self.create_prediction_section()

    def create_square_to_gaj_section(self):
        sqft_label = tk.Label(self.root, text="Square Feet:")
        self.sqft_entry = tk.Entry(self.root)
        convert_button = tk.Button(self.root, text="Convert", command=self.square_to_gaj)
        self.label_result = tk.Label(self.root, text=" ")

        sqft_label.pack()
        self.sqft_entry.pack()
        convert_button.pack()
        self.label_result.pack()

    def square_to_gaj(self):
        try:
            square_feet = float(self.sqft_entry.get())
            gaj = square_feet * 9
            self.label_result.config(text="{} Square feet is equal to {} gaj".format(square_feet, gaj))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

    def create_prediction_section(self):
        input_labels = ["X1:", "X2:", "X3:", "X4:", "X5:", "X6:"]
        self.entry_x_list = []

        for label_text in input_labels:
            label = tk.Label(self.root, text=label_text)
            entry = tk.Entry(self.root)
            self.entry_x_list.append(entry)
            label.pack()
            entry.pack()

        predict_button = tk.Button(self.root, text="Predict", command=self.predict)
        self.predicted_label = tk.Label(self.root, text="Predicted Output: ")

        predict_button.pack()
        self.predicted_label.pack()

    def predict(self):
        try:
            model = joblib.load('linear_regression_model_real_estate.pkl')
            input_values = [float(entry.get()) for entry in self.entry_x_list]
            predicted_output = model.predict([input_values])
            self.predicted_label.config(text=f'Predicted Output: {predicted_output[0]}')
        except Exception as e:
            self.predicted_label.config(text=f'Error: {str(e)}')

if __name__ == "__main__":
    root = tk.Tk()
    app = SquareToGajConverter(root)
    root.mainloop()
