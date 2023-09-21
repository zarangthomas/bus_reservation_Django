from django.contrib import admin

# Register your models here.
from.models import start
admin.site.register(start)

from.models import stop
admin.site.register(stop)

from.models import bus,bookings
admin.site.register(bus)


class bookingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'from_s', 'to_s', 'bus_name', 'date')

admin.site.register(bookings,bookingsAdmin)