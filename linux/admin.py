from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Author, LinuxCategorey,LinuxPost
# Register your models here.
#Email: mdimranhossain0066@gmail.com
#Pass: ghost22boy#
#username : imran

class LinuxPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','is_published','author')
    list_display_links = ('id', 'title',)
    list_editable = ('is_published',)
    search_fields = ('title',)

class LinuxCategoreyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)

admin.site.register(LinuxPost,LinuxPostAdmin)

admin.site.register(LinuxCategorey,LinuxCategoreyAdmin)
