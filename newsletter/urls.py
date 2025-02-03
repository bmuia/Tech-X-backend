# urls.py in your 'accounts' app
from django.urls import path
from .views import NewsletterSubscriptionView

urlpatterns = [
    path('newsletter/subscribe/', NewsletterSubscriptionView.as_view(), name='newsletter_subscribe'),
]
