from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = (
        ('shoes', 'Shoes'),
        ('t-shirts', 'T-Shirts'),
        ('jackets', 'Jackets'),
        ('jeans', 'Jeans')
    )

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    image_url = models.URLField(verbose_name='Image URL')

    # Add more fields as needed

    def __str__(self):
        return self.name
