from django.contrib import admin
from shop.models import Product, Company, Sale
from django.contrib.auth.models import Group, User

admin.site.unregister(Group)
admin.site.unregister(User)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "soni", 'company')
    fields = ("title", "company", "soni", "price")
    search_fields = ("title",)
    list_filter = ("company",)

    def get_readonly_fields(self, request, obj=None):
        if obj: return  ("company",)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("title", "phone", "address", "products_count")

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ("Mijoz", "product", "qty", "total_amount")
    readonly_fields = ("total_amount",)

    def save_model(self, request, obj, form, change):
        obj.total_amount = obj.sale_amount()
        super().save_model(request, obj, form, change)
