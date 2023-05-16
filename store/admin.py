from django.contrib import admin
from .models import Book,BookCopy,Order,OrderItem 

class BookAdmin(admin.ModelAdmin):
  list_display=("title","author","year_published","price","available_copies","total_copies","status")


class BookCopyAdmin(admin.ModelAdmin):
  list_display=("sku","book","is_paid","rented","due_date","lost","lost_date","damaged","removed","removed_date","return_date","reserved")


admin.site.register(Book,BookAdmin) 
admin.site.register(BookCopy,BookCopyAdmin)

admin.site.register(OrderItem)
admin.site.register(Order)
