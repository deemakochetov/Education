from django.db import models

# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.TextField(help_text="Введите имя")
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Good(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.TextField(help_text="Введите название товара")
#    photo = models.ImageField()
    price = models.FloatField(help_text="Введите цену")
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    qty = models.FloatField()
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Order(models.Model):
    id = models.UUIDField(primary_key=True)
    date_time = models.DateField(auto_now=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    status = (
        ('n','New'),
        ('s','Sent'),
        ('r','Received')
    )
class OrderGood(models.Model):
    id = models.UUIDField(primary_key=True)
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    price = models.ForeignKey(Good,on_delete=models.CASCADE)