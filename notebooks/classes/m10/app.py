# app.py

import pickle
import numpy as np

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Example input:
# [AGE, EMPLOY, ADDRESS, DEBTINC, CREDDEBT, OTHDEBT]
sample = np.array([[3, 10, 5, 15.0, 2.0, 3.0]])

prediction = model.predict(sample)

if prediction[0] == 1:
    print("⚠️ High Risk: Defaulter")
else:
    print("✅ Low Risk: Non-Defaulter")