from django.contrib import admin
from django.contrib.auth.models import User
from backend.models import Store, Commodity, Order
# Register your models here.

# admin.site.register(User)
admin.site.register(Store)
admin.site.register(Commodity)
admin.site.register(Order)

admin.site.site_header="后台管理系统"