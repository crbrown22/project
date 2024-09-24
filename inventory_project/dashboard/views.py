from django.shortcuts import render,  redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User
from user_app.forms import ProfileUpdateForm, UserUpdateForm
from datetime import datetime
from django.contrib import messages
# Create your views here.


def homepage(request):
    return render(request, 'homepage.html')


def about(request):
    return render(request, 'about.html')


def flexmob(request):
    return render(request, 'flexmob.html')


def conditioning(request):
    return render(request, 'conditioning.html')


def power(request):
    return render(request, 'power.html')

@login_required(login_url='user-login')
def members(request):
    return render(request, 'members.html')

@login_required(login_url='user-login')
def index(request):
    orders= Order.objects.all()
    products = Product.objects.all()
    members= User.objects.all()
    members_count= members.count()
    product_count = products.count()
    orders_count= orders.count()
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            instance= order_form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('index') 
    else:
        order_form = OrderForm
    context={
        'orders': orders,
        'order_form': order_form,
        'products': products,
        'members': members,
        'members_count' : members_count,
        'product_count' : product_count,
        'orders_count': orders_count,
        
    }

    return render(request, 'index.html', context)

@login_required(login_url='user-login')
def staff(request):
    members= User.objects.all()
    
    context={
        'members': members,
              
    }
    return render(request, 'staff.html',context)

@login_required(login_url='user-login')
def staff_details(request, pk):
    members= User.objects.get(id=pk)
    context={
        'members': members,
    }
    return render(request, 'staff_details.html', context)

@login_required(login_url='user-login')
def staff_delete(request, pk):
    members= User.objects.get(id=pk)
    if request.method == 'POST':
        members.delete()
        return redirect('staff')
    return render (request, 'staff_delete.html')

@login_required(login_url='user-login')
def staff_update(request, pk):
    members= User.objects.get(id=pk)
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.members)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance= request.members.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user-profile')
    else:
        user_form = UserUpdateForm(instance=request.members)
        profile_form = ProfileUpdateForm(instance= request.members.profile)
    context={
            'members':members,
            'user_form':user_form,
            'profile_form':profile_form

    }
    return render(request, 'staff_update.html', context)

@login_required(login_url='user-login')
def products(request):
    items= Product.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name=form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('products') 

    else:
        form = ProductForm
    context={
        "items": items,
        "form": form,
    }
    
    return render(request, 'products.html', context)

@login_required(login_url='user-login')
def product_delete(request, pk):
    items= Product.objects.get(id=pk)
    if request.method == 'POST':
        items.delete()
        return redirect('products')
    return render (request, 'product_delete.html')


@login_required(login_url='user-login')
def product_update(request, pk):
    items= Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=items)
        if form.is_valid():
            form.save()
            product_name=form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been updated')
            return redirect('products') 
    else:
        form = ProductForm(instance=items)
    context= {
        'form': form,
    }
    return render(request, 'product_update.html', context)


@login_required(login_url='user-login')
def orders(request):
    orders = Order.objects.all 
   
    context = {
        'orders': orders,
         

    }
    return render(request, 'orders.html', context)

def orders_staff(request):
    orders = Order.objects.all 
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            instance= order_form.save(commit=False)
            instance.customer = request.user
            instance.save()
            return redirect('orders-staff') 
    else:
        order_form = OrderForm
    context={
        "orders": orders,
        "order_form": order_form,
    }
    
    return render(request, 'orders_staff.html', context)