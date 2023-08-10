from django.contrib import admin
from .models import Menu, Contact, BookTable, Special
# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name','price','category']
    list_editable = ['price']
    list_filter = ('category',)
admin.site.register(Menu, MenuAdmin)

class BookTableAdmin(admin.ModelAdmin):
    list_display = ['name','date','sits']
    list_filter = ('date',)
admin.site.register(BookTable, BookTableAdmin)

admin.site.register(Contact)
admin.site.register(Special)