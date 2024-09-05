# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class ShippingUser(AbstractUser):
    # ... (previous fields)

# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomSignInForm(AuthenticationForm):
    # Add any custom fields you need, e.g., remember_me, etc.
    pass

class CustomSignOutForm(forms.Form):
    # Add any custom fields you need, e.g., reason_for_logout, etc.
    pass

# views.py
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import CustomSignInForm, CustomSignOutForm

def custom_sign_in(request):
    if request.method == 'POST':
        form = CustomSignInForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')
    else:
        form = CustomSignInForm()
    return render(request, 'custom_sign_in.html', {'form': form})

def custom_sign_out(request):
    if request.method == 'POST':
        form = CustomSignOutForm(request.POST)
        if form.is_valid():
            logout(request)
            return redirect('home')
    else:
        form = CustomSignOutForm()
    return render(request, 'custom_sign_out.html', {'form': form})

# urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('sign-in/', views.custom_sign_in, name='custom_sign_in'),
    path('sign-out/', views.custom_sign_out, name='custom_sign_out'),
    path('accounts/', include('allauth.urls')),
]











# api/models.py

from django.db import models

class ShippingUser(AbstractUser):
    # Your additional fields here
    # e.g. address = models.CharField(max_length=255)

    groups = models.ManyToManyField(
        Group,
        related_name='shippinguser_set',  # Change this
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='shippinguser_set',  # Change this
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )























    # from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import ShipmentViewSet, SearchShipmentView
# # from . import views
# from api.views import TodoList


# router = DefaultRouter()
# router.register(r'shipments', ShipmentViewSet, ShipmentViewSet)
# urlpatterns = [
#       path('api/auth/', include('your_app.url')),
#       path('todos/', TodoList.as_view(), name='todo-list'),
#       path('api/', include(router.urls)),
#       path('api/search/<str:tracking_id>/', SearchShipmentView.as_view({'get': 'retrieve'}), name='search-shipment'), 
# ]
# api/urls.py

from django.urls import path
from .views import (
    TodoList,
    TodoDetail,
    ShipmentViewSet,
    SearchShipmentView,
    CustomSignInView,
    CustomSignOutView,
    GoogleLogin,
    TwitterLogin,
    FacebookLogin,
    GoogleAuthAPIView,
    TwitterAuthAPIView,
    FacebookAuthAPIView,
)

urlpatterns = [
    path('todos/', TodoList.as_view(), name='todo-list'),  # List and create todos
    path('todos/<int:pk>/', TodoDetail.as_view(), name='todo-detail'),  # Retrieve, update or delete a todo

    path('shipments/', ShipmentViewSet.as_view({'get': 'list', 'post': 'create'}), name='shipment-list'),  # List and create shipments
    path('shipments/<int:pk>/', ShipmentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='shipment-detail'),  # Retrieve, update or delete a shipment

    path('search/<str:tracking_id>/', SearchShipmentView.as_view({'get': 'retrieve'}), name='search-shipment'),  # Search for a shipment by tracking ID

    path('auth/signin/', CustomSignInView.as_view(), name='custom-signin'),  # Custom sign-in
    path('auth/signout/', CustomSignOutView.as_view(), name='custom-signout'),  # Custom sign-out

    path('auth/google/', GoogleLogin.as_view(), name='google-login'),  # Google login
    path('auth/twitter/', TwitterLogin.as_view(), name='twitter-login'),  # Twitter login
    path('auth/facebook/', FacebookLogin.as_view(), name='facebook-login'),  # Facebook login

    path('auth/google/callback/', GoogleAuthAPIView.as_view(), name='google-auth'),  # Google auth callback
    path('auth/twitter/callback/', TwitterAuthAPIView.as_view(), name='twitter-auth'),  # Twitter auth callback
    path('auth/facebook/callback/', FacebookAuthAPIView.as_view(), name='facebook-auth'),  # Facebook auth callback
]






from django.urls import path
from .views import (
    TodoList,
    TodoDetail,
    ShipmentViewSet,
    SearchShipmentView,
    CustomSignInView,
    CustomSignOutView,
    GoogleLogin,    TwitterLogin,
    FacebookLogin,
    GoogleAuthAPIView,
    TwitterAuthAPIView,
    FacebookAuthAPIView,
)
router = DefaultRouter()
router.register(r'shipments', ShipmentViewSet, basename='shipment')
router.register(r'todos', TodoList, basename='todo')
router.register(r'search', SearchShipmentView, basename='search')

urlpatterns = [
    path('auth/signin/', CustomSignInView.as_view(), name='custom-signin'),  # Custom sign-in
    path('auth/signout/', CustomSignOutView.as_view(), name='custom-signout'),  # Custom sign-out

    path('auth/google/', GoogleLogin.as_view(), name='google-login'),  # Google login
    path('auth/twitter/', TwitterLogin.as_view(), name='twitter-login'),  # Twitter login
    path('auth/facebook/', FacebookLogin.as_view(), name='facebook-login'),  # Facebook login

    path('auth/google/callback/', GoogleAuthAPIView.as_view(), name='google-auth'),  # Google auth callback
    path('auth/twitter/callback/', TwitterAuthAPIView.as_view(), name='twitter-auth'),  # Twitter auth callback
    path('auth/facebook/callback/', FacebookAuthAPIView.as_view(), name='facebook-auth'),  # Facebook auth callback
]

urlpatterns += router.urls
