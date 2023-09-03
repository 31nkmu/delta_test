from django.db import models


class PackageType(models.Model):
    CLOTHING = 'clothing'
    ELECTRONICS = 'electronics'
    OTHER = 'other'

    TYPE_CHOICES = [
        (CLOTHING, 'Одежда'),
        (ELECTRONICS, 'Электроника'),
        (OTHER, 'Разное'),
    ]

    name = models.SlugField(max_length=20, choices=TYPE_CHOICES, unique=True, primary_key=True)

    def __str__(self):
        return self.get_name_display()


class Package(models.Model):
    # название
    title = models.CharField(max_length=120)
    # вес
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.ForeignKey(PackageType, on_delete=models.CASCADE, related_name='packages')
    user_session = models.CharField(max_length=300)
    # цена товара
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    # цена доставки
    delivery = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return self.title
