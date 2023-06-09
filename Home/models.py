from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField("Product Name", max_length=50)
    product_code = models.IntegerField("Product Code")
    product_price = models.PositiveBigIntegerField("Price")
    product_cost = models.PositiveBigIntegerField("Cost")
    product_tax = models.IntegerChoices()
    #product_image = models.ImageField("Product Image")
    
    def __str__(self) -> str:
        return self.product_name

class Service(models.Model):
    service_name = models.CharField("Service Name", max_length=50)
    service_fee = models.PositiveBigIntegerField("Price")
    service_cost = models.PositiveBigIntegerField("Cost")
    
    def __str__(self) -> str:
        return self.service_name
    
class Customer(models.Model):
    customer_id = models.IntegerField(auto_created=True)
    customer_name = models.CharField("Customer Name", max_length=60)
    date_created = models.DateTimeField(auto_now_add=True)

class Sale(models.Model):
    sale_ref = models.AutoField(primary_key=True)
    sale_date = models.DateTimeField(auto_now_add=True)
    sale_amount = models.PositiveBigIntegerField("Total")
    customer_id = models.ForeignKey(
        "Customer", on_delete=models.SET_NULL, null=True
    )
    def __str__(self) -> str:
        return self.sale_ref
    
class Payment_methods(models.Model):
    payment_type_id = models.AutoField(primary_key=True)
    payment_type_name = models.CharField("Payment Name", max_length=20)
    #max_limit = models.BigIntegerField(null=)
    def __str__(self) -> str:
        return self.payment_type_name
    
class Order_item(models.Model):
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.product.product_name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(
        "Customer", on_delete=models.SET_NULL, null=True
    )
    items = models.ManyToManyField(Order_item)
    order_total = models.PositiveBigIntegerField("Total")
    order_date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.order_id
    
    def get_cart_items(self):
        return self.items.all()
    
    def get_cart_total(self):
        return sum([item.product.product_price for item in self.items.all()])