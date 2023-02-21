from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from .models import *
from .forms import CreationUserForm,OrderForm
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('demo')
    else:
        form = CreationUserForm()
        context = {'form': form}
        if request.method == 'POST':
            form = CreationUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, user + 'Registered Successfully.')
            return redirect('login')
        return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('demo')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                redirect('demo')
            else:
                messages.info(request, 'Incorrect Username or Password ')
        context = {}
        return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    order = Order.objects.all()

    total_customers = customer.count()

    total_orders = order.count()
    delivered = order.filter(status = 'Delivered').count()
    pending = order.filter(status = 'Pending').count()

    context = {'orders' : order,'customers' : customer,
               'total_orders' : total_orders,'delivered' : delivered,
               'pending' : pending}
    return render(request, 'accounts/dashboard.html',context)

@login_required(login_url='login')
def products(request):
    products = Product.objects.all()
    return render(request,'accounts/products.html', {'products' : products})

@login_required(login_url='login')
def customer(request,pk_test):
    customer = Customer.objects.get(id=pk_test)

    order = customer.order_set.all()
    order_count = order.count()

    myFilter = OrderFilter(request.GET,queryset = order)
    order = myFilter.qs

    context = {'customer' : customer , 'order' : order ,'order_count' : order_count,
               'myFilter' : myFilter}
    return render(request,'accounts/customer.html',context)

# OrderFormSet = inlineformset_factory(Customer,Order,fields = (product,state))
@login_required(login_url='login')
def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer,Order)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(),instance = customer)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST,instance = customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'form': formset}
    return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
def updateOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer,Order)
    order = Order.objects.get(id=pk)
    form = OrderForm(instance = order)
    if request.method == 'POST':
        form = OrderForm(request.POST,instance = order)
        formset = OrderFormSet(request.POST,instance = customer)
        if form.is_valid():
            formset.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'accounts/delete.html', context)









