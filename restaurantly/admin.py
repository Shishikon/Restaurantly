from django.contrib import admin

from .models import BookTable, Qrcode


class BookTableAdminSite(admin.ModelAdmin):
    list_display = ('name', 'email', 'date', 'time', 'people')
    list_display_links = ('name', 'email')


class QrcodeBookTable(admin.ModelAdmin):
    list_display = ('name', 'email', 'date', 'time', 'people')
    list_display_links = ('name', 'email')


admin.site.register(BookTable, BookTableAdminSite)
admin.site.register(Qrcode, QrcodeBookTable)
