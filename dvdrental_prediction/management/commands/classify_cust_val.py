import pandas as pd
import numpy as np
from django.core.management.base import BaseCommand
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
from dvdrental_prediction.models import ModelInfo
from django.utils import timezone

class Command(BaseCommand):
    help = 'Train a model to classify customer value and save it.'
    def handle(self, *args, **kwargs):
        df = pd.read_csv('customer_payment_dataset.csv')
        # 2 Create target label
        df['value_label'] = (df['total_payment']>100).astype(int)
        # 3 Define feature and label
        features = ['store_id', 'total_payment', 
                    'payment_count', 'average_payment']
        X = df[features]
        y = df['value_label']
        X_train, X_test, y_train, y_test = train_test_split(X, y , 
                                                            test_size=0.2, 
                                                            random_state=42)
        # 5 Train the model
        model = RandomForestClassifier()
        model.fit(X_train, y_train)

        # 6  Prediction and evaluate
        predictions = model.predict(X_test)
        report = classification_report(y_test, predictions)
        self.stdout.write(self.style.SUCCESS(
            "Classification Report: \n" + report))
        
        # 7 save the model to pickle file
        model_filename = 'final_customer_model.pkl'
        joblib.dump(model, model_filename)
        self.stdout.write(
            self.style.SUCCESS(f'Model saved as {model_filename}')
        )
        # 8 save the model info to DB
        modelinfo = ModelInfo.objects.create(
            model_name = 'RandomForestCustomerModel',
            model_file = model_filename,
            training_data = 'customer_payment_dataset.csv',
            training_date = timezone.now(),
            model_summary = report)
        
        self.stdout.write(
            self.style.SUCCESS(f'Model info saved to DB: ID {modelinfo.id}')
        )

        

        
