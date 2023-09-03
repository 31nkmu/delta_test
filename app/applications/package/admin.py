from django.contrib import admin

from applications.package.models import Package, PackageType

admin.site.register(Package)
admin.site.register(PackageType)
