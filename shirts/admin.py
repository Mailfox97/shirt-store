import csv

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.http import HttpResponse

from .models import *


User = get_user_model()


# Register your models here.
def export_csv_email(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'  # your filename

    writer = csv.writer(response)
    writer.writerow(['Email Address'])

    users = queryset.values_list('email')

    for user in users:
        writer.writerow(user)

    return response


export_csv_email.short_description = "Export email"


class UserAdmin(UserAdmin):
    '''
    Registers the action in your model admin
    '''
    actions = [export_csv_email]


class SizeVariantConfig(admin.TabularInline):
    model = Sizevariant


class TshirtConfig(admin.ModelAdmin):
    inlines = [SizeVariantConfig]


admin.site.register(Tshirt, TshirtConfig)
admin.site.register(Category)
admin.site.register(Occassion)
admin.site.register(Sleeve_type)
admin.site.register(Neck_type)
admin.site.register(Ideal_for)
admin.site.register(brand)
admin.site.register(color)
# admin.site.register(Payment)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
