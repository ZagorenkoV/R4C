from django.shortcuts import render, redirect
from .forms import OrderForm

# Create your views here.

def Order(request):
    error = ''
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if not form.is_valid():
            error = 'Форма заполненна некорректно'
        else:
            form.save()
            return redirect('order')

    form = OrderForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'orders/order.html', data)