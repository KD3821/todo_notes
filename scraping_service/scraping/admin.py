from django.contrib import admin
from .models import City, Language, Vacancy, Error, Url

admin.site.register(City)
admin.site.register(Language)
# admin.site.register(Vacancy)
admin.site.register(Url)


@admin.register(Error)
class ErrorAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'data']


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'city', 'language', 'timestamp']
    list_filter = ['city', 'language']
    # fieldsets = [(None, {'fields': ('email', 'password', 'full_name')}),
    #              ('Permissions', {'fields': ('admin', 'staff')}),
    #              ('Settings', {'fields': ('city', 'language', 'send_email')})
    #              ]