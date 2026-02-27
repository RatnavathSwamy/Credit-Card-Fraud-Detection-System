import os
import joblib
import numpy as np
from django.conf import settings
from django.shortcuts import render
from .models import Transaction

# Load model safely
model_path = os.path.join(settings.BASE_DIR, 'fraud_model.pkl')
model = joblib.load(model_path)

def home(request):
    if request.method == "POST":
        amount = float(request.POST['amount'])
        time = int(request.POST['time'])
        age = int(request.POST['age'])
        location = int(request.POST['location'])
        previous = int(request.POST['previous'])

        data = np.array([[amount, time, age, location, previous]])

        result = model.predict(data)

        prediction = "Fraud" if result[0] == 1 else "Not Fraud"

        Transaction.objects.create(
            transaction_amount=amount,
            transaction_time=time,
            customer_age=age,
            location_score=location,
            previous_fraud_count=previous,
            prediction=prediction
        )

        return render(request, "index.html", {"prediction": prediction})

    return render(request, "index.html")

