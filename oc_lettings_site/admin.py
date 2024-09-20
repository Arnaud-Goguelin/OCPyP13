from django.contrib import admin

from letting_app.models import Letting, Address
from profile_app.models import Profile


admin.site.register(Letting)
admin.site.register(Address)
admin.site.register(Profile)
