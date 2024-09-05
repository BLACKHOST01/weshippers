from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Shipment, ShippingUser, ShippingMethod, ShipmentStatus
from .serializers import ShippingUserSerializer, ShipmentSerializer, ShippingMethodSerializer, ShipmentStatusSerializer
# , CustomSignInSerializer, CustomSignOutSerializer
from rest_framework.response import Response
import requests







# from django.shortcuts import get_object_or_404
# import requests

# from django.contrib.auth import login, logout
# from django.shortcuts import redirect
# from django.views.generic import FormView
# from .forms import CustomSignInForm, CustomSignOutForm

# from .socialauthserializer import GoogleAuthSerializer, TwitterAuthSerializer, FacebookAuthSerializer
# # this is the social login viewsets
# from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
# from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
# from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
# from allauth.socialaccount.models import SocialLogin, SocialAccount
# from dj_rest_auth.registration.views import SocialLoginView
# from api.socialauthserializer import get_tokens_for_user






class ShippingUserViewSet(viewsets.ModelViewSet):
    queryset = ShippingUser.objects.all()
    serializer_class = ShippingUserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return ShippingUser.objects.all()
        else:
            return ShippingUser.objects.filter(id=user.id)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)






# this is the shipping viewsets
class ShipmentViewSet(viewsets.ModelViewSet):
    """List all shipments, or create a new one."""
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer






class ShippingMethodViewSet(viewsets.ModelViewSet):
    queryset = ShippingMethod.objects.all()
    serializer_class = ShippingMethodSerializer




# class SearchShipmentView(viewsets.ViewSet):
#     def retrieve(self, request, tracking_id):
#         try:
#             shipment = Shipment.objects.get(tracking_id=tracking_id)  # Adjust based on your model field
#             serializer = ShipmentSerializer(shipment)
#             return Response(serializer.data)
#         except Shipment.DoesNotExist:
#             return Response({'error': 'Shipment not found'}, status=status.HTTP_404_NOT_FOUND)



class ShipmentDetailView(generics.RetrieveAPIView):
    """
    Retrieve a specific shipment by tracking number.
    """
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.all()
    
    def get(self, request, tracking_number, *args, **kwargs):
        try:
            shipment = self.queryset.get(tracking_number=tracking_number)  # Use tracking_number here
            serializer = self.get_serializer(shipment)
            sender_data = {
                'first_name': shipment.sender.first_name,
                'last_name': shipment.sender.last_name,
                'email': shipment.sender.email,
                'phone_number': shipment.sender.phone_number,
                'street_address': shipment.sender.street_address,
                'city': shipment.sender.city,
                'state': shipment.sender.state,
                'zip_code': shipment.sender.zip_code,
                'country': shipment.sender.country,
                'company_name': shipment.sender.company_name,
                'company_address': shipment.sender.company_address,
            }
            response_data = {**serializer.data, 'sender': sender_data}
            return Response(response_data)
        except Shipment.DoesNotExist:
            return Response({"detail": "Shipment not found."}, status=status.HTTP_404_NOT_FOUND)





class UpdateShipmentStatusForUserView(generics.UpdateAPIView):
    queryset = ShipmentStatus.objects.all()
    serializer_class = ShipmentStatusSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ShipmentStatus.objects.filter(user=user)

    def update(self, request, *args, **kwargs):
        shipment_status = self.get_object()
        serializer = self.get_serializer(shipment_status, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(updated_by=self.request.user)
        return Response(serializer.data)








# class CustomSignInView(generics.GenericAPIView):
#     """Custom sign-in view, using the CustomSignInForm."""
#     serializer_class = CustomSignInSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         login(request, user)
#         return Response(status=status.HTTP_200_OK)


# class CustomSignOutView(generics.GenericAPIView):
#     """Custom sign-out view, using the CustomSignOutForm."""
#     serializer_class = CustomSignOutSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         logout(request)  # Add this line to log out the user
#         return Response(status=status.HTTP_200_OK)
    

# # # Views for social authentication providers (Google, Twitter, Facebook)

# class GoogleLogin(SocialLoginView):
#     adapter_class = GoogleOAuth2Adapter

# class TwitterLogin(SocialLoginView):
#     adapter_class = TwitterOAuthAdapter

# class FacebookLogin(SocialLoginView):
#     adapter_class = FacebookOAuth2Adapter

# class GoogleAuthAPIView(generics.GenericAPIView):
#     serializer_class = GoogleAuthSerializer

#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         access_token = serializer.validated_data['access_token']

#          # Use the access token to retrieve user info and authenticate
#         # Here you would typically call the Google API to get user details
#         # For example:
#         response = requests.get(f'https://www.googleapis.com/oauth2/v2/userinfo?access_token={access_token}')
#         user_info = response.json()

#         # Validate user info, create or retrieve user in your database
#         # For example:
#         user, _ = ShippingUser.objects.get_or_create(email=user_info['email'])

#         # Validate user info, create or retrieve user in your database
#         # user = ...

#         # Generate tokens
#         tokens = get_tokens_for_user(user)

#         return Response(tokens, status=status.HTTP_200_OK)

# class TwitterAuthAPIView(generics.GenericAPIView):
#     serializer_class = TwitterAuthSerializer

#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         # Validate Twitter access token and secret and generate tokens here
#         # ...
#         access_token = serializer.validated_data['access_token']
#         access_token_secret = serializer.validated_data['access_token_secret']
#         tokens = get_tokens_for_user(access_token, access_token_secret)

#         return Response(tokens, status=status.HTTP_200_OK)

# class FacebookAuthAPIView(generics.GenericAPIView):
#     serializer_class = FacebookAuthSerializer

#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         access_token = serializer.validated_data['access_token']
#         tokens = get_tokens_for_user(access_token)
#         # Similar logic to handle Facebook access token
#         # ...

#         return Response(tokens, status=status.HTTP_200_OK)


