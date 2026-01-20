from django.contrib import admin
from django.utils.html import mark_safe
from django.contrib.admin import AdminSite
from .models import CustomUser, Series, ProductionCompany, Streaming, MainCast


class MyAdminSite(AdminSite):
    site_header = "GLflix Admin"

    def has_permission(self, request):
        # Only superusers can log in
        return request.user.is_active and request.user.is_superuser

admin_site = MyAdminSite(name='myadmin')

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'get_favorites']
    search_fields = ['username']
    filter_horizontal = ['favorites']          

    def get_favorites(self, obj):
        favs = obj.favorites.all()
        if not favs:
            return "-"
        return mark_safe("<br>".join([s.title for s in favs]))
    get_favorites.short_description = "Favorites"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # exclude superusers (or specifically GL)
        return qs.exclude(is_superuser=True)


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'country', 'release_date', 'episodes', 'get_production_company']
    list_filter = ['genre', 'country', 'release_date', 'production_company']
    search_fields = ['title', 'genre', 'country']
    filter_horizontal = ['main_cast', 'streaming']

    def get_production_company(self, obj):
        return obj.production_company.name if obj.production_company else "-"
    get_production_company.short_description = "Production Company"

@admin.register(ProductionCompany)
class ProductionCompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'get_series']
    search_fields = ['name', 'country']

    def get_series(self, obj):
        series_list = obj.series_set.all()
        if not series_list:
            return "-"
        return mark_safe("<br>".join([s.title for s in series_list]))
    get_series.short_description = "Series"


@admin.register(Streaming)
class StreamingAdmin(admin.ModelAdmin):
    list_display = ['platform', 'url', 'get_series']
    search_fields = ['platform']

    def get_series(self, obj):
        series_list = obj.series_set.all()
        if not series_list:
            return "-"
        return mark_safe("<br>".join([s.title for s in series_list]))
    get_series.short_description = "Series"


@admin.register(MainCast)
class MainCastAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'get_series']
    search_fields = ['name']

    def get_series(self, obj):
        series_list = obj.series_set.all()
        if not series_list:
            return "-"
        return mark_safe("<br>".join([s.title for s in series_list]))
    get_series.short_description = "Series"


