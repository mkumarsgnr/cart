from django.db import models

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    decs = models.CharField(max_length=300)
    pub_date = models.DateField()
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/images",default="")


    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    phone = models.IntegerField(default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    item_json = models.CharField(max_length=5000, default="")
    name = models.CharField(max_length=90, default="")
    amount = models.IntegerField(default=0)
    email = models.CharField(max_length=111, default="")
    address = models.CharField(max_length=111, default="")
    city = models.CharField(max_length=111, default="")
    state = models.CharField(max_length=111, default="")
    zip_code = models.CharField(max_length=111, default="")
    phone = models.CharField(max_length=111, default="")

    def __str__(self):
        return self.name

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
