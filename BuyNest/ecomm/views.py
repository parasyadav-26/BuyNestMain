from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from .models import UserData, Category, Product
from django.contrib.auth import authenticate,login

def index(request):
    return HttpResponse("hello ji jai shree ram")

def home_view(request):
    categories = Category.objects.all()
    return render(request, 'ecomm/home.html', {'categories': categories})

def register_view(request):
    if request.method=='POST':
        first_name= request.POST.get('fname')
        last_name= request.POST.get('lname')
        email= request.POST.get('email')
        password= request.POST.get('password')

        user = UserData.objects.create(first_name= first_name, last_name= last_name, email=email,password=password)
        user.save()
    return render(request, 'ecomm/register.html')

def login_view(request):
    if request.method== 'POST':
        email= request.POST.get('email')
        password= request.POST.get('password')

        try:
            user= UserData.objects.get(email=email, password=password)

            if user:
                request.session['user_id']= user.id
                return redirect('index')
        except:
            return render(request, 'ecomm/login.html', {'error': 'Invalid email or password'})
    return render(request, 'ecomm/login.html')


def products_view(request, category_id):
    # Get the selected category
    category = get_object_or_404(Category, id=category_id)

    # Fetch all products for the selected category
    products = Product.objects.filter(category=category)

    # Optional: Sidebar filters (add more filters if required)
    brand_filter = request.GET.get('brand')
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    color_filter = request.GET.get('color')

    # Apply filters if selected
    if brand_filter:
        products = products.filter(brand__icontains=brand_filter)
    if price_min and price_max:
        products = products.filter(price__gte=price_min, price__lte=price_max)
    if color_filter:
        products = products.filter(color__icontains=color_filter)

    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'ecomm/products.html', context)
