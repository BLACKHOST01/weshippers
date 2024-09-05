from django.urls import path, include
from rest_framework import routers
from .views import (
   
    ShippingUserViewSet,
    ShipmentViewSet,
    ShipmentDetailView,
    UpdateShipmentStatusForUserView,
#     CustomSignInView,
#     CustomSignOutView,
#     GoogleLogin,
#     TwitterLogin,
#     FacebookLogin,
#     GoogleAuthAPIView,
#     TwitterAuthAPIView,
#     FacebookAuthAPIView,
)



router = routers.DefaultRouter()
router.register(r'shipping-users', ShippingUserViewSet)
router.register(r'shipments', ShipmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('shipping-users/create/', ShippingUserViewSet.as_view({'post': 'create'}), name='create-shipping-user'),
    path('shipping-users/<int:pk>/', ShippingUserViewSet.as_view({'get': 'retrieve'}), name='retrieve-shipping-user'),
    path('shipping-users/<int:pk>/update/', ShippingUserViewSet.as_view({'put': 'update'}), name='update-shipping-user'),
    path('shipping-users/<int:pk>/delete/', ShippingUserViewSet.as_view({'delete': 'destroy'}), name='delete-shipping-user'),
    path('search/<str:tracking_number>/', ShipmentDetailView.as_view(), name='shipment-detail'),
    path('shipment-status/user/', UpdateShipmentStatusForUserView.as_view()),

]










# urlpatterns = [
#     path('todos/', TodoList.as_view(), name='todo-list'),  # List and create todos
#     path('todos/<int:pk>/', TodoDetail.as_view(), name='todo-detail'),  # Retrieve, update or delete a todo

#     path('shipments/', ShipmentViewSet.as_view({'get': 'list', 'post': 'create'}), name='shipment-list'),  # List and create shipments
#     path('shipments/<int:pk>/', ShipmentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='shipment-detail'),  # Retrieve, update or delete a shipment


#     path('auth/signin/', CustomSignInView.as_view(), name='custom-signin'),  # Custom sign-in
#     path('auth/signout/', CustomSignOutView.as_view(), name='custom-signout'),  # Custom sign-out

#     path('auth/google/', GoogleLogin.as_view(), name='google-login'),  # Google login
#     path('auth/twitter/', TwitterLogin.as_view(), name='twitter-login'),  # Twitter login
#     path('auth/facebook/', FacebookLogin.as_view(), name='facebook-login'),  # Facebook login

#     path('auth/google/callback/', GoogleAuthAPIView.as_view(), name='google-auth'),  # Google auth callback
#     path('auth/twitter/callback/', TwitterAuthAPIView.as_view(), name='twitter-auth'),  # Twitter auth callback
#     path('auth/facebook/callback/', FacebookAuthAPIView.as_view(), name='facebook-auth'),  # Facebook auth callback
# ]