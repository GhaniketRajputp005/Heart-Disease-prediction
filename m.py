import tkinter as tk
from tkinter import ttk,messagebox
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pickle
import warnings
warnings.filterwarnings('ignore')

def predict_heart_disease(features):
    
    model = pickle.load(open('rf.pkl','rb'))
    prediction = model.predict([features])
    return prediction

class HeartDiseasePredictionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Heart Disease Prediction")

        
        self.feature_labels = ['age', 'sex', 'cp', 'trestbps', 'chol',
                               'fbs', 'restecg', 'thalach', 'exang', 'oldpeak',
                               'slope', 'ca', 'thal']

        self.feature_entries = []

        for i, label in enumerate(self.feature_labels):
            ttk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=5)
            entry = ttk.Entry(root)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.feature_entries.append(entry)

      
        ttk.Button(root, text="Predict", command=self.predict).grid(row=len(self.feature_labels), columnspan=2, pady=10)

    def get_input_features(self):
        try:
            features = [float(entry.get()) for entry in self.feature_entries]
            return features
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter valid numeric values for all features.")
            return None 

    def predict(self):
        features = self.get_input_features()

        if features is not None:
            prediction = predict_heart_disease(features)
            if(prediction == 1):
                result_text='You have Heart Disease Symptoms'
            else:
                result_text="You don't have heart disease Symptoms"
            tk.messagebox.showinfo("Prediction Result", result_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = HeartDiseasePredictionApp(root)
    root.mainloop()
print(tk.TkVersion)