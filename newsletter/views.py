from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from .models import NewsletterSubscription
from .serializers import NewsletterSubscriptionSerializer

class NewsletterSubscriptionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            subscription = NewsletterSubscription.objects.get(user=request.user)
            return Response({
                'subscribed': subscription.subscribed
            })
        except NewsletterSubscription.DoesNotExist:
            return Response({"detail": "You are not subscribed."}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        data = {'subscribed': request.data.get('subscribed', True)}
        
        # If the user doesn't already have a subscription object, create one
        subscription, created = NewsletterSubscription.objects.get_or_create(user=request.user)
        serializer = NewsletterSubscriptionSerializer(subscription, data=data, partial=True)
        
        if serializer.is_valid():
            subscription = serializer.save()
            
            # If the user has just subscribed (subscribed is True)
            if subscription.subscribed:
                # Send the email
                subject = 'You have successfully subscribed to our newsletter!'
                message = f"Hello {request.user.username},\n\nThank you for subscribing to our newsletter!"
                recipient_list = [request.user.email]  # Send to the user's email
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
            
            return Response({"message": "Subscription updated successfully."}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
