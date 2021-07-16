from django.contrib import admin
from .models import User


# admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'full_name', 'timestamp', 'admin', 'staff', 'is_active', 'city', 'language', 'send_email']
    list_filter = ['city', 'language', 'send_email']
    fieldsets = [(None, {'fields': ('email', 'password', 'full_name')}),
                 ('Permissions', {'fields': ('admin', 'staff')}),
                 ('Settings', {'fields': ('city', 'language', 'send_email')})
                 ]
