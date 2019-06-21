from django.contrib import admin
from .models import User,Good,Order,OrderGood
# Register your models here.
admin.site.register(User)
admin.site.register(Good)
admin.site.register(Order)
admin.site.register(OrderGood)