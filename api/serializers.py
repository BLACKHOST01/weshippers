from rest_framework import serializers
from django.contrib.auth import logout
# from .forms import CustomSignInForm, CustomSignOutForm
from .models import Shipment, ShippingUser, ShippingMethod, ShipmentStatus






class ShippingUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingUser
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'street_address',
            'city',
            'state',
            'zip_code',
            'country',
            'company_name',
            'company_address',
            'company_phone',
            'is_business_account',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['is_personal_account'] = instance.is_personal_account
        return representation





class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = '__all__'
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['sender'] = instance.sender.username  # Assuming ShippingUser has a username field
        ret['shipping_method'] = instance.shipping_method.name  # Assuming ShippingMethod has a name field
        return ret





class ShippingMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingMethod
        fields = '__all__'

    def validate_cost(self, value):
        if value <= 0:
            raise serializers.ValidationError('Cost must be a positive number')
        return value

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['carrier'] = instance.get_carrier_display()
        data['name'] = instance.get_name_display()
        return data






# serializers.py
class ShipmentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipmentStatus
        fields = ['id', 'shipment', 'user', 'status', 'updated_by', 'updated_at']







































# class CustomSignInSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ShippingUser
#         fields = ['username', 'password']
#         extra_kwargs = {'password': {'write_only': True}}
        
#     def validate(self, attrs):
#         self.form = CustomSignInForm(data=attrs)
#         if not self.form.is_valid():
#             raise serializers.ValidationError(self.form.errors)
#         return attrs

#     def create(self, validated_data):
#         user = self.form.get_user()
#         return user



# class CustomSignOutSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ShippingUser
#         fields = ['reason']

#     def validate(self, attrs):
#         form = CustomSignOutForm(data=attrs)
#         if not form.is_valid():
#             raise serializers.ValidationError(form.errors)
#         return attrs

#     def create(self, validated_data):
#         logout(self.context['request'])
#         return validated_data









