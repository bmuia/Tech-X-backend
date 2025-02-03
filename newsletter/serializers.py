from rest_framework import serializers
from .models import NewsletterSubscription

class NewsletterSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscription
        fields = ['user', 'subscribed']
    
    def update(self, instance, validated_data):
        instance.subscribed = validated_data.get('subscribed', instance.subscribed)
        instance.save()
        return instance
