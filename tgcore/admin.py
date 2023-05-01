from django.contrib import admin
from tgcore.models import Product, Gallery, TgUser, CustomerMessage


class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = Gallery

class CustomerMessageInline(admin.TabularInline):
    fk_name = 'user'
    model = CustomerMessage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'available', 'created', 'updated')
    search_fields = ('name',)
    list_filter = ('available',)
    inlines = [GalleryInline,]

@admin.register(TgUser)
class TgUserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'register_date')
    list_display_links = ('user_id', 'username')
    search_fields = ('username',)
    inlines = [CustomerMessageInline,]