from django.contrib import admin
from .models import CustomUser
# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    # Customize the way CustomUser is displayed in the admin panel
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')

# Register the CustomUser model with the admin site
admin.site.register(CustomUser, CustomUserAdmin)