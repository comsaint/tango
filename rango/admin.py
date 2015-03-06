from django.contrib import admin

# Register your models here.
from rango.models import Category, Page

#admin.site.register(Category)
#admin.site.register(Page)

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'views', 'likes')
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
    
admin.site.register(Page, PageAdmin)