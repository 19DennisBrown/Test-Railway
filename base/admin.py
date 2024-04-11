from django.contrib import admin
from .models import UserProfile, ProfileStatus
# Register your models here.


admin.site.register({UserProfile, ProfileStatus})