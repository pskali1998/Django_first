from django.contrib import admin
#ADMIN PANEL
# Register your models here.


from .models import Items
from .models import Books
admin.site.register(Items)
admin.site.register(Books)