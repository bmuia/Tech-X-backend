from django.db import models
from django.contrib.auth.models import User

class NewsletterSubscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscribed = models.BooleanField(default=True)  

    def __str__(self):
        return f"{self.user.username} - {'Subscribed' if self.subscribed else 'Unsubscribed'}"
