from django import http
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Customer, Product, Order
from accounts.forms import OrderForm, CustomerForm
from django.contrib import messages

# Create your views here.

def home(request):
    orders =Order.objects.all()
    customers =Customer.objects.all()
    total_customer =customers.count()
    total_order =orders.count()

    delivered =orders.filter(status ='Delivered').count()

    pend_order =orders.filter(status ='Pending').count()   

    context ={'orders': orders, 'customers':customers,'total_customer':total_customer,
    'total_order':total_order, 'delivered':delivered, 'pend_order':pend_order}
    return render(request,'accounts/dashboard.html', context)

def products(request):
    products =Product.objects.all()
    total_products =products.count()
    context ={'products':products, 'total_products':total_products}
    return render(request, 'accounts/products.html', context)

def customers(request,cust_id):    
    customer =Customer.objects.get(id =cust_id)
    cust_orders = customer.order_set.all()
    total_orders =cust_orders.count()
    context ={'customer':customer,'cust_orders':cust_orders, 'total_orders':total_orders}
    return render(request, 'accounts/customer.html', context)

def creat_customer(request):
    form =CustomerForm()
    if request.method =='POST':
        form =CustomerForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer saved successfully')
            return redirect('home')
    context ={'form':form}
    customers =Customer.objects.all()
    return render(request, 'accounts/create_customers.html', context)

def update_customer(request, cust_id):
    customer = Customer.objects.get(id= cust_id)
    form =CustomerForm(instance=customer)
    if request.method =='POST':
        form =CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
        messages.success(request,("Customer updated successfully"))
    context ={'form':form}
    return render(request,'accounts/create_customers.html', context)
def delete_customer(request, cust_id):
    customer =Customer.objects.get(id =cust_id)
    customer.delete()
    messages.success(request,("Customer deleted "))
    return redirect('home')
    #messages.success(request,("Customer deleted "))

def create_order(request):
    form =OrderForm()
    if request.method =='POST':
        form =OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success (request, 'Order(s) successfully created')
            return redirect ('home')
    context ={'form':form}
    return render (request, 'accounts/create_order.html', context)


def update_order(request, pk):
    order =Order.objects.get(id =pk)
    form =OrderForm(instance=Order)
    if request.method =='POST':
        form =OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
        return redirect('home')
    context ={'form':form}
    return render (request, 'accounts/update_order.html', context)

def delete_order(request, order_id):
    orders =Order.objects.get(id =order_id)
    orders.delete()
    return redirect('home')

def del_order(request, order_id):
    dele_ord =Order.objects.get(id =order_id)
    context ={'del_ord':dele_ord}
    return render(request, 'accounts/delete_order.html', context)
