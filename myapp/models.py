from datetime import datetime
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email = email)
        except:
            return False

    def isExist(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description =models.CharField(max_length=200, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/productbs')

    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_product_by_name(names):
        return Product.objects.filter(name__in=names)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_product_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        return Product.get_all_products()


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=60, default='', null=True)
    phone = models.CharField(max_length=10, default='', null=True)
    date = models.DateField(default= datetime.today())
    time = models.TimeField(default=datetime.now())
    status = models.BooleanField(default=False)

    def place_order(self):
        self.save()

    @staticmethod
    def get_order_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')