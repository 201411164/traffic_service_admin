from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User, Product, Log
from .forms import UserForm, ProductForm, UserEditForm


def admin(request):
    if not request.user.is_authenticated:
        return redirect('login')

    users = User.objects.all()
    products = Product.objects.all()
    logs = Log.objects.all()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = UserForm()

    context = {'users': users, 'products': products, 'logs': logs, 'form': form}
    return render(request, 'admin.html', context)


def customer(request):
    if not request.user.is_authenticated:
        return redirect('login')

    products = Product.objects.filter(user=request.user)

    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('customer')
    else:
        form = UserEditForm(instance=request.user)

    context = {'products': products, 'form': form}
    return render(request, 'customer.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('customer')
        else:
            return render(request, 'login.html', {'error_message': '로그인 정보가 잘못되었습니다.'})
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


