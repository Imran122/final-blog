from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Author, Categorey,Post, PostView
# Register your models here.
#Email: mdimranhossain0066@gmail.com
#Pass: ghost22boy#
#username : imran







class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','is_published','author')
    list_display_links = ('id', 'title',)
    list_editable = ('is_published',)
    search_fields = ('title',)
class CategoreyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)

admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Categorey, CategoreyAdmin)
admin.site.register(PostView)
