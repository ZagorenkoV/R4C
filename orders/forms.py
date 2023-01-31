from .models import Order
from django.forms import ModelForm, TextInput

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'robot_serial']

        widgets = {
            'customer': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваш email'
            }),
            'robot_serial': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите серийный номер робота, например R2-D2'
            })
        }