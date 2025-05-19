# dvdrental_prediction/views.py  
from django.shortcuts import render  
from django.http import JsonResponse  
from django.views.decorators.csrf import csrf_exempt  
import logging  
import json  
import joblib  
import numpy as np  
from django.conf import settings  
import os  
  
logger = logging.getLogger(__name__)  
  
# Load model  
def load_model():  
    try:  
        model_path = os.path.join(settings.BASE_DIR, 'final_customer_model.pkl')  
        return joblib.load(model_path)  
    except Exception as e:  
        logger.error(f"Error loading model: {str(e)}")  
        return None  
  
MODEL = load_model()  
  
def home(request):  
    return render(request, 'dvdrental_prediction/home.html')  
  
def about(request):  
    return render(request, 'dvdrental_prediction/about.html')  
  
def customer_prediction_view(request):  
    return render(request, 'dvdrental_prediction/dashboard.html')  
  
@csrf_exempt  
def predict_customer(request):  
    if request.method != 'POST':  
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)  
      
    try:  
        data = json.loads(request.body)  
        features = np.array([  
            float(data['store_id']),  
            # float(data['active']),  
            float(data['total_payment']),  
            float(data['payment_count']),  
            float(data['average_payment'])  
        ]).reshape(1, -1)  
          
        prediction = MODEL.predict(features)[0]  
        probabilities = MODEL.predict_proba(features)[0].tolist()  
          
        return JsonResponse({  
            'prediction': int(prediction),  
            'probability': probabilities  
        })  
    except Exception as e:  
        return JsonResponse({'error': str(e)}, status=400)  