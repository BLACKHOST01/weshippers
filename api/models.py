from django.db import models
import string
import random
from django.contrib.auth.models import User  # Add this import
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import RegexValidator
from django.utils.crypto import get_random_string




"""
Models related to the users of the system.

The ShippingUser model is an extension of Django's built-in User model.
It adds additional fields to store the user's shipping information.
"""

class ShippingUser(AbstractUser):
    """
    This model represents a user in the system that can make shipments.
    The user can be either a personal or business account.
    """

    # Override the groups and user_permissions fields

    groups = None

    user_permissions = None

    phone_number = models.CharField(max_length=20, null=True, blank=True)
    
    street_address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    
    company_name = models.CharField(max_length=100, null=True, blank=True)
    company_address = models.TextField(null=True, blank=True)
    company_phone = models.CharField(max_length=20, null=True, blank=True)
    
    is_business_account = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def is_personal_account(self):
        return not self.is_business_account





# my shipping models

class Shipment(models.Model):
    """
    A shipment represents a physical package that is being tracked by the system.
    Each shipment has a unique tracking number, a sender, a recipient, a shipping
    method, and a status. The status can be one of the following:
    
    - 'pending': The shipment is waiting to be shipped.
    - 'in_transit': The shipment is currently in transit.
    - 'delivered': The shipment has been delivered to the recipient.
    - 'cancelled': The shipment has been cancelled.
    """
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    tracking_number = models.CharField(

        max_length=10, 
        unique=True, 
        editable=False, 
        default=''.join(random.choices(string.digits, k=10))  # Generate a 10-digit tracking number
    )

    sender = models.ForeignKey('ShippingUser', on_delete=models.CASCADE)
    recipient_name = models.CharField(max_length=100)
    recipient_address = models.TextField()
    recipient_phone = models.CharField(max_length=20)
    
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    
    weight = models.DecimalField(max_digits=6, decimal_places=2, help_text="Weight in kg")
    dimensions = models.CharField(max_length=50, help_text="Length x Width x Height in cm")
    
    shipping_method = models.ForeignKey('ShippingMethod', on_delete=models.CASCADE, related_name='shipments')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    estimated_delivery = models.DateTimeField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        # Generate a new tracking number if it is not already set
        if not self.tracking_number:
            self.tracking_number = ''.join(random.choices(string.digits, k=10))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Shipment {self.tracking_number}"

    class Meta:

        ordering = ['-created_at']


class ShippingMethod(models.Model):
    """
    A shipping method represents a type of shipping that can be used to ship
    packages. Each shipping method has a name, a description, and a cost.
    """
    SHIPPING_METHOD_CHOICES = [
        ('G', 'Ground shipping'),
        ('E', 'Expedited shipping'),
        ('SD', 'Same-day shipping'),
        ('I', 'International shipping'),
        ('F', 'Freight shipping'),
    ]
    
    CARRIER_STATUS_CHOICES = [
        ('UPS', 'United Parcel Service'),
        ('FEDEX', 'Federal Express'),
        ('USPS', 'United States Postal Service'),
        ('DHL', 'DHL Express'),
        ('OTHER', 'Other'),
    ]

    carrier = models.CharField(max_length=5, choices=CARRIER_STATUS_CHOICES)
    name = models.CharField(max_length=100, choices=SHIPPING_METHOD_CHOICES)
    description = models.TextField(null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.name




class ShipmentStatus(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    user = models.ForeignKey(ShippingUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[
        ('pending', 'Pending'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ])
    updated_by = models.ForeignKey(ShippingUser, on_delete=models.CASCADE, related_name='updated_shipment_status')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.shipment.tracking_number} - {self.user.email} - {self.status}"