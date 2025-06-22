from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return f"{self.name} {self.model}"


class Network(models.Model):
    FACTORY = 0
    RETAIL = 1
    ENTREPRENEUR = 2

    LEVEL_CHOICES = (
        (FACTORY, 'Factory'),
        (RETAIL, 'Retail Network'),
        (ENTREPRENEUR, 'Individual Entrepreneur'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=20)
    products = models.ManyToManyField(Product)
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    debt = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)]
    )
    creation_time = models.DateTimeField(auto_now_add=True)
    level = models.IntegerField(choices=LEVEL_CHOICES, editable=False)

    def save(self, *args, **kwargs):
        # Automatically set level based on supplier
        if not self.pk:  # Only on creation
            if self.supplier is None:
                self.level = self.FACTORY
            else:
                self.level = self.supplier.level + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_level_display()}: {self.name}"