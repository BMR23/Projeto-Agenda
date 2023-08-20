from django.contrib import admin
from contact.models import Contact, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'email', 'show'
    ordering = 'id',
    # -id = id decrescente
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 20  # 1 item por página
    list_max_show_all = 60  # para que a opção 'mostrar tudo' não seja um tiro no pé
    list_editable = 'first_name', 'last_name', 'show'
    list_display_links = 'id', 'phone',
    # list_filter = 'created_date',
