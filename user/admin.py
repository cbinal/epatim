from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

admin.site.unregister(User)  # Önce mevcut User modelini kaldır


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    verbose_name = _("Kullanıcı")  # Modelin tekil adı
    verbose_name_plural = _("Kullanıcılar")  # Çoğul adı


# Admin başlığını Türkçeleştir
admin.site.site_header = "Kayrem Yönetim Paneli"
admin.site.site_title = "Kullanıcı Yönetimi"
admin.site.index_title = "Hoşgeldiniz!"
