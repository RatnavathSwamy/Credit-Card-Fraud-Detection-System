from django.db import models

class Transaction(models.Model):
    transaction_amount = models.FloatField()
    transaction_time = models.IntegerField()
    customer_age = models.IntegerField()
    location_score = models.IntegerField()
    previous_fraud_count = models.IntegerField()
    prediction = models.CharField(max_length=20)

    def __str__(self):
        return self.prediction


# Create your models here.
