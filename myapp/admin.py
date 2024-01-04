from django.contrib import admin

from .models import Product,Review,Profile,Category,Plan,Code,Cart,CartItem,Order,LandingPage

# Register your models here.
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Plan)
admin.site.register(Code)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(LandingPage)