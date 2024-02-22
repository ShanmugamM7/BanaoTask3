from django.contrib import admin
from .models import UserDetails,BlogPost,Appointment
# Register your models here.
admin.site.register(UserDetails)
admin.site.register(BlogPost)
admin.site.register(Appointment)