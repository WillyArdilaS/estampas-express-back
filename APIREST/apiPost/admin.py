from django.contrib import admin
from apiPost.models import register,login
# Register your models here.


@admin.register(register)
class PostAdmin(admin.ModelAdmin):
    list_display: ['id', 'username']
