from django import forms
from .models import User, Product

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'name', 'phone_number']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_code', 'user_nvmid', 'keyword', 'is_mobile', 'is_shopping', 'is_grouped_item', 'start_date', 'end_date', 'price']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'name', 'phone_number']
