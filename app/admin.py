from django.contrib import admin

from .models import ProductModel, InExCludeModel, BuyModel, ContactModel


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'prise', 'start_date',]
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title',]


@admin.register(InExCludeModel)
class InExCludeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(BuyModel)
class BuyAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'tour' ]

@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email']