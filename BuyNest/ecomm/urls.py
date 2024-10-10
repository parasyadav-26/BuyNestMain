from django.urls import path
from . import views

urlpatterns =[
    path('', views.home_view, name="index" ),
    path('index/', views.index, name="home_view"),
    path('register/', views.register_view, name="register"),
    path('login/',views.login_view, name="login"),
    path('products/<int:category_id>/', views.products_view, name='products_view'),
]