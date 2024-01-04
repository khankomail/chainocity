from django.urls import path
from . import views

urlpatterns = [
  path('',views.dashboard, name=""),

  path('home',views.home, name="home"),
  
  path('register',views.register, name="register"),

  path('my_login',views.my_login,name='my_login'),

  path('logout',views.logout, name="logout"),

  path('dashboard', views.dashboard, name="dashboard"),

  path('profile',views.profile, name="profile"),

  path('delete_profile',views.delete_profile, name="delete_profile"),

  path('product/<int:pk>/',views.product, name="product"),

  path('category/<str:ct>/',views.category, name="category"),

  path('mylink',views.mylink, name="mylink"),

  path('plan',views.plan, name="plan"),

  path('earning',views.earning, name="earning"),

  path('cart',views.cart, name="cart"),

  path('cartadd/<int:product_id>/',views.cart_add, name="cartadd"),

  path('cartdelete',views.cart_delete, name="cartdelete"),

  path('cartupdate',views.cart_update, name="cartupdate"),

  path('checkout/', views.checkout, name='checkout'),

  path('order_confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),

  
]
