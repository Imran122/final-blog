from django.contrib import admin
from .models import Signup,Contact
# Register your models here.
class SignAdmin(admin.ModelAdmin):
    list_display = ('id', 'email','timestamp')
    list_display_links = ('id', 'email')
    
    search_fields = ('email',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email','phone','address')
    list_display_links = ('id', 'name')  
    search_fields = ('name',)

admin.site.register(Signup,SignAdmin)
admin.site.register(Contact,ContactAdmin)
