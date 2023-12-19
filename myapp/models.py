from django.db import models

# Create your models here.

class Product(models.Model):
    p_title = models.CharField(max_length=85)
    p_price = models.DecimalField(max_digits=10, decimal_places=2)
    p_desc = models.TextField()
    p_stock = models.PositiveIntegerField()
    p_image = models.ImageField(upload_to='product_images/', null=True, blank=True, default='default_p.jpg')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.p_title

class Review(models.Model):
    reviewer_name = models.CharField(max_length=100)
    review_title = models.CharField(max_length=85)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)