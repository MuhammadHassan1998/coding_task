from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from .models import Book, Collaboration, Section


class SectionAdmin(DjangoMpttAdmin):
    pass


admin.site.register(Section, SectionAdmin)
admin.site.register(Book)
admin.site.register(Collaboration)
