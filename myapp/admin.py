from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields

from .models import Product

class ProductResourse(resources.ModelResource):
    #category = fields.Field(column_name='category')
    class Meta:
        model = Product

class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResourse
    list_display = (field.name for field in Product._meta.fields if field.name != 'id')
    #inlines = [ProductImageInline]


admin.site.register(Product)

