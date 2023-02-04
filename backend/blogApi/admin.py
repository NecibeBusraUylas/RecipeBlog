from django.contrib import admin
from .models import category, blog

class blogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    
# Register your models here.
admin.site.register(category)
admin.site.register(blog,blogAdmin)