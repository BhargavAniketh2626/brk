from django.shortcuts import render, redirect
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q 
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ProductView(View):
    def get(self, request):
        totalitem = 0
        casualwears = Product.objects.filter(category='CW')
        officewears = Product.objects.filter(category='OW')
        ethnicwears = Product.objects.filter(category='EW')
        sportswears = Product.objects.filter(category='SW')
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request,'app/Home.html',
        {'casualwears':casualwears,
        'officewears':officewears,
        'ethnicwears':ethnicwears,
        'sportswears':sportswears,
        'totalitem':totalitem})

class ProductDetailView(View):
    def get(self, request, pk):
        totalitem = 0
        product= Product.objects.get(pk=pk)
        item_already_in_cart = False
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
        return render(request, 'app/productdetail.html',{'product':product, 'item_already_in_cart':item_already_in_cart, 'totalitem':totalitem})

@login_required
def add_to_cart(request):
 user = request.user
 product_id = request.GET.get('prod_id')
 product = Product.objects.get(id=product_id)
 Cart(user=user, product=product).save()
 return redirect('/cart')

@login_required
def show_cart(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        user = request.user
        cart = Cart.objects.filter(user=user)
        print(cart)
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
                totalamount = amount + shipping_amount
            return render(request, 'app/addtocart.html', {'carts':cart, 'totalamount':totalamount, 'amount':amount, 'totalitem':totalitem})
        else:
            return render(request, 'app/emptycart.html', {'totalitem':totalitem})

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':amount + shipping_amount
        }
        return JsonResponse(data)

def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1   
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data = {
            'quantity': c.quantity,
            'amount':amount,
            'totalamount':amount + shipping_amount
        }
        return JsonResponse(data)

def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data = {
            'amount':amount,
            'totalamount':amount + shipping_amount
        }
        return JsonResponse(data)


def buy_now(request):
 return render(request, 'app/buynow.html')

def team(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/team.html', {'totalitem':totalitem})   

def designers(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/designers.html', {'totalitem':totalitem})   

def contact(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/contactus.html', {'totalitem':totalitem})

def about(request):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/aboutus.html', {'totalitem':totalitem})      

@login_required
def address(request):
 add = Customer.objects.filter(user=request.user)
 return render(request, 'app/address.html', {'add':add, 'active':'btn-primary'})

@login_required
def orders(request):
 op = OrderPlaced.objects.filter(user=request.user)
 return render(request, 'app/orders.html', {'order_placed':op})

def casualwears(request, data=None):
    if data == None:
        casuals = Product.objects.filter(category='CW')
    elif data == 'arrow' or data == 'LouisPhillipe':
        casuals = Product.objects.filter(category='CW').filter(brand=data)
    elif data == 'below':
        casuals = Product.objects.filter(category='CW').filter(discounted_price__lt=1500)
    elif data == 'above':
        casuals = Product.objects.filter(category='CW').filter(discounted_price__gt=1500)
    return render(request, 'app/casualwears.html', {'casuals':casuals})

def officewears(request, data=None):
    if data == None:
        office = Product.objects.filter(category='OW')
    elif data == 'TommyHilfiger' or data == 'Raymond':
        office = Product.objects.filter(category='OW').filter(brand=data)
    elif data == 'below':
        office = Product.objects.filter(category='OW').filter(discounted_price__lt=3500)
    elif data == 'above':
        office = Product.objects.filter(category='OW').filter(discounted_price__gt=3500)
    return render(request, 'app/officewears.html', {'office':office})

def ethnicwears(request, data=None):
    if data == None:
        ethnics = Product.objects.filter(category='EW')
    elif data == 'Parx' or data == 'Rangriti':
        ethnics = Product.objects.filter(category='EW').filter(brand=data)
    elif data == 'below':
        ethnics = Product.objects.filter(category='EW').filter(discounted_price__lt=4500)
    elif data == 'above':
        ethnics = Product.objects.filter(category='EW').filter(discounted_price__gt=4500)
    return render(request, 'app/ethnicwears.html', {'ethnics':ethnics})

def sportswears(request, data=None):
    if data == None:
        sports = Product.objects.filter(category='SW')
    elif data == 'Puma' or data == 'Adidas':
        sports = Product.objects.filter(category='SW').filter(brand=data)
    elif data == 'below':
        sports = Product.objects.filter(category='SW').filter(discounted_price__lt=500)
    elif data == 'above':
        sports = Product.objects.filter(category='SW').filter(discounted_price__gt=500)
    return render(request, 'app/sportswears.html', {'sports':sports})

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form':form})
    
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registered Successfully')
            form.save()
        return render(request, 'app/customerregistration.html', {'form':form})

@login_required
def checkout(request):
 user = request.user
 add = Customer.objects.filter(user=user) 
 cart_items = Cart.objects.filter(user=user)
 amount = 0.0
 shipping_amount = 70.0
 total_amount = 0.0
 cart_product = [p for p in Cart.objects.all() if p.user == request.user]
 if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
        totalamount = amount +shipping_amount  
 return render(request, 'app/checkout.html', {'add':add, 'totalamount':totalamount, 'cart_items':cart_items})

@login_required
def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity).save()
        c.delete()
    return redirect("orders")

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=usr, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, 'Congratulations!! Profile Updated Sucessfully')
        return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})

def home(request):
    return render(request, 'app/home.html')

def room(request, room):
    username = request.GET.get('user')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['user']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?user='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?user='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=user, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})