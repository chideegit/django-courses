from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets, 
        (
            'Custom Field Heading', 
            {
                'fields': (
                    'is_instructor',
                    'is_learner' 
                    
                )
            }
        )
    )

admin.site.register(User, CustomUserAdmin)