from django.contrib import admin

# Register your models here.
from api.models import Product,Category

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
