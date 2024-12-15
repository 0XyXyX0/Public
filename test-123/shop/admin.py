from django.contrib import admin
from shop.models import Tag, Item, Category


class TagItemInLine(admin.StackedInline):
    model = Tag.items.through
    extra = 1

class ItemInLine(admin.StackedInline):
    model = Item
    extra = 1

class TagInLine(admin.StackedInline):
    model = Item.tags.through
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name', 'id']
    ordering = ['id']
    list_per_page = 10

class ItemAdmin(admin.ModelAdmin):
    search_fields = ['name']
    ordering = ['price']
    list_display = ['id', 'name', 'price']
    autocomplete_fields = ['category']
    fields = ['name', 'price', 'description', 'category']
    inlines = [TagInLine]

class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
    search_fields = ['name']
    inlines = [TagItemInLine]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Tag, TagAdmin)

