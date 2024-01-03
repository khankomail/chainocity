from django.db import models
import random
import string
from django.core.validators import RegexValidator

from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name


class Product(models.Model):
    p_title = models.CharField(max_length=85)
    p_price = models.DecimalField(max_digits=10, decimal_places=2)
    p_desc = models.TextField()
    p_stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    p_image = models.ImageField(upload_to='product_images/', null=True, blank=True, default='default_p.jpg')
    p_image2 = models.ImageField(upload_to='product_images/', null=True, blank=True, default='default_p.jpg')
    p_image3 = models.ImageField(upload_to='product_images/', null=True, blank=True, default='default_p.jpg')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.p_title

class Review(models.Model):
    reviewer_name = models.CharField(max_length=100)
    review_title = models.CharField(max_length=85)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Profile(models.Model):

    profile_pic = models.ImageField(null=True, blank=True,default='defaultUser.jpg')

    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE,null=True )


class Plan(models.Model):
    PLAN_CHOICES = [
        ('None', 'None'),
        ('Basic', 'Basic'),
        ('Gold', 'Gold'),
    ]

    name = models.CharField(max_length=10, choices=PLAN_CHOICES, default='None')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    
    

class Code(models.Model):
    alphanumeric_validator = RegexValidator(
        regex='^[a-zA-Z0-9]{5}$',
        message='Code.my must be 5 characters long and contain only letters and numbers.',
    )

    my = models.CharField(max_length=5, validators=[alphanumeric_validator], unique=True)
    other = models.CharField(max_length=5)
    points= models.IntegerField(default=0,null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    @classmethod
    def generate_code(cls):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(5))
    


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def total_price(self):
        return self.product.p_price * self.quantity

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)

    def total_cart_price(self):
        return sum(item.total_price() for item in self.items.all())

    def __str__(self):
        return f"{self.user.username}'s Cart"
    
    


class Order(models.Model):
    PAYMENT_CHOICES = [
        ('easypesa', 'EasyPesa'),
        ('jazzcash', 'JazzCash'),
        ('cashondelivery', 'Cash On Delivery'),
    ]

    ORDER_STATUS_CHOICES = [
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField('CartItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default='cashondelivery')
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='Processing')

    def __str__(self):
        return f"Order #{self.id} - {self.user.username} - {self.created_at}"

    









